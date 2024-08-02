class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Welcome {self.username}")
            return True
        else:
            print("Invalid Info")
            return False

# Derived class 1 (Single Inheritance)
class Flight:
    def __init__(self):
        self.flights = {
            "GA222": {"seats": 5, "destination": "Tokyo"},
            "VI181": {"seats": 3, "destination": "London"},
            "NA007": {"seats": 4, "destination": "Delhi"}
        }

    def check_available_flights(self):
        print("Available Flights:")
        for flight_no, details in self.flights.items():
            print(f"Flight No: {flight_no}, Destination: {details['destination']}, Available Seats: {details['seats']}")

# Derived Class 2 (Multiple Inheritance)
class TicketReservationSystem(User, Flight):
    def __init__(self, username, password):
        User.__init__(self, username, password)  # Fixed incorrect case: user to User
        Flight.__init__(self)
        self.reservation = []

    def display_menu(self):
        while True:
            print("\nEnter 1 to Book Tickets")
            print("Enter 2 to Cancel Reservation")
            print("Enter 3 to Check Seats Availability")
            print("Enter 4 to Exit")

            choice = int(input("Enter your Choice: "))

            if choice == 1:
                if self.sign_in_or_log_in():
                    self.book_ticket()
            elif choice == 2:
                self.cancel_reservation()
            elif choice == 3:
                self.check_available_flights()
            elif choice == 4:
                print("______________________________________")
                print("______________________________________")
                print("__________Exiting the System__________")
                print("______________________________________")
                print("______________________________________")
                break
            else:
                print("Invalid choice. Please try again.")

    def sign_in_or_log_in(self):
        print("\nSign In or Log In")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return self.login(username, password)

    def book_ticket(self):
        print("\nBook Ticket")
        flight_no = input("Enter Flight number: ")
        if flight_no in self.flights and self.flights[flight_no]["seats"] > 0:  # Fixed typo: flight to flights
            passenger_count = int(input("Enter the number of passengers: "))
            age_group = input("Enter age group (Child/Adult/Senior Citizen): ")
            luggage = input("Enter luggage details: ")
            food_preference = input("Enter food preference: ")

            if passenger_count <= self.flights[flight_no]["seats"]:
                self.reservation.append({
                    "flight_no": flight_no,
                    "passenger_count": passenger_count,
                    "age_group": age_group,
                    "luggage": luggage,
                    "food_preference": food_preference
                })
                self.flights[flight_no]["seats"] -= passenger_count
                print("Ticket booked successfully!")
            else:
                print("Not enough seats available.")
        else:
            print("Invalid flight number or no seats available.")

    def cancel_reservation(self):
        print("\nCancel Reservation")
        flight_no = input("Enter flight number to cancel: ")
        for reservation in self.reservation:  # Fixed typo: reservations to reservation
            if reservation["flight_no"] == flight_no:
                self.flights[flight_no]["seats"] += reservation["passenger_count"]
                self.reservation.remove(reservation)
                print("Reservation canceled successfully.")
                return
        print("No reservation found for the given flight number.")

# Running the Ticket Reservation System
if __name__ == "__main__":
    system = TicketReservationSystem(username="user1", password="password123")  # Fixed syntax: username: to username=
    system.display_menu()
