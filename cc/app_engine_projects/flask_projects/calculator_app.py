from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 40px;">
    <h2>Assignment: Arithmetic Calculator</h2>
    <form method="POST">
        <input type="number" step="any" name="num1" placeholder="First Number" required>
        
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        
        <input type="number" step="any" name="num2" placeholder="Second Number" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = "Error (Div by 0)" if num2 == 0 else num1 / num2
        except ValueError:
            result = "Invalid Input"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    # Running on port 5001 to avoid conflicts
    app.run(port=5001, debug=True)