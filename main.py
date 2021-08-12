import json

INPUT_FILE_PATH = "tokipona.json"

with open(INPUT_FILE_PATH, "r") as input_file:
    toki_pona_dict = json.load(input_file)

toki_phrase = ""

while True:
    toki_phrase = input("Enter toki pona phrase (q to quit):\n")
    if toki_phrase == "q":
        break
    words = toki_phrase.split(" ")
    output = ""
    for word in words:
        if word in toki_pona_dict:
            output += toki_pona_dict[word]
        else:
            output += word
        output += " "

    print("Translation:", output, sep="\n")