import requests
from .config import BASE_URL


def _resolve_country_operator(msisdn: str):
    if msisdn.startswith("96"):
        return "OM", "omantel"
    elif msisdn.startswith("85"):
        return "LA", "laotel"
    else:
        raise ValueError("Unsupported MSISDN prefix")


def fetch_subscriptions(msisdn: str) -> list[str]:
    country, operator = _resolve_country_operator(msisdn)

    url = f"{BASE_URL}/check/{country}/{operator}"

    response = requests.get(url, params={"msisdn": msisdn})
    response.raise_for_status()

    return response.json()["data"]


def unsubscribe(msisdn: str, service: str) -> dict:
    country, operator = _resolve_country_operator(msisdn)

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