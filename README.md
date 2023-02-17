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
<!-- ----------More to be filled-------------------- -->
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
		- What is HTML
		- How to create an HTML page
		- What is a markup language
		- What is the DOM
		- What is an element / tag
		- What is an attribute
		- How does the browser load a webpage
		- What is CSS
		- How to add style to an element
		- What is a class
		- What is a selector
		- How to compute CSS Specificity Value
		- What are Box properties in CSS
<!-- ----------More to be filled-------------------- -->
### Back-End
#### Command interpreter or console
	This console works in interactive and non-interactive mode;
	In order to start the console, use the following command: ./console.py

	Use cases:
		- manage (create, update, destroy, etc) objects via a console / command interprete
		- store and persist objects to a file (JSON file)
		- Commands: create, show, destroy, all (shows all), update, help, quit
<!-- ----------to be filled-------------------- -->
##### Execution
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
<!-- ----------More to be filled-------------------- -->
### Front-end
#### Web static
	Background Context
	Web static, what?
	Now that you have a command interpreter for managing our AirBnB objects, it’s time to make them alive!

	Before developing a big and complex web application, we will build the front end step-by-step.

	The first step is to “design” / “sketch” / “prototype” each element:

	- Create simple HTML static pages
	- Style guide
	- Fake contents
	- No Javascript
	- No data loaded from anything
	During this project, I learnt how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

	Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.