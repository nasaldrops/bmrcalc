from flask import Flask, render_template, request

app = Flask(__name__)

#This loads the very first page as if visiting the website for the first time.
@app.route('/')
def home():
    #test = 'index page loaded'
    buttoninfo = 'Calculate Your BMR'
    
    return render_template('index.html', buttoninfo = buttoninfo)#, gendervalue = gendervalue)#, test=test)


#When button is pressed, request.form kicks into action. In this instacnce the app looks to see what the gender is. It looks to see if gender is true, then it strips out the
#values from the corresponding input boxes. Removed GET.
@app.route('/', methods = ['POST'])
def bmrcalc():
    try:

        if "gender" in request.form:

    
            genderselected = request.form.get('gender')
            age = float(request.form['age'])
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            gender = request.form['gender']
            htmlinfo = 'Your BMR is: '
            print(genderselected)
            weightlbs = round((weight * 2.20462),2)
            weightinlbs = 'Your weight in lbs: '
    except:
        pass
  
        
        
    try:    
        if gender == '1':
            bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
            bmrstr = 'Your BMR is: ' + str(bmr)
            print(genderselected)
                 
        else:
            bmr = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
            bmrstr = 'Your BMR is: ' + str(bmr)
            print(genderselected)
               
        return render_template('index.html', htmlinfo = htmlinfo, buttoninfo = bmrstr, yourbmr = bmr, yourage = age, yourweight = weight, gender = gender, yourheight = height,genderselected=genderselected, weightinlbs = weightinlbs, weightlbs = weightlbs)#, gendervalue = gendervalue)
    except:
        buttoninfo = 'Enter Valid Inputs'
        return render_template('index.html', buttoninfo = buttoninfo)#, gendervalue = gendervalue)#, test=test)



if __name__== '__main__':
    
    app.run() 
    #app.run(host='192.168.1.5', port=5000) #running on RPi
