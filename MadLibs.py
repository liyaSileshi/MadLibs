#Liya Tilahun
#MadLibs example is from the project spec doc
#termcolor use found from stackoverflow
#I got help from my friend on using unicode for colors in terminal


print("Welcome to MadLibs!!!!!\u001b[36m")

# the input function will display a message in the terminal
# and wait for user input.
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def adj():
    return user_input("Enter an adjective: ")

def bird():
    return user_input("Enter a type of bird: ")

def room():
    return user_input("Enter a room in a house: ")

def verb_past():
    return user_input("Enter a verb in past tense: ")

def verb():
    return user_input("Enter a verb: ")

def noun():
    return user_input("Enter a noun: ")

def preposition():
    return user_input("Enter a preposition: ")

sen1 = "It was a {adjective}, cold November day.".format(adjective = adj())
sen2 = "I woke up to the {adjective} smell of {bird} roasting in the {room} downstairs.".format(adjective = adj(),
    bird = bird(), room = room())
sen3 = "I {verb_past} down the stairs to see if I could help {verb} the dinner.".format(verb_past = verb_past(),
    verb = verb())
sen4 = 'My mom said, "See if {relative} needs a fresh {noun}"'.format(relative = user_input("Enter a relative's name: "),noun = noun())
sen5 = "So I carried a tray of glasses full of {liquid} {preposition} the {verb} room.".format(liquid = user_input("Enter a liquid: "),
    preposition = preposition(),verb = user_input("Enter a verb ending in -ing: "))
sen6 = "When I got there, I couldn't believe my {body}!".format(body = user_input("Enter a part of the body: "))
sen7 = "There were {plural_noun} {verb} on the {noun}!".format(plural_noun = user_input("Enter a plural noun: "),verb = verb(),
    noun =noun())

print(" ")
print("Generating story...")
print(" ")

#creating a list and storing the sentences in the list
story = [sen1, sen2, sen3, sen4, sen5, sen6, sen7]

#accessing the list using for loop
for words in story:
    print(words)
