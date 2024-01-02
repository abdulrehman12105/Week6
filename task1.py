def check_sack(contents, weight):
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

contents_input = input("Enter the contents (C for cement, G for gravel, S for sand): ").upper()
weight_input = float(input("Enter the weight of the sack in kilograms: "))

# Check the sack and display output
result = check_sack(contents_input, weight_input)
if result is True:
    print(f"Sack accepted! Contents: {contents_input}, Weight: {weight_input} kilograms.")
else:
    print(f"Sack rejected. Reason: {result[1]}")
