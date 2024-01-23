sentence = "which is better python 2 or python 3"
words = sentence.split(" ")
print("words,", words)
new_dict= {x:words.count(x) for x in words}
print("output", new_dict)
