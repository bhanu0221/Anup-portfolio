from flask import Flask, redirect, render_template, request, url_for
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/memories')
def memories():
    image_folder = os.path.join(app.static_folder, 'images', 'memories')
    image_files = os.listdir(image_folder)
    image_urls = [
        url_for('static', filename=f'images/memories/{img}')
        for img in image_files if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    return render_template('memories.html', images=image_urls)



if __name__ == '__main__':
    app.run(debug=True)
