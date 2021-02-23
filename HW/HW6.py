pupils = int(input("Сколько школьников?:"))
apple = int(input("Сколько яблок?:"))

ap_pupils = apple // pupils
ap_basket = apple % pupils

print("Школьники получат по {0} яблок. В корзине останется {1}".format(ap_pupils, ap_basket))