import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class MovieReviewAnalyzer:
    def __init__(self):
        nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_review_sentiment(self, review):
        sentiment_score = self.analyzer.polarity_scores(review)['compound']
        if sentiment_score >= 0.05:
            return "Positive"
        elif sentiment_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

def main():
    print("Welcome to the Movie Review Sentiment Analyzer!")
    analyzer = MovieReviewAnalyzer()

    # Input movie review from the user
    review = input("Enter your movie review: ")

    # Analyze the sentiment of the review
    sentiment = analyzer.analyze_review_sentiment(review)
    print(f"The sentiment of the movie review is: {sentiment}")

if __name__ == "__main__":
    main()
