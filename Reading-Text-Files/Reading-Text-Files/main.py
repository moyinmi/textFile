# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as p:
        lines = p.read()
        lines = lines.translate(str.maketrans("","", string.punctuation))
    return lines
result = read_file_content("C:\\Users\\ADMIN\\Downloads\\Reading-Text-Files\\Reading-Text-Files\\story.txt")
print(result)

def count_words():
    text = read_file_content("C:\\Users\\ADMIN\\Downloads\\Reading-Text-Files\\Reading-Text-Files\\story.txt").split()
    # [assignment] Add your code here
    words ={}
    for word in text:
        if word in words:
            words[word] = words[word] + 1
        else: words[word] = 1 
    return words
    
countWords = count_words()
print(countWords)

