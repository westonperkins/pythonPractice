## Data Types
- <b>Int</b>: any number that does not include a decimal
    - 100, -9, -893489, 1234422
- <b>Float</b>: number with decimal precision
    - 2252.0, -9.4
- <b>String</b>: words or anything really inside quotation marks
    - "Hello", "0", "bruh", "false"
- <b>Boolean</b>: True or False

## Output and Printing Functions
- `print("Hello world")`, `print("hello", 85, False, "9.4")`
    - like `console.log` but for python

## Variables
- `hello = "world"`
    - the variable is `hello` and the value is `"world"`

## Getting user input
- `input('Name: ')`
    - this will prompt the user to respond to <b>Name:</b>
- you can assign input to a variable i.e:
    - `name = input('Name: ')`

## Arithmetic Operators
- +, -, *, /
- exponent: ** 
    - 4 ** 2
        - 4 to the power of 2
- floor division: //
    - divides and rounds down
- modulus: %
    records the remainder of the division

## String Methods
- `.upper()`
     - entire string prints as uppercase
- `.lower()`
    - entire string lowercase
- `.capitalize()`
    - capitalizes the first letter in the string
- `.count()`
    - inside of the parenteses you can out a certain value and see how many of that value are inside
        - `.count('e')`: counts how many 'e's are inside whatever you call 'count' on

## Conditions and Conditional operators
- ==, !=, <=, >=, <, >
- or, and
    - you can also use the `not` keyword:
        - `result = 5 or not 11`
            - this will print true if "result" is equal to 5 or not 11
- If, Else, Elif

## Lists and tuples
- collections are unordered ordered groups of elements and
- List:
    - `x = [4, True, 'hi']`
    - `len(x)` prints the length of the list 'x'
    - `x.append(<value>)` adds a new value to the list 'x'
    - `x.entends(<list>)` adds a new list value to the end of the list 'x'
    - `x.pop()` removes the last element from the list
        - you can also pass an index as an argument into 'pop()' and it will remove the element with that index
    - Lists are mutable and values can be changed or values can be added to the list
- Tuples:
    - `x = (4, True, 'hi')`
    - Tuples are immutable and values cannot be changed
    - If you add a value to a tuple or try to change a value inside it, you will get an error message

## For loop
- enumerate (`enumerate()`) adds a counter to an iterable and returns it in a form of enumerating object
    - i.e counting the values in a list and assigning its index

## While loop
- "while condition is true, do this" 
- you can impliment a 'break' statement to occur, this breaks the loop if the break condition is met

## Slice operator
- syntax: `[start:stop:step]`
    - the values are all index based
    - i.e:
        - `x = [0,1,2,3,4,5,6,7,8]`
        - `sliced = x[0:4:2]`
            - start at index 0, stop at index 4, step by 2
            - sliced will print out <b>`[0,2]`</b>
                - starts at 0, stops at 4, steps by 2 index places, this includes the final step but does not include the stop value
- you can reverse a list with the slice operator
    - `x[::-1]` 
        - this is the same as saying `x[0:8:-1]
            - start at the first index, end at the last index, and then step by -1
            
## Sets
- unordered unique collection of elements
- there are no duplicates, there are no indexes (we do not keep track of orders)
- sets are very quick when it comes to: lookups, removals, or additions

## Dictionaries
- key value pair
    - similar to a map, hashmap, object, etc.

## Comprehensions
- 1 line initialization of a list, tuple, dictionary
    - `x = [x + 5 for x in range(5)]`
        - this prints `[5,6,7,8,9]`

## Unpack Operator
-  `x = [33,12,55,77,43,52]`
    - `print(x)` will print `[33,12,55,77,43,52]`
    - `print(*x)` will print `33 12 55 77 43 52`
        - `*` references to unpack
        - <b>Look at `index.py` for a better use case example</b>
        - `**` two asterisks for dictionaries

## *args, **kwargs
- stands for arguments, and keyword arguments
- allows you to pass in an unlimited amount of arguments and keyword arguments
    - useful when you dont know how many argument or keyword arguments you want to pass into a function
- <b>Look at `index.py` for a better use case example</b>

## Lambda
- one line anonymous function

## F strings
- imbed variables without having to reformat them
    - `x = f'hello {6+8} {tim}'`