firstlist=["stdID","stdName","Standard","Age","Hindi","English","Maths","Science","Computer","Total"]
firstlist1=["std101","Ashish","10th",15,67,89,87,89,90,422]
firstlist2=["std102","Abhishek","10th",14,85,45,48,90,45,313]
firstlist3=["std103","Aman","10th",15,23,56,78,78,67,302]
firstlist4=["std104","Rahul","10th",14,45,67,45,46,56,258]
firstlist5=["std105","Ruby","10th",13,89,67,89,93,65,403]
firstlist6=["std106","Sumsn","10th",13,90,46,67,67,67,337]
firstlist7=["std107","saurabh","10th",15,45,23,34,45,34,181]
firstlist8=["std108","Sunil","10th",14,23,45,67,78,90,303]
firstlist9=["std109","kamlesh","10th",15,56,78,90,67,345]
firstlist10=["std110","Rohan","10th",15,34,12,24,45,56,171]
studentrecord=[firstlist,firstlist1,firstlist2,firstlist3,firstlist4,firstlist5,firstlist6,firstlist7,firstlist8,firstlist9,firstlist10]
for row in studentrecord:
    print(row)
#Displaying name of student whose marks in English is greater than 50
print("--------------------------------------------------------------")
print("Name of students whose marks in english is greater than ")
for rowindex in range(1,len(studentrecord)):
    English=int(studentrecord[rowindex][5])
    if(English>=50):
        print(studentrecord[rowindex][1])
print("-----------------------------------------------------")

# Second task: Find and display the names and ages of the students with the top four marks in Math
# Initialize list to store top four marks
top_four_marks = []

for x in range(1, len(studentrecord)):
  mark = studentrecord[x][6]
  if len(top_four_marks) < 4:
      top_four_marks.append(mark)
      top_four_marks.sort(reverse=True)
  else:
      if mark > top_four_marks[-1]:
          top_four_marks[-1] = mark
          top_four_marks.sort(reverse=True)

# Print the names and ages of the students with the top four marks in Math
print("Names and ages of students with the top four marks in Math:")
for x in range(1, len(studentrecord)):
  if studentrecord[x][6] in top_four_marks:
      print(studentrecord[x][1], studentrecord[x][3])
      
print("-----------------------------------------------------")


# third task : Display name,id,age of student who are bottom three scrore in computer 
print("Display name, id, age of students who are the bottom three scores in Computer")

# Initialize list to store bottom three scores
bottom_three_scores = []

for x in range(1, len(studentrecord)):
    score = studentrecord[x][8]
    if len(bottom_three_scores) < 3:
        bottom_three_scores.append(score)
        bottom_three_scores.sort()
    else:
        if score < bottom_three_scores[-1]:
            bottom_three_scores[-1] = score
            bottom_three_scores.sort()

# Print the names, ids, and ages of the students with the bottom three scores in Computer
print("Name\t\tID\t\tAge")
for x in range(1, len(studentrecord)):
    if studentrecord[x][8] in bottom_three_scores:
        print(f"{studentrecord[x][1]}\t{studentrecord[x][0]}\t{studentrecord[x][3]}")




