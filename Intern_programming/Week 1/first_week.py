names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isla", "Jack",
         "Kelly", "Liam", "Maya", "Noah", "Olivia", "Peter", "Quinn", "Ruby", "Sophia", "Thomas",
         "Umaima", "Victor", "William", "Xander", "Yasmin", "Zachary", "Zara", "Aisha", "Ben", "Chloe"]
weights_first_day = [52, 48, 39, 55, 42, 58, 45, 63, 40, 50, 47, 59, 43, 56, 41, 60, 44, 57, 49, 62, 38, 54, 51, 61, 46, 53, 37, 64, 52]

# Get weights for the last day with validation
weights_last_day = []
for i in range(len(names)):
    while True:
        weight = int(input(f"Enter the weight for {names[i]} on the last day (in kg): "))
        if validate_weight(weight):
            weights_last_day.append(weight)
            break
        else:
            print("Invalid weight. Please enter a weight between 20 and 120 kg.")

# Calculate weight differences
weight_differences = []
for i in range(len(names)):
    weight_difference = weights_last_day[i] - weights_first_day[i]
    weight_differences.append(weight_difference)

# Identify significant weight changes
large_changes = []
for name, diff in zip(names, weight_differences):
    if abs(diff) > 2.5:
        change_type = "gain" if diff > 0 else "loss"
        large_changes.append((name, abs(diff), change_type))

# Print the names, weights on the first day, weights on the last day, and weight differences
print("Names | Weight on the first day (kg) | Weight on the last day (kg) | Weight difference (kg)")
print("-------|-----------------------------|-----------------------------|-------------------------")
for name, weight1, weight2, diff in zip(names, weights_first_day, weights_last_day, weight_differences):
    print(f"{name:8} | {weight1:30} | {weight2:30} | {diff:20}")

# Print significant weight changes
if large_changes:
    print("\n\nPupils with a significant weight change (more than 2.5 kg):")
    for name, diff, change_type in large_changes:
        print(f"- {name}: {diff} kg {change_type}")