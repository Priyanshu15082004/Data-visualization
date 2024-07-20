student = [
  ["stdid", "stdname", "standard", "Age", "Hindi", "English", "Math", "Science", "Computer", "Total"],
  ["std101", "Ashish kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
  ["std102", "Abhishek kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
  ["std103", "Aman", "10th", 15, 23, 56, 78, 78, 67, 302],
  ["std104", "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258],
  ["std105", "Ruby", "10th", 13, 89, 67, 89, 93, 65, 402],
  ["std106", "Suman", "10th", 13, 90, 46, 67, 67, 67, 337],
  ["std107", "Saurabh", "10th", 15, 45, 23, 34, 45, 34, 181],
  ["std108", "Sumit", "10th", 14, 23, 45, 67, 78, 90, 303],
  ["std109", "Kamlesh", "10th", 15, 45, 56, 78, 99, 67, 345],
  ["std110", "Rohan", "10th", 15, 34, 12, 24, 45, 56, 171]
]
print("printing the list ")
for x in range(1,10):
  print(student[x]);

print("-----------------------------------------------------")
# First task: Display the name of student whose marks in English is greater than 50
print("Display the name of student whose marks in English is greater than 50")
for x in range(1, len(student)):
  if student[x][5] > 50:
      print(student[x][1])
print("-----------------------------------------------------")

# Second task: Find and display the names and ages of the students with the top four marks in Math
# Initialize list to store top four marks
top_four_marks = []

for x in range(1, len(student)):
  mark = student[x][6]
  if len(top_four_marks) < 4:
      top_four_marks.append(mark)
      top_four_marks.sort(reverse=True)
  else:
      if mark > top_four_marks[-1]:
          top_four_marks[-1] = mark
          top_four_marks.sort(reverse=True)

# Print the names and ages of the students with the top four marks in Math
print("Names and ages of students with the top four marks in Math:")
for x in range(1, len(student)):
  if student[x][6] in top_four_marks:
      print(student[x][1], student[x][3])

print("-----------------------------------------------------")


# third task : Display name,id,age of student who are bottom three scrore in computer 
print("Display name, id, age of students who are the bottom three scores in Computer")

# Initialize list to store bottom three scores
bottom_three_scores = []

for x in range(1, len(student)):
    score = student[x][8]
    if len(bottom_three_scores) < 3:
        bottom_three_scores.append(score)
        bottom_three_scores.sort()
    else:
        if score < bottom_three_scores[-1]:
            bottom_three_scores[-1] = score
            bottom_three_scores.sort()

# Print the names, ids, and ages of the students with the bottom three scores in Computer
print("Name\t\tID\t\tAge")
for x in range(1, len(student)):
    if student[x][8] in bottom_three_scores:
        print(f"{student[x][1]}\t{student[x][0]}\t{student[x][3]}")






