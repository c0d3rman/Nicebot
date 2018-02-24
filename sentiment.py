# This file is used to experiment with different sentiment analysis models and qualitatively evaluate them.

sentences = [
	"I really do enjoy a good wine",
	"I like to hate Michael Bay films, but I couldn't fault this one",
	"This is at least as yummy as the cheese",
	"This is the least yummy cheese"
]


import time
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from pattern.en import sentiment

for sentence in sentences:
	print sentence + "\n****************"

	# TextBlob
	start = time.time()
	blob = TextBlob(sentence, analyzer=NaiveBayesAnalyzer())
	end = time.time()
	print "TextBlob: " + str(blob.sentiment.p_pos) + "% positive (" + str(end - start) + ")"

	# pattern.en
	start = time.time()
	s = sentiment(sentence)
	end = time.time()
	print "pattern.en: " + str(s[0]) + "% positive (" + str(end - start) + ")"

	print "\n"