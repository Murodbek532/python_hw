from datetime import datetime, date, timedelta
import re
import pytz
import time

# 1. Age Calculator
def age_calculator():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days += (date(today.year, today.month, 1) - date(prev_year, prev_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    print(f"Age: {years} years, {months} months, {days} days")

# 2. Days Until Next Birthday
def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
    delta = next_birthday - today
    print(f"Days until next birthday: {delta.days}")

# 3. Meeting Scheduler
def meeting_scheduler():
    current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))

    current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_dt = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
    print("Meeting will end at:", end_dt)

# 4. Timezone Converter
def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    src_tz_str = input("Enter your current timezone (e.g., 'UTC', 'US/Eastern'): ")
    dst_tz_str = input("Enter target timezone: ")

    dt_naive = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    src_tz = pytz.timezone(src_tz_str)
    dst_tz = pytz.timezone(dst_tz_str)

    dt_src = src_tz.localize(dt_naive)
    dt_dst = dt_src.astimezone(dst_tz)
    print("Converted time:", dt_dst)

# 5. Countdown Timer
def countdown_timer():
    target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    target_dt = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = target_dt - now
        if remaining.total_seconds() <= 0:
            print("Time is up!")
            break
        print("Time remaining:", remaining)
        time.sleep(1)

# 6. Email Validator
def email_validator():
    email = input("Enter email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")

# 7. Phone Number Formatter
def phone_formatter():
    num = input("Enter 10-digit phone number: ")
    if len(num) == 10 and num.isdigit():
        formatted = f"({num[0:3]}) {num[3:6]}-{num[6:]}"
        print("Formatted:", formatted)
    else:
        print("Invalid phone number")

# 8. Password Strength Checker
def password_checker():
    password = input("Enter password: ")
    strong = True
    if len(password) < 8:
        strong = False
    if not any(c.isupper() for c in password):
        strong = False
    if not any(c.islower() for c in password):
        strong = False
    if not any(c.isdigit() for c in password):
        strong = False
    print("Strong password" if strong else "Weak password")

# 9. Word Finder
def word_finder():
    text = "This is a sample text. This text is for testing word finder."
    word = input("Enter word to find: ")
    matches = [m.start() for m in re.finditer(word, text)]
    print(f"Word '{word}' found at positions:", matches)

# 10. Date Extractor
def date_extractor():
    text = input("Enter text: ")
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(pattern, text)
    print("Dates found:", dates)


if __name__ == "__main__":
    age_calculator()

