import datetime
dateTimeTpyes = ["date"
                 "time",
                 "datetime",
                 "timedelta",
                 "timezone"]

def showDatetimeUsage():
    checkDate = datetime.date(1997, 8, 31)
    print(f"{checkDate.month}/{checkDate.day}/{checkDate.year}")
    print(datetime.date.today())
    exampleTime = datetime.time(5, 3, 23, 0)
    print(exampleTime.hour)
    print(exampleTime.minute)
    print(exampleTime.second)
    print(exampleTime.microsecond)
    print(datetime.time.min)
    print(datetime.time.max)
    exampleDateTime = datetime.datetime(1997, 8, 31, 5, 3, 23, 0)
    print(f"{exampleDateTime.month}/{exampleDateTime.day}/{exampleDateTime.year} at {exampleDateTime.hour}:{exampleDateTime.minute}:{exampleDateTime.second}")
    print(datetime.datetime.today())
    print(datetime.datetime.now())
    print(datetime.datetime.combine(checkDate, exampleTime))
    print(datetime.datetime.min)
    print(datetime.datetime.max)
    print(datetime.datetime.resolution)
    #Abstract class tzinfo also exists
    exampleTimeDelta = datetime.timedelta(days = 1, seconds = 30, microseconds = 50,
                                          milliseconds = 20, minutes = 5, hours = 1,
                                          weeks = 1
                                          )
    print(exampleTimeDelta)
    print(datetime.timedelta.min)
    print(datetime.timedelta.max)
    print(datetime.timedelta.resolution)
    exampleTimeDelta = datetime.timedelta(hours = 5)
    exampleTimeZone = datetime.timezone(exampleTimeDelta)
    print(datetime.timezone.min)
    print(datetime.timezone.max)
    print(exampleTimeZone.utcoffset(None))
    print(exampleTimeZone.tzname(None))
showDatetimeUsage()
