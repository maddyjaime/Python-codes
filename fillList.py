'''
Maddy Jaime
Commander Schenk
Fill List (12)
19 January 2019
'''
import sys

list1 = []                                                          #sets up blank list

long = input("how long do you want the list to be?")
if ((int(long)>0)&(int(long)<5)):
    for i in range(int(long)):                                      #iterates through loop given amount of times
        user_input = input ("Enter  your Age")
        try:
           val = int(user_input)                                    #makes sure input is number and not word
           list1.append(user_input)                                 #adds input to list
        except:
            print("your input was not valid. The program will exit.")
            sys.exit()                                              #code completely shuts off bc input didn't match criteria
else:
    print("your input was not valid. Code will exit")               #if input for list length is not valid, exit
    sys.exit()


print("your list is: " ,list1)                                      #prints list

while True:
    input1 = input("what indexer do you want to look at? ")         #asks for user input
    intinput = int(input1)
    if ((int(input1)>-1)&(int(input1)<int(long))):                  #if user input is >-1 and <3, enter if statement
        print(list1[intinput])                                      #print indexer of list
        break
