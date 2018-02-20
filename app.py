from flask import Flask, render_template, request, json, jsonify

app = Flask('FaaS')


@app.route("/")
def test(word):
	return "word..."

@app.route("/home", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		query = request.form['query']
		string = request.form['list']
		delimiter = request.form['delimiter']

		choices = string.split(delimiter)

		resultDict ={"Query": query, "List": choices}

		response = jsonify(resultDict)
		result = json.dumps(resultDict, sort_keys = False, indent = 4).replace("\n", "").replace("\\", "").replace("\"", "")
		print(result)
		return render_template("index.html", result=result)
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)