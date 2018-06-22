import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you meant %s instead? Press Y or N " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "That word does not exists"
        else:
            return "Your entry was wrong, please double check"
    else:
        return "That word does not exists"

word_input = input('Please enter the word that you need: ')

print("You are searcing for {}".format(word_input.lower()))

output = translate(word_input)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
