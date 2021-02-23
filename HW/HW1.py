print("Hello, world!")
print(40+50*20)
print("Total", 1040)
print(4+1 < 20-3)
print("90 is more than 5?", 90 >= 5)

# Don't use F*** in comments :)
Ilon_money = 100000000000 # $
My_money = 20 # hrn
Vova_money = 100000000000000000000000000
Hillel = "My money after hillel = {} $ Hooray!!!"
print(Hillel.format(Ilon_money*My_money*Vova_money))
print(f"But more is possible: {Vova_money ** 2} $")
print("-"*100)
# What about you?!
print("Last name:", end=' ')
lastname = input()
print("Your city:", end=' ')
city = input()
print("Passport number:", end=' ')
passnum = input()
print("Bank card numder:", end=' ')
bcn = input()
print(f"Your personal data:\n{lastname}\n{city}\n{passnum}\n{bcn}")