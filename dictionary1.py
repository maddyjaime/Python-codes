'''
Maddy Jaime
Commander Schenk
Sets and Dictionaries (11)
19 January 2019
'''

y = input("what word do you want to add?")                          #asks for user input

set1 = {"apple" , "banana" , "pineapple" , "pear"}                  #defines set1
print("your original set is : " ,set1)                              #prints set1


set1.add(y)                                                         #adds input to set1
print("your updated set is: ", set1)                                #prints set with user input


set2 = {"hi" , "hello" , "howdy" , "hola"}                          #defines set2
set1.update(set2)                                                   #print set2

set1.add("hi")
print



while True:                                                         #sets up forever loop
    x = input("what is your number between 0-3? ")
    if ((int(x)>-1) & (int(x)<4)):                                  #checks that input is between 1-2
        print(set1, "\n")                                           #prints set1
        break


thisdict =  {'brand' : 'Ford','model': 'Mustang','year': 1964}      #sets up thisdict
print("your original dictionary is: ",thisdict)                     #prints original dictionary
d1 = {y: x}                                                         #adds input to end of dictionary
thisdict.update(d1)

print(thisdict)                                                     #print new dictionary
