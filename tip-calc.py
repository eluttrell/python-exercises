billTot = raw_input("What was the bill total? ")
service = raw_input("How was the service? (good, fair, bad) ")
billTot = int(float(billTot))
service = service.lower()
if service == "good":
    tip = billTot * .2
    tip = "%.2f" % tip
    tip = str(tip)
    print "You should tip $" + tip
elif service == "fair":
    tip = billTot * .15
    tip = "%.2f" % tip
    tip = str(tip)
    print "You should tip $" + tip
else:
    tip = billTot * .1
    tip = "%.2f" % tip
    tip = str(tip)
    print "You should tip $" + tip
