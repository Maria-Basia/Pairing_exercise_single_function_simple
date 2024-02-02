
"""
Given a text that contains one #TODO it returns True
"""
def test_one_TODO_returns_True():
    result = check_text("hello WORLD #TODO")
    assert result == True