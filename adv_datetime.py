import datetime

def get_datetime():
    now = datetime.datetime.now()
    print(now)

    dt = datetime.datetime(1999, 12, 31)
    print(dt)

    print("date:", dt.year, dt.month, dt.day)
    print("time:", dt.hour, dt.minute, dt.second, dt.microsecond)


    print("TODAY is?", now.weekday())

    print(now.date(), type(now.date()))
    print(now.time(), type(now.time()))


    nowdate = datetime.datetime.now().date()
    nowtime = datetime.datetime.now().time()

    print("date:", nowdate.year, nowdate.month, nowdate.day, nowdate.weekday())
    print("time:", nowtime.hour, nowtime.minute, nowtime.second, nowtime.microsecond)


def timedelta_ex():
    current = datetime.datetime.now()
    print("CURRENT:", current)
    past = datetime.datetime(1999, 12, 31)
    print("PAST:", past)
    print("CURRENT = PAST AFTER ?", current > past)

    # datetime - datetime : timedelta (gap)
    diff = current - past
    print(diff, type(diff))

    # timedelta
    print("timedelta:", diff.days, diff.seconds, diff.microseconds)
    print("total seconds:", diff.total_seconds())

    # datetime + timedelta : NEW datetime
    print("current:", current)
    diff = datetime.timedelta(100, 0, 0)
    print("100DAYS AFTER:", current + diff)


def format_date():
    """
        datetime -> str : .strftime()
        str -> datetime : .strptime()
    """
    current = datetime.datetime.now()
    print("current:", current)

    # datetime -> str : strftime()
    print(current.strftime("%Y-%m-%d %H:%M"))
    print(current.strftime("%YYEAR %mMONTH %dDAY %HHOUR %MMINUTE"))

    # str -> datetime : strptime()
    s = "2021-05-24 17:00:00"
    dt = datetime.datetime.strptime(s,
                                    "%Y-%m-%d %H:%M:%S")
    print(dt, type(dt))


if __name__ == "__main__":
    # get_datetime()
    # timedelta_ex()
    format_date()