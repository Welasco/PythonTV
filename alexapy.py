from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"
    #return render_template('home.html')


@app.route("/api/tv/")
def tv():
    return "TV!"


@app.route('/alexa/television', methods=['POST'])
def television():
    #content = request.json
    print(request.headers)
    #print(request.get_json(silent=False))
    #print(request.get_json(force=True))
    print(request.get_json())
    #print(request.data)
    #r = "{\"test\": \"test\"}"
    #r = r'{"test": "test"}'
    r = '''
    {
          "version": "1.0",
          "sessionAttributes": {
            "supportedHoroscopePeriods": {
              "daily": true,
              "weekly": false,
              "monthly": false
            }
          },
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "Uhuuuu so far so good!"
            },
            "card": {
              "type": "Simple",
              "title": "Television",
              "content": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless."
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Can I help you with anything else?"
              }
            },
            "shouldEndSession": false
          }
    }
    '''
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0')
