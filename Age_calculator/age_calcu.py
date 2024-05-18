import datetime
import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 130)  
    engine.setProperty('volume', 190)  
    engine.setProperty("voice","english_rp")
    engine.say(text)
    engine.runAndWait()

class human:
    def __init__(self):
        self.name=input("enter the name of the person:- ")
        self.age=int(input("enter the age of a person:- "))
        self.country=input("enter your country name where you were bron:- ")
        self.year_birth = int(input("Enter the year of birth (YYYY): "))
        self.month_birth = int(input("Enter the month of birth (MM): "))
        self.day_birth = int(input("Enter the day of birth (DD): "))
        self.date_birth=datetime.date(self.year_birth,self.month_birth,self.day_birth)
        print(f"your name is {self.name}, your age is {self.age} and your date of birth is {self.date_birth}, place of birth is {self.country}")
        speak(f"your name is {self.name}, your age is {self.age} and your date of birth is {self.date_birth}, place of birth is {self.country}")
    def find(self):
        today=datetime.date.today()
        age=today-self.date_birth
        age_days=age.days
        age_years=age_days//365
        print(f"your correct age is--{age_years}--please dont messup with your age")
        speak(f"your correct age is--{age_years}--please dont messup with your age")

    
person=human()
person.find()