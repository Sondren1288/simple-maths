# Contributing
If you wish to contribute a *function*, please add a docstring as a description of the function.
Inline comments are also greatly appreciated, especially for parts that are harder to follow, or just for reasoning.
If possible, try also to keep the return statement clean, so that it is somewhat easy to see what is returned.
```python
    return length_
```
is preferred over
```python
    return sum([1 for x in list_])
```
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


## A not on structure
The code will be subdivided into folders based on category.
If you feel that your function does not fit into any of these folders, you may make a new directory with the appropriate name, and add your function to it.

Several functions can do the same, as long as they do it differently \(see (A note on complexity)[##a-note-on-complexity] for an example\).
These functions should be in the same file, and preferably ordered by their complexity.
The easier the function is to understand, the higher up in this order it should be. 


