
txt = "my captain assignment."
#capitalize
x = txt.capitalize()
print (x)

#replace
x = txt.replace("captain", "python")
print(x)

#casefold
x = txt.casefold()
print(x)



txt = "banana"
#ljust
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#center
x = txt.center(30)
print(x)

#lstrip
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#maketrans
mytable = txt.maketrans("b", "t")
print(txt.translate(mytable))

#isidentifier
x = txt.isidentifier()
print(x)

#islower
x = txt.islower()
print(x)

#rjust
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#rstrip
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#strip
x = txt.strip()
print("of all fruits", x, "is my favorite")



txt = "my captain assignment."
#count
x = txt.count("captain")
print(x)

#endswith
x = txt.endswith(".")
print(x)

#find
x = txt.find("captain")
print(x)

#rpartition
x = txt.rpartition("captain")
print(x)

#rsplit
x = txt.rsplit(", ")
print(x)

#upper
x = txt.upper()
print(x)


txt = "Hello, welcome to my world."
#index
x = txt.index("welcome")
print(x)

#isupper
x = txt.isupper()
print(x)

#lower
x = txt.lower()
print(x)

#partition
x = txt.partition("welcome")
print(x)

#rfind
x = txt.rfind("to")
print(x)

#rindex
x = txt.rindex("my")
print(x)

#istitle
x = txt.istitle()
print(x)

#isprintable
x = txt.isprintable()
print(x)

#isalnum
x = txt.isalnum()
print(x)

#isalpha
x = txt.isalpha()
print(x)

#split
x = txt.split()
print(x)

#title
x = txt.title()
print(x)


#isdecimal
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)


#isdigit
txt = "52100"
x = txt.isdigit()
print(x)

#isnumeric
x = txt.isnumeric()
print(x)

#zfill
x = txt.zfill(7)
print(x)




#isspace
txt = "   "
x = txt.isspace()
print(x)


myTuple = ("Dhivya", "Aishu", "Anjana")
#join
x = "#".join(myTuple)
print(x)


txt = "My name is Dhivya\nWelcome to my captain"
#splitlines
x = txt.splitlines()
print(x)

#startswith
x = txt.startswith("My")
print(x)

#swapcase
x = txt.swapcase()
print(x)


mydict = {83:  80}
txt = "Hello sam!"
#translate
print(txt.translate(mydict))


txt = "My name is Ståle"
#encode
x = txt.encode()
print(x)


#expandtabs
txt = "H\ta\tp\tp\ty"
x =  txt.expandtabs(2)
print(x)

#format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


