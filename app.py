from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
  return "Hello wrold!!"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
  