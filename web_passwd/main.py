#coding=utf-8
from flask import send_file
div='''
<div class="post-masonry col-md-4 col-sm-6">
                            <div class="post-thumb">
                                <img src="pic/num_for_photo.jpg" alt="">
                                <div class="title-over">
                                    <h4><a href="#">good photo</a></h4>
                                </div>
                                <div class="post-hover text-center">
                                    <div class="inside">
                                        <i class="fa fa-plus"></i>
                                        <h4><a href="#">good photo</a></h4>
                                        <p>图片均源自百度图片，本站不负任何法律责任- -</p>
                                    </div>
                                </div>
                            </div>
                        </div> <!-- /.post-masonry -->
                        \n
'''

#coding=utf-8
from flask import Flask,render_template
app = Flask(__name__)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import uniout

import os
def traverse(f):
    all=[]
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            print('文件: %s' % tmp_path)
            tmp_path="/static/pic/"+tmp_path.split("/")[-1]
            all.append(tmp_path)
    return all


path = 'static/pic'
path_=u'/Users/wangjiao/Desktop/web_passwd/templates/'
def change_html():
    global div
    global path
    all_html = ""
    all_pic = traverse(path)
    for i in all_pic:
        num = i.split("/")[-1].split(".")[0]
        all_html = all_html + div.replace("num_for_photo", str(num))
    html=open(path_+"index.html")
    html_read=html.read().split("<!-- 分割线 -->")
    html_new=html_read[0]+div+html_read[2]
    html.close()
    #os.remove(path_+"index.html")
    html=open(path_+"index.html")
    html.write(html_new)
    html.close()


def start(keyword):
    import pic
    pic.start(keyword)

def pan():
    from rude import panduan
    panduan()

@app.route('/<type>/<keyword>')
def get_pic(type,keyword):
    if not type=="start" and type=="p":
        pic = traverse(path)
        return render_template("index.html",users=pic)
    elif(type=="start"):
        import threading
        thread=threading.Thread(target=start,args=(keyword,))
        thread.setDaemon(True)
        thread.start()
        return "OK"
    else:
        import threading
        thread = threading.Thread(target=, args=(keyword,))
        thread.setDaemon(True)
        thread.start()
@app.route('/')
def show():
    pic = traverse(path)
    return render_template("index.html", users=pic)

app.run(host='0.0.0.0')