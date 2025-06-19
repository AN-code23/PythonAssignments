#Count the frequency of each word in a paragraph using a dictionary
#Hint : each word will be a key and its frequency will be its count in a dict

paragraph = "hello world hello python python world"
word_count = {}
for word in paragraph.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)





