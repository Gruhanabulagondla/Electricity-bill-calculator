def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        bill = (
            (100 * 1.50)
            + (100 * 2.50)
            + (300 * 4.00)
            + ((units - 500) * 6.00)
        )

    return bill


def main():
    print("========== ELECTRICITY BILL CALCULATOR ==========")

    while True:
        try:
            units = float(input("\nEnter electricity units consumed: "))

            if units < 0:
                print("Units cannot be negative.")
                continue

            bill = calculate_bill(units)

            fixed_charge = 50
            total = bill + fixed_charge

            print("\n========== ELECTRICITY BILL ==========")
            print(f"Units Consumed: {units}")
            print(f"Energy Charges: ₹{bill:.2f}")
            print(f"Fixed Charge: ₹{fixed_charge:.2f}")
            print("--------------------------------------")
            print(f"Total Bill: ₹{total:.2f}")

            break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()