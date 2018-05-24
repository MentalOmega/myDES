import base64
import json
import time
from io import BytesIO

from flask import Flask
from flask import render_template, request

import junit.myDes
import junit.sbox

app = Flask(__name__)
app.config.from_object('config')
app.config['status'] = dict()


@app.route('/')
def hello_world():
    return render_template("task1.html")


@app.route('/doyoukown/', methods=['post'])
def task_one():
    deltaB = request.form.get("deltaS")
    f = junit.sbox.task1()
    data = f.run(deltaB)
    print(data)
    data = json.dumps(data)
    # dict转json
    return data


@app.route('/task2_home/')
def task_two_home():
    return render_template('task2.html')


@app.route('/task2_go/', methods=['post', 'get'])
def task_two():
    bit = request.form.get("bit")
    bit = int(bit)
    key = request.form.get("key")
    text = request.form.get("text")
    choose = request.form.get("choose")
    seed = request.form.get("seed")
    status = app.config['status']
    status[seed] = 0
    choose = int(choose)
    import matplotlib as mpl
    mpl.use('Agg')

    import matplotlib.pyplot as plt
    x = [0] * 65
    for i in range(0, 1000):
        x[junit.myDes.chooseChange(bit, key, text, choose)] += 1
        status[seed] = i / 10

    print(x)
    # 数据的直方图
    index = [i for i in range(0, 65)]
    print(index)
    plt.bar(index, x)

    plt.xlabel('Change of output ciphertext')
    plt.ylabel("Number of occurrences")
    if choose == 1:
        plt.title(
            'Secret key:' + key + "  " + "Plaintext:" + text + "\n" + "Change the digits of plaintext:" + str(bit))
    elif choose == 2:
        plt.title(
            'Secret key:' + key + "  " + "Plaintext:" + text + "\n" + "Change the digits of ciphertext:" + str(bit))
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([1, 64, 0, 50])
    plt.grid(True)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = '''
    <img src="data:image/png;base64,{}" />
    '''
    html = """
        data:image/png;base64,{}
    """
    html = html.format(data)
    plt.close()
    status.pop(seed)
    print(status)
    return html
    return render_template("task2.html", plotPic=html)


@app.route('/task_check/', methods=['POST'])
def task_two_check():  # ajax是异步的，导致session不能及时更新
    status = app.config['status']
    seed = request.form.get("seed")
    print(seed)
    print(status.get(seed))
    return str(status.get(seed))


@app.route('/ss')
def hello():
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    fig = Figure(figsize=[6, 6])

    ax = fig.add_axes([.1, .1, .8, .8])
    ax.scatter([0.2, 0.3], [0.25, 0.35])
    canvas = FigureCanvasAgg(fig)
    sio = BytesIO()
    buf = sio
    canvas.print_png(buf)
    data = base64.encodebytes(sio.getvalue()).decode()

    headers = {
        'Content-Type': 'image/png',
        'Content-Length': len(data)
    }
    html = '''
        <img src="data:image/png;base64,{}" />
        '''
    html = html.format(data)
    return html
    return render_template("task2.html", plotPic=html)


@app.route("/jianshu")
def jianshu():
    import matplotlib
    matplotlib.use('Agg')  # 不出现画图的框
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64

    # 这段正常画图
    plt.axis([0, 5, 0, 20])  # [xmin,xmax,ymin,ymax]对应轴的范围
    plt.title('My first plot')  # 图名
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 图上的点,最后一个参数为显示的模式
    # -----------

    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    print(data)
    html = '''
       <html>
           <body>
               <img src="data:image/png;base64,{}" />
           </body>
        <html>
    '''
    plt.close()
    # 记得关闭，不然画出来的图是重复的
    return html.format(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
