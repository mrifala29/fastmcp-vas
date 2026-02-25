import os
import requests
from fastmcp import FastMCP
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL not set in environment variables")

mcp = FastMCP("subscription-mcp")

def resolve_country_operator(msisdn: str):
    if msisdn.startswith("96"):
        return "OM", "omantel"
    elif msisdn.startswith("85"):
        return "LA", "laotel"
    else:
        raise ValueError("Unsupported MSISDN prefix")


@mcp.tool(
    name="list_subscriptions",
    description="Get active subscription services for a phone number"
)
def list_subscriptions(msisdn: str) -> list[str]:

    country, operator = resolve_country_operator(msisdn)

    url = f"{BASE_URL}/check/{country}/{operator}"

    response = requests.get(url, params={"msisdn": msisdn})
    response.raise_for_status()

    return response.json()["data"]


@mcp.tool(
    name="unsubscribe_service",
    description="Unsubscribe a service for a phone number"
)
def unsubscribe_service(msisdn: str, service: str) -> dict:

    country, operator = resolve_country_operator(msisdn)

    url = f"{BASE_URL}/unsub/{country}/{operator}"

    response = requests.get(
        url,
        params={
            "msisdn": msisdn,
            "service": service
        }
    )
    response.raise_for_status()

    return response.json()["data"]


if __name__ == "__main__":
    mcp.run()