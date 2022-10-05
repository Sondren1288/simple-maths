# Contributing
If you wish to contribute a *function*, please add a docstring as a description of the function.
Inline comments are also greatly appreciated, especially for parts that are harder to follow, or just for reasoning.
If possible, try also to keep the return statement clean, so that it is somewhat easy to see what is returned.
A descriptive name like `length_` is easier understood than `sum([1 for x in list_])`. 
One could argue that the name of the function should tell what the last step is, but it is still preferred for clarity.
```python
    length_ = sum([1 for x in list_])
    return length_
```
is preferred over
```python
    return sum([1 for x in list_])
```
You should also aim to not have multiple functions in a single commit.
If there happens to be an implementation of one of your functions already that is equivalent, the ones that are not there already can still be added.
Please keep this in mind when making pull-requests.

The project uses 4 spaces and not tabs. 
It also, as a general rule, uses 2 newlines between functions.

As a student, my commit-speed may be somewhat unstable, but I will try to get through PRs as they come in.


## A note on docstrings
The docstrings does not need to be complex or in depth, but they should tell what the function does, and what to expect in return.
Larger and more complex function naturally have larger docstrings.

The below is taken from the official (PEP257 Docstring Convention)[https://peps.python.org/pep-0257/].
When adding docstrings, try to add the arguments as well, so that it is easier for others to know what the different parts are.
```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```
Helping by committing only improvements to docstrings and comments are also greatly appreciated.


## A note on complexity
Using functools and similar is fine, but there should be a version with simple "pure" python as well. 
Take product for an example. The function
```python
from numbers import Number
from functools import reduce
from collections.abc import Iterable
import operator
def product(iterable: Iterable[Number]) -> Number:
    product_ = reduce(operator.mul, iterable, 1)
    return product_
    
```
Works, is good, and it does what it says it does. It is, however, not necessarily easy to see exactly what is happening.
This function should exist in this repository, but it should be secondary to a function that does it "easy".
```python
from numbers import Number
from collections.abc import Iterable
def product(iterable: Iterable[Number]) -> Number:
    product_ = 1
    for num in iterable:
        product_ *= num
    return product_
```
Is a simple, easy function that most people who have coded anything in python understands.
It is also a function most people could have easily written themselves.
It should however still exist in this repository, and should be prioritized over function like the one above it. 


## A note on structure
The code will be subdivided into folders based on category.
If you feel that your function does not fit into any of these folders, you may make a new directory with the appropriate name, and add your function to it.

Several functions can do the same, as long as they do it differently \(see (A note on complexity)[##a-note-on-complexity] for an example\).
These functions should be in the same file, and preferably ordered by their complexity.
The easier the function is to understand, the higher up in this order it should be. 


## A note on what a "function" is
The important part of the function is that it should be able to run by itself without the rest of the file.
There should be no values used in the function that are defined outside the function.
The file should also *not* contain any print statements or any input statements.
If you wish to include a run of the function in the file, you may do so, but this should be done in either a `main()` function, 
or preferably in a `if __name__ == '__main__:`.

This will get approved
```python
def sum(iterable: Iterable[Number]) -> Number:
    sum_ = 0
    for num in iterable:
        sum_ += num
    return sum_

if __name__ == '__main__':
    # Test sum of a list
    sum_ = sum([1,2,3,4,5])
    print(sum_)
```

This will *not* get approved
```python
sum_ = 0
def sum(iterable: Iterable[Number]) -> Number:
    for num in iterable:
        sum_ += num
    return sum

s = input("List of numbers to sum: ")
s = s.split(' ')
s = [int(n) for n in s]
print(sum(s))
```
