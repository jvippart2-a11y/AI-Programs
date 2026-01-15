rooms = {
    "Kitchen": [1, 0, 1, 0],
    "Hall": [0, 1, 1, 0],
    "Bedroom": [0, 0, 0, 0],
    "Store Room": [0, 0, 0, 0]
}

performance = 0
total_cells = 0

for room in rooms.values():
    total_cells += len(room)

positions = {
    0: "LEFT",
    1: "CENTER-LEFT",
    2: "CENTER-RIGHT",
    3: "RIGHT"
}


def vacuum_agent(room_name, room):
    global performance
    print(f"\nEntering {room_name}")

    for i in range(len(room)):
        print(f"Moving to {positions[i]} position")

        if room[i] == 1:
            print("Dirt found -> SUCK")
            room[i] = 0
            performance += 1
        else:
            print("Already clean -> MOVE")


def room_status(room):
    clean = room.count(0)
    dirty = room.count(1)

    neat_percent = (clean / len(room)) * 100
    dirty_percent = (dirty / len(room)) * 100

    return neat_percent, dirty_percent


print("INITIAL STATUS\n")

for name, room in rooms.items():
    neat, dirty = room_status(room)
    print(f"{name} {room} | Neat: {neat:.0f}% | To clean: {dirty:.0f}%")


for name, room in rooms.items():
    vacuum_agent(name, room)


print("\nFINAL STATUS\n")

for name, room in rooms.items():
    neat, dirty = room_status(room)
    print(f"{name} {room} | Neat: {neat:.0f}% | To clean: {dirty:.0f}%")


performance_percent = (performance / total_cells) * 100
print(f"\nOverall performance: {performance_percent:.2f}%")
