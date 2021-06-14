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
	for (i, n) in enumerate(the_list, start=1):
		print(i, end='')
		print(".")
		print("  Title: " + n.title)
		print("  Author: " + n.author)
		print("  Publisher: " + n.publisher)
		

# handles yes/no query user input
def yn(question):
	value = input(question + " (y/n): ")
	if (v_yn(value)==True):
		if (value == "y"):
			return True
		return False
	else:
		return yn(question)

# validates yes/no query
def v_yn(value):
	if (value == "y" or value == "n"):
		return True
	else:
		print("Enter y or n.")
		return False

# handles 1-5 selection user input
def list_pick(question):		
	value = input(question)
	if list_val(value) == True:
		return int(value)
	else:
		return list_pick(question)


# validates 1-5 selection user input
def list_val(value):
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

# adds a book from the current API call to the user's reading lst
def book_adder(search_results, user_list, index):
	reading_list.append(search_results[index -1])
	#show current reading list:
	print("Your Current List:")
	display_list(user_list)
	return


# prints the menu and allows the user to pick which option to use
def menu_pick():
	print("Menu:")
	print("1. Search For Books")
	print("2. View your reading list")
	print("3. Quit")
	choice = input("Pick your menu item: ")
	if (choice == "1" or choice == "2" or choice == "3"):
		return choice
	print("Please enter valid number.")
	return menu_pick()

# this is so that the whole application doesn't run when we run the testing suite
if __name__ == '__main__':
	# User Loop
	while True:
		choice = menu_pick()
		if choice == "1":
			# Clear out previous search results, if any
			q = input("Enter your query: ")
			results = api_call(q)
			if results:
				bookshelf = json_unpack(results)
				print("Your Results:")
				display_list(bookshelf)
				add = yn("Add book to your list?")
				while add == True:
					number = list_pick("Enter the list number of the book to add (Pick 1-5): ")
					# this should GIVE BACK a number that works
					book_adder(bookshelf, reading_list, number)
					add = yn("Add book to your list?")
				continue
			continue
		elif choice == "2":
			print("Your Current List:")
			display_list(reading_list)
		else:
			print("Goodbye!")
			break



