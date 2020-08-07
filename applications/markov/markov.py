print('\n')
print('\n')
print('˚'*75)
import random

# Read in all the words in one go
# with open("applications/markov/input.txt") as f:
with open("input.txt") as f:
    words = f.read()

# Get just the words
split_words = words.split()
# print(split_words) # A single big list of all the words

dataset = {}

# Put all the words into dataset
for i in range(len(split_words)-1):
    word = split_words[i]
    next_word = split_words[i + 1]

    # If it doesn't already exist, add it and the next word
    if word not in dataset:
        dataset[word]=[next_word]

    # If it does already exist, append the next word
    else:
        dataset[word].append(next_word)

    # A list for the sentence starting words
    startwords = []
    for key in dataset.keys():
        if key[0].isupper() or len(key) > 1 and key[1].isupper():
            startwords.append(key)
    word = random.choice(startwords)

    # Sentence construction
    stopped = False
    stop_signs = "?.!"

    while not stopped:
        # A startwords word
        print(word, end=' ')

        # If it's a stop word, stop
        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        # Choose a following word
        following_words = dataset[word]

        word = random.choice(following_words)

# I'm not sure why it's not working, I follow the lecture exactly as far as I could tell. 
# https://youtu.be/j0bxDg0PXRM?t=306

# When he runs it :
# https://youtu.be/j0bxDg0PXRM?t=2062