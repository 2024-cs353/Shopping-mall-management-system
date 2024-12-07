def get_user_input():
    user_input = input("Input Question：")
    return check_forbidden_words(user_input)


def check_forbidden_words(user_input):
    if "TestInstance" in user_input:
        return "InputSuccess"
    return user_input
