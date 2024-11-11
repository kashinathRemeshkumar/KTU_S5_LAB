def assess(a, b, c, d, e, f, g, h, i, j, k):
    disease = []
    if a == 'y' and b == 'y' and c == 'y' and e == 'y' and f == 'y' and i == 'y':
        disease.append("common cold")
    if a == 'y' and b == 'y' and d == 'y' and g == 'y' and j == 'y' and h == 'y':
        disease.append('chicken pox')
    if d == 'y' and b == 'y' and g == 'y' and j == 'y' and k == 'y':
        disease.append('measles')
    if a == 'y' and d == 'y' and c == 'y' and e == 'y' and f == 'y' and k == 'y':
        disease.append("common cold")
    
    return disease

# Input from user
name = input("Enter your name: ")
a = input("Do you have fever (Y/N): ").lower()
b = input("Do you have headache (Y/N): ").lower()
c = input("Do you have runny nose (Y/N): ").lower()
d = input("Do you have vomiting (Y/N): ").lower()
e = input("Do you have sneezing (Y/N): ").lower()
f = input("Do you have cough (Y/N): ").lower()
g = input("Do you have seizure (Y/N): ").lower()
h = input("Do you have swollen glands (Y/N): ").lower()
i = input("Do you have sore throat (Y/N): ").lower()
j = input("Do you have rashes (Y/N): ").lower()
k = input("Do you have body pain (Y/N): ").lower()

# Diagnosis
diagnosis = assess(a, b, c, d, e, f, g, h, i, j, k)

# Output diagnosis results
if diagnosis:
    print("Possible diagnosis:")
    for condition in diagnosis:
        print(condition)
else:
    print("No diagnosis can be made.")
