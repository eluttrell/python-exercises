import datetime


def when_100():
    name = raw_input("Name? ").capitalize()
    age = int(raw_input("Age? "))
    date = datetime.datetime.now()
    year = date.year
    if age > 100:
        at100 = year + (100 - age)
        print "Looks like you turned 100 in %d %s. You are really old. Sorry." % (at100, name)
    elif age < 100:
        at100 = year + (100 - age)
        print "%s, you will turn 100 years old in %d." % (name, at100)
    else:
        pass

when_100()
