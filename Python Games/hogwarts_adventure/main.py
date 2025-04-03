import random
import time
from colorama import init, Fore, Style
import story  # Import the module, not a specific function, to avoid partial init issues

init()

COLOR_MAP = {
    "yellow": Fore.YELLOW,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "blue": Fore.BLUE
}

def type_text(text, color="white", delay=0.02):
    print(COLOR_MAP.get(color, Fore.WHITE), end="")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def get_choice(options, prompt="Choose your path", wizard=None):
    while True:
        type_text(f"{prompt} ({', '.join(options)}, menu): ", "yellow", 0)
        choice = input().strip().lower()
        if choice == "menu" and wizard:
            show_menu(wizard)
        elif choice in options:
            return choice
        else:
            type_text("Invalid choice—try again!", "red")

def show_menu(wizard):
    type_text("\n=== Wizard’s Grimoire ===", "yellow")
    type_text(f"Name: {wizard.name}", "white")
    type_text(f"House: {wizard.house or 'Unsorted'}", "white")
    type_text(f"Year: {wizard.year}", "white")
    type_text(f"Health: {wizard.health}/100", "cyan")
    type_text(f"Mana: {wizard.mana}/100", "cyan")
    type_text(f"House Points: {wizard.house_points}", "yellow")
    type_text(f"Morality: {wizard.morality} ({'Light' if wizard.morality > 0 else 'Neutral' if wizard.morality == 0 else 'Shadow'})", "white")
    type_text("\nSkills:", "magenta")
    for skill, level in wizard.skill_tree.items():
        type_text(f"  {skill.capitalize()}: Level {level}", "magenta")
    type_text("\nSpells Known:", "magenta")
    for spell in wizard.spells_known:
        type_text(f"  {spell.capitalize()}", "magenta")
    type_text("\nInventory:", "green")
    if wizard.inventory:
        for item in wizard.inventory:
            type_text(f"  - {item}", "green")
    else:
        type_text("  Empty", "green")
    type_text("\n=====================", "yellow")

class Wizard:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.health = 100
        self.mana = 100
        self.house_points = 50
        self.morality = 0
        self.inventory = []
        self.skill_tree = {
            "charms": 1, "defense": 1, "herbology": 1, "transfiguration": 1,
            "potions": 1, "divination": 0, "dark arts": 0
        }
        self.spells_known = ["stupefy"]
        self.protego_active = False
        self.year = 1

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if self.protego_active:
            damage = damage // 2
            type_text(f"{self.name}’s Protego halves the blow to {damage}!", "cyan")
            self.protego_active = False
        self.health = max(0, self.health - damage)
        type_text(f"{self.name} takes {damage} damage—health now at {self.health}!", "red")

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        type_text(f"{self.name} heals {amount}—health rises to {self.health}!", "green")

    def use_magic(self, spell, enemy=None, context=None):
        mana_costs = {"stupefy": 15, "expelliarmus": 20, "protego": 10, "expecto patronum": 30, "accio": 10, "wingardium leviosa": 10, "sectumsempra": 25}
        if spell not in self.spells_known:
            type_text(f"{self.name} hasn’t mastered {spell.capitalize()} yet!", "red")
            return False
        if self.mana < mana_costs.get(spell, 20):
            type_text(f"{self.name}’s wand sputters—mana too low!", "red")
            return False
        messages = {
            "stupefy": f"'Stupefy!'—a crimson bolt streaks from {self.name}’s wand, crackling with power!",
            "expelliarmus": f"'Expelliarmus!'—{enemy.name if enemy else 'the foe'}’s wand spins away in a flash of light!",
            "protego": f"'Protego!'—a shimmering shield envelops {self.name}, glowing like starlight!",
            "expecto patronum": f"'Expecto Patronum!'—a majestic silvery stag bursts forth, charging with radiant grace!",
            "accio": f"'Accio!'—objects soar toward {self.name} with a whoosh!",
            "wingardium leviosa": f"'Wingardium Leviosa!'—items lift gracefully under {self.name}’s deft command!",
            "sectumsempra": f"'Sectumsempra!'—dark slashes tear through the air, sharp and menacing!"
        }
        type_text(messages.get(spell), "magenta")
        if spell == "stupefy" and enemy:
            enemy.take_damage(20)
        elif spell == "expelliarmus" and enemy:
            enemy.take_damage(15)
            enemy.can_cast_spells = False
        elif spell == "protego":
            self.protego_active = True
        elif spell == "expecto patronum" and enemy:
            enemy.take_damage(30 if enemy.type == "shadow" else 15)
        elif spell == "wingardium leviosa" and enemy and context == "troll":
            type_text(f"The troll’s club rises—crashing down upon its own head with a thunderous crack!", "cyan")
            enemy.take_damage(100)  # Instant win
        elif spell == "sectumsempra" and enemy:
            enemy.take_damage(25)
            type_text(f"Blood seeps—‘Dark magic!’—the air grows heavy!", "red")
        self.mana -= mana_costs[spell]
        type_text(f"{self.name}’s mana falls to {self.mana}!", "cyan")
        return True

    def use_item(self, item):
        if item not in self.inventory:
            type_text(f"No {item} in {self.name}’s satchel!", "red")
            return False
        if item == "Healing Potion":
            self.heal(30)
            self.inventory.remove("Healing Potion")
            return True
        elif item == "Mandrake Draught":
            self.heal(50)
            self.inventory.remove("Mandrake Draught")
            type_text(f"{self.name} drinks a Mandrake Draught—vigor surges through their veins!", "green")
            return True
        return False

    def advance_skill(self, skill):
        if self.skill_tree[skill] < 5:
            self.skill_tree[skill] += 1
            type_text(f"{self.name}’s mastery of {skill.capitalize()} rises to Level {self.skill_tree[skill]}!", "cyan")
            if skill == "charms" and self.skill_tree[skill] == 2:
                self.spells_known.append("wingardium leviosa")
                type_text(f"{self.name} learns Wingardium Leviosa!", "magenta")
            elif skill == "defense" and self.skill_tree[skill] == 2:
                self.spells_known.append("expelliarmus")
                type_text(f"{self.name} learns Expelliarmus!", "magenta")
            elif skill == "defense" and self.skill_tree[skill] == 3 and self.year >= 3:
                self.spells_known.append("expecto patronum")
                type_text(f"{self.name} learns Expecto Patronum!", "magenta")
            elif skill == "dark arts" and self.skill_tree[skill] == 3 and self.year >= 6:
                self.spells_known.append("sectumsempra")
                type_text(f"{self.name} learns Sectumsempra—a dangerous spell!", "magenta")

    def modify_house_points(self, points):
        self.house_points += points
        if points > 0:
            type_text(f"{self.house}’s hourglass glimmers—{points} points added, now at {self.house_points}!", "yellow")
        else:
            type_text(f"{self.house}’s hourglass dims—{abs(points)} points lost, now at {self.house_points}!", "yellow")

    def align_with_good(self):
        self.morality += 1
        type_text(f"The light within {self.name} grows—Morality rises to {self.morality}!", "green")

    def align_with_dark(self):
        self.morality -= 1
        type_text(f"Shadows creep into {self.name}’s heart—Morality falls to {self.morality}!", "red")

class Enemy:
    def __init__(self, name, health, attack, type="normal"):
        self.name = name
        self.health = health
        self.attack = attack
        self.type = type
        self.can_cast_spells = True

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        type_text(f"{self.name} reels—{damage} damage taken, health now at {self.health}!", "red")

    def use_ability(self, wizard):
        if not self.can_cast_spells:
            type_text(f"{self.name} flails helplessly, its wand lost!", "red")
            wizard.take_damage(self.attack // 2)
        else:
            if self.type == "shadow" and random.random() < 0.5:
                type_text(f"{self.name} summons dark power—its strength surges ominously!", "red")
                self.attack += 5
            type_text(f"{self.name} unleashes a ferocious assault on {wizard.name}!", "red")
            wizard.take_damage(self.attack)

def main_game():
    type_text("\n=== Welcome to Hogwarts: A Magical Odyssey ===", "yellow")
    type_text("Embark on a seven-year journey where your wand carves your legend in the annals of wizarding history.", "white")
    type_text("Every choice shapes your path—will you walk in light or shadow?", "white")
    name = input("Enter your wizard’s name: ").strip()
    player = Wizard(name)
    type_text(f"\nGreetings, {player.name}. Your tale begins now.", "cyan")
    for year in range(1, 8):
        story.play_year(player, year)  # Call via module to avoid circular import
    type_text(f"\n=== Epilogue ===\n{player.name}’s epic saga concludes after seven years of wonder and peril!", "yellow")
    type_text(f"House: {player.house} | Points: {player.house_points} | Morality: {player.morality}", "yellow")
    type_text("Thank you for playing—may your magic endure!", "white")

if __name__ == "__main__":
    main_game()
