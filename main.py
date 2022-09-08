a=5
b=6
print(f"the sum is {a/b}")

a="sandip"
print(a[0:5])

# s=input("enter your name")
# d=input("enter your last name")
#num1=int(s)
#num2=int(d)
#sum=num1+num2
# print("your firstname is ",s + "your lastname is",d +"sum is ", sum)

mark=[20,30,40,10]
print(mark)

mark.sort()
print(mark)

mark.insert(1,10)
print(mark)

ht={
    "name":"kbc",
    "age":25,
    "contact":9853535,
}
print(ht.get("name"))
print(ht.get("contact"))
print(ht.pop("name"))
print(ht)


a=input("enter a number");
b=input("enter another number")
if(a>b):
    print(a,"is greater")