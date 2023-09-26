from flask import Flask,render_template
import pymysql
app = Flask(__name__)

# flask案例，展示豆瓣网前250部高分电影资料

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index2():
    return render_template("index.html")


@app.route('/movie')
def movie():

    dataList = []
    # 建立连接
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='pc',charset='utf8mb4')
    # 建立游标,python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    cursor = conn.cursor()
    # 4. 关闭游标
    sql = 'select * from qx'
    result = cursor.execute(sql)
    data = cursor.fetchall()  #查询得到的结果是元组（（1,...）,（2,...））
    for item in data:
        dataList.append(item)
    cursor.close()
    # 5. 关闭连接
    conn.close()
    return render_template("movie.html",movies=dataList)

@app.route('/score')
def score():
    score1 =[] #评分
    num1 = [] #每个评分对应的电影数量
    # 建立连接
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='pc',charset='utf8mb4')
    # 建立游标,python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    cursor1 = conn.cursor()
    # 4. 关闭游标
    sql1 = 'SELECT 分类,COUNT(*) FROM `qx` GROUP BY 分类 ORDER BY COUNT(*) DESC LIMIT 10;'
    cursor1.execute(sql1)
    data1 = cursor1.fetchall()  #查询得到的结果是元组（（1,...）,（2,...））
    for item in data1:
        score1.append(str(item[0]))
        num1.append(item[1])
    cursor1.close()

    score2 =[]
    num2 = []#数量
    cursor2 = conn.cursor()
    # 4. 关闭游标
    sql2 = 'SELECT 岗位名称,COUNT(*) FROM `qx` GROUP BY 岗位名称 ORDER BY COUNT(*) DESC LIMIT 10;'
    cursor2.execute(sql2)
    data2 = cursor2.fetchall()  #查询得到的结果是元组（（1,...）,（2,...））
    for item in data2:
        score2.append(str(item[0]))
        num2.append(item[1])
    cursor2.close()

    score3 =[]
    num3 = []#数量
    cursor3 = conn.cursor()
    # 4. 关闭游标
    sql3 = 'SELECT 薪资,COUNT(*) FROM `qx` GROUP BY 薪资 ORDER BY COUNT(*) DESC LIMIT 10;'
    cursor3.execute(sql3)
    data3 = cursor3.fetchall()  #查询得到的结果是元组（（1,...）,（2,...））
    for item in data3:
        score3.append(str(item[0]))
        num3.append(item[1])
    cursor3.close()

    score4 = []
    num4 = []  # 数量
    cursor4 = conn.cursor()
    # 4. 关闭游标
    sql4 = 'SELECT 公司地址,COUNT(*) FROM `qx` GROUP BY 公司地址 ORDER BY COUNT(*) DESC LIMIT 10;'
    cursor4.execute(sql4)
    data4 = cursor4.fetchall()  # 查询得到的结果是元组（（1,...）,（2,...））
    for item in data4:
        score4.append(str(item[0]))
        num4.append(item[1])
    cursor4.close()

    score5 = []
    num5 = []  # 数量
    cursor5 = conn.cursor()
    # 4. 关闭游标
    sql5 = 'SELECT 工作经验,COUNT(*) FROM `qx` GROUP BY 工作经验 ORDER BY COUNT(*) DESC;'
    cursor5.execute(sql5)
    data5 = cursor5.fetchall()  # 查询得到的结果是元组（（1,...）,（2,...））
    for item in data5:
        score5.append(str(item[0]))
        num5.append(item[1])
    cursor5.close()

    score6 = []
    num6 = []  # 数量
    cursor6 = conn.cursor()
    # 4. 关闭游标
    sql6 = 'SELECT 学历要求,COUNT(*) FROM `qx` GROUP BY 学历要求 ORDER BY COUNT(*) DESC;'
    cursor6.execute(sql6)
    data6 = cursor6.fetchall()  # 查询得到的结果是元组（（1,...）,（2,...））
    for item in data6:
        score6.append(str(item[0]))
        num6.append(item[1])
    cursor6.close()

    # 5. 关闭连接
    conn.close()

    return render_template("score.html",score1=score1,num1=num1,score2=score2,num2=num2,score3=score3,num3=num3,score4=score4,num4=num4,score5=score5,num5=num5,score6=score6,num6=num6)

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/word')
def word():
    return render_template("word.html")


if __name__ == '__main__':
    app.run()
