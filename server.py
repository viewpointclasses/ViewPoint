from flask import Flask, request,render_template
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/courses',methods=['GET'])
def services():
    return render_template('services.html')
@app.route('/blog',methods=['GET'])
def blog():
    return render_template('blog-home-2.html')
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')
@app.route('/blogpost',methods=['GET'])
def blogpost():
    return render_template('blog-post.html')
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80)