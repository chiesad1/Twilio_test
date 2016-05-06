from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your number to this list!
# callers ={
# 	"+12013346493": "Hey boy!"
# }

@app.route("/", methods=['GET','POST'])
def hello_monkey():
	# Get the caller's phone number from the incoming Twilio request
	resp = twilio.twiml.Response()
	resp.say("Hello World!")

	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)