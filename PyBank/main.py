import csv



# Define the input file path

file_path = "Resources/budget_data.csv"



# Initialize variables

total_months = 0

total_profit_loss = 0

previous_profit_loss = None

profit_loss_changes = []

dates = []



# Read in the budget data CSV file

with open(file_path, 'r') as budget_data:

    # Create a CSV reader object

    csvreader = csv.reader(budget_data, delimiter=',')

    

    # Read the header row

    header = next(csvreader)

    

    # Loop through the rows in the CSV file

    for row in csvreader:

        # Extract the date and profit/losses values

        date = row[0]

        profit_loss = int(row[1])

        

        # Increment the total number of months

        total_months += 1

        

        # Add the profit/loss to the total

        total_profit_loss += profit_loss

        

        # If this is not the first row, calculate the profit/loss change

        if previous_profit_loss is not None:

            profit_loss_change = profit_loss - previous_profit_loss

            profit_loss_changes.append(profit_loss_change)

            dates.append(date)

        

        # Set the previous profit/loss to the current value

        previous_profit_loss = profit_loss



# Calculate the average profit/loss change

average_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)



# Find the greatest increase and decrease in profit/losses

greatest_increase = max(profit_loss_changes)

greatest_decrease = min(profit_loss_changes)

greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]

greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]



# Print the results to the console

print("Financial Analysis")

print("------------------")

print(f"Total Months: {total_months}")

print(f"Total Profit/Loss: ${total_profit_loss}")

print(f"Average Change: ${average_profit_loss_change:.2f}")

print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")



# Export the results to a text file

output_file = "analysis/financial_analysis.txt"

with open(output_file, 'w') as outfile:

    outfile.write("Financial Analysis\n")

    outfile.write("------------------\n")

    outfile.write(f"Total Months: {total_months}\n")

    outfile.write(f"Total Profit/Loss: ${total_profit_loss}\n")

    outfile.write(f"Average Change: ${average_profit_loss_change:.2f}\n")

    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")

    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")



print(f"Results exported to {output_file}")
