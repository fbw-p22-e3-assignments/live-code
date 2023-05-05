# Django ORM III

## Field Lookups when Querying the Database:

Field lookups are used to filter and query data from a database based on specific criteria. These lookups allow us to perform more complex searches and retrieve specific data we require from the database. 

Example:
Suppose we have a model called 'Employee' with fields 'name', 'age', and 'salary'. We can use field lookups to retrieve all employees with an age greater than or equal to 25 using the following code:

```python
Employee.objects.filter(age__gte=25)
```
Here '__gte' is the field lookup that stands for 'greater than or equal to'.

## Querying using Complex Conditional Statements:

The QuerySet is a powerful tool that allows us to create complex queries by using conditional statements like 'AND', 'OR', and 'NOT'. These statements can be used to combine multiple filters together and retrieve the data we require.

Example:
Suppose we have a model called 'Book' with fields 'title', 'author', and 'year_published'. We can use complex conditional statements to retrieve all books written by 'Stephen King' and published after the year 2000 using the following code:

```python
Book.objects.filter(author='Stephen King' AND year_published__gt=2000)
```
Here, we used two filters and joined them using the 'AND' operator.

## Chaining QuerySets:

We can chain multiple QuerySets together to create a more complex query. This is useful when we want to filter the data based on multiple criteria.

Example:
Suppose we have a model called 'Product' with fields 'name', 'price', and 'category'. We can chain multiple QuerySets together to retrieve all products with a price greater than 10 and belonging to the 'Electronics' category using the following code:

```python
Product.objects.filter(price__gt=10).filter(category='Electronics')
```
Here, we used two filters chained together to create the desired query.

## Object Annotation:

Object annotation is a way of adding extra information to a QuerySet. This information can be used to provide additional context to the data we are retrieving.

Example:
Suppose we have a model called 'Order' with fields 'customer', 'date', and 'amount'. We can annotate the QuerySet to add an extra field called 'total_amount' that calculates the total amount of all orders using the following code:

```python
from django.db.models import Sum
orders = Order.objects.annotate(total_amount=Sum('amount'))
```
Here, we used the Sum() function to calculate the total amount and added it as an extra field called 'total_amount' to the QuerySet.

## Aggregation, Counting, and Ordering using QuerySets:

We can use QuerySets to perform aggregation functions like counting, averaging, and summing on data. We can also use QuerySets to order the data based on specific criteria.

Example:
Suppose we have a model called 'Employee' with fields 'name', 'age', and 'salary'. We can use QuerySets to retrieve the top 5 employees with the highest salaries using the following code:

```python
from django.db.models import Max
top_employees = Employee.objects.order_by('-salary')[:5]
```
Here, we used the order_by() function to order the data based on the 'salary' field in descending order and retrieved the top 5 employees using slicing.

To count the number of employees in a department, we can use the count() function:

```python
num_employees = Employee.objects.filter(department='IT').count()
```

Similarly, we can use the aggregate() function to perform more complex aggregation operations like calculating the average salary of employees in a department:

```python
from django.db.models import Avg
avg_salary = Employee.objects.filter(department='IT').aggregate(Avg('salary'))
```

Here, we used the aggregate() function to calculate the average salary of employees in the 'IT' department using the Avg() function.

In conclusion, using field lookups, complex conditional statements, QuerySet chaining, object annotation, and aggregation functions, we can perform powerful and complex queries on data in our database using Django.

