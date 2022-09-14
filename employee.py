import json

class Employee:
	def __init__(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__)
