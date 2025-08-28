import os
from agents import Runner, OpenAIChatCompletionsModel, set_tracing_disabled,Agent
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
my_base_url =os.getenv("BASE_URL")
# print(my_key,base_url)

client = AsyncOpenAI(
    api_key= my_key,
    base_url= my_base_url
)    
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

japanese_assistant= Agent(
    name="Allie",
    model= MODEL,
    instructions="your name is Allie. You are a helpful agent which will help users related to there japanese. dont answer questions if they are not related to japanese. "
)

prompt = input("Enter your question: ")
set_tracing_disabled(True)
result = Runner.run_sync(
    starting_agent= japanese_assistant,
    input = prompt
)

print(result.final_output)