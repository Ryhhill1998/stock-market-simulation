import dataclasses
import enum


class Side(enum.StrEnum):
    BUY = enum.auto()
    SELL = enum.auto()


@dataclasses.dataclass(frozen=True)
class Order:
    order_id: str
    side: Side
    price: int  # Using integers to avoid float errors
    quantity: int


@dataclasses.dataclass(frozen=True)
class Trade:
    price: int
    quantity: int
    maker_id: str
    taker_id: str


class OrderStatus(enum.StrEnum):
    FILLED = enum.auto()
    PARTIALLY_FILLED = enum.auto()
    RESTED = enum.auto()  # No match but added to the book
    REJECTED = enum.auto()  # Invalid order
    CANCELLED = enum.auto()  # For market orders that didn't find liquidity


@dataclasses.dataclass(frozen=True)
class MatchResult:
    order_status: OrderStatus
    trades: list[Trade]
    remaining_quantity: int
