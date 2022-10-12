from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = dict()


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now()
    currentDate = currentDate.strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    try:
        if int(number)%2==0:
            msg='even'
        elif int(number)%2!=0:
            msg='odd'
    except:
        msg='not an integer!'
    return render_template('result.html', num=number, name=msg)

    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
     return render_template(
        'studentForm.html',
        organizations=[{'orgName': 'Charlotte Hack'}, {'orgName': 'Code 9'}, {'orgName': 'Women who Code'}, {'orgName': 'Runtime teror'}, {'orgName': 'FrontPage Freebirds'}])


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    orgNAme = request.form['organization']
    
    studentOrganisationDetails[studentName] = orgNAme
    
    return render_template(
        'studentDetails.html',
        studentOrganisationDetails=studentOrganisationDetails)

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
