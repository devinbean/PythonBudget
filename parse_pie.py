filename = 'export.csv'

def plot_pie(filename):
    
    from itertools import chain
    from collections import OrderedDict
    import csv
    import matplotlib.pyplot as plt

    def flatten(listOfLists):
        "Flatten one level of nesting"
        return chain.from_iterable(listOfLists)

    memo = []
    price = []
    finalmemo = []
    finalprice = []

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

    category = OrderedDict.fromkeys(["Total", "Other", "Gas", "Fast Food", "Bar and Restaurant","Transportation","Groceries","Entertainment"],0.0)

    category_map = {"5814": "Fast Food", "5812":"Bar and Restaurant","5813": "Bar and Restaurant","7999": "Bar and Restaurant", "5542":"Gas", "4112": "Transportation", "4789": "Transportation", "4121": "Transportation", "4111": "Transportation", "4131": "Transportation","5499":"Groceries","7922":"Entertainment",
"5735": "Entertainment","7832": "Entertainment","5968": "Entertainment"}


    for key, val in orderddata.iteritems():
        if val:
            category["Total"] += abs(float(val))
        for cat_key in category_map.keys():
            if cat_key in key:
                category[category_map[cat_key]] += abs(float(val))

    category["Other"] = category["Total"] - sum([category["Gas"], category["Fast Food"], category["Bar and Restaurant"], category["Transportation"], category["Entertainment"]])

    category.pop("Total")

    for key, val in category.items():
        if val == 0:
            category.pop(key)

    sizes = category.values()
    labels = category.keys()

#
#    plt.pie(sizes, labels=labels, autopct='%1.f%%', pctdistance=0.7 ,shadow=True, startangle=90)
#
#    plt.axis('equal')
#
#    plt.show()

if __name__ == "__main__": plot_pie(filename)












