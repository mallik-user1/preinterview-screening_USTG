sentence = "which is better python 2 or python 3"
# Split the sentece in to the words
words = sentence.split(" ")
#print("words,", words)
# using dictionary comprehension iterate all words and increment count for each word
new_dict= {x:words.count(x) for x in words}
print("output", new_dict)
