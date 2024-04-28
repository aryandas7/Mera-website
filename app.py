#print("Hello, World")
#xxxx
#print(__name__)

#xxxx

#from flask import Flask
#app=Flask(__name__)
#@app.route("/")
#def hello_world():
#  return "Hello, Aryan"

#print(__name__)
#if __name__=="__main__":
#  print("I am inside if now")

#if __name__=="__main__":
#  app.run(host="0.0.0.0",debug=True)
#xxxx
from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
  return render_template('Home.html')

print(__name__)
if __name__=="__main__":
  print("I am inside if now")

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)

#xxxx
