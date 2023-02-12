# AirBnB clone

## About the project
	This project creates a basic clone of the popular AirBnB consisting of;
		Back-End
			- console like a minishell, 
			- file storage/MySQL Database
			- Rest APIs
			- Deployment
		Front-End
			- structure in form of HTML/CSS
	
----------More to be filled--------------------

### Command interpreter or console
	This console works in interactive and non-interactive mode;
----------to be filled--------------------
### Learning Objectives
	At the end of this project, we were expected to be able to explain to anyone, without the help of Google:
		- How to create a Python package
		- How to create a command interpreter in Python - using the cmd module
		- What is Unit testing and how to implement it in a large project
		- How to serialize and deserialize a Class
		- How to write and read a JSON file
		- How to manage datetime
		- What is an UUID
		- What is *args and how to use it
		- What is **kwargs and how to use it
		- How to handle named arguments in a function

### Execution
	The shell/interpreter works like this in interactive mode:

		$ ./console.py
		(hbnb) help

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit

		(hbnb) 
		(hbnb) 
		(hbnb) quit
		$
	But also in non-interactive mode:

		$ echo "help" | ./console.py
		(hbnb)

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit
		(hbnb) 
		$
		$ cat test_help
		help
		$
		$ cat test_help | ./console.py
		(hbnb)

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit
		(hbnb) 
		$
----------More to be filled--------------------