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

# handles yes/no query
def yn(question):
	value = input(question + " (y/n):")
	if (value == "y"):
		return True
	elif (value == "n"):
		return False
	else:
		print("Please answer [y/n].")
		return yn(question)

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

def book_adder(search_results, user_list):
	add_q = yn("Add Book To List?") 
	print(str(add_q))
	if (add_q == True):
		to_add = input("Enter the list number of the book to add: ")
		index = int(to_add)
		reading_list.append(results[index -1])
		#show current reading list:
		print("Your Current List:")
		display_list(user_list)
		book_adder(search_results, user_list)
	return

# User Loop
while True:
	cont = yn("Ready To Search?") 
	if cont == True:
		results=[]
		q = input("Enter your query: ")
		api_call(q, results)
		print("Your Results:")
		display_list(results)
		book_adder(results, reading_list)
	elif cont == False:
		print("BREAK")
		break






