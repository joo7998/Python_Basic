import datetime             # module import

def get_datetime():
    now = datetime.datetime.now()
    print(now)

    # customized datetime
    dt = datetime.datetime(2000,01,01)
    print(dt)


    print(dt.year, dt.month, dt.day)
    print(dt.hour, dt.minute, dt.second, dt.microsecond)

    # weekday  mon=0, sun=6
    print(now.weekday())

    # datetime = date + time
    print(dt.date(), type(dt.date()))
    print(now.time(), type(now.time()))


    nowdate = datetime.datetime.now().date()
    nowtime = datetime.datetime.now().time()

    print(nowdate.year, nowdate.month, nowdate.day, nowdate.weekday())
    print(nowtime.hour, nowtime.minute, nowtime.second, nowtime.microsecond)


def timedelta_ex():
    current = datetime.datetime.now()
    print(current)
    past = datetime.datetime(2011, 1, 1)
    print(past)

    # compare
    print(current > past)

    # datetime - datetime : timedelta
    diff = current - past
    print(diff)

    # timedelta
    print(diff.days, diff.seconds, diff.microseconds)
    print(diff.total_seconds())    # result in seconds

    # datetime + timedelta = new datetime
    print(current)
    diff = datetime.timedelta(100, 0, 0)
    print(current + diff)

def format_date():
    # datetime -> str : strftime()
    # str -> datetime : strptime()

    current = datetime.datetime.now()
    print(current)

    # datetime -> str : strftime()
    print(current.strftime("%Y-%m-%d %H-%M"))
    print(current.strftime("%Y YEAR %m MONTH %d DAY %H HOUR %M MINUTE"))

    # str -> datetime : strptime()
    s = "2021-05-24 17:11:11"
    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    print(dt, type(dt))



if __name__ =="__main__":
    # get_datetime()
    # timedelta_ex()
    format_date()