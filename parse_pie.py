def plot_pie(filename):
    from itertools import chain
    import numpy as np
    from collections import OrderedDict, defaultdict
    import csv
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from map_test import get_json	
    
    
    def flatten(listOfLists):
        "Flatten one level of nesting"
        return chain.from_iterable(listOfLists)

    category_map, categories = get_json()

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
    
    
    data = zip(finalmemo,finalprice)
    
    d = defaultdict(list) 

    for k, v in data:
        if k != '' and v != '':
            d[k].append(v)
    
    orderddata = OrderedDict(d)

    cats = ['Total','Other']	
    cats.extend(categories)
    category = OrderedDict.fromkeys(cats,0.0)

    for key, val in orderddata.iteritems():
        if val:
            category["Total"] += abs(sum(map(float,val)))
        for cat_key in category_map.keys():
            if cat_key in key[-4:]:
                category[category_map[cat_key]] += abs(sum(map(float,val)))

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

    patches, text = plt.pie(sizes, colors = cs, pctdistance=0.7 ,shadow=True, startangle=90)

    plt.legend(patches, legendent, fontsize=8,loc="upper left",bbox_to_anchor=(0.75,1))
    plt.axis('equal')
    plt.show()

if __name__ == "__main__": plot_pie(filename)
