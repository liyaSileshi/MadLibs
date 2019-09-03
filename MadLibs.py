#Liya Tilahun
#MadLibs example is from the project spec doc
print("Welcome to MadLibs!!!!!")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def adj():
    return input("Enter an adjective: ")


sen1= "It was a {adjective}, cold November day.".format(adjective = user_input("Enter an adjective: "))
sen2="I woke up to the {adjective} smell of {bird} roasting in the {room} downstairs.".format(adjective= user_input("Enter an adjective: "),
    bird=user_input("Enter a type of bird: "), room= user_input("Enter a room in a house: "))
sen3= "I {verb_past} down the stairs to see if I could help {verb} the dinner.".format(verb_past=user_input("Enter a verb in past tense: "),
    verb= user_input("Enter a verb: "))
sen4='My mom said, "See if {relative} needs a fresh {noun}"'.format(relative=user_input("Enter a relative's name: "),noun=user_input("Enter a noun: ") )
sen5= "So I carried a tray of glasses full of {liquid} into the {verb} room.".format(liquid=user_input("Enter a liquid: "),
    verb=user_input("Enter a verb ending in -ing: "))
sen6 = "When I got there, I couldn't believe my {body}!".format(body=user_input("Enter a part of the body: "))
sen7= "There were {plural_noun} {verb} on the {noun}!".format(plural_noun= user_input("Enter a plural noun: "),verb=user_input("Enter a verb: "),
    noun=user_input("Enter a noun:"))

print(" ")
print("Generating story...")
print(" ")
#creating a list and storing the sentences in the list
story=[sen1, sen2, sen3, sen4, sen5, sen6, sen7]

#accessing the list using for loop
for words in story:
    print(words)
