from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import csv
import os

class Job:
    #===================驱动浏览器====================
    def open_browser(self):
        self.browser=webdriver.Chrome() #驱动谷歌浏览器
        self.browser.implicitly_wait(10) #设置隐式等待
        self.wait=WebDriverWait(self.browser,10) #设置显示等待


    #====================程序的主函数==================
    def work_on(self):
        self.open_browser() #打开浏览器
        print("开始抓取。。。。")
        #让浏览器打开起始页面
        self.browser.get("https://we.51job.com/pc/search?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&searchType=2&sortType=0&metro=")
        #将进度条下拉倒最底部
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        #设置循环来控制抓取的页数
        for page in range(20):
            print("正在抓取第",str(page+1),"页...")
            self.get_info() #获取当前页的工作信息
            self.save_info() #保存当前页的工作信息
            self.change_page() #进行翻页
        #退出浏览器
        self.browser.close()


    #==================获取工作信息(xpath)====================
    def get_info(self):
        try:

            #获取岗位名称
            title=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/a/div[1]/span[1]')))
            title=[item.text for item in title]
            #获取薪资
            price=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/a/p[1]/span[1]')))
            price=[item.text for item in price]
            #获取工作地址
            dz=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/a/p[1]/span[2]/span[1]')))
            dz=[item.text for item in dz]
            #获取工作经验要求
            gzt=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/a/p[1]/span[2]/span[3]')))
            gzt=[item.text for item in gzt]
            #获取学历要求
            xl=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/a/p[1]/span[2]/span[5]')))
            xl=[item.text for item in xl]
            #岗位描述
            bq = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//p[@class="tags"]')))
            bq = [item.text for item in bq]
            bq =str(bq).split()
            #获取公司名称
            shop=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="e sensors_exposure"]/div[2]/a')))
            shop=[item.get_attribute("title") for item in shop]
            # 分类
            sort = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="e sensors_exposure"]/div[2]/p[2]')))
            sort = [item.text for item in sort]

            self.data=zip(title,sort,price,dz,gzt,xl,shop,bq) #整合写入csv的序列

        except selenium.common.exceptions.TimeoutException: #请求超时异常
            self.get_info() #递归重新调用一次函数
        except selenium.common.exceptions.StaleElementReferenceException: #页面加载失败异常
            self.browser.refresh() #刷新页面


    #==================保存信息(csv)=====================
    def save_info(self):
        file_exists = os.path.isfile("51job.csv")

        with open("51job.csv","a",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            if not file_exists:
                header = ['岗位名称', '分类', '薪资', '公司地址', '工作经验', '学历要求', '公司名称', '岗位描述']
                writer.writerow(header)
            for i in self.data:
                writer.writerow(i)
        f.close()


    #===================进行翻页========================
    def change_page(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn-next"]'))).click()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
        except selenium.common.exceptions.TimeoutException:  # 请求超时异常
            self.get_info()  # 递归重新调用一次函数
        except selenium.common.exceptions.StaleElementReferenceException:  # 页面加载失败异常
            self.browser.refresh()  # 刷新页面

job=Job()
job.work_on()