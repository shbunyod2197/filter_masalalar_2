# 1
roy = ["apple", "banana", "kiwi", "strawberry"]
print(roy)

a = list(filter(lambda c: len(c) > 5, roy))
print(a)

# 2
roy = ["apple", "pear", "grape", "plum"]
print(roy)

a = list(filter(lambda el:'a' in el, roy))
print(a)

# 3
roy = ["Ali", "vali", "Sardor", "john"]
print(roy)

b = list(filter(lambda a: a[0] == a.isupper(), roy))
print(b)

# 4
roy = ["123", "abc", "456", "78a"]
print(roy)

a = list(filter(lambda el: el.isdigit(), roy))
print(a)

# 5
roy = ["", "hello", "", "world"]
print(roy)

a = list(filter(lambda el: el != "", roy))
print(a)

# 6
roy = ["hi", "hello", "world", "python"]
print(roy)

a = list(filter(lambda el: len(el) % 2 == 0, roy))
print(a)

# 7
roy = ["java", "python", "javascript", "c++"]
print(roy)

a = list(filter(lambda el: len(el) > 6, roy))
print(a)

# 8
roy = ["python", "java", "kotlin", "go"]
print(roy)

a = list(filter(lambda c: c[-1] == 'n', roy))
print(a)

# 9
roy = ["abc1", "hello", "test2", "world"]
print(roy)

a = list(filter(lambda c: c.isalnum(), roy))
print(a)

# 10
roy = ["abc1", "hello", "test2", "world"]
print(roy)

a = list(filter(lambda c: c.isalpha(), roy))
print(a)

# 11
roy = [None, 1, 2, None, 3, 4]
print(roy)

a = list(filter(lambda c: c != None, roy))
print(a)

# 12
roy = [True, False, True, False]
print(roy)

a = list(filter(lambda c: c == True, roy))
print(a)

# 13
roy = [0, 1, False, 2, "", 3]
print(roy)

a = list(filter(lambda el: el, roy))
print(a)

# 14
roy = [1, 2.5, 3, "4", 5]
print(roy)

a = list(filter(lambda el: el == int(el), roy))
print(a)

# 15
roy = [1, 2.5, 3, "4", 5]
print(roy)

a = list(filter(lambda el: el == float(el), roy))
print(a)
