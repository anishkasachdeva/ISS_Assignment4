
Lab Name 	: Natural Language Processing Lab
Experiment Name : Morphology
# Objective

Objective of the experiment is to rewrite the whole experiment in python using flask , ajax,and databases.

How to run :
	To run the server, open the port on localhost using the app.py file.

Domain is http://127.0.0.1:5000 . 
	On opening it in browser, you'll be first navigated to Introduction page.



### Prerequisites
------

python3
Flask
Flask-SQLAlchemy



## Built With
-------
* [Flask]
* [Python]
* HTML,CSS and JS - For all the web development aspects




## Design of our Project
-------
-->Main object here is writing a website using another webframework FLASK.
-->We have used that code which was already written , and modified to the format such that flask uses
-->We wrote experiment section of project using HTML,CSS ,JS and sent the values to python script which will send back the corresponding correct answer

 -->All this was done using AJAX's POST and GET requests.
 -->The quiz section of this project was implemented using a database 
 -->All the resources for the file are self-contained in the "static" folder and is loaded from the server side.
-->The project was co-ordinated using GITHUB/GITLAB giving us an opportunity to learn how to do collaborative work as well.
-->We also included unit testing by running some manual test-cases and checking the values by inputting them to the backend and checking the final result.



## IMPLEMENTATION
-->We used Flask webframework
--> Required folder structure of static and templates have been created 
-->Implementation of databases has been done in the Quiz section of the experiment , using sql



### File Description
app (folder) :
			This folder contains all html, css, javascript files and python files.
-- app/ –> All the code for the application (Static and Template Files) <br/>
-- app/templates/ –> All HTML Files are located here,which will be rendered<br/>
-- app/static/ –> all css,js files are here.Also , images also located here which are required for experiment <br/>
-- app/static/css,js -> all css and js files required 
-- app/static/js/exp.js –> this file includes AJAX for sending requests to database and getting back data <br/>
-- app/static/vendors ->




### HTML Files

-- Theory.html,Experiment.html,Procedure.html,Objective.html,Quizzes.html,Further_Readings.html,Feedback.html --> are loaded on every corresponding request. Instead of routing files from the backend we are aiming to perform frontend routing and hence we only render one html file once. <br/>
-- Any user action only changes the content of the html file and does not refresh the page. <br/>
Information on different pages

	Introduction:
				This page gives the description about what Morphology is.
				Morphology is the study of words, how they are formed, and their relationship to other words in the same language.
				It analyzes the structure of words and parts of words, such as stems, root words, prefixes, and suffixes.

	Theory:
			This page gives more knowledge about what morphemes are and how the addition and deletion of morphemes from a word changes its form and meaning.

	Experiment:
				This page is the actual experiment page where you can perform the experiment on Morphology.
				Before performing the experiment, go through Procedure.

	Quizzes:
			This page is the actual experiment page where you can perform the experiment on Morphology.
			Before performing the experiment, go through Procedure.

	Further Readings :
					This page gives you information for more materials to read about Morphology.	
	
	Experiment:
	          First a drop-down box is given, which contains the rootwords to select.
			  On selecting the rootword,now the user has to select the morphemes to be deleted from the rootword and to be added to the rootword from the 8 dropdowns given in the table according to the "Number" and "Case" mentioned in the table.
			  On selecting corresponding answers, click on Submit button.
			  According to the correctness and incorrectness of the options selected from the dropdowns, the "correct symbol" and "wrong symbol" will be displayed in front of the corresponding row.
			  If all are correct, the message "Correct Answer!" is displayed.
			  If any of them is incorrect, the message "Wrong Answer!" is displayed with the correct answer table.


## Authors

Anishka Sachdeva - [anishkasachdeva](https://github.com/anishkasachdeva/)
Lakshmi Madhuri Yarava -  [madhuriyarava](https://github.com/madhuriyarava/)

## Acknowledgments

Our Teaching Assistant **Mugdha Abhyankar** who helped us in doing this project
