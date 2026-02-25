import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

async def main():
    transport = StdioTransport(
        command="python",
        args=["main.py"]
    )

    client = Client(transport)

    async with client:
        result = await client.call_tool(
            "list_subscriptions",
            {"msisdn": "96899842693"}
        )
        print("Result:", result)

asyncio.run(main())