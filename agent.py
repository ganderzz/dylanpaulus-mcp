import asyncio
from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("fast-agent client")


@fast.agent(instruction="You are a helpful AI Agent", servers=["dp_mcp"])
async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
