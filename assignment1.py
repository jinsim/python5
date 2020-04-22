class FourCal:
    def __init__(self, name, age, school):
        self.name = name 
        self.age = age 
        self.school = school
        self.add_num = 0
        self.sub_num = 0
        self.mul_num = 0
        self.div_num = 0
    def add(self, n1, n2):
        self.add_num += 1
        return(n1+n2)
    def sub(self, n1, n2):
        self.sub_num += 1
        return(n1-n2)
    def mul(self, n1, n2):
        self.mul_num += 1
        return(n1*n2)
    def div(self, n1, n2):
        self.div_num += 1
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
            return none
        return(n1/n2)
    def ShowCount(self):
        return(self.add_num, self.sub_num, self.mul_num, self.div_num)
my = FourCal("김범진", 22, "고려대학교")
print(my.add(2,4))
print(my.add(2,4))
print(my.mul(2,4))
print(my.div(2,4))
add, sub, mul, div = my.ShowCount()
print("덧셈: %d" % (add))
print("뺄셈: %d" % (sub))
print("곱셈: %d" % (mul))
print("나눗셈: %d" % (div))
