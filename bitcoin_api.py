"""
Bitcoin price API helper module.
Fetches real-time Bitcoin prices from Blockchain.info API.
"""
import requests
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

BLOCKCHAIN_TICKER_URL = "https://blockchain.info/ticker"


class BitcoinPriceError(Exception):
    """Custom exception for Bitcoin price fetching errors."""
    pass


def get_ticker() -> Dict[str, Dict[str, float]]:
    """
    Fetch current Bitcoin prices for all supported currencies.

    Returns:
        Dictionary with currency codes as keys and price data as values.
        Example: {'USD': {'15m': 50000.0, 'last': 50000.0, ...}, ...}

    Raises:
        BitcoinPriceError: If the API request fails.
    """
    try:
        response = requests.get(BLOCKCHAIN_TICKER_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch Bitcoin ticker: {e}")
        raise BitcoinPriceError(f"Unable to fetch Bitcoin prices: {e}")


def get_btc_price(currency: str) -> Optional[float]:
    """
    Get the current Bitcoin price for a specific currency.

    Args:
        currency: Currency code (e.g., 'USD', 'EUR')

    Returns:
        Current Bitcoin price in the specified currency, or None if not available.
    """
    try:
        ticker = get_ticker()
        currency_upper = currency.upper()
        if currency_upper in ticker:
            return ticker[currency_upper].get('15m') or ticker[currency_upper].get('last')
        return None
    except BitcoinPriceError:
        return None


def to_btc(currency: str, amount: float) -> Optional[float]:
    """
    Convert fiat currency amount to Bitcoin.

    Args:
        currency: Currency code (e.g., 'USD', 'EUR')
        amount: Amount in fiat currency

    Returns:
        Equivalent amount in Bitcoin, or None if conversion fails.
    """
    price = get_btc_price(currency)
    if price:
        return amount / price
    return None


def to_fiat(currency: str, btc_amount: float) -> Optional[float]:
    """
    Convert Bitcoin amount to fiat currency.

    Args:
        currency: Currency code (e.g., 'USD', 'EUR')
        btc_amount: Amount in Bitcoin

    Returns:
        Equivalent amount in fiat currency, or None if conversion fails.
    """
    price = get_btc_price(currency)
    if price:
        return btc_amount * price
    return None
