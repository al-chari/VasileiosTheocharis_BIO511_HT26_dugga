#Packages that will be imported,
import pandas as pd
import matplotlib.pyplot as plt
import random

from setuptools.unicode_utils import try_encode

# Question 1
#making it a variable
my_age = 24
# using the existing variable and adding 0.5
add_age = my_age + 0.5
#printing the add_age type to check it
print(type(add_age))
# Class is float because it has a decimal now not only an integer


#Question 2
# defining the list to be used, doggy, 5 and elsa were later additions
my_names= ["alice", "bob", "charlie", "doggy", 5, "elsa"]
#from the resulting list only Alice and Charlie were right
#from the second list doggy is also present


def get_long_names(names) :
    #define the empty variable that will be returned
    long_names = []
    #making the for loop to go through all the names
    for name in names:
        # beginning with trying this way if it cannot even get the length it will skip over it eg for the number 5
        # The other way around wouldn't let it progress because without the try it insists of going through
        # meaning it would try to get the length of 5 and fail
        try:
            if len(name) > 4 :
               long_names.append(name)
        #when there object is not a string at all it is printed but because it is an except it only happens when
        # the try cannot run at all
        except :
                print(name, "type not string")
    return long_names
my_long_names = get_long_names(my_names)
print(my_long_names)
#Question 3
#I imported pandas here because it is more familiar you can also use for example read
#input just to make it easier to modify when running
filename = "cnv_data.csv"
#there the input file is read
file=pd.read_csv(filename)
#the output file as in the image stored
#the file name you want to use for the export here I have scatter.png to save it in my preferred format but can be changed
file_out = "scatter.png"
#the print below is a test preferably you only want to print heads though
#print(file)
plt.scatter(file["log2_ratio"], file["copy_number"])
#title, could be more descriptive
plt.title("CNV DATA")
#labels to patch the data
plt.xlabel("log2_ratio")
plt.ylabel("copy_number")
plt.show()
plt.savefig(file_out)


#Question 4
#the players
# I was going to hard code it the plan was to create the scenario for the draw with only alice as a base
# then hard come each other case based of what either would have other than the same thing
# time is ending should have used a dictionary same as for the count of who is winning and set the conditions
players = ["alice", "bob"]
#for loop in order to run it for both players
for player in players:
    rps = ["rock", "paper", "scissors"]
    #creating the number that will be addded onto up to 20 for all the roles
    count=0
    #the dictionary that will be appended starting from 0
    games= {"alice": 0, "bob": 0, "draw": 0}
    #creating the while loop and setting it as long as it is below 20 because the counting starts from 0
    while count < 20  :
    #defining each player for every round
        alice= random.choice(rps)
        bob= random.choice(rps)
        if alice == bob :
            games["draw"]= games.get("draw") + 1
        #elif alice != if :
            #if alice = "rock"
                #games["alice"]= games["alice"] + 1
    #here we return the results both by adding to count and appending the dictionary with the result
    else :
        winner=max(games, key=games.get)
        print("the winner is", winner)
    # adding to the count every run to prevent it from going past 20
    count = count + 1