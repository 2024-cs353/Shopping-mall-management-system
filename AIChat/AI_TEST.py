from AI_Input import get_user_input
from AI_Process import get_ai_response


def main():
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'exit':
            break
        response = get_ai_response(user_input)
        print("AI's answer：", response)


if __name__ == "__main__":
    main()
