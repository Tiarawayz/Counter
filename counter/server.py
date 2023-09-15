from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'Keep it on the low'

@app.route('/')
def num():
    return render_template('refresh.html')

@app.route('/', methods=['post'])
def show_count():
    if request.form['alter']=='add':
        session['count'] += 1
    elif request.form['alter']=='reset':
        session['count'] = 0
    return render_template('refresh.html')

@app.route('/destroy_session')
def refresh():
    session.pop()
    return render_template('/')

if __name__=="__main__":
    app.run(debug=True)