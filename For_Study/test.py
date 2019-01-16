name="xxxx"

class t:
    ko = "x123"
    print('全局')
    def __init__(self):
        self.ko


    def p(self):
        print(self.ko)

r=t()
r.p()
r.p()
r.p()