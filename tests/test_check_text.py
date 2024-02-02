from lib.check_text import *
import pytest

"""
Given a text that contains one #TODO it returns True
"""
def test_one_TODO_returns_True():
    result = check_text("hello WORLD #TODO")
    assert result == True

"""
Given a text that doesn't contain the word #TODO it returns False
"""
def test_no_TODO_returns_False():
    result = check_text("hello WORD") 
    assert result == False

"""
Given a text that contains a word similar to TODO returns False
"""
def test_similar_to__TODO_returns_False():
    result = check_text("hello WORLD TODO") 
    assert result == False

"""
Given a text that contains #TODO followed by punctuation returns True
"""
def test__TODO_with_punctuation_returns_True():
    result =check_text("Hello world #TODO.") 
    assert result == True


"""
Given a non-string input it shows an error message 
"""
def test__wrong_input_format():
    with pytest.raises(Exception) as error:
        check_text(5)
    error_message = str(error.value)
    assert  error_message =="Please provide text"