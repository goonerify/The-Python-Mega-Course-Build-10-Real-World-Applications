import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_canonical_str(val):
    upper = val.upper()
    lower = val.lower()
    cap = val.capitalize()
    title = val.capitalize()

    return (upper, lower, cap, title)

def translate(w):
    for key in get_canonical_str(w):
        if key in data:
            return data[key]

    matches = get_close_matches(w, data.keys(), cutoff=0.8)
    if len(matches) > 0:
        response = input(f"Did you mean {matches[0]}? Enter Y if yes, or N if no.")

        if response.lower() == 'y':
            return translate(matches[0])
        elif response.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "I didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for datastr in output:
        print(f"{datastr}")
elif type(output) == str:
    print(f"{output}")

