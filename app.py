from flask import flask,render_template,request
app=flask(_name_)
@app.route('/')
def home();
    return render_template('register.html')
@app.route('/success',methods=['GET','POST'])
def success();
    if request.method=="POST":
        nmae=request.form['name']
        email=request.form['name']
        password=request.form['password']
        return render_template('register.html')
    else:
        return render_template('register.html')
    if__name__=='main__':
        app.run(host='0.0.0.0')    

