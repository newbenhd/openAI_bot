import os
import sys
from collections.abc import Callable
from dotenv import load_dotenv
from chatGPT import ChatGTP
load_dotenv()


def check_api_key():
    api_key = os.getenv("OPENAPI_API_KEY")
    if "OPENAI_API_KEY" not in os.environ:
        print("Missing ChatGPT api key")
        print("Directions to set api key:")
        print("1. Sign up OpenAI and get api key. Link: https://platform.openai.com/account/api-keys")
        print("2. Run something to set api key")
        sys.exit()


def check_arguments():
    if len(sys.argv) <= 1 or len(sys.argv) >= 3 or not isinstance(sys.argv[1], str):
        print("Argument invalid")
        print("Please give me a text in quote")
        sys.exit()


def run_functions(fns: list[Callable[[], None]]):
    for fn in fns:
        fn()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_functions([check_api_key, check_arguments])
    chat = ChatGTP(api_key=os.getenv("OPENAI_API_KEY"), model="text-davinci-003")
    print(chat.ask(text=sys.argv[1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
