day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day = int(raw_input('Day (0-6)'))
if day == 0 or day == 6:
    print "Today is %s. Sleep in." % day_of_week[day]
else:
    print "Today is %s. Go to work." % day_of_week[day]
