# This script reads the lines from a text file
# and returns a random line printed with a ascii font
# one word at a time
# Usage:
# install pip
#  sudo easy_install pip
# install feedparser
#  sudo pip install pyfiglet
# run the script
#  python oracolo.py [input_text_file]
# if you want to use the questions from domande.txt
# (the script was made for them)
#  python oracolo.py domande.txt

import sys
from random import randint
from pyfiglet import Figlet

filepath = sys.argv[1]
text = open(filepath, "r")
questions = text.readlines()
index = randint(1, len(questions))
random_question = questions[index]
#print random_question
words = random_question.split()
f = Figlet(font='slant')
for word in words:
	print f.renderText(word)