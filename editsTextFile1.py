'''
Maddy Jaime
Commander Schenk
Edits text file (24)
25 January 2019
'''

input1 = input("what do you want to add?")  #asks for user input
file = "animala.txt"
f= open(file , "a")                         #opens text file and prepares to append
text = f.write(input1)                      #adds user input
text3= f.write("\n")
f.close()                                   #closes text file

f2 = open(file , 'r')                       #reopens text file
text2 = f2.read()                           #reads text file
print(text2)                                #prints new text

f.close()                                   #closes text file
