'''
Maddy Jaime
19 January 2019
'''

def number():
    x= input("number: ")
    y= input("number 2: ")
    print("returned value: " ,int(x)+int(y))            #adds two numbers together


def name():
    name1 = input("what is your name?")
    print("your name is: " ,name1)                      #prints user's name


def animal():
    animal= input("what is your favorite animal?")
    print("your favorite animal is: " ,animal)          #prints favorite animal

def pick():
    while True:
        m = input("pick a number between 1-10")
        if ((int(m)>-1) & (int(m)<11)):                 #if input is valid, print
            print("your number is: " ,m)
            break
