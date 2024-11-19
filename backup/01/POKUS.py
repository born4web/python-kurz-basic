ingredience = ["vejce", "mléko", "máslo"]
potrebne = ["vejce", "mléko", "mouka", "cukr", "máslo"]
for prisada in potrebne:
    if prisada in ingredience:
        print(f"Mam {prisada}")
    else:
        print(f"Chybi {prisada}")