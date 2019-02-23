##########################################################################
#Program Name: loops.py
#Author(s): Mr. Laan, Corrie-lyn, BB
#Date Started: September 21, 2015 (one month from October 21, 2015!)
#Last Modified: September 17, 2018
#Description: A demonstration of different ways you can make loops work.
##########################################################################

#a message for the user
print ("Tell me your favourite city")
city = input()

#now enter a loop where you never leave until the answer is Pickering
while city != "Pickering":
    print ("Really " + city + "? Why not Pickering?")
    print ("Any other favourite city?")
    city = input()  #try to get them to say pickering to exit the loop
#end while 

#this is out of the loop so it will only print after you have escaped it
print ("Yay you exited the loop by declaring Pickering your favourite!  Why did you pick Pickering???")

#now we will look at a for loop which runs a pre determined number of times
#if you really want you can change the number of times a for loop runs on the fly
print ("How many times have you been to Pickering?")
count = int (input()) #get a number from the user, not a string.

#This is where the loop begins.  The loop will run count times
for counter in range (0, count): #counter is a new variable that tracks the number of times through the loop.
    print (str(counter) + " Pickering!")
    counter = counter + 1 #this line counts each time the loop runs
#end for
#big question why does the counter never reach the number you inputted for count?

print ("We are now out of the Pickering counting loop of doom!")

