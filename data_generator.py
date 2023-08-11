import secrets
import random
import datetime

def n_size_string(n):
    v = secrets.token_bytes(n).hex()
    mp = len(v) // 2
    return v[:mp]

def n_size_int(n):
    if n <= 0:
        return 0
    min_value = 10 ** (n - 1)  # Minimum value with n digits
    max_value = 10 ** n - 1  # Maximum value with n digits
    return random.randint(min_value, max_value)

def random_ts():
    start_date = datetime.datetime(2000,1,1)
    end_date = start_date.now()
    time_difference = end_date - start_date
    delta = datetime.timedelta(random.randint(0, int(time_difference.total_seconds())))
    random_time_stamp = start_date + delta
    return random_time_stamp