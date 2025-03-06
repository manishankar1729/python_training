input_str = "Hello world and Hello Earth"
words = input_str.split()
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1

for k,v in dict.items():
    print(f"frequeny of {k} is {v}")