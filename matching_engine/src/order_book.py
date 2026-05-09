import constants
from src import models


class OrderBook:
    def __init__(self, orders: list[models.Order] | None = None) -> None:
        self._orders = orders

    def process_limit_order(self, order: models.Order) -> models.MatchResult:
        """
        The core engine entry point.
        Matches against existing liquidity or rests the remainder.
        """

        ...

    def process_market_order(self, side: constants.Side, quantity: int) -> models.MatchResult:
        """
        Immediately consumes liquidity at the best available prices.
        Does not enter the book.
        """

        ...

    def cancel_order(self, order_id: str) -> bool:
        """Removes a resting order. Returns True if successful."""

        ...

    def get_best_bid(self) -> int | None:
        """Returns the highest buy price currently on the book."""

        ...

    def get_best_ask(self) -> int | None:
        """Returns the lowest sell price currently on the book."""

        ...

    def get_volume_at_price(self, side: constants.Side, price: int) -> int:
        """Returns the total quantity resting at a specific price level."""

        ...
