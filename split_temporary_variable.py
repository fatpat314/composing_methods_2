# by Kami Bigdely
# Split temporary variable

patty = 70 # [gr]
pickle = 20 # [gr]
tomatoes = 25 # [gr]
lettuce = 15 # [gr]
buns = 95 # [gr]

sandwich_patty = 2 * patty
sandwich_pickles = 4 * pickle
sandwich_tomatos = 3 * tomatoes
sandwich_lettuce = 2 * lettuce
sandwich_buns = 2 * buns


NY_Burger_Weight = (sandwich_patty + sandwich_pickles + sandwich_tomatos \
            + sandwich_lettuce + sandwich_buns)
print("NY Burger Weight", NY_Burger_Weight)
kimchi = 30 # [gr]
mayo = 5 # [gr]
golden_fried_onion = 20 # [gr]




Seoul_Kimchi_Burger_Weight = (sandwich_patty + sandwich_pickles + sandwich_tomatos 
                + kimchi + mayo + golden_fried_onion + sandwich_buns)
print("Seoul Kimchi Burger Weight", Seoul_Kimchi_Burger_Weight)
