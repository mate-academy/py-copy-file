import time
from datetime import datetime


def create_log_file() -> str:
    current_time = datetime.now()
    filename = f"app-{current_time.hour:02d}_{current_time.minute:02d}" \
               f"_{current_time.second:02d}.log"
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    with open(filename, "w") as file:
        file.write(timestamp)

    print(f"Created file: {filename}")
    print(f"Timestamp: {timestamp}\n")


while True:
    create_log_file()
    time.sleep(1)
