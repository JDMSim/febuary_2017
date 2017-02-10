from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['Post'])
def process():
    # do some validations here!
    if len(request.form['name']) < 1:
        flash('Name cannot be empyt!')
        session['color'] = 'alert alert-danger'
    else:
        flash("Success! Welcome  {}".format(request.form['name']))
        session['color'] = 'alert alert-success'
    return redirect('/')
app.run(debug=True)
