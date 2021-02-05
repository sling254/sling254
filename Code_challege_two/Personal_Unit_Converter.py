
name = input("Please key in your name:")
print('-----------------------')
print("Hello " + name + ", welcome to your Pesonal Unit Convertor")
print('>>>>Please choose which conversion you would like to perform')
import inquirer

questions = [
  inquirer.List('units',
                message="Would you like to perform?",
                choices=['cm to inches', 'percent to letter grade', 'Cups to ml', 'grams to ounces', 'fahrenheit to celsius'],
                carousel=True
                
            ),
]
answers = inquirer.prompt(questions)

choose = answers["units"]

def cm_to_inches(value):
    v = value/2.54
    print("The value in inches is: ", v)

def percent_to_letter_grade(Range):
    if Range >= 80 and Range <= 100:
        print("Grade: A")
    elif Range >= 70 and Range < 80:
        print("Grade: B")
    elif Range >=60 and Range <70:
        print("Grade: C")
    elif Range >=50 and Range <60:
        print("Grade: D")
    elif Range >=20 and Range <40:
        print("Grade: E")
    elif Range >=0 and Range <20:
        print("Grade: F")
    else:
        print("Please key in a valid Percentage")

def cups_to_ml(value):
    v = value * 240
    print("The value in ml is: ", v)

def grams_to_ounces(value):
    v = value*28.35
    print("The value in ounces is: ", v)

def fahrenheit_to_celsius(value):
    v = (value-32)/1.8
    print("The value in celsius is: ", v)

if choose == 'cm to inches':

    v = int(input("Enter the value in cm: "))
    cm_to_inches(v)
    
elif choose == 'percent to letter grade':
  
    v = int(input("Enter the Percentage: "))
    percent_to_letter_grade(v)
    
elif choose == 'Cups to ml':
    v =int(input("Enter the value in cups: "))
    cups_to_ml(v)
elif choose == 'grams to ounces':
    v =int(input("Enter the value in grams: "))
    grams_to_ounces(v)
elif  choose == 'fahrenheit to celsius':
    v =int(input("Enter the value in fahrenheit: "))
    fahrenheit_to_celsius(v)

print("GoodBye", name)








