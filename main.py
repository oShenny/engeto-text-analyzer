"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Šenk
email: oshenny@icloud.com
"""

# * 3 paragraphs to be analyzed by verified user. He may choose each of paragraphs in the TEXTS. No other is available.
TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]
line = 60 * "-"

# ? LOGIN ----------------------------------------------------------------------------------

# * verified users who are able to use the program.
verified_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

entered_user = input("username: ")
entered_password = input("password: ")

# * Condition verifying if user-entered credentials match our verified users.
if entered_user in verified_users:
    if verified_users[entered_user] == entered_password:
        print(line)
        print(f"Welcome to the app, {entered_user.capitalize()}!")
        print("This app analyzes three paragraphs and shows text statistics.")
        print(line)
    else:
        print(f"Your password is incorrect. Program terminating...")
        exit()
else:
    print(f"User is not registered. Program terminating...")
    exit()

# ? SELECTING PARAGRAPH --------------------------------------------------------------------

selected_paragraph = input("Enter a number (1-3) to select a paragraph: ")

# * Condition verifying if the user-entered number is within the range of 1 to 3 to select a paragraph for analysis.
if selected_paragraph.isdigit():
    sp_int = int(selected_paragraph) - 1

    if sp_int in range(0, 3):
        pass
    else:
        print(
            "You've selected a number outside the valid range. Program terminating..."
        )
        exit()

else:
    print("The entered value must be a number. Program terminating...")
    exit()

# ? ANALYSIS ------------------------------------------------------------------------------

# * Defining statistics as a dictionary to be used in future work.
statistics = {
    "words": 0,
    "titlecase_words": 0,
    "uppercase_words": 0,
    "lowercase_words": 0,
    "numeric_strings": 0,
    "sum_of_numbers": 0,
}

paragraph = TEXTS[sp_int].split()

statistics["words"] = len(paragraph)

# * For loop that calculates 4 key statistical measures.
for word in paragraph:

    if word.istitle():
        statistics["titlecase_words"] = statistics["titlecase_words"] + 1

    elif word.isupper():
        statistics["uppercase_words"] = statistics["uppercase_words"] + 1

    elif word.islower():
        statistics["lowercase_words"] = statistics["lowercase_words"] + 1

    elif word.isnumeric():
        statistics["numeric_strings"] = statistics["numeric_strings"] + 1
        statistics["sum_of_numbers"] = statistics["sum_of_numbers"] + int(word)

print(
    f"""{line}
The text contains {statistics["words"]} total words.
It includes {statistics['titlecase_words']} words in title case.
It contains {statistics['uppercase_words']} words in uppercase.
It has {statistics['lowercase_words']} words in lowercase.
It includes {statistics['numeric_strings']} numeric strings.
The total sum of all numbers is {statistics['sum_of_numbers']}.
{line}"""
)

# ? DIAGRAM ------------------------------------------------------------------------------

diagram = {}

# * Creating a diagram storing the length of each word in the paragraph.
for word in paragraph:
    length = len(word.strip(",."))

    if length in diagram:
        diagram[length] = diagram[length] + 1

    else:
        diagram[length] = 1

print(f"LEN| {"OCCURRENCES".center(40)}  |NR.")
print(line)

# * Prints the diagram in order, using asterisks (*) to represent the count for each number.
for num in sorted(diagram):

    if len(str(num)) == 1:
        print(
            num, " |", "*" * diagram[num], " " * (40 - diagram[num]), "|", diagram[num]
        )

    elif len(str(num)) == 2:
        print(
            num, "|", "*" * diagram[num], " " * (40 - diagram[num]), "|", diagram[num]
        )
