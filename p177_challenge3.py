
def same_class(o1, o2):
    print(o1 is o2)

x = 10
y = x
same_class(x, y)

y = "10"
same_class(x, y)
