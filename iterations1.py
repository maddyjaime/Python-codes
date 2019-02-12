'''
Maddy Jaime
Commander Schenk
Both types of iteration (13)
18 January 2019
'''

times = input("how many times do you want to iterate? ")    #asks for iteration
name = input("what is your name?")                          #asks for name
for i in range(int(times)):                                 #iterates through how many times input is
    print(name*int(times))                                  #prints name the amount of times inputted


while True:                                                 #while loop
    number = input("what is your number 1-10 ")             #asks for number
    if ((int(number)>0)&(int(number)<11)):                  #if number is 1-10, enter break part
        print("your valid input is: " ,number)              #prints valid input
        break                                               #break

x=0                                                         #set iterator to 0
while x in range (3):                                       #sets loop to 3
    print("hello")                                          #prints hello
    x+=1                                                    #adds 1 to iterator
