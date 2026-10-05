from datetime import date


def calculate_age(birth_date):
    today = date.today()

    if birth_date > today:
        return None

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1

        # Find the number of days in the previous month
        if today.month == 1:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_month = today.month - 1
            previous_year = today.year

        days_in_previous_month = (
            date(previous_year, previous_month + 1, 1)
            - date(previous_year, previous_month, 1)
        ).days if previous_month != 12 else 31

        days += days_in_previous_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    print("=" * 40)
    print("        AGE CALCULATOR")
    print("=" * 40)

    while True:
        birth_date_input = input(
            "Enter your date of birth (DD-MM-YYYY): "
        )

        try:
            day, month, year = map(int, birth_date_input.split("-"))
            birth_date = date(year, month, day)
            break

        except ValueError:
            print("Invalid date. Please enter it as DD-MM-YYYY.")
            print("Example: 15-08-2005\n")

    age = calculate_age(birth_date)

    if age is None:
        print("\nDate of birth cannot be in the future.")
        return

    years, months, days = age

    print("\n" + "=" * 40)
    print("             YOUR AGE")
    print("=" * 40)

    print(f"Years  : {years}")
    print(f"Months : {months}")
    print(f"Days   : {days}")

    print(f"\nYou are {years} years, {months} months, and {days} days old.")

    today = date.today()

    if birth_date.day == today.day and birth_date.month == today.month:
        print("🎉 Happy Birthday!")


if __name__ == "__main__":
    main()
