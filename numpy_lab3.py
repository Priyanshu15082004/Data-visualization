import numpy as np
# ------------------------------------------------question -1

# Calculate the total revenue generated by two product categories in a store
# Input:
# category1_revenue = np.array([500, 600, 700, 5501)
# category2_revenue = np.array([450, 700, 800, 600])


category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])
sum = category1_revenue + category2_revenue
print("Total Revenue:",sum)


#  --------------------------------------------------quesstion 2 

# Calculate the profit made by a company

# Input: revenue np.array([10000, 12000, 11000, 10500]) 
# expenses np.array([4000, 5000, 4500,4800])

revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

profit = revenue - expenses
print("Profit:", profit)


# ---------------------------------------------------------question 3

# Determine which products in a store are out of stock (quantity is 0). 
# Input: inventory= np.array([10, 0, 5, 0, 20, 0])

inventory = np.array([10, 0, 5, 0, 20, 0])
out_of_stock = np.where(inventory == 0)[0]
print("Out of Stock Products:", out_of_stock)


#-------------------------------------------------- quesstion 4

# Calculate the total cost of items in a shopping cart, considering the quantity and price per item.


quantities = np.array([2, 3, 5, 1])  
prices_per_item = np.array([10, 20, 30, 40])
total_cost = quantities * prices_per_item
print("Total Cost:",total_cost)