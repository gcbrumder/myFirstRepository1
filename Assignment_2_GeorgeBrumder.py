# This script is for Assignment 2 for BUS 392
#It will allow a user to input various books they read and it will tell them how many pages they should read next time
user_name = input("What is your name?")
first_name = user_name.split()[0]
book_one_title = input("What is the title of a book you're reading?")
book_one_pages = int(input("How many pages are in that book?"))
book_two_title = input("What is the title of a different book you're reading?")
book_two_pages = int(input("How many pages are in that book?"))
print("Thank you " + first_name)
print(f"One book you read was called {book_one_title[:25]} and it had {book_one_pages} pages.")
print(f"The other book you read was called {book_two_title[:25]} and it had {book_two_pages} pages.")
total_pages = book_one_pages + book_two_pages
print(f"In total you have read a combined number of {total_pages} pages.")
suggested_pages = total_pages * 1.25
print(f"Next time, you should read 125% more pages, which is equal to {suggested_pages:.0f} pages!")

