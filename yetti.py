# data = list(filter(lambda x: x.isalpha(), "malina 250-maktab"))
# data = list(filter(lambda x: x%2==0, [45, 23, 12, 32, 11, 30]))
# data = list(filter(lambda x: x, [45, 23, 1, 0, 5, 6]))
# data = list(filter(lambda x: x>=18, [12, 16, 19, 21, 13, 29]))
# print(data)


data = list(map(lambda x: abs(x), [2,1,4,-5,3,-10]))
# data = list(map(lambda x: int(x), input().split()))
data = list(map(lambda x: x*2, [12, 3, 10, 5, 6]))
data = list(map(lambda x: x*0.9, [100_000, 150_000, 99_000]))
data = list(map(lambda x: x%2==0, [23, 12, 10, 15]))
print(data)