def total_with_gst(purchase: float, first_tues: bool) -> float:
    """Checks if discount applies, returns total with GST"""
    ELIGIBLE_THRESHOLD = 50
    GST = 0.05
    if purchase > ELIGIBLE_THRESHOLD and first_tues:
        print("Congratulations, you get a discount!")
        purchase = purchase * 0.85
    
    total = purchase * (1 + GST)
    return total

def main() -> None:
    # testing function
    print(total_with_gst(40, True)) # no discount
    print(total_with_gst(60, True)) # discount
    print(total_with_gst(50, True)) # no discount
    print(total_with_gst(40, False)) # no discount
    print(total_with_gst(60, False)) # no discount
    print(total_with_gst(50, False)) # no discount

main()