import pywhatkit
from datetime import datetime
import re

def validate_phone(phone):
    """
    Validates international phone number format.
    Example: +919876543210
    """
    pattern = r'^\+\d{10,15}$'
    return bool(re.match(pattern, phone))

def validate_time(hour, minute):
    return 0 <= hour <= 23 and 0 <= minute <= 59

try:
    print("=" * 50)
    print("WhatsApp Message Scheduler")
    print("=" * 50)

    mobile = input("Enter receiver's number (+countrycode): ").strip()

    if not validate_phone(mobile):
        raise ValueError(
            "Invalid phone number. Example: +919876543210"
        )

    message = input("Enter message: ").strip()

    if not message:
        raise ValueError("Message cannot be empty.")

    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))

    if not validate_time(hour, minute):
        raise ValueError("Invalid time entered.")

    now = datetime.now()

    if hour < now.hour or (
        hour == now.hour and minute <= now.minute
    ):
        raise ValueError(
            "Scheduled time must be in the future."
        )

    print("\nScheduling message...")
    pywhatkit.sendwhatmsg(
        mobile,
        message,
        hour,
        minute,
        wait_time=15,
        tab_close=True,
        close_time=3
    )

    print("Message scheduled successfully!")

except ValueError as e:
    print(f"Input Error: {e}")

except Exception as e:
    print(f"Unexpected Error: {e}")
