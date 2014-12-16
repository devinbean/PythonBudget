def plot_pie(filename):
    
    from itertools import chain
    from collections import OrderedDict
    import csv
    import re
    import matplotlib.pyplot as plt

    def flatten(listOfLists):
        "Flatten one level of nesting"
        return chain.from_iterable(listOfLists)


    memo = []
    price = []
    finalmemo = []
    finalprice = []
    fastfood_price = []
    bar_and_restaurant = []
    gas = []
    transport = []
    groceries = []
    entertainment = []
    total = []

    with open(filename,'rU') as budget:
        reader = csv.reader(budget)
        for rows in reader:
            
            memo.append(rows[3:4])
            price.append(rows[4:5])

    flatmemo = flatten(memo)
    flatprice = flatten(price)

    for rows in flatmemo:
        finalmemo.append(rows)

    for rows in flatprice:
        finalprice.append(rows)

    del finalmemo[0]
    del finalprice[0]

    data = dict(zip(finalmemo,finalprice))
    orderddata = OrderedDict(data)


    for key, value in orderddata.iteritems():
        if value:
            total.append(float(value))
        if '5814' in key:
            fastfood_price.append(float(value))
        if any(s in key for s in ['5812','5813','7999']):
            bar_and_restaurant.append(float(value))
        if '5542' in key:
            gas.append(float(value))
        if any(s in key for s in ['4112','4789','4121','4111','4131']):
            transport.append(float(value))
        if any(s in key for s in ['5499']):
            groceries.append(float(value))
        if any(s in key for s in ['7922','5735','7832','5968']):
            entertainment.append(float(value))




    total = abs(sum(total))
    entertainment = abs(sum(entertainment))
    groceries = abs(sum(groceries))
    transport = abs(sum(transport))
    gas = abs(sum(gas))
    fastfood_price = abs(sum(fastfood_price))
    bar_and_restaurant = abs(sum(bar_and_restaurant))
    other = total - (bar_and_restaurant + fastfood_price + gas + transport + groceries + entertainment)

#    print 'Total: %0.2f' % total
#    print 'Other: %0.2f' % other
#    print 'Gas: %0.2f' % gas
#    print 'Fast Food: %0.2f' % fastfood_price
#    print 'Bar and Resaurant: %0.2f' % bar_and_restaurant

    labels = ['Other', 'Fast Food', 'Bar and Restaurant','Gas', 'Transport', 'Groceries', 'Entertainment']
    sizes = [other, fastfood_price, bar_and_restaurant, gas, transport, groceries,entertainment]

    for idx, expense in enumerate(sizes):
        if expense == 0:
            del sizes[idx]
            del labels[idx]


    plt.pie(sizes, labels=labels, autopct='%1.f%%', pctdistance=0.7 ,shadow=True, startangle=90)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()

if __name__ == "__main__": plot_pie(filename)













