import enum


class Side(enum.StrEnum):
    BUY = enum.auto()
    SELL = enum.auto()


class OrderStatus(enum.StrEnum):
    FILLED = enum.auto()
    PARTIALLY_FILLED = enum.auto()
    RESTED = enum.auto()  # No match but added to the book
    REJECTED = enum.auto()  # Invalid order
    CANCELLED = enum.auto()  # For market orders that didn't find liquidity
