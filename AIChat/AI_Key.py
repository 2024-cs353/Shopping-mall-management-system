def keyword_detection(user_input):
    """
    Detect specific keywords in the user input.
    If the keyword 'hi' is found, return a predefined response.
    """
    if "hi" in user_input.lower():
        return "你好!请问有什么能够帮助你的"
    if "Ciallo" in user_input.lower():
        return "柚子÷"
    return None
