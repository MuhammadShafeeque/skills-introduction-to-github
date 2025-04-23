import calendar
from datetime import datetime

def print_calendar_with_today():
    # Get today's date and time
    now = datetime.now()
    today = now.day
    month = now.month
    year = now.year

    # Print today's date and time
    print(f"Today's Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Create a calendar for the current month
    cal = calendar.TextCalendar()
    cal_str = cal.formatmonth(year, month)

    # Highlight today's date in the calendar
    highlighted_cal = cal_str.replace(f" {today} ", f"[{today}] ")
    if today < 10:  # Handle single-digit dates
        highlighted_cal = highlighted_cal.replace(f" {today}\n", f"[{today}]\n")

    print(highlighted_cal)

# Call the function
print_calendar_with_today()