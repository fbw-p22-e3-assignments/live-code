# Extending Classes

#### 1. Employee Class

- Create an `Employee` class which accepts 5 arguments and sets the following properties:

  - `id` of the employee as a number
  - `firstName` of the employee as a string
  - `lastName` of the employee as as string
  - `taxId` as a number
  - `salary` as a number

- The `Employee` class should have a `generatePaySlip` method which returns a string in the format:

```
       Employee ID: id
       Name: firstName lastName
       Tax ID: taxId
       Pay: monthlySalary --> will need to be calculated based off of salary
```

