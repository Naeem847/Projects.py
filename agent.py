state = {'A': 'Dirty', 'B': 'Dirty', 'Vacuum': 'A'}
print("Initial State:", state)
cost = 0
while True:
    location = state['Vacuum']
    if state[location] == 'Dirty':
        # Clean the current room
        print(f"Cleaning {location}")
        state[location] = 'Clean'
        cost += 1
    else:
        # Move to the other room
        if location == 'A':
            print("Moving to B")
            state['Vacuum'] = 'B'
            cost += 1
        else:
            print("Moving to A")
            state['Vacuum'] = 'A'
            print("Cleaning B")
            state['B'] = 'Clean'
            cost += 1    
    # Check if all rooms are clean
    if state['A'] == 'Clean' and state['B'] == 'Clean':
        print("All rooms are clean!!")
        print("Final State:", state)
        print("Performance Measure (Cost):", cost)
        break