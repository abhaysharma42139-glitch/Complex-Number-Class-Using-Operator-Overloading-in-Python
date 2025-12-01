🔢 Complex Number Class Using Operator Overloading in Python

This Python program demonstrates how to implement a Complex Number class using Object-Oriented Programming (OOP) and dunder (magic) methods for operator overloading.
It allows you to perform addition and subtraction on complex numbers using the + and - operators just like built-in types.

✨ Features

Create a complex number using:

Real part

Imaginary part

Display the number in a i + b j format

Add two complex numbers using the + operator
→ internally uses __add__()

Subtract two complex numbers using the - operator
→ internally uses __sub__()

Demonstrates OOP concepts:

Classes & objects

Custom methods

Operator overloading

Dunder methods

🧠 How It Works
1. Constructor (__init__)

Initializes the real and imaginary values for each complex number.

2. Display Method (Getnum)

Prints the complex number in a readable format:

a i + b j

3. Operator Overloading
Addition (__add__)

Enables:

num3 = num1 + num2


It adds the real parts and imaginary parts separately.

Subtraction (__sub__)

Enables:

num4 = num1 - num2


It subtracts real and imaginary parts separately.

🧪 Example Demonstration
num1 = Complex(4, 5)
num2 = Complex(7, 9)

num3 = num1 + num2   # Uses __add__()
num4 = num1 - num2   # Uses __sub__()

num3.Getnum()
num4.Getnum()

Sample Output
4 i + 5 j
7 i + 9 j
11 i + 14 j
-3 i + -4 j

✔️ Use Case

Perfect for beginners learning:

Python OOP

Magic methods

Operator overloading

Class design principles
