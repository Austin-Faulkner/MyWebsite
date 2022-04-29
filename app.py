from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():  # put application's code here
    return render_template('homepage02.html')


@app.route('/work_exp')
def work_exp():
    return render_template('work_exp.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/whySE')
def whySE():
    return render_template('whySE.html')


if __name__ == '__main__':
    app.run()
