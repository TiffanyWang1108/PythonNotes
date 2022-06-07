import datetime

now = datetime.datetime.now()
c_time = now.strftime("%Y%m%d_%H%M%S")

log_name = c_time + ".log"
with open(log_name, "w+", encoding="utf-8") as f:
    # datetime [level] line message
    message = f"{now} [info] line: 14 this is a log message"
    f.write(message)
