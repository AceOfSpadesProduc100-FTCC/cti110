# This project is to project the product's sales, calculating the profit as a certain percentage of the total sales.
# 9/6/2019
# CTI-110 P2T1 - Sales Prediction
# Connor Mitchell
#

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))

