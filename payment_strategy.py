from abc import ABC, abstractmethod


# Abstract Base Strategy
class PaymentStrategy(ABC):

  @abstractmethod
  def pay(self, amount: float) -> None:
    """Execute the payment transaction."""
    pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

  def __init__(self, card_number: str = "XXXX-XXXX-XXXX-1234"):
    self.card_number = card_number

  def pay(self, amount: float) -> None:
    masked = self.card_number[-4:]
    print(f"Paid ₹{amount:,.2f} using Credit Card ending in {masked}.")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):

  def __init__(self, email: str = "user@example.com"):
    self.email = email

  def pay(self, amount: float) -> None:
    print(f"Paid ₹{amount:,.2f} using PayPal account ({self.email}).")


# Concrete Strategy 3 (UPI)
class UPIPayment(PaymentStrategy):

  def __init__(self, vpa: str = "user@okaxis"):
    self.vpa = vpa

  def pay(self, amount: float) -> None:
    print(f"Paid ₹{amount:,.2f} via UPI ID ({self.vpa}).")


# Context Class
class PaymentContext:

  def __init__(self, strategy: PaymentStrategy):
    self._strategy = strategy

  @property
  def strategy(self) -> PaymentStrategy:
    return self._strategy

  @strategy.setter
  def strategy(self, strategy: PaymentStrategy) -> None:
    if not isinstance(strategy, PaymentStrategy):
      raise TypeError("Strategy must implement PaymentStrategy interface.")
    self._strategy = strategy

  def pay(self, amount: float) -> None:
    if amount <= 0:
      raise ValueError("Payment amount must be greater than zero.")
    self._strategy.pay(amount)


# -----------------------------
# Execution
# -----------------------------
if __name__ == "__main__":
  # Start with Credit Card
  context = PaymentContext(CreditCardPayment(card_number="4111-2222-3333-9876"))
  context.pay(1000)

  # Switch strategy at runtime to PayPal
  context.strategy = PayPalPayment(email="alex@domain.com")
  context.pay(500)

  # Switch strategy at runtime to UPI
  context.strategy = UPIPayment(vpa="alex@oksbi")
  context.pay(250)
