This page is a non-exhaustive list of good practices in Python.

These good practices follows the [PEP 8 style guide](https://peps.python.org/pep-0008/), that we advise you to read.

## Naming conventions

In python, the most common cases are: `snake_case` (lower case separated by a `_`), `PascalCase` (capital letters as a separation, including the first word), and `UPPER_CASE`. The usages are the following:

- `snake_case` for file names, folder names, variables, functions, methods, objects, and also your package name.
- `PascalCase` to define classes and exceptions.
- `UPPER_CASE` for constants.

!!! note
    For protected methods and internal functions, you can use a `_` before, e.g. `_my_function`. For private methods, use two `_`, e.g. `__my_method`.

## Code readability

We listed below some advises to make the code easier to read.

- Use `_` to name a variable that will not be used. It will directly indicate that this variable will not be used, and we can forget about it. For instance, if we are only interested in the first value of a tuple: `a, _ = f()`, or if you don't need the index in a for loop: `for _ in range(10):`
- Remove all your unused imports. It makes the code shorter, faster, and easier to read.
- Avoid having many nested loops. Instead, you can refactor your code to return early, or make new functions. We recommend to have at most 2 levels of nested indentation inside functions/methods.

## Type hints

We recommend to use type hints inside each function and method (see [PEP guidelines](https://peps.python.org/pep-0484/)). Two basic examples can be found below.

!!! note
    When nothing is returned, `None` can be used as the function output type. Also, some typings can be imported from `typing`, e.g. `List`.

```python
from typing import List

def greeting(name: str) -> None:
    print(f'Hello {name}!')

def list_multiplication(l: List[float], a: int) -> List[float]:
    return [a * x for x in l]
```

There are many advantages of type hints. In particular, it:

- enables code completion
- is less error prone (since your IDE may help you track bugs before they happen)
- improves readability
- guide the user to understand the input/output of any function

## Catching bad inputs

It can be very useful to run a sanity check before running some functions to make sure every argument satisfies some constraints. When the arguments don't satisfies the contraint, you can return a meaningful error message, and it can save you a lot of time of bug fixing.

```python
from model import MyModel

def f(x: MyModel, a: float):
    assert isinstance(x, MyModel), f"The argument 'x' has to be a MyModel object, but found {type(x)}."
    assert 0 < a < 1, f"The argument 'a' should be included in ]0, 1[, but found {a}."
    ...
```

## Documentation

All packages must be documented. For that, a documentation is already ready-for-use (see its [usage](../features/doc)). In particular, it means that every function and method should be properly described using dosctrings.

!!! note
    Comments can also be used, but are **not** encouraged. Indeed, the usage of docstrings + type hints + meaningful variable names can be more clear that comments. Also, sometimes we may forgot to update the comment, making the code inconsistent with the comments. Still, sometimes, it can be useful for some "tricky" parts of the code.

## Code testing

Testing your code becomes crucial when your project gets bigger. Even though it takes some time to implement, it may save you twice this time in debugging. Mostly, it will improve the stability or your package and make sure it's always fully functional. See [here](../features/test) for an explanation on how to use `pytest` for your project.

## Code formatting

Tools like [black](https://github.com/psf/black) helps you format your code. It will make it more readable, automatically. See [here](../features/black) for an explanation on how to use `black` for your project.

## What to **not** do

- Never `import *` from a package. Else, you never know know which functions comes from which package, and it can cause conflicts/bugs.
- Don't overwrite python builtins and reserved keywords, such as `None`, `list`, `id`, ...
- Never use a list (or any mutable variable) as a default argument of a function. Indeed, you'll not have the same default argument each time, since it can be muted. For instance, if you set `default_arg=[]`, then at the next call it may not be empty anymore. Instead, use `default_arg=None`, and you can set it to `[]` later on in the code.