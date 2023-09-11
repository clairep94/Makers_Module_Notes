# DATA STRUCTURES:

## EXAMPLES OF DATA STRUCTURES:

```shell

# Nested dictionary
{
  'acebook' : {
    'password' : 'password123',
    'added_on' : '22/03/22',
  },
  'makersbnb' : {
    'password' : 'qwerty789',
    'added_on' : '22/03/22',
  }
}

# List of dictionaries
[
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]
```


## ADVANCED LIST -- FILTER, LAMBDA, MAP, LIST COMPREHENSION:
Use these instead of for loops

### FILTER:

Requires a list that returns a True/False condition to satisfy

* Check over elements of a list to see if the condition is satisfied


``` shell
def function(value) -> list:
    def condition_function(lst): #boolean condition
        return lst[key] == value
    
    return list(filter(condition_function, lst))


#EXAMPLE:
class Cohort():
    def _init_(self) -> None:
        self.list_of_students = [{dict1}, {dict2}, {dict3}, {dict4}]

    def list_employed_by(self, employer: str) -> list:
        def same_employer(student): #boulean condition
            return student["employer"] == employer

        return list(filter(same_employer, self.list_of_students))    

```

### LAMBDA & FILTER:
A Lambda is a small function with no name. It replaces the `same_employer()` function above.

* There is no `return` keyword

* The lambda function will automatically return the value of the expression in its body.

``` shell
list(filter(lambda <variable>: <comparitive expression containing variable>, list))


#EXAMPLE:
return list(filter(lambda student: student["employer"] == employer, self.list_of_students)]
```


### LIST COMPREHENSION:
Returns a list 

``` shell
list_2 = [func(i) for i in list if i satisfies a condition]
```

### MAP:
Similar to list comprehension but returns an map object of Iterable

``` shell
>>> result = map(lambda number: number * 2, [1, 2, 3, 4])

>>> result #creates a map object, not a list
<map object at 0x102488040>

>>> list(result) #list
[2, 4, 6, 8]

```

## ADVANCED DICTIONARY:

### DICTIONARY COMPREHENSION:
