from src import models


class OrderBook:
    def process_limit_order(self, order: models.Order) -> models.MatchResult:
        """
        The core engine entry point.
        Matches against existing liquidity or rests the remainder.
        """
        if order.quantity <=0 or order.price<=0:
            return models.MatchResult(
                order_status=models.OrderStatus.REJECTED,
                trades=[],
                remaining_quantity=order.quantity
            )
        # Order = BUY 40 @ 101
        # ask = {100:20, 101:30}
        # 100 = 20 shares 
        # 101 = 30 shares
        
        trades = []
        remainder = order.quantity
        
        # BUY
        if order.side == models.Side.BUY:
            while remainder > 0:
                best_ask = min(self.ask) # 100
                available = self.ask[best_ask] #20
                quant = min(remainder,available) #20
                trades.append(price=best_ask, quantity=quant, maker_id= "no_idea", taker_id=order.order_id)
                remainder -= quant # remainder = 40 -20
                self.ask[best_ask] -= quant # ask {101:30}
            
            return models.MatchResult(
                order_status=models.OrderStatus.FILLED,
                trades=trades,
                remaining_quantity=remainder
            )
                
                
            
        
        
        

    def process_market_order(self, side: models.Side, quantity: int) -> models.MatchResult:
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

    def get_volume_at_price(self, side: models.Side, price: int) -> int:
        """Returns the total quantity resting at a specific price level."""

        ...
