class fuck:
    def __init__(self, x) -> None:
        self.x = x
        self.penis = []


class shit(fuck):
    def __init__(self, x) -> None:
        super().__init__(x)


x = fuck(3)
print(x.x)
print(x.penis)

y = shit(3)
print(y.x)
print(y.penis)