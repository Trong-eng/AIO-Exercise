def count_words(file_path):
    counter_words = {}
    words = file_path.split()
    for word in words :
        if word in counter_words:
            counter_words[word] += 1
        else:
            counter_words[word] = 1
    return counter_words
file_path = open('/content/P1_data.txt','r')
file_path = file_path.read()
result = count_words( file_path )
assert result ['who'] == 3
print ( result ['man'])