#list of any 10 elements
firstlist =[20,30,'Hello',43,90,'i',39,20,'am','fine']
#Displaying a list
print(firstlist)
#Displaying a list by using * without formatting
print(*firstlist)
#Displaying element for using loop
for x in firstlist:
    print(x)
    #-----------------------------------------------------
print("no of elements:" ,len(firstlist))
#------------------------------------------------

    #create a list of any 20 elements and display element using forward index in reverse order
# Create a list of 20 elements
elements = list(range(1, 21))  # This will create a list [1, 2, 3, ..., 20]

# Display elements using forward index in reverse order
reversed_elements = [elements[i] for i in range(len(elements)-1, -1, -1)]

# Print the original and reversed lists
print("Original List:", elements)
print("Reversed List Using Forward Index:", reversed_elements)
