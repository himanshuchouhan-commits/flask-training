from flask import Flask ,render_template,request,redirect,url_for

app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>hello Im YOYO</h1>"

@app.route('/wellcome')
def wellcome():
    return"<h1> wellcome to yoyo's site</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sucess/<int:a>')
def sucess(a):
    return "<h1>the person is pass the soure is</h1> "+ str(a)

@app.route('/fail/<int:a>')
def fail(a):
    return "<h1>the person is fail the soure is</h1> "+ str(a)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        dsa=float(request.form['dsa'])
        oopm=float(request.form['oopm'])
        avg=(maths+dsa+oopm)/3
        result=''
        if avg>=80:
            result='sucess'
        else:
            result='fail'
            return redirect(url_for(result,a=avg))





if __name__ == '__main__':
    app.run(debug=True)