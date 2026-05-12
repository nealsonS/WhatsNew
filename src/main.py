from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from tools.search import web_search
from dotenv import load_dotenv
import yaml


def load_config(path: str):
    with open(path, "r") as f:
        CONFIG = yaml.safe_load(f)

    return CONFIG


def main():
    load_dotenv()
    CONFIG = load_config("../config.yaml")
    # system_prompt = SystemMessage()
    messages = [
        SystemMessage(
            "You are a researcher tasked on finding out what current and hot topics based on the user's topic of their choosing. Keep it consise!",
        ),
        HumanMessage("What's new on Visual Language Models?"),
    ]
    model = ChatAnthropic(**CONFIG["MODEL"])

    for chunk in model.stream(messages):
        print(chunk.text, end="")


if __name__ == "__main__":
    main()
