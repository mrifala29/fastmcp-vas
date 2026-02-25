import requests
import phonenumbers

from .config import BASE_URL
from phonenumbers import geocoder, carrier


def _resolve_country_operator(msisdn: str):
    try:
        parsed = phonenumbers.parse("+" + msisdn)

        country_code = phonenumbers.region_code_for_number(parsed)
        print(country_code)
        operator_name = carrier.name_for_number(parsed, "en").lower()
        print(operator_name)

        operator_map = {
            "omantel": "omantel",
            "oman telecommunications": "omantel",
            "lao telecom": "laotel",
            "laotel": "laotel",
        }

        operator_internal = operator_map.get(operator_name)

        if not operator_internal:
            raise ValueError(f"Unsupported operator: {operator_name}")

        return country_code, operator_internal

    except Exception:
        raise ValueError("Invalid or unsupported MSISDN")


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