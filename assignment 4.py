# x = ["apple","banana"]
# y = ["apple","banana"]
# z = x
# print(z)
#------------------------------------------------------------------
#add name with A= method
# a ="vikas"
# print(a)
# print(id(a))
# a=a+"Tiwari"
# print(a)
# print(id(a))
# #-------------------------------------------
# #del is a keyword
# a="vikas"
# print(a[1])
# del
# print(a)
# #----------------------------------------------
#Slicing
# name="I am a python trainer"
# print(name)
# print("name[2:4]",name[2:4])
# print("name[5:9]",name[5:9])
# print("name[:15]",name[:15])
# print("name[2:]",name[2:])
# print("name[:]",name[:])
# print("name[0:17:3]",name[0:17:3])
# print("name[::]",name[::])
# print("name[::-1]",name[::-1])
#----------------------------------------------------------
# str ="rahul tiwari"
# print(str)
# str=str.capitalize()
# print(str)
#-----------------------------------------------------------------
# str ="rahul tiwari"
# print(str)
# str=str.title()
# print(str)
#---------------------------------------------------------
#python center() method allign string to the center by filling padding
# str="Hello"
# str2 = str.center(20)
# print("Old value:",str)
# print("New value:",str2)
#-------------------------------------------------------------------
#pythom string count() method 
# str = "my name is Rahul Tiwari"
# oc1 = str.count('a')
# oc2 = str.count('a',6,16)
# print(oc1)
# print(oc2)
#--------------------------------------------------------------------------
# str ="Hello this is python class"
# isends = str.endswith("is",0,10)
# print(isends)
#-------------------------------------------------------------
# str="Hello this is python class"
# iss= str.startswith("is,8,16")
# print(iss)
#------------------------------------------------------------------------------
##searching method find()
# str="Welcome to the python class"
# str2=str.find("t")
# str3=str.find("t",15,25)
# print(str2,str3)
#-------------------------------------------------------------------------------------
# str = "Welcome to the python class"
# str2=str.index("th",19,21)
# print(str2)
# #---------------------------------------------------------------------------------
# str="14325"
# str3="Welcome 123"
# str2 = str.isalnum()
# str4=str3.isalnum()
# print(str2)
# print(str4)
#--------------------------------------------------------
# str="rahul"
# str2=str.isupper()
# print(str2)
#----------------------------------------------------------
# str="anant"
# str=str.upper()
# print(str)
#------------------------------------------------------------------------
# str = ".....python...."
# str2=str.lstrip(',')
# str3=str.rstrip(',')
# str4=str.strip(',')
# print(str)
# print(str2)
# print(str3)
# print(str4)
#------------------------------------------------------------------
# str="java is a java programming  java language java"
# str2=str.replace("java","c",2)
# print(str2)
#-----------------------------------------------------------------------
# Swapcase()
# text ="1234567778hdsuhsdjj@#"
# alphabet = 0
# digit =0
# special = 0

# for char in text:
#     print()
  
#     if char.isalpha():
#         alphabet += 1
#     elif char.isdigit():
#         digit += 1
#     else :
#         special += 1
# print("alphabet", alphabet)
# print("digit",digit)
# print("special",special)
#---------------------------------------------------------
# file=open("anudip.txt",'a')
# file.write("Welcome to python class")
# file.close()
# print("created data succesfully")
#-------------------------------------------------
# file=open("anudip.txt",'r')
# file.read()
# file.close()
# print("")
#---------------------------------------------------------------
# file=open("anudip.txt",'r')
# print(file.tell())
# file.seek(5)
# data=file.read(50)
# print(file.tell())
# print(data)
# file.close
#-----------------------------------------------------------------
# #specify the path to the file you want to search in........................... 
# file_path ="C:\Users\Acer\Desktop\Java\anudip\"
# #Specify the keyword or phrase you want to search for.............................. 
# search_keyword=input("Enter the text which you want to search:")
# with open(file_path,"r")as file:
#     #Read each line of the file..........................
#     for line in file:
#         #Check if the keyword exists in the line(case- insensitive search)...........................
#         if search_keyword.lower()in the.lower():
#             print(line.strip())#Print matching lines withput eading traing whitespac.................
# print(f"Search for'{search_keyword}'completed.")   
#-------------------------------------------------------------------------------------------------------------------------------------------------         
# import pickle
# file=open("anudip.dat","ab")
# li=[10,20,30,40,50]
# pickle.dump(li,file)
# file.close()
# print("Data stored")
# #------------------------------------------------------------
# file=open("Anudip.dat","rb")
# data=pickle.load(file)
# print(data)
# f.close
#--------------------------------------------------------------------------
# import csv
# f = open ("makkhi.csv",'a',newline="")
# wo=csv.writer(f)
# data = [["a","b","c","d"],[16,12,14,10],[26,24,22,20],[36,34,32,30]]
# wo.writerows(data)
# f.close()
#------------------------------------------------------
#Write a program to count the occurrence of word "INDIA" in a text file India txt
# filename = "anudip.txt"
# word_to_count = "INDIA"

# with open(filename, 'r') as file:
#     content = file.read()
#     count = content.count(word_to_count)

# print(f"The word '{word_to_count}' appears {count} times in {filename}")
#------------------------------------------------------------------------------------------
# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.


def read_and_display(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = "python.txt"
read_and_display(filename)
#2. Write a function in Python to count and display the total number of words in a text file "ABC.txt"



def count_and_display_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
count_and_display_words(filename)



#3. Write a function in Python to count uppercase character in a text file "ABC.txt"

def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print(f"Total number of uppercase characters in '{filename}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
count_uppercase_characters(filename)


#4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.


def display_words_less_than_4_characters(filename):
    try:
        with open(filename, 'r') as file:
            words = []
            for line in file:
                line_words = line.strip().split()
                words.extend([word for word in line_words if len(word) < 4])
            
            print(f"Words less than 4 characters in '{filename}':")
            for word in words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
display_words_less_than_4_characters(filename)
