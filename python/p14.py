#list methods

lst = [56,78,45,34,32,34,45,665,4453,55]
print(lst)

lst.append(700)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

print(lst.index(45))
print(lst.count(45))

m = lst.copy()
print(m)

lst.insert(5, 250)
print(lst)

m = [900,1000,1200]
lst.extend(m)
print(lst)

k=lst+m
print(k)
print(lst)