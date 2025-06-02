from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret-key'  # Secret key for session

# Login Page HTML
login_html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Jewellery Shop Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      padding: 50px;
    }
    .container {
      max-width: 400px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      text-align: center;
    }
    input, button {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
    }
    .error { color: red; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Login to Jewellery Shop</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="Username" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    {% if error %}
    <p class="error">{{ error }}</p>
    {% endif %}
  </div>
</body>
</html>
'''

# Dashboard Page HTML
dashboard_html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Dashboard - Jora Jewellers</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      padding: 40px;
    }
    .container {
      max-width: 1000px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h2 {
      text-align: center;
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 15px;
      margin-top: 20px;
    }
    .gallery img {
      width: 100%;
      border-radius: 10px;
      box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }
    button {
      padding: 10px 20px;
      margin-top: 20px;
      background-color: #f44336;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Welcome to Jora Jewellers!</h2>
    <p style="text-align:center;">You are successfully logged in.</p>
    <div class="gallery">
      <img src="{{ url_for('static', filename='gold-ring.jpeg') }}" alt="Gold Ring" />
      <img src="{{ url_for('static', filename='Payal-1.jpeg') }}" alt="Payal 1" />
      <img src="{{ url_for('static', filename='Payal-2.jpeg') }}" alt="Payal 2" />
      <img src="{{ url_for('static', filename='Payal-3.jpeg') }}" alt="Payal 3" />
      <img src="{{ url_for('static', filename='Payal-4.jpeg') }}" alt="Payal 4" />
      <img src="{{ url_for('static', filename='Payal-5.jpeg') }}" alt="Payal 5" />
    </div>
    <a href="{{ url_for('logout') }}"><button>Logout</button></a>
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Jora Jewellers" and password == "Manoj@320":
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password!"
    return render_template_string(login_html, error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template_string(dashboard_html)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
