from src import models
from src.books import order_book


class SimpleOrderBook(order_book.OrderBook):
    def process_limit_order(self, order: models.Order) -> models.MatchResult:
        ...

    def process_market_order(self, side: models.Side, quantity: int) -> models.MatchResult:
        ...

    def cancel_order(self, order_id: str) -> bool:
        ...

    def get_best_bid(self) -> int | None:
        ...

    def get_best_ask(self) -> int | None:
        ...

    def get_volume_at_price(self, side: models.Side, price: int) -> int:
        ...
