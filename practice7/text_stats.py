def count_words(text):
    words=text.split()
    return len(words)
def average_word_length(text):
    words=text.split()
    d=[]
    for i in words:
        d.append(len(i))
    return(sum(d)/len(d))  


text="djsj shudfi ahd"
print(count_words(text))
print(average_word_length(text))