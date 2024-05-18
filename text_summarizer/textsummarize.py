import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    """Preprocess the text: tokenize, remove stopwords, and lowercase."""
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return sentences, words

def calculate_word_frequency(words):
    """Calculate word frequency in the text."""
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def calculate_sentence_scores(sentences, word_freq):
    """Calculate sentence scores based on word frequency."""
    sentence_scores = {}
    for sentence in sentences:
        for word in word_freq:
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_freq[word]
                else:
                    sentence_scores[sentence] = word_freq[word]
    return sentence_scores

def generate_summary(sentences, sentence_scores, num_sentences=3):
    """Generate summary by selecting top-scoring sentences."""
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary_sentences = [sentence[0] for sentence in sorted_scores[:num_sentences]]
    summary = ' '.join(summary_sentences)
    return summary

def main():
    text = input("enter your text: ")
    
    # Preprocess the text
    sentences, words = preprocess_text(text)
    
    # Calculate word frequency
    word_freq = calculate_word_frequency(words)
    
    # Calculate sentence scores
    sentence_scores = calculate_sentence_scores(sentences, word_freq)
    
    # Generate summary
    summary = generate_summary(sentences, sentence_scores)
    
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()
