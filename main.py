str1=input("Введите первую строку")
str2=input("Введите вторую строку")

sort_str1=sorted(str1.lower())
sort_str2=sorted(str2.lower())

if sort_str1==sort_str2:
    print("Строки анограммы")
else:
    print("Строки не анограммы")