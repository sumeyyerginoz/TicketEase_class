# Create a list to represent the available seats
reservation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Create lists to keep track of occupied and empty seats
occupied_seats = []
empty_seats = []

# Create welcome message and menu options
welcome_message = "Welcome to the Ticket Reservation System"
menu = " 1-Reserve a Seat \n 2-Fast Reserve \n 3-Check Seat Availability \n 4-Cancel Reservation \n 5-Exit"

# Print the welcome message
print(welcome_message)

# Start a loop to get user input
while True:
    # Print the menu and get user input for their desired operation
    print(menu)
    try:
        choice = int(input("Please select your desired operation: "))
    except:
        print("Please enter a valid number.")
    
    # If the user wants to reserve a seat
    if choice == 1:
        # Get the seat number they want to reserve
        seat_number = int(input("Which seat would you like to reserve: ")) - 1
        
        # Check if the seat is available
        if reservation[seat_number] == 0:
            # If it is, reserve the seat and update the occupied_seats and reservation lists
            occupied_seats.append(seat_number + 1)
            reservation.insert(seat_number, 1)
            del reservation[seat_number + 1]
            print("Seat", seat_number + 1, "has been successfully reserved.")
        elif reservation[seat_number] == 1:
            # If it's not, let the user know that the seat is already taken
            print("This seat is already occupied. Please select another seat.")
        else:
            # If the user enters an invalid input, let them know
            print("Please enter a valid operation.")
    
    # If the user wants to fast reserve a seat
    if choice == 2:
        # Loop through the available seats and reserve the first one found
        print("Reserving a seat...")
        for i in range(20):
            if reservation[i] == 0:
                print("Your seat has been reserved:", i + 1)
                reservation.insert(i, 1)
                occupied_seats.append(i + 1)
                del reservation[i + 1]
                break
    
    # If the user wants to check seat availability
    if choice == 3:
        # Clear the empty_seats list and print the number of occupied seats
        empty_seats = []
        print("Occupied Seats:", occupied_seats)
        print("Number of Occupied Seats:", (reservation.count(1)))
        
        # Loop through the reservation list and add empty seats to the empty_seats list
        for i in range(20):
            if i + 1 in occupied_seats:
                continue
            else:
                empty_seats.append(i + 1)
    
        # Print the number of empty seats and the list of empty seats
        print("Number of Empty Seats:", (reservation.count(0)))
        print(empty_seats)
    
    # If the user wants to cancel a reservation
    if choice == 4:
        # Get the seat number to cancel the reservation for
        try:
            n = int(input("Which seat would you like to cancel the reservation for: "))
        except ValueError:
            print("You entered an alphanumeric value. Please enter only numerical values.")
   
        print("Cancelling the reservation for seat number", n, "...")
       
        reservation[n-1] = 0
        occupied_seats.remove(n)
        empty_seats.append(n)
   
    if choice == 5:
        break