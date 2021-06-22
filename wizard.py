# to call APIs
import requests

# to parse json
import json

# Important Variables

# holds ongoing reading list
reading_list=[]


#object to store book data
class Book:
  def __init__(self, title, author, publisher):
    self.title = title
    self.author = author
    self.publisher = publisher

# Important Functions

# displays info in list of results
def display_list(the_list):
	# add functionality for empty list
	if (len(the_list)==0):
		print('No items currently in list.')
	for (i, n) in enumerate(the_list, start=1):
		print(i, end='')
		print(".")
		print("  Title: " + n.title)
		print("  Author: " + n.author)
		print("  Publisher: " + n.publisher)
		

# handles yes/no query user input
def yes_or_no(question):
	value = input(question + " (y/n): ")
	if (validate_yes_or_no(value)==True):
		if (value == "y"):
			return True
		return False
	else:
		return yes_or_no(question)

# validates yes/no query
def validate_yes_or_no(value):
	if (value == "y" or value == "n"):
		return True
	else:
		print("Enter y or n.")
		return False

# handles 1-5 selection user input
def list_pick(question):		
	value = input(question)
	if validate_1_5(value) == True:
		return int(value)
	else:
		return list_pick(question)


# validates 1-5 selection user input
def validate_1_5(value):
	try:
		num = int(value)
	except: 
		print("Please make a selection from 1-5.")
		return False
	if (num < 1 or num > 5):
		print("Please make a selection from 1-5.")
		return False
	return True


# unpack API info
def json_unpack(data):
	shelf = []
	for item in data["items"]:
		if 'title' not in item['volumeInfo']:
			title = ""
		else:
			title=item["volumeInfo"]["title"]
		if 'authors' not in item['volumeInfo']:
			author = ""
		else:
			author=item["volumeInfo"]["authors"][0]
		if 'publisher' not in item['volumeInfo']:
			publisher= ""
		else:
			publisher=item["volumeInfo"]["publisher"]
		# print(publisher)
		shelf.append( Book(title, author, publisher))
	return shelf


# queries API
def api_call(q):
	parameters = {'q':q, 'maxResults':5}
	r = requests.get("https://www.googleapis.com/books/v1/volumes", params=parameters)
	if r:
		data = r.json()
		return data
	print("No results. Please enter valid query.")
	return False

# ask if user wants to add a book
def ask_to_add(bookshelf, reading_list):
	add = yes_or_no("Add book to your list?")
	while add == True:
		number = list_pick("Enter the list number of the book to add (Pick 1-5): ")
		# this should GIVE BACK a number that works
		book_adder(bookshelf, reading_list, number)
		add = yes_or_no("Add another book to your list?")
	return

# adds a book from the current API call to the user's reading list
def book_adder(search_results, user_list, index):
	reading_list.append(search_results[index -1])
	#show current reading list:
	print("Your Current List:")
	display_list(user_list)
	return


# prints the menu and allows the user to pick which option to use
def menu_print():
	print("----------------------------")
	print("| Menu:                    |")
	print("| 1. Search For Books      |")
	print("| 2. View your reading list|")
	print("| 3. Quit                  |")
	print("----------------------------")
	return

#  choose from the man menu
def menu_choose():
	choice = input("Pick your menu item: ")
	if (choice == "1" or choice == "2" or choice == "3"):
		return choice
	print("Please enter valid number.")
	return menu_print()

#run book query on menu choice 1
def book_query():
# Clear out previous search results, if any
		q = input("Enter your query: ")
		results = api_call(q)
		if results:
			bookshelf = json_unpack(results)
			print("Your Results:")
			display_list(bookshelf)
			ask_to_add(bookshelf, reading_list)
		return(True)

# the basic user loop
def run_wizard():
	while True:
		menu_print()
		choice = menu_choose()
		if choice == "1":
			book_query()
		elif choice == "2":
			print("Your Current List:")
			display_list(reading_list)
		else:
			print("Goodbye!")
			break


# this is so that the whole application doesn't run when we run the testing suite
if __name__ == '__main__':
	# User Loop
	run_wizard()


