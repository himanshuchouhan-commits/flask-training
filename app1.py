from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <html>
            <body>
                <h1>Hello Im YOYO</h1>
                <a href="/wellcome">Wellcome</a> |
                <a href="/index">Index</a> |
                <a href="/calculate">Calculate</a>
            </body>
        </html>
    '''


@app.route('/wellcome')
def wellcome():
    return '''
        <html>
            <body>
                <h1>Wellcome to yoyo's site</h1>
            </body>
        </html>
    '''


@app.route('/index')
def index():
    return render_template('app1.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return index()

    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return render_template('app1.html', result='Cannot divide by zero', error=True)
        result = num1 / num2
    else:
        return render_template('app1.html', result='Invalid operation', error=True)

    return render_template('app1.html', result=f'Result: {result}', error=False)


if __name__ == '__main__':
    app.run(debug=True)
