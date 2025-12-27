class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks= marks
    
    def avg(self):
        sum =0
        for i in self.marks:
            sum+=i
        print("hii",self.name,"your score is:",sum/len(self.marks))
s1=Student("Rahul",[98,94,84])
s2 = Student("Bhanu",[85,85,86,99])
s2.avg()
s1.avg()