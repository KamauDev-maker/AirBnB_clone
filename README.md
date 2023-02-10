<p align="center">
  <img src="https://github.com/KamauDev-maker/AirBnB_clone.git/images/download.png" alt="HolbertonBnB logo">
</p>

## Descripton of the project
The goal of the project is to deploy a clone of [AirBnB Website](https://www.airbnb.com/ "AirBnB Website") using my server. The final version of this project will have:
- A command interpreter to manipulate data without a visual interface, like a shell(perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
## Getting Started
To start the command interpreter type in these commands in your terminal:
```bash
Cloning the repo and starting the console:
================================
git clone https://github.com/KamauDev-maker/AirBnB_clone.git
cd AirBnB_clone
```
## Execution
Your shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
================================
EOF help quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
Also in non-interactive mode: (like the Shell project in C)
```bash
$  echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
==============================
EOF help quit
(hbnb)
$
```
## classes 
1.  User 
2.  BaseModel
3.  State
4.  City
5.  Amenity
6.  Place
7.  Review  

## commands
```bash
-  all - shows all objects the program has access to.
-  create - Creates and instance based on given class.
-  destroy  - Destroys/deletes an object based on classs and uuid.
-  show - shows an object based on class and uuid.
-  update - updstes existing attributes an objects based on class name.
```
<br>
<br>
<center> <h2>
Examples
</h2></center>
<h3>
Primary command syntax
</h3>
###### Example 0: Create an object
Usage: create < class_name >
```
(hbnb)  create User
```
```
(hbnb) create User
11f692aa-8dfd-4e6b-b354-d0259e667979
(hbnb)
```
###### Example 1: show an object
Usage: show < class_name > < _id >
```
(hbnb) show User 11f692aa-8dfd-4e6b-b354-d0259e667979
[User] (11f692aa-8dfd-4e6b-b354-d0259e667979) {'id': '11f692aa-8dfd-4e6b-b354-d0259e667979', 'created_at': datetime.datetime(2023, 2, 10, 13, 41, 2, 413345), 'updated_at': datetime.datetime(2023, 2, 10, 13, 41, 2, 413373)}
(hbnb)
```
###### Example 2: Destroy an object
Usage: destroy < class_name > <_id>
```
(hbnb) destroy User 11f692aa-8dfd-4e6b-b354-d0259e667979
(hbnb) show User 11f692aa-8dfd-4e6b-b354-d0259e667979
** no instance found **
(hbnb)
```
###### Example 3: Update an object
Usage: update < class_name> <_id> < attribute name > < attribute value >
```
(hbnb) update User 1ae80232-28c6-47bb-a920-0dbcb8b8f2db first_name "Oscar"
(hbnb) show User 1ae80232-28c6-47bb-a920-0dbcb8b8f2db
[User] (1ae80232-28c6-47bb-a920-0dbcb8b8f2db) {'id': '1ae80232-28c6-47bb-a920-0dbcb8b8f2db', 'created_at': datetime.datetime(2023, 2, 10, 14, 5, 18, 255517), 'updated_at': datetime.datetime(2023, 2, 10, 14, 9, 25, 273537), 'first_name': 'Oscar'}
(hbnb)
```
## Author
- [Oscar Kamau](https://github.com/KamauDev-maker "Oscar Kamau")
