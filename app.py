from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/feedback/form')
# def feedback_form():
#     return render_template('feedback.html')

# @app.route('/feedback/list')
# def feedback_list():
#     return render_template('feedback_list.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
