import pandas as pd
import re
import math

# 读取CSV文件
df = pd.read_csv('51job.csv')

# 清洗第八列数据
a = df.iloc[:,7].str.lstrip('[')  # 删除第一个字符 '['

a = a.str.rstrip(',')
a = a.str.rstrip(']')
a = a.str.strip("'")  # 删除单引号 ''
a = list(a)
a = [item.replace('\\n', ',') for item in a]
a = pd.DataFrame(a,columns=['岗位描述'])

# 拼接前几列数据
b = df.iloc[:, :7]  # 前7列数据
ab = pd.concat([b, a], axis=1)  # 拼接数据

xz = ab['薪资']


cleaned_data = []
formatted_data = []
for salary_range in xz:
    salary_range = str(salary_range)
    salary_range = salary_range.replace('千', '000')
    salary_range = salary_range.replace('万', '')
    salary_range = salary_range.replace('/年', '')
    if '·13薪' in salary_range:
        salary_range = salary_range.replace('·13薪', '')

        salary_range = salary_range.split('-')
        min_salary = float(salary_range[0])
        max_salary = float(salary_range[1])
        if min_salary > 1000:
            min_salary /= 10000
        if max_salary > 1000:
            max_salary /= 10000
        min_salary *= 13
        max_salary *= 13
    elif '·14薪' in salary_range:
        salary_range = salary_range.replace('·14薪', '')

        salary_range = salary_range.split('-')
        min_salary = float(salary_range[0])
        max_salary = float(salary_range[1])
        if min_salary > 1000:
            min_salary /= 10000
        if max_salary > 1000:
            max_salary /= 10000
        min_salary *= 14
        max_salary *= 14
    elif '·15薪' in salary_range:
        salary_range = salary_range.replace('·15薪', '')

        salary_range = salary_range.split('-')
        min_salary = float(salary_range[0])
        max_salary = float(salary_range[1])
        if min_salary > 1000:
            min_salary /= 10000
        if max_salary > 1000:
            max_salary /= 10000
        min_salary *= 15
        max_salary *= 15

    elif '·16薪' in salary_range:
        salary_range = salary_range.replace('·16薪', '')

        salary_range = salary_range.split('-')
        min_salary = float(salary_range[0])
        max_salary = float(salary_range[1])
        if min_salary > 1000:
            min_salary /= 10000
        if max_salary > 1000:
            max_salary /= 10000
        min_salary *= 16
        max_salary *= 16

    elif '-' in salary_range:
        salary_range = salary_range.split('-')
        min_salary = float(salary_range[0])
        max_salary = float(salary_range[1])
        if min_salary > 1000:
            min_salary /= 10000
        if max_salary > 1000:
            max_salary /= 10000
        min_salary *= 12
        max_salary *= 12
    else:
        min_salary = max_salary = float(salary_range)

    cleaned_data.append((round(min_salary, 1), round(max_salary, 1)))
for item in cleaned_data:
    formatted_item = "-".join([f"{int(x)}" if (not math.isnan(x) and int(x) == x) else f"{x}" for x in item]) + "万"
    formatted_data.append(formatted_item)
ab['薪资'] = formatted_data

dz = ab['公司地址']
dz_i = []
for i in dz:
    if '·' in i:
        i = i.split('·')
        i = i[0]
    else:
        i = i
    dz_i.append(i)
ab['公司地址'] = dz_i
# print(ab)
# 保存到CSV文件
ab.to_csv('qx.csv', index=False)

# print(ab.isnull().sum())
