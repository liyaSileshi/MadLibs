print("Welcome to MadLibs!!!!!")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
t1= "It was a "
t2="{adjective}".format(adjective = user_input("Enter an adjective: "))
t3=", cold November day."
t4=" I woke up to the"
t5=" {adjective}".format(adjective= user_input("Enter an adjective: "))
t6=" smell of"
t7="{bird}".format(bird=user_input("Enter a type of bird: "))
t8= "roasting in the"
t9="{room}".format(room= user_input("Enter a room in a house: "))
t10="downstairs. "
t11="I"
t12="{verb1}".format(verb1=user_input("Enter a verb in past tense: "))
t13="down the stairs to see if I could help"
t14="{verb2}".format(verb2= user_input("Enter a verb: "))
t15="the dinner. "
t16='My mom said, "See if"'
t17="{relative}".format(relative=user_input("Enter a relative's name: "))
t18="needs a fresh"
t19="{noun}.".format(noun=user_input("Enter a noun: "))
t20= " So I carried a tray of glasses full of"
t21="{liquid}".format(liquid=user_input("Enter a liquid: ")
t22="into the"
t23="{verb}".format(verb=user_input("Enter a verb ending in -ing: "))
t24="room."
t25= " When I got there, I couldn't believe my"
t26="{body}!".format(body=user_input("Enter a part of the body (plural): "))
t27= " There were"
t28="{plural_noun}".format(plural_noun= user_input("Enter a plural noun: "))
t29="{verb}".format(verb=user_input("Enter a verb: "))
t30="on the"
t31="{noun}".format(noun=user_input("Enter a noun:"))
t32="!"


print(" ")
print("Generating story...")
print(" ")
#creating a list and storing the sentences in the list
story=[]

#accessing the list using for loop
for words in story:
    print(words)
