# if else

age = input("enter your age: ")

if int(age) >= 18:
    print("you are and adult")
    print("and you can vote")
elif 18 > int(age) > 3: # haha, python me likh ske hain aise
    print("school ke bacche")
else:
    print("kids")
