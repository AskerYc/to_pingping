from flask import Flask,send_file
from flask import render_template
import os
from flask import send_from_directory

app = Flask(__name__)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)))#html是个文件夹

@app.route('/welcome_pingping')
def index():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./index.html")

@app.route('/js/Key.js')
def index1():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./js/Key.js")


@app.route('/js/game.js')
def index2():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./js/game.js")

@app.route('/js/popup.js')
def index3():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./js/popup.js")

@app.route('/js/soundjs-0.6.0.min.js')
def index4():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./js/soundjs-0.6.0.min.js")


@app.route('/css/index.css')
def index5():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./css/index.css")


@app.route('/css/intro.png')
def index6():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./css/intro.png")

@app.route('/css/levels_bg.png')
def index7():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./css/levels_bg.png")

@app.route('/audio/jazz.mp3')
def index8():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/jazz.mp3")

@app.route('/audio/rewind.mp3')
def index9():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/rewind.mp3")

@app.route('/audio/step.mp3')
def index10():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/step.mp3")

@app.route('/audio/unlock.mp3')
def index11():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/unlock.mp3")

@app.route('/assets/clock.png')
def index12():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./assets/clock.png")

@app.route('/assets/door.png')
def index13():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./assets/door.png")

@app.route('/assets/key.png')
def index14():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./assets/key.png")

@app.route('/assets/peep.png')
def index15():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./assets/peep.png")


@app.route('/favicon.png')
def index16():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./favicon.png")


@app.route('/audio/ding.mp3')
def index17():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/ding.mp3")

@app.route('/audio/error.mp3')
def index18():
	# return render_template("index.html")
	# return send_from_directory(root, "index.html")
	return send_file("./audio/error.mp3")



if __name__ == '__main__':
	app.run(debug=True)