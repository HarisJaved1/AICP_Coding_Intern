# Records the milk yield for a single cow per milking.


def record_yield():
    
    cow_id = input("Enter the cow's ID (3 digits): ")
    while len(cow_id) != 3:
        cow_id = input("Invalid ID. Please enter a 3-digit code: ")

    while True:
        try:
            yield_str = input("Enter the yield (liters, one decimal place): ")
            yield_1 = float(yield_str)
            if yield_1 < 0:
                raise ValueError("Invalid yield. Please enter a non-negative number.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number with one decimal place.")

    return cow_id, yield_1

def main():
    
    num_cows = 4
    herd_yields = {}

    for day in range(7):
        print(f"\n--- Day {day+1} ---")
        for _ in range(num_cows):
            cow_id, yield_1 = record_yield()
            if cow_id not in herd_yields:
                herd_yields[cow_id] = [0, 0]  # [morning yield, evening yield]
            herd_yields[cow_id][day % 2] += yield_1

    # Print recorded yields for each cow
    print("\nRecorded Yields:")
    for cow_id, yields in herd_yields.items():
        print(f"Cow {cow_id}: {yields}")

if __name__ == "__main__":
    main()



# Task 2 & Task 3 Calculates and displays statistics, top performer, and low yielders.


herd_yields = {
    100: [8.2, 7.8, 8.5, 7.9, 8.1, 7.7, 8.3],
    101: [10.7, 11.2, 10.5, 11.0, 10.9, 11.1, 10.8],
    102: [12.4, 11.8, 12.1, 11.9, 12.3, 11.7, 12.2],
    103: [5.9, 6.1, 5.7, 6.2, 5.8, 6.0, 5.6],
}

def calculate_statistics(herd_yields):
    

    # Calculate total weekly volume for each cow
    total_volumes = {cow_id: sum(yields) for cow_id, yields in herd_yields.items()}

    # Find the cow with the highest total yield
    top_performer_id, top_yield = max(total_volumes.items(), key=lambda item: item[1])

    # Identify low yielders (less than 12 liters for 4 or more days)
    low_yielders = []
    for cow_id, yields in herd_yields.items():
        low_yield_days = sum(1 for yield_1 in yields if yield_1 < 12)
        if low_yield_days >= 4:
            low_yielders.append(cow_id)

    # Print calculated statistics
    print("\nTotal Weekly Volume of Milk:")
    for cow_id, volume in total_volumes.items():
        print(f"Cow {cow_id}: {volume:.1f} liters")
    print(f"Total Herd: {sum(total_volumes.values()):.0f} liters (rounded to nearest whole number)")
    print(f"\nAverage Yield per Cow: {round(sum(total_volumes.values()) / len(herd_yields)):.0f} liters (rounded to nearest whole number)")

    # Print top performer and low yielders
    print("\nTop Performer:")
    print(f"Cow {top_performer_id}: {top_yield:.1f} liters")
    if low_yielders:
        print("\nLow Yielders (under 12 liters for 4+ days):")
        print(", ".join([f"Cow {cow_id}" for cow_id in low_yielders]))
    else:
        print("No cows fell below the low yield threshold for the week.")

if __name__ == "__main__":
    calculate_statistics(herd_yields)


    
