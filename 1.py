def min_price(priceA, priceB):
    sortedA = sorted(priceA)
    sortedB = sorted(priceB)
    i = 0
    j = 0
    min1 = float('inf')
    while i < len(sortedA) and j < len(sortedB):
        current_diff = abs(sortedA[i] - sortedB[j])
        min1 = min(min1, current_diff)
        if sortedA[i] < sortedB[j]:
            i += 1
        else:
            j += 1
    return min1
#测试例子
priceA = [1,3,15,11,2]
priceB = [23,127,235,19,8]
result = min_price(priceA, priceB)
print(result)
priceA1 = [99,150,200]
priceB1 = [210,145,95]
result = min_price(priceA1, priceB1)
print(result)

#时间复杂度为O（nlogn+mlogm）取决于A和B数组的长度，长度不同时间复杂度也对随之不同