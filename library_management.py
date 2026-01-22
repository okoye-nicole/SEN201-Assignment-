def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    library.append({"title": title, "author": author})
    print("Book added successfully!")

def view_books():
    if not library:
        print("No books available.")
    else:
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")

def search_book():
    search_title = input("Enter book title to search: ")
    found = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            print(f"Book Found - Title: {book['title']}, Author: {book['author']}")
            found = True
            break
    if not found:
        print("Book not found.")

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Exiting Library System...")
        break
    else:
        print("Invalid choice. Try again.")t1)

system.display_students()

