order_amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").strip().lower()

if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")
    print("Eligibility status: Not eligible")
else:
    if order_amount >= 5000:
        discount_percentage = 15
        eligibility = "Eligible for 15% discount"
    elif order_amount >= 2000 and membership == "yes":
        discount_percentage = 10
        eligibility = "Eligible for 10% discount"
    else:
        discount_percentage = 0
        eligibility = "No discount"

    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    print("Original amount: ₹", order_amount)
    print("Discount percentage:", discount_percentage, "%")
    print("Discount amount: ₹", round(discount_amount, 2))
    print("Final payable amount: ₹", round(final_amount, 2))
    print("Eligibility status:", eligibility)
