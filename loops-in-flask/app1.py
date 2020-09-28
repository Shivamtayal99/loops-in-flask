from flask import Flask,render_template
app = Flask(__name__)

@app.route('/loopsinflask')
def loopinflask():
    list1=['Shivam','Shubham','Monu','Sonu','Vishal']
    return render_template('index.html',list=list1)

app.run(port=5001,debug=True)
