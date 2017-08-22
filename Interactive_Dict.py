

import json
from difflib import get_close_matches

with open("C:\\Users\\ar1\\PycharmProjects\\Python_Dev\\data.json") as json_file:
    json_data = json.load(json_file)

def find_word(word):
    word = word.lower()
    if word in json_data:
        return json_data[word]
    elif len(get_close_matches(word,json_data.keys())[0])>0:
        print(" Looks like there is a spelling mistake. Found this word instead :  {}".format(get_close_matches(word,json_data.keys())[0]))
        new_word= get_close_matches(word,json_data.keys())[0]
        return json_data[new_word]
    else:
        return "The word is not found. Sorry"

word= input("Enter the word please:")

output = find_word(word)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)



