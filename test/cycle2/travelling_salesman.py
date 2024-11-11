import random

def calculate_tour_distance(tour,distance_matrix):
    distance=0
    for i in range(len(tour)):
        distance+=distance_matrix[tour[i]][tour[(i+1)%len(tour)]]
    return distance


def swapped(tour):
    swapped=tour[:]
    
    i,j=random.sample(range(len(tour)),2)
    tour[i],tour[j]=tour[j],tour[i]
    return swapped

def travel(distance_matrix,iteration=1000):
    length=len(distance_matrix)
    current_tour=list(range(length))

    random.shuffle(current_tour)
    current_length=calculate_tour_distance(current_tour,distance_matrix)

    for i in range(iteration):
        swap=swapped(current_tour)

        new_tour_length=calculate_tour_distance(swap,distance_matrix)

        if new_tour_length<current_length:
            current_length=new_tour_length
            current_tour=swap
    return current_tour,current_length

distance_matrix=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print(f"optimal tour strategy:\n{travel(distance_matrix)}")