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
            "unsubscribe_service",
            {
                "msisdn": "96899842693",
                "service": "kidzoo"
            }
        )

        print("Raw result:", result)
        print("Data only:", result.data)

asyncio.run(main())