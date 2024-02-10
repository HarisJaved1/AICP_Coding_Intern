def calculate_outing_cost():
  #Calculates the total cost of an outing for the senior citizens club and the cost per person.

  

  # Get the number of senior citizens attending the outing
  while True:
    try:
      num_seniors = int(input("Enter the number of senior citizens attending the outing (10-36): "))
      if 10 <= num_seniors <= 36:
        break
      else:
        print("Error: The number of senior citizens must be between 10 and 36.")
    except ValueError:
      print("Error: Please enter a valid number.")

  # Calculate the number of carers required
  num_carers = 2 if num_seniors <= 24 else 3

  # Determine the cost per senior citizen based on the number attending
  if 12 <= num_seniors <= 16:
    cost_per_senior = 150 + 14 + 21
  elif 17 <= num_seniors <= 26:
    cost_per_senior = 190 + 13.5 + 20
  elif 27 <= num_seniors <= 36:
    cost_per_senior = 225 + 13 + 19
  else:
    raise ValueError("Invalid number of senior citizens.")

  # Calculate the total cost of the outing
  total_cost = num_seniors * cost_per_senior

  return total_cost, cost_per_senior

# Get the outing cost and cost per person
total_cost, cost_per_senior = calculate_outing_cost()

# Print the results
print(f"Total cost of the outing: ${total_cost:.2f}")
print(f"Cost per senior citizen: ${cost_per_senior:.2f}")



# Define a function to record attendee information
def record_attendee(name, payment=None):
    """
    Records attendee information with optional payment details.

    Args:
        name: Name of the attendee.
        payment: Amount paid by the attendee (optional).

    Returns:
        A dictionary containing attendee information.
    """
    attendee_info = {"name": name}
    if payment:
        attendee_info["payment"] = payment
    return attendee_info

# Get outing cost and cost per person
total_cost = 5587.50  # Replace with actual total cost
cost_per_senior = 223.50  # Replace with actual cost per person

# Initialize variables
attendees = []  # List to store attendee information
total_collected = 0  # Total amount collected

# Determine number of available spots
max_seniors = 36
num_seniors = len(attendees)
available_spots = max_seniors - num_seniors



# Loop to add new attendees
while True:
    if available_spots == 0:
        print("No more spots available.")
        break
    name = input("Enter attendee name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    # Move payment prompt inside the loop to define payment variable within scope
    payment = float(input("Enter amount paid (optional): "))

    attendees.append(record_attendee(name, payment))
    num_seniors += 1
    available_spots -= 1

# Calculate total collected
for attendee in attendees:
    if "payment" in attendee:
        total_collected += attendee["payment"]

# Print list of attendees and total collected
print("Attendees:")
for attendee in attendees:
    print(f"- {attendee['name']}", end="")
    if "payment" in attendee:
        print(f" (Paid: ${attendee['payment']:.2f})")
    else:
        print()
print(f"\nTotal collected: ${total_collected:.2f}")
print(f"Total cost: ${total_cost:.2f}")

# Get the outing cost and cost per person from Task 1
estimated_cost, cost_per_senior = total_cost, cost_per_senior

# Calculate the profit or loss
profit_or_loss = total_collected - estimated_cost

# Determine if the outing broke even or made a profit
if profit_or_loss >= 0:
    print(f"The outing has broken even or made a profit of ${profit_or_loss:.2f}.")
else:
    print(f"The outing has incurred a loss of ${abs(profit_or_loss):.2f}.")
