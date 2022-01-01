from flask import Flask
import mysql.connector


app = Flask(__name__)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

print(mycursor)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
