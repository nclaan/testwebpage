####################################################################################################
#Program Name: If Statements, Boolean, and Loops
#Author: Brianna Drew, Mr. Laan
#Date Started: September 22, 2015
#Last Modified: September 19, 2018
#Description: A program that involves if statements, boolean expressions, and loops
####################################################################################################

print ("Hello, did you have a good day today?")
response = input()

if response == "yes" or response == "Yes" or response == "YES":
    print ("That's good!")

elif response == "no" or response == "No" or response == "NO":
    print ("Oh no! Well, tomorrow is a new day!")
    
while response != "yes" and response != "Yes" and response != "YES" and response != "no" and response != "No" and response != "NO":

    print ("try again!")
    response = input()
	
    if response == "yes" or response == "Yes" or response == "YES":
	    print ("That's good!")
		
    elif response == "no" or response == "No" or response == "NO":
	    print ("Oh no! Well, tomorrow is a new day!")

    else:
        print ("Whaaaaaaaaaat???")
