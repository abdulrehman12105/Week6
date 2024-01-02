def check_sack(contents, weight):
    # Constants for weight ranges
    MIN_GRAVEL_WEIGHT = 49.9
    MAX_GRAVEL_WEIGHT = 50.1
    MIN_CEMENT_WEIGHT = 24.9
    MAX_CEMENT_WEIGHT = 25.1

    # Check contents and weight
    if contents in ['C', 'G', 'S']:
        if (contents in ['G', 'S'] and MIN_GRAVEL_WEIGHT < weight < MAX_GRAVEL_WEIGHT) or \
           (contents == 'C' and MIN_CEMENT_WEIGHT < weight < MAX_CEMENT_WEIGHT):
            return True
        else:
            return False, "Invalid weight for the given contents."
    else:
        return False, "Invalid contents. Use 'C' for cement, 'G' for gravel, or 'S' for sand."

# Function to check a customer's order for delivery
def check_order(order):
    total_weight = 0
    rejected_sacks = 0

    for sack in order:
        contents_input = sack[0]
        weight_input = sack[1]

        # Check the sack and update total weight and rejected sack count
        result = check_sack(contents_input, weight_input)
        if result is True:
            total_weight += weight_input
        else:
            rejected_sacks += 1
            print(f"Rejected sack - Contents: {contents_input}, Weight: {weight_input}. Reason: {result[1]}")

    return total_weight, rejected_sacks

# Function to calculate the price for a customer's order
def calculate_price(order):
    regular_price = 0
    special_pack_count = 0

    for sack in order:
        contents_input = sack[0]

        # Calculate regular price based on contents
        if contents_input == 'C':
            regular_price += 3
        elif contents_input == 'G' or contents_input == 'S':
            regular_price += 2

        # Check for special pack contents
        special_pack_contents = [('C', 1), ('G', 2), ('S', 2)]
        if set(order).issuperset(set(special_pack_contents)):
            special_pack_count += 1

    # Calculate the total price and amount saved for special packs
    total_price = regular_price - (special_pack_count * 10)
    amount_saved = special_pack_count * 5

    return regular_price, total_price, amount_saved

# Input data for a customer's order
num_sacks_cement = int(input("Enter the number of cement sacks required: "))
num_sacks_gravel = int(input("Enter the number of gravel sacks required: "))
num_sacks_sand = int(input("Enter the number of sand sacks required: "))

# Create a list of sacks based on user input
customer_order = [('C', 25.0)] * num_sacks_cement + [('G', 50.0)] * num_sacks_gravel + [('S', 50.0)] * num_sacks_sand

# Check the customer's order for delivery
order_result = check_order(customer_order)

# If all sacks are accepted, calculate and display the price for the order
if order_result[1] == 0:
    price_result = calculate_price(customer_order)
    print(f"\nRegular price for the order: ${price_result[0]}")
    print(f"Total price for the order: ${price_result[1]}")
    print(f"Amount saved with special packs: ${price_result[2]}")
else:
    print("Order contains rejected sacks. Cannot calculate the price.")
