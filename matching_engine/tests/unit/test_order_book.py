import typing

import pytest

import models
from src import constants
from order_book import OrderBook


# -------------------- FIXTURES -------------------- #
@pytest.fixture
def order_book_factory() -> typing.Callable[[list[models.Order]], OrderBook]:
    def _create(orders: list[models.Order]) -> OrderBook:
        return OrderBook(orders)

    return _create


# -------------------- PROCESS LIMIT ORDER -------------------- #
def test_process_limit_order_rested(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None:
    # ARRANGE
    orders: list[models.Order] = []
    order_book: OrderBook = order_book_factory(orders)

    # ACT
    order = models.Order(order_id="1", side=constants.Side.BUY, price=100, quantity=1)
    result: models.MatchResult = order_book.process_limit_order(order)

    # ASSERT
    expected_result = models.MatchResult(order_status=constants.OrderStatus.RESTED, trades=[], remaining_quantity=1)
    assert result == expected_result


def test_process_limit_order_filled(order_book_factory: typing.Callable[[list[models.Order]], OrderBook]) -> None:
    orders = [
        models.Order(order_id="1", side=constants.Side.BUY, price=100, quantity=1),
        models.Order(order_id="2", side=constants.Side.BUY, price=100, quantity=1),
        models.Order(order_id="3", side=constants.Side.BUY, price=100, quantity=1),
        models.Order(order_id="4", side=constants.Side.BUY, price=100, quantity=1),
        models.Order(order_id="5", side=constants.Side.BUY, price=100, quantity=1),
    ]


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
