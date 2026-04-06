# Coin and Note Exchange Program

def exchange_money(amount):
    denominations = [100, 50, 20, 10, 5, 2, 1
    result = {}

    for denom in denominations:
        count = amount // denom
        if count > 0:
            result[denom] = count
            amount = amount % denom

    return result


def main():
    try:
        amount = int(input("Enter the amount: "))
        if amount < 0:
            print("Please enter a positive amount.")
            return

        breakdown = exchange_money(amount)

        print("\nDenomination breakdown:")
        for denom, count in breakdown.items():
            print(f"{denom} : {count}")

    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
