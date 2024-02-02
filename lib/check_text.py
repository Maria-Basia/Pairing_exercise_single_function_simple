def check_text(text):
    if type(text) != str:
        raise Exception("Please provide text")
    if "#TODO" in text:
        return True
    else:
        return False