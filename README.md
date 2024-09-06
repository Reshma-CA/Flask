# Flask Project
This is a simple Flask project that demonstrates how to create a basic web application using the Flask framework. The application includes a homepage and some basic routes.

## Features

- Minimal Flask setup
- Basic routing with home page,About page,Product page,Contact page, Login page, Admin Dashboard page
- Extendable structure with static files and templates

- ## Login Page
![img1](https://github.com/user-attachments/assets/44721904-8237-49d2-9155-0e6e5cfbf72f)

 ## Admin Page
![admin](https://github.com/user-attachments/assets/1daa56f4-9cc0-41e1-b0e0-a1157b415a9c)
 ## Home Page
![home](https://github.com/user-attachments/assets/28878462-d18e-4982-9ced-3e37dc3bdd8a)

 ## About Page
 ![about](https://github.com/user-attachments/assets/c19f6a1a-a8fc-48c0-ab73-70218263b5c6)

 ## Products Page
 ![products](https://github.com/user-attachments/assets/7db1b164-a402-41c1-86d0-b81408728fb7)

 ## Contact Page
![contact](https://github.com/user-attachments/assets/8d280f02-7749-453c-8f79-670448c2ef46)

   

## Flask

Python Flask is a micro web framework written in Python. It's designed to be lightweight, simple, and easy to use, making it a popular choice for developing web applications. Flask provides the essential tools to build web applications, such as routing (URL mapping), request handling, and template rendering, but it doesn't include many features out of the box. This minimalist approach allows developers to add only the components they need, making Flask flexible and scalable for both small and large applications.

### Key Features of Flask

#### 1.Lightweight
 Flask has a simple core and relies on extensions to add additional functionality, keeping the base framework small and fast.
#### 2.Routing
 Flask allows you to map URLs to specific functions, making it easy to define how your web application responds to different routes.
#### 3.Templates 
Flask uses Jinja2, a powerful templating engine, to help you generate HTML dynamically.

#### 4.Flexibility 
You can easily integrate Flask with various databases, APIs, and front-end technologies.

#### 5.Extensibility
 Flask supports numerous extensions to add features like authentication, form handling, and database integration.

#### 6.Development Server 
Flask comes with a built-in development server that provides useful debugging information and reloads automatically when code changes are detected.



## Set Up a Flask Project

#### 1.Install Flask
First, ensure you have Python installed. Then, install Flask in a virtual environment.

```bash
mkdir flask_project
cd flask_project
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
pip install Flask

```
#### 2.Create the Flask App
Inside your project folder, create a file called app.py with the following content

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

```
#### 3.Test the Flask App
Run the app


```bash
python app.py

```

