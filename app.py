from flask import Flask, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Simple Calculator</h2>

    <form action="/calculate">
        Number 1:
        <input type="number" name="a" required><br><br>

        Number 2:
        <input type="number" name="b" required><br><br>

        Operation:
        <select name="op">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>
    """

@app.route('/calculate')
def calculate():

    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    op = request.args.get('op')

    if op == "add":
        result = add(a, b)

    elif op == "subtract":
        result = subtract(a, b)

    elif op == "multiply":
        result = multiply(a, b)

    elif op == "divide":
        result = divide(a, b)

    else:
        result = "Invalid Operation"

    return f"<h2>Result: {result}</h2>"

if __name__ == "__main__":
    app.run()
