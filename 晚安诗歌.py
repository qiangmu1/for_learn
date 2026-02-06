from flask import Flask, render_template
from datetime import datetime
from random import randint
def fun():
    hours=datetime.now().hour
    if 0<hours<7:
        return "凌晨时分，睡个回笼觉吧"
    elif hours<9:
        return "早上好"
    elif hours<13:
        return "中午好"
    elif hours<17:
        return "下午好"
    else:
        return "晚上好"
app=Flask(__name__)
@app.route("/reading")
def reading():
    return  render_template('愚弄网站.html')
@app.route("/date")
def date():
    num=randint(1,299)
    now=datetime.now()
    formatted_time=now.strftime("%Y-%m-%d%H:%M:%S")
    with open(r"C:\Users\29787\Desktop\诗经\文件{}.txt".format(num),'r',encoding='utf-8') as f:
        return render_template('愚弄网站.html',h=f"现在是北京时间{formatted_time},{fun()}",poem=f.read())

app.run(debug=True,port=5000,host='0.0.0.0')
