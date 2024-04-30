#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
    language that combines remarkable power with very clear syntax"
print(str[str.find("object"):str.find("object")+14] + str[str.find("Python"):str.find("Python")+6] + str[str.find("with"):])