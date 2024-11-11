from itertools import permutations
""" 
  t w o 
  t w o
f o u r """


def is_valid(assignment):           #T W O F U R
    t=assignment['T']
    w=assignment['W']
    o=assignment['O']
    f=assignment['F']
    u=assignment['U']
    r=assignment['R']

    if len(set(assignment.values()))!=len(assignment):
        return False
    if f==0 or t==0:
        return False
    
    c10=(o+o)//10
    c100=(w+w+c10)//10
    c1000=(t+t+c100)//10

    if (o+o)%10 !=r:
        return False
    if (w+w+c10)%10!=u:
        return False
    if (t+t+c1000)%10!=o:
        return False
    
    return True

def local_search():
    letters=['T','W','O','F','U','R']
    permut=permutations(range(10),len(letters))
    
    for perm in permut:
        assignment={'T':perm[0],
        'W':perm[1],
        'O':perm[2],
        'F':perm[3],
        'U':perm[4],
        'R':perm[5]}

        if is_valid(assignment):
            print(assignment)
            return True
        
local_search()


    