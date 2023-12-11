import csv

def product(num1, num2):
    # Add two numbers
    result = num1 * num2

    # Save result to CSV file
    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = ['Number 1', 'Number 2', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        writer.writerow({'Number 1': num1, 'Number 2': num2, 'Product': result})

    return result
