import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

class Flight:
    def __init__(self):
        self.flights = {
            "GA222": {"seats": 5, "destination": "Tokyo"},
            "VI181": {"seats": 3, "destination": "London"},
            "NA007": {"seats": 4, "destination": "Delhi"}
        }

    def check_available_flights(self):
        available_flights = "Available Flights:\n"
        for flight_no, details in self.flights.items():
            available_flights += f"Flight No: {flight_no}, Destination: {details['destination']}, Available Seats: {details['seats']}\n"
        return available_flights

class TicketReservationSystem(User, Flight):
    def __init__(self, username, password):
        User.__init__(self, username, password)
        Flight.__init__(self)
        self.reservation = []
        self.create_login_gui()

    def create_login_gui(self):
        self.root = tk.Tk()
        self.root.title("Ticket Reservation System")

        tk.Label(self.root, text="Username").grid(row=0, column=0)
        tk.Label(self.root, text="Password").grid(row=1, column=0)

        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show='*')

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Login", command=self.check_login).grid(row=2, column=1)

        self.root.mainloop()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.login(username, password):
            messagebox.showinfo("Login Successful", f"Welcome {username}")
            self.root.destroy()
            self.display_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def display_menu(self):
        while True:
            print("\nEnter 1 to Book Tickets")
            print("Enter 2 to Cancel Reservation")
            print("Enter 3 to Check Seats Availability")
            print("Enter 4 to Exit")

            choice = int(input("Enter your Choice: "))

            if choice == 1:
                self.book_ticket()
            elif choice == 2:
                self.cancel_reservation()
            elif choice == 3:
                print(self.check_available_flights())
            elif choice == 4:
                print("Exiting the System")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_ticket(self):
        print("\nBook Ticket")
        flight_no = input("Enter Flight number: ")
        if flight_no in self.flights and self.flights[flight_no]["seats"] > 0:
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
        for reservation in self.reservation:
            if reservation["flight_no"] == flight_no:
                self.flights[flight_no]["seats"] += reservation["passenger_count"]
                self.reservation.remove(reservation)
                print("Reservation canceled successfully.")
                return
        print("No reservation found for the given flight number.")

if __name__ == "__main__":
    system = TicketReservationSystem(username="user1", password="password123")
