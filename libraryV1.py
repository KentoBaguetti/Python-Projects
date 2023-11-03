def start(): # the start method
    allBooks = [ # The list that contains all the books. The Main list.
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    borrowedISBNS = [] # This list will hold the ISBN numbers of books that are borrowed.
    printMenu() # Calls the menu of options
    selection = input("Your selection> ") # asks the user for what they want to do with info from the menu
    while selection != "5" or selection.lower() != "x": # continue asking user for input until they input the exit key
        if selection == "1" or selection.lower() == "a": # run this if statement if the first key character is inputted
            addBook(allBooks) # runs the addBook method
            printMenu() # once the addBook method is called, print the menu
            selection = input("Your selection> ") # ask the user for their input on what they want to do
        elif selection == "2" or selection.lower() == "r": # run this if statement if the second key character is inputted
            list = borrowBooks(allBooks, borrowedISBNS) # calls the borrowBooks method. Creates a list of borrowed books from that call
            for i in list: # this loop iterates through the borrowed books
                for j in allBooks: # this loop iterates through all books
                    if i[1] == j[0]:
                        j[4].append(i[0])
                        borrowedISBNS.append(i[1]) # add the borrowed book to the list of borrowed ISBNS
            printMenu() # print menu again for user
            selection = input("Your selection> ") # ask the user for their input for next event
        elif selection == "3" or selection.lower() == "t": # run this if statement if the 3rd keyword is used
            returnBook(borrowedISBNS, allBooks) # call the returnBooks method
            printMenu() # print the menu for the user
            selection = input("Your selection> ") # ask the user for their next input for the next choice
        elif selection =="4" or selection.lower() == "l": # run this if statement if the fourth keyword is called
            listAllBooks(allBooks, borrowedISBNS) # call the listAllBooks method
            printMenu() # print the menu
            selection = input("\nYour selection> ") # ask user for their next input
        elif selection == "5" or selection.lower() == "x": # run this if they want to exit the program
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$") # IMPORTANT FINAL MESSAGE
            listAllBooks(allBooks, borrowedISBNS) # list all the books one final time
            break
        else:
            print("Wrong selection! Please selection a valid option.") # if an invalid input in entered, ask for another input
            printMenu()
            selection = input("Your selection> ")

def printMenu(): # the print menu method that gives the user their options
    print("\n######################")
    print("1: (A)dd a new book.")
    print("2: Bo(r)row books.")
    print("3: Re(t)urn books.")
    print("4: (L)ist all books.")
    print("5: E(x)it.")
    print("######################\n")

def addBook(allBooks): # the method to add books to the library, uses the library as a parameter
    bookName = input("Book name> ") # asks the user for the name of the book
    while "*" in bookName or "%" in bookName: # checks if there is a * or % in the name
        print("Invalid book name!") # if * or % is in the book name, prompt an error
        bookName = input("Book name> ") # ask for the book name again, run loop again
    authorName = input("Author name> ") # ask for author name, can be anything
    bookEdition = input("Edition> ") # ask for book edition
    checkEdition = False # flag variable to check if the edition is an integer
    while not checkEdition: # check if the edition is an integer, if not keep asking
        if bookEdition.isnumeric(): # checks if the edition is an integer
            checkEdition = True # if it is an integer, make flag true
            bookEdition = int(bookEdition) # make the bookEdition variable and integer
        else: # if the bookEdition variable is not an integer, keep asking them to enter the book edition
            print("Invalid book edition!")
            bookEdition = input("Edition> ")
    bookISBN = input("ISBN> ") # ask for the ISBN code of the book
    checkVector = "1313131313131" # check vector for the ISBN code
    checkISBN = False # flag variable to check if the ISBN is valid
    dupFlag = False # flag is check if the ISBN is a duplicate
    while not checkISBN: # run loop while checkISBN is false
        for i in allBooks: # check for duplicate ISBN's
            if i[0] == bookISBN: # compares current books with new book ISBN
                dupFlag = True # if they are duplicates, set flag to true
        if bookISBN.isnumeric() and len(bookISBN) == 13 and dupFlag == False: # if its not a dup and ISBN is a number and 13 chars long,
            sum = 0 # sum for check vector and code vector sum
            for j in range(13):
                sum += int(checkVector[j])*int(bookISBN[j]) # check if the ISBN code is valid with check vector
            if sum%10 == 0: # if code is valid, checkISBN == True for valid code
                checkISBN = True
                newBook = [bookISBN, bookName, authorName, bookEdition, []] # create a list for the new valid book
                allBooks.append(newBook) # add new valid book to the library
                print("A new book is added successfully.") # print statement to say a book was added
            else: # if the ISBN isn't valid, prompt an error message, go back to main menu
                checkISBN = True # ISBN was checked but not validated
                print("Invalid ISBN!")
        elif bookISBN.isnumeric() and len(bookISBN) == 13 and dupFlag == True: # if statement for if the ISBN is a duplicate
            print("Duplicate ISBN is found! Cannot add the book.") # print statement for duplicate ISBN's
            checkISBN = True # ISBN was checked but not validated
        else: # if the ISBN wasn't a number or not the right length
            print("Invalid ISBN!")
            bookISBN = input("ISBN> ") # keep asking for a proper ISBN

def borrowBooks(bookList, borrowList): # borrowBook method, takes the library list and list of borrowed ISBN's as parameters
    borrowerName = input("Enter the borrower name> ") # ask for the borrowers name
    bookName = input("Search term> ").lower() # ask for the book name and make it lowercase since the program is case insensitive
    list = [] # list to hold information on books that will be borrowed
    for i in bookList: # iterate through all the books in the library
        if bookName.endswith("*") and bookName[0:len(bookName)-1] in i[1].lower() and i[0] not in borrowList: # checks-
            # -if the search term has a * and is available to borrow
            borrower = [borrowerName, i[0]] # create a list for the borrower and book being borrowed
            list.append(borrower) # add ^list to the list of borrowed books
            print("-\"{}\" is borrowed!" .format(i[1])) # print the name of the book being borrowed
        elif bookName.endswith("%") and bookName[0:len(bookName)-1] in i[1].lower() and i[0] not in borrowList: # checks-
            # -if the search term has % and is available for borrow
            borrower = [borrowerName, i[0]] # create a list for the borrower and book being borrowed
            list.append(borrower) # add ^list to the list of borrowed books
            print("-\"{}\" is borrowed!" .format(i[1])) # print the name of the book being borrowed
        elif bookName == i[1].lower() and i[0] not in borrowList: # checks for the exact book name and if its available
            borrower = [borrowerName, i[0]] # create a list for the borrower and the book being borrowed
            list.append(borrower) # add ^list to the list of borrowed books
            print("-\"{}\" is borrowed!" .format(i[1])) # print the name of the book being borrowed
    if len(list) == 0: # if no books had been borrowed, it means they don't exist or cant be borrowed.
        print("No books found!") # tells the user no books have been found to be borrowed
    return list # return the list of borrowed booked

def returnBook(borrowList, allBooks): # return book method, uses the list of borrowed books and library as parameters
    ISBN = input("ISBN> ") # asks the user for the ISBN of the book they want to return
    if ISBN in borrowList: # if the book is being borrowed,
        borrowList.remove(ISBN) # remove the book from the borrowed list
        for i in allBooks: # finds the name of the book being returned
            if i[0] == ISBN:
                name = i[1]
        print("\"{}\" is returned.".format(name)) # prints out the name of the book being returned
    else:
        print("No book is found!") # if the ISBN is not found, no book has been returned
    return borrowList # return the list of new borrowed books

def listAllBooks(allBooks, borrowedBooks): # method that lists all the books in the library
    for i in allBooks:
        if i[0] in borrowedBooks:
            print("---------------")
            print("[Unavailable]") # if the book is being borrowed, it is unavailable
        else: # if the book is not being borrowed, it is available
            print("---------------")
            print("[Available]") # availbe book
        print(i[1] + " - " + i[2])
        print("E: {} ISBN: {}" .format(i[3], i[0])) # prints out the edition and ISBN of the book
        print("Borrowed by: {}" .format(i[4])) # returns a list of people who borrowed the book

start() # calling the start method
