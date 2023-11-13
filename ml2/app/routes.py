from app import app
from flask import render_template, session, redirect, url_for, request
from app.forms import inputfield
from app.predict import predict




app.config['SECRET_KEY']='ml2electricbogaloo'
@app.route('/', methods=['GET', 'POST'])

@app.route('/predictomat',methods=['GET','POST'])

def predictomat():
    
    form = inputfield()

    if form.validate_on_submit():


        for fieldname, value in form.data.items():
            session[fieldname] = value
        
        
        session['prediction'] = predict(session)
        return redirect(url_for('predictomat'))

    return render_template('predictomat.html',form=form)
    

@app.route('/main',methods=['GET'])

def main():
    return render_template('main.html')

