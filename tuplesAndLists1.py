
'''
Maddy Jaime
Commander Schenk
Tuples and lists (10)
18 January 2019
'''

tuple1 = ('a' , 'b' , 'c' , 'd' , 'e')          #defines tuple1
print("touple 1 is: " ,tuple1)                  #prints tuple

number = int(input("what is your number?"))     #asks for input of number

tuple2 = ('A' , 'B' , 'C' , 'D' , 'E')
listTuple= list(tuple2)                         #converts tuple into list
print("this is your tuple/list: " ,listTuple)
listTuple.append("HIIIIII")
print(listTuple)

print("tuple 2 is: " , tuple2)                  #prints second tuple

print("your new tuple is: " ,tuple1+tuple2, "\n")#adds tuples and prints


i=0                                             #sets iterator to 0
while True:                                     #sets up while loop
    print(tuple1)                               #print tuple1
    i+=1
    if (i>number-1):                            #if i is < num -1, print
        print("\n")
        break                                   #break loop


hellolist = [1, 2 , 3 , 4 , 5]                  #sets up list
print("Your list is: " ,hellolist)
print("length of list is: " , len(hellolist))   #prints length of list
print("your original list is: ",hellolist)
hellolist.append(number)                        #appends input to list
print("Your new list is : ",hellolist, "\n")     #prints list


odd = [1, 3, 5]                                 #defines another list
print("this is your original list: " ,odd)
odd.extend([1,1,1])                             #adds [1,1,1] to list
print("this is your extended list: ", odd, "\n")#prints
