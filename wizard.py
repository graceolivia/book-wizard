# to call APIs
import requests

# to parse json
import json

# Important Variables

# holds current search results
results=[]
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
	if list_val(value, question) == True:
		return int(value)
	else:
		return list_pick(question)



# validates 1-5 selection user input
def list_val(value, question):
	try:
		num = int(value)
	except: 
		print("Please make a selection from 1-5.")
		return False
	if (num < 1 or num > 5):
		print("Please make a selection from 1-5.")
		return False
	return True


# queries API
def api_call(q, storage):
	# empty storage
	parameters = {'q':q, 'maxResults':5}
	# ERROR HANDLING NEEDED HERE
	r = requests.get("https://www.googleapis.com/books/v1/volumes", params=parameters)
	data = r.json()
	# print(data)
		# add data
	for item in data["items"]:
		# print(n)
		if 'title' not in item['volumeInfo']:
			title = ""
		else:
			title=item["volumeInfo"]["title"]
		# print(title)
		if 'authors' not in item['volumeInfo']:
			author = ""
		else:
			author=item["volumeInfo"]["authors"][0]
		# print(authors)
		if 'publisher' not in item['volumeInfo']:
			publisher= ""
		else:
			publisher=item["volumeInfo"]["publisher"]
		# print(publisher)
		storage.append( Book(title, author, publisher))

# ask user if they want to add books

def book_adder(search_results, user_list, index):
	reading_list.append(results[index -1])
	#show current reading list:
	print("Your Current List:")
	display_list(user_list)
	return

if __name__ == '__main__':
	# User Loop
	while True:
		cont = yn("Ready To Search?")
		if cont == True:
			# Clear out previous search results, if any
			results=[]
			q = input("Enter your query: ")
			api_call(q, results)
			print("Your Results:")
			display_list(results)
			add = yn("Add book to your list?")
			while add == True:
				number = list_pick("Enter the list number of the book to add (Pick 1-5): ")
				# this should GIVE BACK a number that works
				book_adder(results, reading_list, number)
				add = yn("Add book to your list?")
			continue
		elif cont == False:
			print("Goodbye!")
			break



