# import requests

# class HoroscopePredictor:
#     def __init__(self, birth_date, zodiac_sign):
#         self.birth_date = birth_date
#         self.zodiac_sign = zodiac_sign

#     def fetch_horoscope(self):
#         url = f"https://horoscope-api.herokuapp.com/horoscope/{self.zodiac_sign.lower()}/{self.birth_date}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()['horoscope']
#         else:
#             return "Failed to fetch horoscope data."

#     def generate_personalized_predictions(self):
#         # Generate personalized predictions based on birth date and zodiac sign
#         # This can be customized based on astrological beliefs or general trends

#         personalized_predictions = f"Today's personalized predictions for {self.zodiac_sign}:"
#         if self.zodiac_sign == 'Aries':
#             personalized_predictions += "You may feel a surge of energy and enthusiasm today. It's a good time to start new projects."
#         elif self.zodiac_sign == 'Taurus':
#             personalized_predictions += "You may experience a sense of stability and security today. Focus on nurturing your relationships."
#         # Add more personalized predictions for other zodiac signs

#         return personalized_predictions

#     def get_daily_predictions(self):
#         horoscope = self.fetch_horoscope()
#         personalized_predictions = self.generate_personalized_predictions()

#         return f"Today's horoscope for {self.zodiac_sign}:\n{horoscope}\n\n{personalized_predictions}"

# def main():
#     print("Welcome to the Personalized Horoscope Predictor!")

#     # Gather user information
#     birth_date = input("Enter your birth date (MM-DD): ")
#     zodiac_sign = input("Select your zodiac sign: ")

#     # Create HoroscopePredictor instance
#     predictor = HoroscopePredictor(birth_date, zodiac_sign)

#     # Get and display daily predictions
#     predictions = predictor.get_daily_predictions()
#     print(predictions)

# if __name__ == "__main__":
#     main()



import requests

class HoroscopePredictor:
    def __init__(self):
        self.api_url = "https://horoscope-api.herokuapp.com/horoscope/{sign}/{date}"

    def get_horoscope(self, sign, date):
        url = self.api_url.format(sign=sign.lower(), date=date)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['horoscope']
        else:
            return "Failed to fetch horoscope data."

def main():
    print("Welcome to the Personalized Horoscope Predictor!")
    predictor = HoroscopePredictor()

    # Input user's birth date and zodiac sign
    birth_date = input("Enter your birth date (MM-DD): ")
    zodiac_sign = input("Enter your zodiac sign: ")

    # Get horoscope prediction for the user
    horoscope = predictor.get_horoscope(zodiac_sign, birth_date)
    print("Here's your personalized horoscope prediction for today:")
    print(horoscope)

if __name__ == "__main__":
    main()
