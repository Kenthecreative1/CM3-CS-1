def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    """Converts a dollar amount string (e.g., '$50.00') to a float."""
    return float(d.strip("$"))

def percent_to_float(p):
    """Converts a percentage string (e.g., '15%') to a float (e.g., 0.15)."""
    return float(p.strip("%")) / 100

if __name__ == "__main__":
    main()
