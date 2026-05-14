# Richest Customer Wealth

rows = int(input("Enter number of customers: "))
cols = int(input("Enter number of bank accounts per customer: "))

accounts = []

print("\nEnter wealth values:")

for i in range(rows):
    customer = list(map(int, input(f"Customer {i+1}: ").split()))

    # Ensure correct number of inputs
    while len(customer) != cols:
        print(f"Please enter exactly {cols} values.")
        customer = list(map(int, input(f"Customer {i+1}: ").split()))

    accounts.append(customer)

# Find maximum wealth
max_wealth = 0

for customer in accounts:
    wealth = sum(customer)
    max_wealth = max(max_wealth, wealth)

# Output
print("\nAccounts Matrix:")
for row in accounts:
    print(row)

print("\nRichest Customer Wealth:", max_wealth)
