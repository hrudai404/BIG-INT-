# Function to find eligible customers
def eligible_customers(customers, min_orders, min_price):
    eligible = []
    for customer, orders in customers.items():
        qualifying_orders = [order for order in orders if order >= min_price]
        if len(qualifying_orders) >= min_orders:
            eligible.append(customer)
    return eligible

# Test Data (from your Zephyr steps)
customers = {
    "Aagam": [120, 150],
    "Balu": [80, 90, 70],
    "Charan": [200, 300, 250]
}
min_orders = 2
min_price = 100

# Step 1: Call the eligibility function
try:
    eligible_list = eligible_customers(customers, min_orders, min_price)
    print("Function executed successfully.")
except Exception as e:
    print("Function execution failed:", e)

# Step 2: Capture the list of eligible customers
print("Eligible customers returned by function:", eligible_list)

# Step 3: Compare with expected result
expected_eligible = ["Aagam", "Charan"]
if eligible_list == expected_eligible:
    print("Test Passed: Eligible customers list is correct.")
else:
    print("Test Failed: Expected", expected_eligible, "but got", eligible_list)

# Step 4: Optional validation - ensure Bob is not included
if "Balu" not in eligible_list:
    print("Validation Passed: Bob is correctly excluded.")
else:
    print("Validation Failed: Bob should not be included.")
