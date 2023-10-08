# PYTHON:

## KEY CODE:
[Here is a list of Python's built-in functions](https://docs.python.org/3/library/functions.html)


## EXECUTING PYTHON CODE:
You can run python code in the terminal:
```
; mkdir my_python_code
; cd my_python_code
; touch hello_world.py
```

Then in VSC:
```
# File: hello_world.py
print("Hello, world!")
```

Then back in terminal:
```
; cd ~/Documents/my_python_code
; python3 hello_world.py
```



## BASIC PYTHON SUMM:

### METHODS - eg. String methods:
Methods are like functions, except that they are closely tied to a particular piece of data.

* [all the `String`-specific methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

* Python strings actually belong to a family of data types called `sequences`.
* [Sequence docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)


## INDEXING & SLICE NOTATION:
Python uses Zero Indexing. Start at `q` and `0` and count.
<i></i>

```
0  1  2  3  4  5  6  7  8
q  u  i  c  k     f  o  x
```
`string[-5]` returns `"k"`

Slice Notation:
`string[start_index:stop_index:step]` 
Note that stop_index is not inclusive, but start_index is.



### FLOAT, INT, BOOLEAN:
[Float and Integer documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

[Additional methods on floats](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float)

For boolean, instead of
```
def is_it_zero(num):
    if num == 0:
        return True
    else:
        return False```

do:

```
def is_it_zero(num):
    return num == 0```


## CONDITIONALS & CONTROL FLOW:

### SUMMARY:

* `if:` 
* `elif:`
* `else:`

* conditional operators: `==`, `!=`, `>`, `>=`, `<`, `<=`
* `%`

### LOOPS:

* `for:`
* `for i in range (start_at, stop_before, step_by)`
* `for char in string:`
* `for var in list:`
* `while:` + `Boolean conditional`
  * If running in terminal, press `Ctrl + C` to stop running


### FUNCTIONS:

* `return` for saving variables
* `print` for checking a variable

```
def add(num1: float, num2: float):
    print f"The first number is {num1}"
    print f"The second number is {num2}"
    return num1 + num2
```