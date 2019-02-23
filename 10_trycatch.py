#################################################################
#Program Name: trycatch.py
#Author(s): Mr. Laan	
#Date Started: September 26, 2017
#Last Modified: September 19, 2018
#Description:a way to take in only the data you want and reject everything else without crashing the program
#most of the code came from this great site check it out for more details: https://www.python-course.eu/exception_handling.php
################################################################
#the while true line loops the try until the break line if the lines under try throw an error the except part runs and the loop runs again
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break #if we got here the input above threw no issues and we can exit the loop and skip the except lines below
    except ValueError:#If we go here one of the n= lines had issues, this prints an error and sends us back to the top of the try to try again!
        print("No valid integer! Please try again ...")
print ("Great, you successfully entered an integer!")
