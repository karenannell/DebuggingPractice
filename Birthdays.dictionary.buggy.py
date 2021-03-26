#Debugging birthdays: buggy

#keep track of when our friend’s birthdays are, and be able to find that information based on their name.
#Create a dictionary (in your file) of names and birthdays.
#When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.


Birthdays ={
    "Albert Einstein": "14/3/1889"
    "Bill Gates": "28/10/1955"
    "Steve Jobs": "24/2/1955"
    }

print("Welcome to the Birthday game! We have the birthdays to:")
time.sleep(1)

for i in Birthdays:
    print(x)
    time.sleep(0.7)
friend = input("\nWho's birthday do you want to look up?")

if i in Birthdays:
    print("The birthday of {} is: ".format(friend))
    print(Birthdays[friend])

#There are 4 bugs in this code! I found: 
