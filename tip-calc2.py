billTot = int(raw_input("What was the bill total? "))
service = raw_input("How was the service? (good, fair, bad) ").lower()
guests = int(raw_input("How many people in your party?"))
if guests > 1:
    if service == "good":
        tip = billTot * .2
        total = billTot * 1.2
        indTot = total / guests
        tip = "%.2f" % tip
        total = "%.2f" % total
        indTot = "%.2f" % indTot
        print "You should tip: $" + tip
        print "Your total is: $" + total
        print "Each member of your party's share of the bill is: $" + indTot
    elif service == "fair":
        tip = billTot * .15
        indTot = total / guests
        tip = "%.2f" % tip
        total = "%.2f" % total
        indTot = "%.2f" % indTot
        print "You should tip $" + tip
        print "Your total is: $" + total
        print "Each member of your party's share of the bill is: $" + indTot
    else:
        tip = billTot * .1
        indTot = total / guests
        tip = "%.2f" % tip
        total = "%.2f" % total
        indTot = "%.2f" % indTot
        print "You should tip $" + tip
        print "Your total is: $" + total
        print "Each member of your party's share of the bill is: $" + indTot
else:
    if service == "good":
        tip = billTot * .2
        total = billTot * 1.2
        tip = "%.2f" % tip
        total = "%.2f" % total
        print "You should tip: $" + tip
        print "Your total is: $" + total
    elif service == "fair":
        tip = billTot * .15
        total = billTot * 1.15
        tip = "%.2f" % tip
        total = "%.2f" % total
        print "You should tip: $" + tip
        print "Your total is: $" + total
    else:
        tip = billTot * .1
        total = billTot * 1.1
        tip = "%.2f" % tip
        total = "%.2f" % total
        print "You should tip: $" + tip
        print "Your total is: $" + total
