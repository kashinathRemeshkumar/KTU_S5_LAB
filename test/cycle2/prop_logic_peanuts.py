from sympy import symbols,And,Or,Not,Implies,satisfiable

john_likes_peanuts=symbols("john_likes_peanuts")
anil_eats_peanuts=symbols("anil_eats_peanuts")
harry_eats_peanuts=symbols("harry_eats_peanuts")
peanuts=symbols("peanuts")
alive=symbols("alive")
food=symbols("food")
apple=symbols("apple")
vegitable=symbols("vegitable")


# If it's food, then John likes it
# Peanuts, apple, and vegetable are food
# If Anil eats peanuts and is alive, then it's food
# Anil eats peanuts and is alive
# Harry eats peanuts if Anil eats peanuts

kb=And(
    Implies(food,john_likes_peanuts),
    Or(peanuts,apple,vegitable),
    Implies(And(anil_eats_peanuts,alive),food),
    And(anil_eats_peanuts,alive),
    Implies(anil_eats_peanuts,harry_eats_peanuts)

)
print(f"does john like peanuts {satisfiable(kb.subs({peanuts:True}))[john_likes_peanuts]}")