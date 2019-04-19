#!/usr/bin/env python3
from flask import Flask,render_template,request,jsonify, send_file,json
import sqlite3
db = sqlite3.connect('data.db', check_same_thread=False)
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS data(a1 TEXT, a2 TEXT,
                       a3 TEXT, a4 TEXT)
	''')
db.commit()
app = Flask(__name__)

@app.route('/')
@app.route('/Introduction.html')
def introduction():
	return render_template('Introduction.html')

@app.route('/Experiment.html')
def experiment():
	return render_template('Experiment.html')

@app.route('/Theory.html')
def theory():
		return render_template('Theory.html')

@app.route('/Procedure.html')
def procedure():
		return render_template('Procedure.html')

@app.route('/Objective.html')
def objective():
	return render_template('Objective.html')

@app.route('/Further Readings.html')
def furthereadings():
	return render_template('Further Readings.html')

@app.route('/Quizzes.html')
def quizzes():
	return render_template('Quizzes.html')

@app.route('/default.html')
def default():
	return render_template('default.html')

@app.route('/content.html')
def content():
	return render_template('content.html')

@app.route('/template1.html')
def template():
	return render_template('template1.html')


@app.route('/Feedback.html')
def feedback():
	return render_template('Feedback.html')


@app.route('/process',methods=['POST'])
def process():
	inputdata = request.form['word']
	del11 = request.form['del1']
	add11 = request.form['add1']
	del22 = request.form['del2']
	add22 = request.form['add2']
	del33 = request.form['del3']
	add33 = request.form['add3']
	del44 = request.form['del4']
	add44 = request.form['add4']

	WORDS = ["बच्चा","लड़का","घोड़ा","गधा","बच्ची","लड़की","नदी","गली","माला","लता","शाखा","गाथा","माली","जोहरी","कूली","आदमी"]

	CORRECT_ANS_1 = ["आ","आ","आ","आ","आ","ए","ए","ओं"]
	#CORRECT_ANS_1 = [["Delete","Add","Number","Case"],["आ","आ","sing","dr"],["आ","आ","plu","dr"],["आ","आ","sing","ob"],["आ","आ","plu","ob"]]
	CORRECT_ANS_2 = ["ई","ई","ई","ई","ई","इयाँ","ई","इयों"]
	#CORRECT_ANS_2 = [["Delete","Add","Number","Case"],["ई","ई","sing","dr"],["ई","इयाँ","plu","dr"],["ई","ई","sing","ob"],["ई","इयों","plu","ob"]]
	CORRECT_ANS_3 = ["आ","आ","आ","आ","आ","आयें","आ","आओं"]
	#CORRECT_ANS_3 = [["Delete","Add","Number","Case"],["आ","आ","sing","dr"],["आ","आयें","plu","dr"],["आ","आ","sing","ob"],["आ","आओं","plu","ob"]]
	CORRECT_ANS_4 = ["ई","ई","ई","ई","ई","ई","ई","इयों"]
	#CORRECT_ANS_4 = [["Delete","Add","Number","Case"],["ई","ई","sing","dr"],["ई","ई","plu","dr"],["ई","ई","sing","ob"],["ई","इयों","plu","ob"]]

	if inputdata==WORDS[0] or inputdata==WORDS[1] or inputdata==WORDS[2] or inputdata==WORDS[3]:
		count=1
		if del11==CORRECT_ANS_1[0] and add11==CORRECT_ANS_1[4]:
			ans1="correct"
		else:
			ans1="incorrect"

		if del22==CORRECT_ANS_1[1] and add22==CORRECT_ANS_1[5]:
			ans2="correct"
		else:
			ans2="incorrect"

		if del33==CORRECT_ANS_1[2] and add33==CORRECT_ANS_1[6]:
			ans3="correct"
		else:
			ans3="incorrect"

		if del44==CORRECT_ANS_1[3] and add44==CORRECT_ANS_1[7]:
			ans4="correct"
		else:
			ans4="incorrect"
		return jsonify({'ans1' : ans1,'ans2' : ans2,'ans3' : ans3,'ans4' : ans4,'count' : count})


	elif inputdata==WORDS[4] or inputdata==WORDS[5] or inputdata==WORDS[6] or inputdata==WORDS[7]:
		count=2
		if del11==CORRECT_ANS_2[0] and add11==CORRECT_ANS_2[4]:
			ans1="correct"
		else:
			ans1="incorrect"

		if del22==CORRECT_ANS_2[1] and add22==CORRECT_ANS_2[5]:
			ans2="correct"
		else:
			ans2="incorrect"

		if del33==CORRECT_ANS_2[2] and add33==CORRECT_ANS_2[6]:
			ans3="correct"
		else:
			ans3="incorrect"

		if del44==CORRECT_ANS_2[3] and add44==CORRECT_ANS_2[7]:
			ans4="correct"
		else:
			ans4="incorrect"
		return jsonify({'ans1' : ans1,'ans2' : ans2,'ans3' : ans3,'ans4' : ans4,'count' : count})


	elif inputdata==WORDS[8] or inputdata==WORDS[9] or inputdata==WORDS[10] or inputdata==WORDS[11]:
		count=3
		if del11==CORRECT_ANS_3[0] and add11==CORRECT_ANS_3[4]:
			ans1="correct"
		else:
			ans1="incorrect"

		if del22==CORRECT_ANS_3[1] and add22==CORRECT_ANS_3[5]:
			ans2="correct"
		else:
			ans2="incorrect"

		if del33==CORRECT_ANS_3[2] and add33==CORRECT_ANS_3[6]:
			ans3="correct"
		else:
			ans3="incorrect"

		if del44==CORRECT_ANS_3[3] and add44==CORRECT_ANS_3[7]:
			ans4="correct"
		else:
			ans4="incorrect"
		return jsonify({'ans1' : ans1,'ans2' : ans2,'ans3' : ans3,'ans4' : ans4,'count' : count})



	elif inputdata==WORDS[12] or inputdata==WORDS[13] or inputdata==WORDS[14] or inputdata==WORDS[15]:
		count=4
		if del11==CORRECT_ANS_4[0] and add11==CORRECT_ANS_4[4]:
			ans1="correct"
		else:
			ans1="incorrect"

		if del22==CORRECT_ANS_4[1] and add22==CORRECT_ANS_4[5]:
			ans2="correct"
		else:
			ans2="incorrect"

		if del33==CORRECT_ANS_4[2] and add33==CORRECT_ANS_4[6]:
			ans3="correct"
		else:
			ans3="incorrect"

		if del44==CORRECT_ANS_4[3] and add44==CORRECT_ANS_4[7]:
			ans4="correct"
		else:
			ans4="incorrect"
		return jsonify({'ans1' : ans1,'ans2' : ans2,'ans3' : ans3,'ans4' : ans4,'count' : count})

@app.route('/quiz',methods=['POST'])
def quiz():
	cursor = db.cursor()
	a1 = request.form['ans1']
	a2 = request.form['ans2']
	a3 = request.form['ans3']
	a4 = request.form['ans4']
	if a1 or a2 or a3 or a4 :
		cursor.execute('''INSERT INTO data(ans1,ans2,ans3,ans4) VALUES(?,?,?,?)''', (a1,a2,a3,a4))
		db.commit()
		cursor.execute("SELECT * FROM data")
		print(cursor.fetchall());
		return jsonify({'sucess' : 'Response has been recorded'})
	else:
		return jsonify({'error' : 'Please answer atleast one question'})



if __name__ == '__main__':
	app.run(debug=True)
