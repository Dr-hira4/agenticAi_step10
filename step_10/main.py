from agent import Agent, Runner
from connection import config
import asyncio

#srf LLM context:instructions de rahe haoin agents ko

agent = Agent(
    name="PoliceAssistant",
    instructions="User ka name Hira hai. Hamesha polite raho or jawab mein 'Hira' keh kar bulao."
)

async def main():
    reault = await Runner.run(
        starting_agent=agent,
        input="Who is the founder of Pakistan?",
        run_config=config #Ye bhi LLM context hai
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())