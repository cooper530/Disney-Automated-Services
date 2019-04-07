month = 4
day = 17
park = "hws"
ride = "Toy Story Mania!"
input_time = '4:30PM'
#Enter in minutes, 0 if exact time only, 1440 if no grace period is needed
grace_period = 10
#How many times the system will search
cycle_time = 5

def convert_to_24(time):
    """Converts 12 hours time format to 24 hours
    """
    time = time.replace(' ', '')
    time, half_day = time[:-2], time[-2:].lower()
    if half_day == 'am':
        return time
    elif half_day == 'pm':
        split = time.find(':')
        if split == -1:
            split = None
        return str(int(time[:split]) + 12) + time[split:]
    else:
        raise ValueError("Didn't finish with AM or PM.")


input_time = convert_to_24(input_time)

(h, m) = input_time.split(':')
input_time = int(h) * 60 + int(m)
#print(input_time)