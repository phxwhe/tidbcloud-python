# import necessary packages
import flask
import json
import mysql.connector

# create the flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to TiDB Cloud
config = {
    'host': 'tidb.72f6f72.e93d9e16.us-west-2.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': 'pingcap',
    'password': 'pingcap1',
    'database': 'demo'
}


@app.route('/fruit', methods=['GET'])
def index():
   conn = mysql.connector.connect(**config) 
   cur = conn.cursor()
   cur.execute("SELECT * FROM fruit")

   row_headers=[x[0] for x in cur.description]
   myresult = cur.fetchall()
   json_data=[]
   for result in myresult:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)


# run the app
app.run()
