from flask import Flask , render_template
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route('/about')
def about(): # about page
    return render_template("about.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")# profile page
    
@app.route('/contact')
def contact():
    return render_template("contact.html")# contact page

if __name__ == '__main__':
    app.run(debug=True)