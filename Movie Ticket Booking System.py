movies = ["Pushpa 2", "Avatar", "Avengers"]

shows = ["10:00 AM", "2:00 PM", "6:00 PM"]

seats = ["A1", "A2", "A3", "A4", "A5"]

bookings = []

users = []


# ================= AVAILABLE DETAILS =================

print("\n==============================")
print("   AVAILABLE MOVIES")
print("==============================")

for i in range(len(movies)):
    print(i, movies[i])


print("\n==============================")
print("   AVAILABLE SHOWS")
print("==============================")

for i in range(len(shows)):
    print(i, shows[i])


print("\n==============================")
print("   AVAILABLE SEATS")
print("==============================")

for i in range(len(seats)):
    print(i, seats[i])


# ================= MAIN MENU =================

while True:

    print("\n==============================")
    print("   MOVIE TICKET BOOKING")
    print("          SYSTEM")
    print("==============================")

    print("1. ADMIN (OWNER)")
    print("2. USER (CUSTOMER)")
    print("3. EXIT")

    role = input("Select role: ")


    # ================= ADMIN =================

    if role == "1":

        while True:

            print("\n========== ADMIN ==========")
            print("1. ADD MOVIE")
            print("2. ADD SHOW")
            print("3. VIEW SEATS")
            print("4. DELETE MOVIE")
            print("5. DELETE SHOW")
            print("6. VIEW BOOKINGS")
            print("7. EXIT")

            choice = input("Enter choice: ")


            # ADD MOVIE

            if choice == "1":

                movie = input("Enter movie name: ")

                movies.append(movie)

                print("Movie added successfully!")


            # ADD SHOW

            elif choice == "2":

                show = input("Enter show time: ")

                shows.append(show)

                print("Show added successfully!")


            # VIEW SEATS

            elif choice == "3":

                print("\nAVAILABLE SEATS:")

                if len(seats) == 0:

                    print("No seats available.")

                else:

                    for i in range(len(seats)):
                        print(i, seats[i])


            # DELETE MOVIE

            elif choice == "4":

                print("\nMOVIES:")

                if len(movies) == 0:

                    print("No movies available.")

                else:

                    for i in range(len(movies)):
                        print(i, movies[i])

                    number = int(
                        input("Enter movie index: ")
                    )

                    movies.pop(number)

                    print("Movie deleted!")


            # DELETE SHOW

            elif choice == "5":

                print("\nSHOWS:")

                if len(shows) == 0:

                    print("No shows available.")

                else:

                    for i in range(len(shows)):
                        print(i, shows[i])

                    number = int(
                        input("Enter show index: ")
                    )

                    shows.pop(number)

                    print("Show deleted!")


            # VIEW BOOKINGS

            elif choice == "6":

                print("\n========== BOOKINGS ==========")

                if len(bookings) == 0:

                    print("No bookings available.")

                else:

                    for booking in bookings:

                        print("\nName :", booking[0])
                        print("Movie:", booking[1])
                        print("Show :", booking[2])
                        print("Seat :", booking[3])


            # EXIT ADMIN

            elif choice == "7":

                break


            else:

                print("Invalid choice!")


    # ================= USER =================

    elif role == "2":

        while True:

            print("\n========== USER ==========")
            print("1. VIEW MOVIES")
            print("2. VIEW SHOWTIMES")
            print("3. VIEW SEATS")
            print("4. BOOK TICKET")
            print("5. VIEW BOOKING")
            print("6. EXIT")

            choice = input("Enter choice: ")


            # VIEW MOVIES

            if choice == "1":

                print("\nAVAILABLE MOVIES:")

                if len(movies) == 0:

                    print("No movies available.")

                else:

                    for i in range(len(movies)):
                        print(i, movies[i])


            # VIEW SHOWTIMES

            elif choice == "2":

                print("\nAVAILABLE SHOWTIMES:")

                if len(shows) == 0:

                    print("No shows available.")

                else:

                    for i in range(len(shows)):
                        print(i, shows[i])


            # VIEW SEATS

            elif choice == "3":

                print("\nAVAILABLE SEATS:")

                if len(seats) == 0:

                    print("No seats available.")

                else:

                    for i in range(len(seats)):
                        print(i, seats[i])


            # BOOK TICKET

            elif choice == "4":

                if len(movies) == 0:

                    print("No movies available.")

                elif len(shows) == 0:

                    print("No shows available.")

                elif len(seats) == 0:

                    print("No seats available.")

                else:

                    print("\nAVAILABLE MOVIES:")

                    for i in range(len(movies)):
                        print(i, movies[i])

                    movie_number = int(
                        input("Select movie index: ")
                    )

                    movie = movies[movie_number]


                    print("\nAVAILABLE SHOWTIMES:")

                    for i in range(len(shows)):
                        print(i, shows[i])

                    show_number = int(
                        input("Select show index: ")
                    )

                    show = shows[show_number]


                    print("\nAVAILABLE SEATS:")

                    for i in range(len(seats)):
                        print(i, seats[i])

                    seat_number = int(
                        input("Select seat index: ")
                    )

                    seat = seats[seat_number]


                    name = input("Enter your name: ")

                    users.append(name)


                    booking = [
                        name,
                        movie,
                        show,
                        seat
                    ]

                    bookings.append(booking)


                    seats.pop(seat_number)


                    print("\n==============================")
                    print("     TICKET BOOKED")
                    print("==============================")

                    print("Name :", name)
                    print("Movie:", movie)
                    print("Show :", show)
                    print("Seat :", seat)


            # VIEW BOOKING

            elif choice == "5":

                print("\nYOUR BOOKINGS:")

                if len(bookings) == 0:

                    print("No booking found.")

                else:

                    for booking in bookings:

                        print("\nName :", booking[0])
                        print("Movie:", booking[1])
                        print("Show :", booking[2])
                        print("Seat :", booking[3])


            # EXIT USER

            elif choice == "6":

                break


            else:

                print("Invalid choice!")


    # ================= EXIT =================

    elif role == "3":

        print("\nThank you!")

        break


    else:

        print("Invalid role!")
