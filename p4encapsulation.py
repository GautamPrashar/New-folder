class Students:
    def __init__(self, name, rollno, subject):
        self.name=name
        self.rollno=rollno
        self.subject=subject
    def demofunc(self):    
        print("My name is "+self.name)
        print("My rollno is ",+self.rollno)
        print("My subject is"+self.subject)
st1=Students("Ram",20,"Commerce")
st2=Students("Sam",25,"Arts")
st3=Students("Fam",15,"Science")
st1.demofunc()
st2.demofunc()
st3.demofunc()