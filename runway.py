import json
from flask import Flask, Response
from employee import Employee

employee_list = []
for i in range(0,5):
	employee = Employee("first" + str(i), "last")
	employee_list.append(employee)

app = Flask(__name__)
@app.route("/")
def index():

	resp = Response(json.dumps(list(map(lambda e: e.toJSON(), employee_list))))
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp.headers['Content-Type'] = 'application/json'
	return resp

if __name__ == "__main__":
	app.run()

