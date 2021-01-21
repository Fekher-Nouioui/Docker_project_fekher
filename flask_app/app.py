from flask import Flask,render_template,url_for,request
import prediction



app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    data=""
    if request.method == 'POST':
        song_name = request.form['song_name']
        #fileName = '/home/fekher-nouioui/Downloads/Dataset_projet_docker/'+song_name
        fileName = './../prediction_data/'+song_name
        result=prediction.predict(fileName)
        return render_template('index.html',data=result)
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
