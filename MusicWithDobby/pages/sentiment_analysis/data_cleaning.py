# data cleaning
import string
# import nltk

from collections import Counter
from matplotlib import pyplot as plt
# from nltk.tokenize import word_tokenize
# from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from dataclasses import dataclass

text = open('chat.txt',encoding = 'utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = cleaned_text.split()
# tokenized_words = word_tokenize(cleaned_text, "english")

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# print(final_words)
list = []
emotion_list = []
with open('pages\sentiment_analysis\emotions.txt', 'r') as file:
    for line in file:
        # print(line)
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        list.append(emotion)
        if word in final_words:
            emotion_list.append(emotion)   
# print(set(list))
w = Counter(emotion_list)
print(w)

@dataclass
class Mood:
    emoji : str
    score : float

def get_mood(sentiment_text , threshold):
    score : float = TextBlob(sentiment_text).sentiment.polarity

    friendly_threshold : float = threshold
    hostile_threshold : float = -threshold

    if score >= friendly_threshold:
        return Mood('😄',score)
    elif score <= hostile_threshold:
        return Mood('😟',score)
    else:
        return Mood('😐',score)

def emotion(score):
    if score<= -0.3:
        return 'Sad'
    if score> -0.3 and score<=0.3:
        return 'Calm'
    if score< 0.8 and score>0.3:
        return 'Happy'
    if score>=0.8:
        return 'Energetic'
    
def use():

    Score = get_mood(cleaned_text, threshold = 0.3).score
    return emotion(Score)


# graph
# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# fig.autofmt_xdate()
# plt.savefig('graph.png')
# plt.show()
