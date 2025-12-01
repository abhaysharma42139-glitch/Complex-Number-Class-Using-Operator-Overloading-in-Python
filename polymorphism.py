# OPERATOR OVERLOADING
# same operator but multiple function 
'''print(11+2)#add
print("Abhay"+"Sharma")#concatenate
print([1,2,3]+[4,5,6])#merge'''

# creating class for complex number
# using operator overloading and polymorphism
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def Getnum(self):
        print(self.real,"i +",self.img,"j")
    '''def add(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal, newimg)'''
# creating dunder function for addition
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal, newimg)
# creating ddunder function for subtraction
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal, newimg)
num1=Complex(4, 5)
num1.Getnum()
num2=Complex(7, 9)
num2.Getnum()
# to get this sum we have to create a function but if we do not want to create any function instead just directly write num1+ num2, then we can use dunder function
'''num3=num1.add(num2)
num3.Getnum()'''
# instead of now calling function and writing num1.add(num2), we have created dunder function , we could directly write as written below

num3=num1+num2
num3.Getnum()
num4=num1-num2
num4.Getnum()