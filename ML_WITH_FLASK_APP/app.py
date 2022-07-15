from flask import Flask,render_template,url_for

app = Flask(__name__)

topics= [
    {
    'Title':'EDA',
    'Problem':'Analysis',
    'Explanation':'Cleaning of data to the Required shape'
  },
  {
    'Title':'Data Analytics',
    'Problem':'Visualization',
    'Explanation':'Visualization of the data using graphs'
  },
]

@app.route("/")
@app.route("/Home")
def home():
    return render_template("Home.html")
@app.route("/About")
def about():
   return render_template("About.html",title='About')
@app.route("/Topics")
def Topics():
   return render_template("Topics.html",topics=topics,title='Topics')


if __name__=='__main__':
    app.run(debug=True)