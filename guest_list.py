guest_list = []
done = False
i = 1

while done == False:
    guest = input("Guest (Type \"Done\" if done): ").strip().lower()
    if guest == "done":
        break
    elif guest in guest_list:
        pass
    else:
        guest_list.append(guest)


print("Guest List:")
for guests in guest_list:
    print(f"{i}. {guests.title()}")
    i += 1
