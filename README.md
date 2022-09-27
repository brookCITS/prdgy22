# Week 2 - OOP Concepts

## 1 - Functions
Create a function that will take two inputs (start, end) and generate and return a list containing all the even numbers between the two inputs. ex: start = 10 and end = 20 will out put [10,12,14,16,18,20]

Add a third input that's a boolean (start, end, even) and based on its value return a list of even numbers or odd numbers. ex: even = False will return [11,13,15,17,19]

save it in the file even.py

## 2 - Classes
create a character class with instance variables name, level, position, and lives. The name should be initialized when the instance of the class is created but the rest should be initialized with default values (level = 0, lives = 3, and position = 0).

- create a method called move() which takes a value speed and changes the position
- create a method called level_up() which adds 1 to the level
- create a method called kill() which subtracts 1 from lives
- create a method called bonus() which adds 1 to lives
- create 4 instance of this class and test all the methods twice

## 3 - Inheritance
Create a class called Shapes with an instance variable name that gets defined in the init method. Add a method called area which will do nothing (pass).

create a new class called Circle which inherits from Shapes class. override the init method so it takes a radius and saves it as an instance variable. override the area method so it returns the area of a circle with the given radius.

Create another class called Rectangle which inherits from Shapes class. override the init method so it takes a length, width and save them as an instance variables. override the area method so it returns the area of a Rectangle with the given length and width.


## 4 - Polymorphism
## Payroll
Create a class called payroll which has two instance variable, company name and employee_list.
- initialize the name by passing the value to the init method but for the employee_list, just make it an empty employee_list

- create a method called add_employee() which takes an Employee object and adds it to the employee_list

- create a method called get_payroll() which has no input but will loop through the employee_list and print out the name and salary of the employee (call the payment method on the employee object to get the salary)
