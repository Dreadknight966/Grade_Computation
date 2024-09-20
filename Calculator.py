from flask import Flask, render_template, request


calculator = Flask(__name__)

@calculator.route('/')
def index():
    return render_template('index.html')

@calculator.route('/calculate',methods=['POST'])
def calculate():
    x= 0
    y=0
    z=0
    y_dean=0
    z_dean=0
    message = ""
    qualifymessage = ""
    dean_passing_grade = 90
    passing_grade = 75
    x_weight = .20
    y_weight = .30
    z_weight = .50
    x = float(request.form['x'])
    a = int(request.form['a'])


    if a >= 4:
        message = "Sorry it is not possible for you to pass :D"
        y = 0
        z = 0
    elif a < 4 and x < 50.5:
        qualifymessage = "Sorry you can't qualify for dean's list :D"
        message = "You can pass :D"
        
        prelim_contribution = x * x_weight
        needed_for_passing = passing_grade - prelim_contribution
        
        grade_needed = needed_for_passing / (y_weight + z_weight)
        y = grade_needed
        z = grade_needed
    elif x >= 50 and a < 4:
        message = "You can pass :D"
        qualifymessage = "You have a chance qualilfy for dean's list :D"
       
        prelim_contribution = x * x_weight
        needed_for_passing = passing_grade - prelim_contribution
        
        grade_needed = needed_for_passing / (y_weight + z_weight)
        y = grade_needed
        z = grade_needed

        dean_grade_needed = dean_passing_grade - prelim_contribution
        dean_grade = dean_grade_needed / (y_weight + z_weight)
        y_dean = dean_grade
        z_dean = dean_grade
    else:
        qualifymessage = "You can't qualify for dean's list :D"
        y_dean = 0
        z_dean = 0

    return render_template('index.html', midterms = y, finals = z, message = message, qualifymessage = qualifymessage, Midterms_dean = y_dean, Finals_dean = z_dean)


if __name__ == '__main__':
    calculator.run(debug=True)