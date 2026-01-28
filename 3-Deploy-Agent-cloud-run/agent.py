from google.adk.agents.llm_agent import Agent


def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
    currency_date: str = "latest",
):
    """Retrieves the exchange rate between two currencies on a specified date."""
    import requests

    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()


root_agent = Agent(
    model="gemini-2.5-flash",
    name="currency_exchange_agent",
    description=(
        "A financial assistant that provides real-time and historical "
        "currency exchange rates using the Frankfurter API."
    ),
    instruction=(
        "You are a currency expert. When users ask about exchange rates, "
        "extract the ISO currency codes and the date. Use the get_exchange_rate "
        "tool to fetch data. Provide a clear, concise answer including the "
        "effective date of the rate."
    ),
    tools=[get_exchange_rate],
)
