from lib.check_text import *
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
    result = check_text("hello WORLD") 
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