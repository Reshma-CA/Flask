from flask import Flask,render_template,request
import os

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/images'

@app.route('/<int:num1>')
def index(num1):
    return render_template('index.html',n1=num1)

@app.route('/num/<int:age>')
def num(age):
    if age<18:
        return "you are not eligible for this"
    elif age>=18:
        return "you are eligible for this"
    
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/product')
def products():
   return render_template('products.html')

@app.route('/product/laptop')
def laptop():
    return "laptop"

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'Reshma' and request.form['password'] == 'Reshma1@':
            return render_template('dashboard.html')
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html',error=error)
    else:
        return render_template('login.html')

# For form GET method 
@app.route('/register_result',methods=['GET'])
def register_result():
    name = request.args.get('username')
    email = request.args.get('email')
    phone = request.args.get('phonenumber')
    return render_template('register_result.html',name=name,email=email,phone=phone)

# For form POST method 
@app.route('/register_result',methods=['POST'])
def register_result_post():
    name = request.form['username']
    email = request.form['email']
    phone = request.form['phonenumber']
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return render_template('register_result.html',name=name,email=email,phone=phone)

# app.add_url_rule('/home','home',home)

if __name__ == '__main__':
    app.run(debug=True)