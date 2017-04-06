import sys

words = []

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    last_word = line[-1]
    words.append(last_word)

for word in words:
    print word
