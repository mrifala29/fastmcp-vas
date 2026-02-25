from fastmcp import FastMCP
from .services import fetch_subscriptions, unsubscribe

mcp = FastMCP("vas-mcp")


@mcp.tool(
    name="list_subscriptions",
    description="Get active subscription services for a phone number"
)
def list_subscriptions(msisdn: str) -> list[str]:
    return fetch_subscriptions(msisdn)


@mcp.tool(
    name="unsubscribe_service",
    description="Unsubscribe a service for a phone number"
)
def unsubscribe_service(msisdn: str, service: str) -> dict:
    return unsubscribe(msisdn, service)