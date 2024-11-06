from flask import Flask, render_template, abort

app = Flask(__name__)


def factorial(n):
    if n < 0:
        return None  
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


@app.route('/<int:number>')
def show_factorial(number):
    result = factorial(number)
    if result is None:
        abort(400, description="Se ha producido un error")
    return render_template('factorial.html', number=number, result=result)

if __name__ == '__main__':
    app.run(debug=True)
