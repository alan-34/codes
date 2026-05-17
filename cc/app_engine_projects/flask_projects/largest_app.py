from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Find Largest Number</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 40px;">
    <h2>Assignment: Find Largest Number Among Three</h2>
    <form method="POST">
        <p><input type="number" step="any" name="num1" placeholder="Enter 1st number" required></p>
        <p><input type="number" step="any" name="num2" placeholder="Enter 2nd number" required></p>
        <p><input type="number" step="any" name="num3" placeholder="Enter 3rd number" required></p>
        <button type="submit">Find Largest</button>
    </form>

    {% if result is not none %}
        <h3>The largest number is: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def find_largest():
    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.form.get('num1'))
            n2 = float(request.form.get('num2'))
            n3 = float(request.form.get('num3'))

            # Logic to find the max value
            if n1 >= n2 and n1 >= n3:
                result = n1
            elif n2 >= n1 and n2 >= n3:
                result = n2
            else:
                result = n3
        except ValueError:
            result = "Invalid Input"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    # Running on port 5002 so you can run both apps at the same time
    app.run(port=5002, debug=True)