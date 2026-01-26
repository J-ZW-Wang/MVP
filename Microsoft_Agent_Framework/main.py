from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
import os
import asyncio

# TO DO
# - Setup orchestration for multiple agents: one agent to handle user input, another to fetch data from APIs, etc.
# - Implement structure output
# - Setup tools


def get_chat_agent():
    load_dotenv("./Microsoft_Agent_Framework/.env")
    openai_api_key = os.getenv("openai_api_key")

    agent = OpenAIChatClient(
        api_key=openai_api_key, model_id="gpt-5.2-2025-12-11"
    ).as_agent(
        name="chat_agent",
        instructions="You are a helpful assistant that provides concise and accurate information.",
    )

    return agent


async def main():
    chat_agent = get_chat_agent()
    user_input = input("User: ")
    while user_input != "Exit":
        print("Agent: ", end="", flush=True)
        async for chunk in chat_agent.run_stream(user_input):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        user_input = input("\nUser: ")


if __name__ == "__main__":
    asyncio.run(main())
