import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

# from app.services import _resolve_country_operator
# test_number="6281575810314"
# print(test_number)
# _resolve_country_operator(test_number)


async def main():
    transport = StdioTransport(
        command="python",
        args=["main.py"]
    )

    client = Client(transport)

    async with client:
        result = await client.call_tool(
            "list_subscriptions",
            {"msisdn": "6281575810314"}
        )
        print("Result:", result)

asyncio.run(main())