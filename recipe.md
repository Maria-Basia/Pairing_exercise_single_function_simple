# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_test(text):

    Parameters:
        text: a string containing words (e.g. "hello WORLD #TODO")

        Returns:
        a boolean True or False

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text that contains one #TODO it returns True
"""
test_one_TODO_returns_True("hello WORLD #TODO") => True

"""
Given a text that doesn't contain the word #TODO it returns False
"""
test_no_TODO_returns_False("hello WORLD") => False

"""
Given a text that contains a word similar to TODO returns False
"""
test_similar_to__TODO_returns_False("hello WORLD TODO") => False

"""
Given a text that contains #TODO followed by punctuation returns True
"""
test__TODO_with_punctuation_returns_True("Hello world #TODO.") => True

"""
Given a non-string input it shows an error message 
"""
test__wrong_input_format(5) => "Please provide text"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
