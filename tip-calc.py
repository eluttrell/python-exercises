billTot = int(float(raw_input("What was the bill total? ")))
service = raw_input("How was the service? (good, fair, bad) ")
service = service.lower()
if service == "good":
    tip = billTot * .2
    total = billTot * 1.2
    tip = "%.2f" % tip
    total = "%.2f" % total
    print "You should tip $%s, and your total is $%s." % (tip, total)

elif service == "fair":
    tip = billTot * .15
    total = billTot * 1.15
    tip = "%.2f" % tip
    total = "%.2f" % total
    print "You should tip $%s, and your total is $%s." % (tip, total)
else:
    tip = billTot * .1
    total = billTot * 1.1
    tip = "%.2f" % tip
    total = "%.2f" % total
    print "You should tip $%s, and your total is $%s." % (tip, total)
