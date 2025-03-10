D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

# Union 
D_UNION = {**D1, **D2}
print(f"D_UNION = {D_UNION}")

#insterectuon
for k in D1:
    if k in D2:
        print(f"intersection is at key: {k}, value in D1: {D1[k]}")

#difference
difference = {}
for k in D1:
    if k not in D2:
        difference[k] = D1[k]
print(f"D1- D2 = {difference}")



#merge
for key, value in D1.items():
    if key in D2:
        D_UNION[key] = D1[key] + D2[key]

print(f"D_MERGE = {D_UNION}")
