import dataclasses

from src import constants


@dataclasses.dataclass(frozen=True)
class Order:
    order_id: str
    side: constants.Side
    price: int  # Using integers to avoid float errors
    quantity: int


@dataclasses.dataclass(frozen=True)
class Trade:
    price: int
    quantity: int
    maker_id: str
    taker_id: str


@dataclasses.dataclass(frozen=True)
class MatchResult:
    order_status: constants.OrderStatus
    trades: list[Trade]
    remaining_quantity: int
