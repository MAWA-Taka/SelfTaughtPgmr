class Apple:
    def __init__(self, k, s, w, c):
        self.kind = k
        self. size = s
        self.weight = w
        self.color =c
a = Apple("ふじ", "L", 200, "yellow")
print("品種：{}、サイズ：{}、重さ：{}、色合い：{}".format(a.kind, a.size, a.weight, a.color))
