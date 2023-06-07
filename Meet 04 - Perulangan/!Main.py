""" 
print("===== For Loop =====")

# Maks
for i in range (11):
    print(i)

# Min, Max
for i in range (1, 11):
    print(i) 
    
# Min, Max, Step (2)
for i in range (1, 11, 2):
    print(f"i = {i}")    

print("===== While Loop =====")

i = 0

while i <= 10:
    print(i)
    i += 1
    
print("===== Break Loop =====")

for i in range (1, 11):
    if i == 5:
        print("STOP")
        break
    print(i)
    
print("===== Continue Loop =====")

for i in range (1, 11):
    if i == 5:
        print("SKIP")
        continue
    print(i) """