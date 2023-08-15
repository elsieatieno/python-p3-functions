#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()


def greet(name):
    print("Hello, " + name + "!")

greet("Guido")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

greet_with_default()
greet_with_default("Yukio")

def add(num1, num2):
    return num1 + num2

add(45,55)

def halve(number):
    return number / 2 

halve(4)


# def greet(name):
#     print("Hello, {}!".format(name))

# def greet_with_default(name="programmer"):
#     print("Hello, {}!".format(name))
