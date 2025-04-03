import random
import pyfiglet
from time import sleep

def print_title_screen():
    # Create ASCII art for the title
    title = pyfiglet.figlet_format("Chore Boss 3000", font="starwars")
    
    # Print the title
    print(title)
    print("👨‍🍳👩‍🎨 Welcome to the Ultimate Chore Assignment Machine! 🤖")
    print("Because teamwork makes the dream work (and Mom needs a break).")
    
    # Pause for dramatic effect
    sleep(3)

def assign_chores():
    chores = [
        "Load and Unload Dishwasher 🍽️ (hope you like puzzles!)",
        "Clean Counters 🧼 and Polish Appliances ✨(sparkle and shine time!)",
        "Clean Floors 🧹 (pretend you're Cinderella!)",
        "Organize Living Rooms 🛋️ (find the remote!)",
        "Take Out Trash 🗑️ (bonus cardio!)",
        "Clean Upstairs Bathroom 🚽 (hold your nose!)",
        "Clean Middle Bathroom 🚿 (scrub-a-dub-dub!)",
        "Clean Downstairs Bathroom 🛁 (a throne fit for royalty!)"
    ]

    funny_remarks = [
        "Welcome to the Chore Team, future cleaning champion! 🏆",
        "Get ready to become a household hero! 🦸‍♂️",
        "Congrats, you just signed up for greatness! 💪",
        "Brace yourself, chores are coming! ⚡",
        "The cleaning gods have chosen you! 👑",
        "Welcome aboard, the mess is yours to conquer! 🧙‍♀️",
        "You’re about to become a chore legend! 🎤",
        "Your destiny? To clean. Your reward? Snacks. 🍪",
        "Are you ready for the challenge? 💥",
        "You’ve been chosen by the Chore Gods! 🔮",
        "Every hero needs a sidekick. Are you ready? 🦸‍♀️",
        "The floor is yours to scrub... literally. 🧹",
        "I hope you're wearing your cleaning shoes! 👟",
        "It's not a chore, it’s an adventure! 🌍",
        "Get your cleaning game face on! 😎",
        "Welcome to the club of cleanliness! 🧽",
        "A hero in the making... armed with a mop. 🧴",
        "Let's make this place shine, one chore at a time! ✨",
        "You’ll be so good at this, they’ll name a vacuum after you! 🏆",
        "May your chores be swift and your rewards sweet! 🍭"
    ]
    
    print_title_screen()
    print("✨ Let's turn chaos into cleanliness! ✨")
    print("Type the names of the kids, one at a time. Type 'done' when finished.")
    
    kids = []
    while True:
        name = input("Enter a kid's name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name:  # Ensures non-empty names
            kids.append(name)
            # Pick a random funny remark after entering each kid's name
            print(f"🎉 {name} added! {random.choice(funny_remarks)}")
    
    if not kids:
        print("\nNobody signed up for the fun? Fine, no chores for anyone. 😤")
        print("Exiting program...")
        return
    
    print("\n🔮 The Chore Boss 3000 is working its magic...\n")
    sleep(2)  # Build suspense
    random.shuffle(chores)  # Randomize the chores list
    
    assignments = {}
    for i, kid in enumerate(kids):
        chore = chores[i % len(chores)]  # Loop through chores if more kids than chores
        assignments[kid] = chore
    
    print("🎉 Here's the lineup of chore champions! 🎉\n")
    for kid, chore in assignments.items():
        print(f"✨ {kid}: {chore} ✨")
        sleep(0.5)  # Adds a bit of flair to the announcements
    
    print("\nAll chores assigned! You're welcome. 🦸‍♀️🦸‍♂️")
    print("Remember: The sooner you finish, the sooner you can play!")
    
    # Pause before exiting
    input("\nPress Enter to exit the program and get to work! 💪")

# Run the program
if __name__ == "__main__":
    assign_chores()
