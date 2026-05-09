import typing

import pytest

import models
from order_book import OrderBook


# -------------------- FIXTURES -------------------- #
@pytest.fixture
def order_book_factory() -> typing.Callable[[list[models.Order]], OrderBook]:
    def _create(orders: list[models.Order]) -> OrderBook:
        return OrderBook(orders)

    return _create


# -------------------- PROCESS LIMIT ORDER -------------------- #
def test_process_limit_order(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None:
    pass


# -------------------- PROCESS MARKET ORDER -------------------- #
def test_process_market_order(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None: ...


# -------------------- CANCEL ORDER -------------------- #
def test_cancel_order(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None: ...


# -------------------- GET BEST BID -------------------- #
def test_get_best_bid(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None: ...


# -------------------- GET BEST ASK -------------------- #
def test_get_best_ask(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None: ...


# -------------------- GET VOLUME AT PRICE -------------------- #
def test_get_volume_at_price(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None: ...
