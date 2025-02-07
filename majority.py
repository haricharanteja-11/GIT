from collections import Counter
n = list(map(int,input("Enter: ").split()))
x = Counter(n)
for key,value in sorted(x.items(),key = lambda y:(y[1],-y[0]),reverse=True):
    print(key)
    break