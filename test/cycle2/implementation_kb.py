import pytholog as pl


kb=pl.KnowledgeBase("flavour")

kb([
    'likes(hari,ladoo)',
    'likes(john,pizza)',
    'likes(vickey,cheese)',
    'likes(sam,ice cream)',

    'flavour(ladoo,sweet)',
    'flavour(pizza,savoury)',
    'flavour(cheese,savoury)',
    'flavour(ice cream,sweet)',

    'food_flavour(X,Y):-flavour(X,Y)',
    'food_to_like(X,Y):-likes(X,Z),flavour(Z,L),food_flavour(Y,L),neq(Y,Z)'
])

print(kb.query(pl.Expr("likes(hari,ladoo)")))  # Check if Noor likes sausage
print(kb.query(pl.Expr("likes(sam,ice cream)")))    # Check if Noor likes pasta

print(kb.query(pl.Expr("food_flavour(What,sweet)")))
# Find a dish Noor might like based on her preferences
print(kb.query(pl.Expr("food_to_like(hari, What)")))  # Dishes Noor might like

# Find what food items have a savory flavor
print(kb.query(pl.Expr("food_flavour(What,savoury)")))