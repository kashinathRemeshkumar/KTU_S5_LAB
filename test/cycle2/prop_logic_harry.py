from sympy import And,Or,Not,Implies,satisfiable,symbols

rain=symbols("it_is_raining")
hagrid=symbols("harry_visits_hagrid")
dumbeldore=symbols("harry_visits_dumbeldore")

kb=And(
    Implies(Not(rain),hagrid),
    Not(And(hagrid,dumbeldore)),
    Or(hagrid,dumbeldore),
    dumbeldore
)

print(kb,"\n")

print(satisfiable(kb))

print("did harry visit hagrid",satisfiable(kb.subs({hagrid:True})))
print("is it raining ",satisfiable(kb.subs({rain:True})))