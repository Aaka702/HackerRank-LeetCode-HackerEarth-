def convert_to_24_hour(time_str):
    # Extract the time components
    time_components = time_str.split(":")
    hour = int(time_components[0])
    print(hour)
    minute = int(time_components[1][:-2])  # Remove "AM" or "PM" part
    print(minute)
    period = time_components[1][-2:]  # Get "AM" or "PM"
    print(period)

    # Convert to 24-hour format
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    # Format the hour and minute as strings with leading zeros
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Construct the 24-hour time string
    time_24_hour = f"{hour_str}:{minute_str}"

    return time_24_hour

# Test the function
time_12_hour = input("Enter the time")
time_24_hour = convert_to_24_hour(time_12_hour)
print(f"The time {time_12_hour} in 24-hour format is: {time_24_hour}")
