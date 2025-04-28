def vacuum_cleaner():
    rooms = {'A': 'dirty', 'B': 'dirty'}
    current_position = 'A'

    while 'dirty' in rooms.values():
        if rooms[current_position] == 'dirty':
            rooms[current_position] = 'clean'
            print(f"Cleaned {current_position}")
        if current_position == 'A':
            current_position = 'B'
        else:
            current_position = 'A'

    print("All rooms are clean now!")

vacuum_cleaner()
