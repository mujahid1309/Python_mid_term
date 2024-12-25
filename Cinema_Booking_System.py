class Star_Cinema:
    __hall_list = []  # Class attribute to store Hall objects

    @classmethod
    def entry_hall(cls, hall):
        # Insert a Hall object into the hall_list
        cls.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        # Initialize Hall with rows, cols, and hall number.
        self.__seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        # Add this Hall instance to the Star_Cinema hall_list
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        # Add a show to the show_list and initialize seats.
        show = (id, movie_name, time)
        self.show_list.append(show)
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, id, seat_list):
        # Book seats for a specific show by ID.
        if id not in self.__seats:
            raise ValueError("Invalid show ID.")

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f"Seat ({row}, {col}) is invalid.")

            if self.__seats[id][row][col] == 1:
                raise ValueError(f"Seat ({row}, {col}) is already booked.")

            self.__seats[id][row][col] = 1

    def view_show_list(self):
        # Display all the shows in the hall.
        if not self.show_list:
            print("No shows available.")
        else:
            for show in self.show_list:
                print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        """View available seats for a specific show by ID."""
        if id not in self.__seats:
            raise ValueError("Invalid show ID.")

        print("Available seats (0 = free, 1 = booked):")
        for row in self.__seats[id]:
            print(" ".join(map(str, row)))

# Replica system for cinema booking
def cinema_booking_system():
    hall1 = Hall(7, 7, "H1")

    # Add shows
    hall1.entry_show("111", "Mufasa: The Lion King", "25/12/2024 2:00 PM")
    hall1.entry_show("222", "Sujon Majhi", "25/12/2024 4:30 PM")
    hall1.entry_show("333", "Moana 2", "25/12/2024 7:50 PM")

    while True:
        print("\n1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. Exit")
        
        option = input("ENTER OPTION: ")

        if option == "1":
            hall1.view_show_list()

        elif option == "2":
            show_id = input("ENTER SHOW ID: ")
            if show_id in [show[0] for show in hall1.show_list]:
                hall1.view_available_seats(show_id)
            else:
                print("Invalid show ID.")

        elif option == "3":
            show_id = input("Show Id: ")
            if show_id in [show[0] for show in hall1.show_list]:
                tickets = int(input("Number of Ticket?: "))
                seat_list = []
                for _ in range(tickets):
                    row = int(input("Enter Seat Row: "))
                    col = int(input("Enter Seat Col: "))
                    if 0 <= row < hall1._Hall__rows and 0 <= col < hall1._Hall__cols:
                        if hall1._Hall__seats[show_id][row][col] == 0:
                            seat_list.append((row, col))
                        else:
                            print(f"Seat ({row}, {col}) is already booked.")
                    else:
                        print(f"Seat ({row}, {col}) is invalid.")

                if seat_list:
                    hall1.book_seats(show_id, seat_list)
                    print(f"Seats {seat_list} booked for show {show_id}")
            else:
                print("Invalid show ID.")

        elif option == "4":
            print("Exiting system. Tata bye bye!!!")
            break

        else:
            print("Invalid option. Try again.")

# Start the system
cinema_booking_system()
