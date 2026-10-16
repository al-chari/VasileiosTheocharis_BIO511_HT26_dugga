#This is my dugga

#Q is question and above each of the I also wrote which section of a question they are

#Q1
#a)
Name= "Vasileios_Theocharis"

#b) just a basic len and a print to show it
lonnn=len(Name)

print(lonnn)

#c)
#because we only really care about printing it I nestled the count in the printing
# the idea is to print the count of the letter a as that occurs in my name twice
# in Va and cha.
print(Name.count("a"))


#Q2
#this is my list for the assignment
my_list =[1, 5, "4", "six", 3.14]

#a),b)
# making the function and nestling in it a for loop to go through each variable in the list
def clean_list(list):
    new_list=[]
    for a in list:
        #the normal error I had added in the beginning did not work for the float also a try would have been better
            if type(a) == float:
                print(a,"is a float and cannot be used")
                #if it is already an integer just appending is enough
            elif type(a)==int:
                new_list.append(a)
        #here we try and convert the ones that are not I am not sure why it discards "4"
            elif a.isdigit== True:
                new_list.append(int(a))
        #so this is for everything else printing a simple message to tell people we cannot use it
            else:
                print(a, "is not an integer nor can be converted to one")
    return new_list

newlist=clean_list(my_list)
#printing it to check
print(newlist)

#c) due to the small issue with my function I will use the provided one here on out I am writing mostly pseudocode because I am a slow writter and I am running out of time

new_list2=[1, 5, 4, 3]
#making a loop to go through everything
for a in new_list2:
	#defining the higher and lower locations in the list
	low=new_list2[a-1]
	higher=new_list2[a+1]
	#making the sum a variable because it is easier
	summa=sum(a, low, higher)
	print(sum)

#Q3
# I had forgotten to set it to the environment but here is the data
print("add file name to access:")
datas=input()
dataset=open(datas)
# importing the package we need in this case matplot
import matplotlib as plt
#setting the X and Y I do not know the columns right now
# I know I should have accessed them differenly
x=dataset[position_mb]
y=dataset[log2_ratio]
#making the scatter plot
plt.scatter(x,y)
#saving the plot
print("Please input the name you want the file to be saved as as well as format eg .png")
sas=input()
plt.savefig(sas)

#Q4 seems like instead of proper pseudocode I am making an outline with code mixed in I hope it still counts
#guessing this is a recommended package for doing random numbers haven't used it
import random
#simulating the dice by setting it randomly from 1-6
#defining the two inputs
def dice(alice,bob, games)
	#dictionary everything is saved in
	dictionary={}
	#this would have been used for the counting games in the loop
	while counting<games:
	# should run twice once for alice once for bob
	random.randint(1, 6)
	#it should be with an if alice > elif bob > else draw and append them to the dictionary
	#each dictionary part should be the name of the run
	#returning the results once we are done for the function so that it is not empty
	return
