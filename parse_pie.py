
def plot_pie(filename):
  
    from itertools import chain
    import numpy as np
    from collections import OrderedDict
    import csv
    import matplotlib.pyplot as plt
    from matplotlib import cm

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

    category = OrderedDict.fromkeys(["Total", "Other", "Cash","Gas","Fast Food","Tobacco","Alcohol","Groceries", "Bar and Restaurant","Entertainment","Transportation","Medical","Amazon","Rent"],0.0)

    category_map = {"5814": "Fast Food", "5812":"Bar and Restaurant","5813": "Bar and Restaurant","7999": "Bar and Restaurant", "5542":"Gas", "4112": "Transportation", "4789": "Transportation", "4121": "Transportation","4789": "Transportation", "4111": "Transportation", "4131": "Transportation","5499":"Groceries","5411":"Groceries","7922":"Entertainment",
"5735": "Entertainment","7832": "Entertainment","5968": "Entertainment","5921": "Alcohol","5993":"Tobacco","ATM":"Cash","8021":"Medical","5942":"Amazon","7299":"Rent"}


    for key, val in orderddata.iteritems():
        if val:
            category["Total"] += abs(float(val))
        for cat_key in category_map.keys():
            if cat_key in key:
                if any(char.isdigit() for char in val):
                    category[category_map[cat_key]] += abs(float(val))

    category["Other"] = category["Total"] - sum(category.values()[2:])

    category.pop("Total")

    for key, val in category.items():
        if val == 0:
            category.pop(key)

    sizes = category.values()
    labels = category.keys()

    N = int(len(sizes))

    cs = cm.Set1(np.arange(N)/float(N))

    percent = [str(round(100.*x/sum(sizes),1)) for x in sizes]


    legendent = [j + " " + percent[i] + "%" for i,j in enumerate(labels)]

    print legendent

    patches, text = plt.pie(sizes, colors = cs, pctdistance=0.7 ,shadow=True, startangle=90)

    plt.legend(patches, legendent, fontsize=8)

    plt.axis('equal')




    plt.show()

if __name__ == "__main__": plot_pie(filename)












