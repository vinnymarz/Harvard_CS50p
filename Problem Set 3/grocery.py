grocery_list ={}

while True:
    try:
        item = input().strip().upper()
        if item not in grocery_list.keys():
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
    except KeyError:
        continue
    except EOFError:
        break
    
for item, count in sorted(grocery_list.items()):
    print(f"{count} {item}")
