import string
def get_most_common_letter(text):

    counter = {}
    for char in text:
#         counter[char] = counter.get(char, 0) + 1
        if char in string.ascii_lowercase: #added this to take out punctuations and spaces
            counter[char] = text.count(char)

    # letter = sorted(counter.items(), key=lambda item: item[1])[0][1] #returns 7, expected "o"
    # print(sorted(counter.items(), key=lambda item: item[1])) #[('o', 7), ('e', 4), ('r', 4), ('f', 4), ('t', 3), ('h', 3), ('i', 2), ('s', 1), ('n', 1)]
    letter = sorted(counter.items(), key=lambda x:x[1], reverse=True)[0][0]
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")