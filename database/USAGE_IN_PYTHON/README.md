## Database - Usage in Python

### Topics covered
Establish a connection with Python, execute queries and use the returning data.

### Goal achieved

By the end of the exercise your CLI tool will be able to remove items from warehouses when an order is placed and keep a log of all actions taken by users and employees.

These changes will be made persistent by storing the data in a postgres database.

### Steps

Set the current code to read the data from the database.

> you have to change cli/loader.py

Run your unit tests to make sure everything works. Run the query tool manually as well, in case the unit tests don't cover all features.

### Add Feature: Placing Orders
Change your code so that it actually removes the ordered items from the warehouses in the Python objects.
Make sure these changes survive the session by saving the new state of the data back into the database. To do this, you can call the method `stock.to_dict()` that will return a dictionary that you can use to update your database.
>
> List all the items after placing an order and then quit, to see the total amount of items in all warehouses after the order.
>
> Search again the same item after placing an order and confirm the items removed were the correct ones.
>
> Make sure you only remove the items when the employee is authenticated and the required amount is available.

