from flask import Flask, jsonify
from count.wordcount import count_file
app = Flask(__name__)

WORDS  = ["han","hon","hen","den","det","denne","denna"]
w_count = {}

@app.route('/wordcount/api/v1.0/get_wordcount', methods=['GET'])
def get_wordcount():
        return jsonify(count_file("05cb5036-2170-401b-947d-68f9191b21c6",w_count,WORDS))


if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)
