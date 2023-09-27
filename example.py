from flask import Flask, request, Response
from soap import Soap

app = Flask(__name__)
soap = Soap(app)

@app.route('/JokeServices', methods=['POST'])
def jokeServices():
    soap.deserialize()
    return Response(response = soap.deserialize(), content_type='text/xml; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True)