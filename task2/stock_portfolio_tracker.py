stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00
}
portfolio = {}
total_investment = 0.0
print("=== Stock Portfolio Tracker ===")
print("Available stocks and sample prices:")
for symbol, price in stock_prices.items():
    print(f"{symbol}: ${price:.2f}")
print("\nEnter a stock symbol and quantity.")
print("Type DONE as the stock symbol when finished.")
while True:
    symbol = input("\nStock symbol (or DONE): ").upper().strip()
    if symbol == "DONE":
        break
    if symbol not in stock_prices:
        print("That stock is not in the sample price list. Try again.")
        continue
    try:
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Quantity must be a positive whole number.")
            continue
    except ValueError:
        print("Please enter a whole number for quantity.")
        continue
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
print("\n=== Portfolio Summary ===")
if not portfolio:
    print("No stocks were added.")
else:
    for symbol, quantity in portfolio.items():
        value = stock_prices[symbol] * quantity
        total_investment += value
        print(
            f"{symbol}: {quantity} shares x ${stock_prices[symbol]:.2f}"
            f" = ${value:.2f}"
        )
    print(f"Total investment value: ${total_investment:.2f}")
    # Optional: save the summary to a text file
    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Summary\n")
        for symbol, quantity in portfolio.items():
            value = stock_prices[symbol] * quantity
            file.write(
                f"{symbol}: {quantity} shares, value = ${value:.2f}\n"
            )
        file.write(f"Total investment value: ${total_investment:.2f}\n")
    print("Summary saved to portfolio_summary.txt")