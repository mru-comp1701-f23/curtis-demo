def total_with_gst(purchase: float, first_tues: bool) -> float:
    """Checks if discount applies, returns total with GST"""
    ELIGIBLE_THRESHOLD = 50
    GST = 0.05
    if purchase > ELIGIBLE_THRESHOLD and first_tues:
        print("Congratulations, you get a discount!")
        purchase = purchase * 0.85
    else:
        print("Sorry, no discount for you")
    
    total = purchase * (1 + GST)
    return total

def main() -> None:
    purchase = float(input("What is the purchase value? "))
    first_tuesday = True
    total = total_with_gst(purchase, first_tuesday)
    print(f"Your total is ${total:.2f}")

main()