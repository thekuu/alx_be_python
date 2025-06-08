def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
display_current_datetime()


def calculate_future_date():
    try:
        days = int(input("Enter number of days to add (positive integer): "))
        
        if days < 0:
            print("Please enter a positive number of days.")
            return
        current_date = datetime.now().date()
        future_date = current_date + timedelta(days=days)
        print(f"\nCurrent date: {current_date.strftime('%Y-%m-%d')}")
        print(f"Future date after adding {days} days: {future_date.strftime('%Y-%m-%d')}")
    
    except ValueError:
        print("Invalid input. Please enter a whole number.")
calculate_future_date()