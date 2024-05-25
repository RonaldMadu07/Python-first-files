prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
hobby = "\nAnd what hobbies do you like? "

name = input(prompt)
hobby = input(hobby)

active = ""
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
print("Hello, " + name + "! " + hobby + " is a brilliant choice.")

