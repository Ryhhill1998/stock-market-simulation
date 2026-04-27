import pytest

from src.order_book import OrderBook


@pytest.fixture
def order_book() -> OrderBook:
    return OrderBook()


def test_process_limit_order(order_book: OrderBook) -> None: ...


def test_process_market_order(order_book: OrderBook) -> None: ...


def test_cancel_order(order_book: OrderBook) -> None: ...


def test_get_best_bid(order_book: OrderBook) -> None: ...


def test_get_best_ask(order_book: OrderBook) -> None: ...


def test_get_volume_at_price(order_book: OrderBook) -> None: ...
