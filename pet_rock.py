# Simple pet rock simulator
name = input("What is your pet rock's name? ")

# Initial stats
happiness = 5
hunger = 5
age = 0

# Game loop
while True:

    # Display current stats
    print(f"\n{name}'s current happiness: {happiness}, hunger: {hunger}, age: {age}")
    command = input(f"What do you want {name} to do? (type 'exit' to quit) \n Play \n Feed \n Sleep \n") 

    # Handle commands
    if command.lower() == 'exit':
        print("Thanks for playing!")
        break

    elif command.lower() == 'feed':
        hunger -= 2
        happiness -= 1
        age += 1
        print(f"You fed {name}. He doesn't like it very much.")
    
    elif command.lower() == 'play':
        happiness += 1
        hunger += 1
        age += 1
        print(f"You played with {name}. He used a lot of energy!")

    elif command.lower() == 'sleep':
        hunger += 1
        happiness -= 1
        age += 5
        print(f"{name} took a nap. He feels rested but a bit hungry.")
    
    if hunger > 10:
        print(f"{name} is too hungry and has died!")
        break

    if happiness > 10:
        print(f"{name} is too happy and has rolled away looking for new adventures!")
        break

    if hunger < 0:
        print(f"{name} is fat now. It dies of a heart attack!")
        break

    if happiness < 0:
        print(f"{name} is too sad and has crumbled to pieces!")
        break

    elif age > 50:
        print(f"{name} has grown old and is now a wise rock.")
        choice = input("Do you want to retire it? (yes/no) ")
        if choice.lower() == 'yes':
            print(f"You retired {name}. It will live out its days in peace.")
            break
        else:
            print(f"{name} continues its journey with you.")

    # Secret ending
    elif age > 100:
        print("New option unlocked: Pray")
        if command.lower() == 'pray':
            print(f"You prayed for {name}. It became a God! It consumes the entire world for food.")
            break

    # Else for unknown commands
    else:
        print(f"{name} is still with you. Please select an action.")