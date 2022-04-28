from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def game():
    return render_template("main.html")



#if runs with Python, app run with debug mode (allows edits to appear instantly)
if __name__ == "__main__":
    app.run(debug=True)

