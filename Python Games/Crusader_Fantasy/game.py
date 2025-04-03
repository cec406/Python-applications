import random
import time
import json
import textwrap
import os

# Global variables
player_health = 50
player_faith = 10
player_fatigue = 0
inventory = ["longsword", "shield", "Bible"]
story_flags = {}
typing_speed = 0.03  # Slightly slower for drama
line_delay = 0.5  # Delay between lines for readability

# Helper Functions
def get_terminal_width():
    """Get the current terminal width, defaulting to 80 if undetectable."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def type_text(text, speed=typing_speed):
    """Prints text line-by-line with medieval flair, wrapping at word boundaries."""
    print("\033[93m✠\033[0m ", end="")  # Decorative cross
    terminal_width = get_terminal_width() - 4  # Adjust for cross and padding
    lines = text.strip().split("\n")
    for line in lines:
        wrapped_lines = textwrap.fill(line.strip(), width=terminal_width)
        for wrapped_line in wrapped_lines.split("\n"):
            print(wrapped_line, flush=True)
            time.sleep(line_delay)  # Delay between lines
    print("\033[93m ✠\033[0m")  # Closing cross
    time.sleep(0.2)  # Brief pause after each text block

def get_choice(prompt, options):
    """Displays choices with line separation and single numbering."""
    if not options:  # Handle no-choice scenes (e.g., combat)
        return "1"  # Default to first outcome if no choices
    type_text(prompt)
    for i, desc in enumerate(options.values(), 1):
        print(f"{i}. {desc}\n")  # Newline after each option
    try:
        choice = input("Thy will (1-{}): ".format(len(options))).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return str(int(choice))  # Convert to string key
        raise ValueError
    except ValueError:
        type_text("Thou hast faltered in thy choice—divine guidance takes thee forth.")
        return "1"  # Default to first option

def adjust_health(amount, reason):
    global player_health
    player_health = max(0, player_health + amount)
    color = "\033[92m" if amount > 0 else "\033[91m"  # Green or Red ANSI
    type_text(f"{color}{reason} ({'+' if amount > 0 else ''}{amount} HP)\033[0m")

def adjust_faith(amount, reason):
    global player_faith
    player_faith = max(0, min(10, player_faith + amount))
    color = "\033[93m" if amount > 0 else "\033[97m"  # Yellow or White ANSI
    type_text(f"{color}{reason} ({'+' if amount > 0 else ''}{amount} Faith)\033[0m")

def adjust_fatigue(amount, reason):
    global player_fatigue
    player_fatigue = max(0, min(10, player_fatigue + amount))
    color = "\033[93m" if amount > 0 else "\033[92m"  # Yellow or Green ANSI
    type_text(f"{color}{reason} ({'+' if amount > 0 else ''}{amount} Fatigue)\033[0m")

def save_game(chapter):
    with open("crusader_save.json", "w") as f:
        json.dump({"chapter": chapter, "health": player_health, "faith": player_faith, "fatigue": player_fatigue, "inventory": inventory, "flags": story_flags}, f)
    type_text("Thy tale is etched upon the sacred scroll.")

def load_game():
    try:
        with open("crusader_save.json", "r") as f:
            data = json.load(f)
            global player_health, player_faith, player_fatigue, inventory, story_flags
            player_health = data["health"]
            player_faith = data["faith"]
            player_fatigue = data["fatigue"]
            inventory = data["inventory"]
            story_flags = data["flags"]
            type_text("A past crusade is summoned from the annals.")
            return data["chapter"]
    except FileNotFoundError:
        return 1

# Combat System
def combat(enemy_name, enemy_health, enemy_attack, chapter_num, special_mechanic=None):
    global player_health, player_faith, player_fatigue, inventory
    player_status = {}
    enemy_status = {}
    special = 0
    
    difficulty_factor = 1 + (chapter_num - 1) * 0.2
    if "sword of light" in inventory:
        difficulty_factor += 0.2
    enemy_health = int(enemy_health * difficulty_factor)
    enemy_attack = int(enemy_attack * difficulty_factor)
    
    if player_fatigue >= 8:
        enemy_attack += 2
        type_text("Weariness clouds thy vigilance, O knight!")
    
    type_text(f"A clash of fates begins! {enemy_name}, spawn of darkness, stands afore thee!")
    
    while player_health > 0 and enemy_health > 0:
        type_text(f"\nThy vigor: \033[92m{player_health}\033[0m HP | {enemy_name}: \033[91m{enemy_health}\033[0m | Faith: \033[93m{player_faith}\033[0m | Fatigue: \033[93m{player_fatigue}\033[0m")
        if special_mechanic:
            type_text(f"{special_mechanic['name']}: {special}/{special_mechanic['max']}")
        
        actions = {
            "1": "Strike with thy longsword (d6)",
            "2": "Bash with thy shield (d4 + stun)",
            "3": "Pray unto the Lord (heal d6, 3 Faith)",
            "4": "Parry the foe’s blow (reduce next hit)",
            "5": "Rest to ease thy burden (reduce Fatigue)",
        }
        if "sword of light" in inventory:
            actions["6"] = "Unleash the Sword of Light (d8)"
        if "rusted dagger" in inventory:
            actions["7"] = "Hurl the rusted dagger (d4, lose item)"
        if "healing herbs" in inventory:
            actions["8"] = "Consume healing herbs (heal 5)"
        
        choice = get_choice("How shalt thou meet this foe?", actions)
        damage = 0
        stun = False
        
        if choice == "1":
            damage = random.randint(1, 6)
            enemy_health -= damage
            type_text(f"Thy longsword cleaves through, dealing \033[91m{damage}\033[0m unto {enemy_name}!")
            adjust_fatigue(1, "The strike wearies thy arm")
        elif choice == "2":
            damage = random.randint(1, 4)
            enemy_health -= damage
            type_text(f"Thy shield smites {enemy_name} for \033[91m{damage}\033[0m, a thunderous rebuke!")
            adjust_fatigue(1, "The effort strains thy frame")
            if random.random() < 0.3:
                enemy_status["stunned"] = 1
                type_text(f"{enemy_name} staggers, stunned by thy might!")
                stun = True
        elif choice == "3" and player_faith >= 3:
            heal = random.randint(1, 6)
            player_health += heal
            adjust_faith(-3, "Prayer taxes thy spirit")
            type_text(f"A prayer ascends, and divine grace heals thee for \033[92m{heal}\033[0m HP!")
            player_status["blessed"] = 3
        elif choice == "4":
            player_status["parrying"] = 1
            type_text("Thou raisest thy guard, ready to parry the next blow!")
        elif choice == "5":
            adjust_fatigue(-2, "Rest restores thy vigor")
            type_text("Thou dost pause, breathing deep to steady thy soul.")
        elif choice == "6" and "sword of light" in inventory:
            damage = random.randint(1, 8)
            enemy_health -= damage
            type_text(f"The Sword of Light blazes forth, searing {enemy_name} for \033[91m{damage}\033[0m!")
            adjust_fatigue(1, "Its holy weight tires thee")
        elif choice == "7" and "rusted dagger" in inventory:
            damage = random.randint(1, 4)
            enemy_health -= damage
            inventory.remove("rusted dagger")
            type_text(f"Thou hurlest the rusted dagger, striking {enemy_name} for \033[91m{damage}\033[0m!")
        elif choice == "8" and "healing herbs" in inventory:
            heal = 5
            player_health += heal
            inventory.remove("healing herbs")
            type_text(f"Thou consumest the herbs, mending thy flesh for \033[92m{heal}\033[0m HP!")
        
        if special_mechanic and not stun:
            special += 1
            if special >= special_mechanic["max"]:
                if special_mechanic["name"] == "Whip Charge":
                    damage = random.randint(10, 15)
                    player_health -= damage
                    type_text(f"{enemy_name} lashes with a fiery whip, searing thee for \033[91m{damage}\033[0m!")
                    player_status["burning"] = 3
                elif special_mechanic["name"] == "Submerged":
                    damage = 10
                    player_health -= damage
                    type_text(f"The waters surge, dragging thee under for \033[91m{damage}\033[0m!")
                special = 0
        
        if enemy_health > 0 and not stun:
            damage = random.randint(1, enemy_attack)
            if "parrying" in player_status:
                damage //= 2
                del player_status["parrying"]
                type_text("Thy parry halves the foe’s wrath!")
            player_health -= damage
            type_text(f"{enemy_name} smites thee with fell might, dealing \033[91m{damage}\033[0m!")
            if random.random() < 0.2:
                player_status["bleeding"] = 3
                type_text("A wound opens, thy blood doth flow!")
        
        for status in list(player_status.keys()):
            player_status[status] -= 1
            if status == "bleeding" and player_status[status] > 0:
                player_health -= 2
                type_text(f"Bleeding drains thy life for \033[91m2 HP\033[0m!")
            elif status == "burning" and player_status[status] > 0:
                player_health -= 3
                type_text(f"Flames sear thee for \033[91m3 HP\033[0m!")
            if player_status[status] <= 0:
                del player_status[status]
        
        for status in list(enemy_status.keys()):
            enemy_status[status] -= 1
            if enemy_status[status] <= 0:
                del enemy_status[status]
    
    victory = player_health > 0
    type_text(f"\n{'Hallelujah!' if victory else 'Woe!'} {enemy_name} {'falls to thy righteous blade' if victory else 'hath claimed thy soul'}.")
    return victory

# Scene Handler
def scene(text, choices, outcomes):
    try:
        type_text(text)
        if not choices:  # Combat or automatic scenes
            return outcomes.get("default", lambda: True)()
        valid_options = {str(i+1): choice for i, choice in enumerate(choices)}
        choice = get_choice("\n\033[93m=== What shalt thou do, O Crusader? ===\033[0m", valid_options)
        result = outcomes.get(choice, outcomes["default"])()
        return result
    except Exception as e:
        type_text(f"ERROR: The tapestry of fate unraveled - {str(e)}")
        return False

# Random Event Generator
def random_event():
    events = [
        lambda: combat("Orc Scout", 20, 4, 1) and type_text("From its ruin, thou claimest a pouch of herbs!") and inventory.append("healing herbs"),
        lambda: adjust_health(-5, "A hidden snare snaps shut, biting into thy leg"),
        lambda: adjust_faith(2, "A faint hymn lifts thy spirit, a whisper from the heavens"),
    ]
    return random.choice(events)()

# Instructions
def instructions():
    type_text("""
    Welcome, noble soul, to *The Chronicles of the Crusader*. Herein lie the instructions to guide thee on thy holy quest:

    1. Thou shalt play as Sir Gideon of Acre, a knight of the Third Crusade, wielding faith and steel.
    2. Thy journey unfoldeth through chapters, each a trial of valor and spirit.
    3. At each step, choices shall appear—number them 1 to 4 (or more, as thy inventory groweth). Enter the number of thy will (e.g., '1') and press Enter.
    4. In battle, options abound: strike with thy longsword, bash with thy shield, pray for healing (costing Faith), and more as thou gainest relics.
    5. Thy stats be thus:
       - Health (HP): If it falleth to 0, thy quest endeth.
       - Faith (0-10): Fuel for divine aid, earned or spent in thy deeds.
       - Fatigue (0-10): Weariness that weakeneth thee if too high.
       - Inventory: Relics like thy Bible or a golden key aid thy path.
    6. Thy progress saveth to a sacred scroll ('crusader_save.json') betwixt chapters, to be recalled if thou choosest.

    Prepare thy heart, for shadows and grace await. Art thou ready?
    """)
    choice = get_choice("Choose thy fate:", {"1": "Ready to play"})
    if choice == "1":
        return True
    return False  # In case of invalid input, loop back (handled in main)

# Story Content
def intro():
    type_text("""
    In the Year of Our Lord 1187, beneath the blistering sun of the Third Crusade, thou art Sir Gideon of Acre, a knight forged in the fires of faith and steel. Thy armor, once resplendent under the banners of King Richard the Lionheart, now bears the scars of battles fought to reclaim Jerusalem from the Saracen yoke. The desert sands hath been thy forge, thy longsword thy sacred chant, and thy tattered Bible—bound in weathered leather—thy solace through nights of blood and lamentation.

    Yet this eve, as the wind wailed through thy encampment like the cries of the damned, a vision gripped thee. A lion, majestic and fearsome, stood afore thy tent, its golden mane crowned with thorns that wept crimson rivers upon the parched earth. Its eyes blazed with celestial fire, and its voice thundered across the boundless plains: 'Rise, Gideon, and tread the path beyond.' Thou didst fall to thy knees, clutching thy shield as the world melted into shadow.

    When thy senses returned, the desert was no more. The stars of the Holy Land hath vanished. Instead, thou standest in a realm unknown—a tapestry woven of medieval Europe’s stern keeps, Narnia’s enchanted groves, and Mordor’s ash-laden peaks. The air hums with a divine mystery, and thy heart pounds beneath thy breastplate, torn betwixt dread and holy purpose.

    Welcome to *The Chronicles of the Crusader*, Sir Gideon. Herein lies thy destiny, a land where faith and blade shall be tested against shadows older than time itself.

    Ready to play? Type 'Begin the journey'
    """)
    while True:
        response = input().strip()
        if response.lower() == "begin the journey":
            return 1
        elif response.lower() == "load":
            return load_game()
        else:
            print("Pray, type 'Begin the journey' to proceed, or 'load' to recall a past tale.")
            time.sleep(0.5)

def chapter_one():
    type_text("\n--- Chapter I: The Forest of Shadows ---")
    scenes = [
        {
            "text": """
            The veil of the world lifts as a dreamlike mist parts afore thine eyes, unveiling a forest ancient and foreboding. Mighty oaks, gnarled and stooped, reach with twisted limbs toward a sky veiled by a shroud of leaves, their bark etched by centuries of silent woe. The air hangs heavy with the scent of moss and rot, a cloying breath that clings to thy throat. Thy boots sink into the loamy soil, and the faint rustle of unseen things stirs the undergrowth. Thou risest from where thou knelt in prayer during that fateful vision, thy armor chiming softly in the oppressive hush. The forest breathes around thee, alive with unseen watchers, and a chill wind bears whispers—perchance the voices of angels, or the murmurs of a darker host.
            """,
            "choices": ["1. Draw thy sword, vigilant for peril", "2. Kneel once more in prayer", "3. Harken unto the whispers", "4. Seek a path through the gloom"],
            "outcomes": {
                "1": lambda: adjust_health(-5, "The shadows stir, a branch snaps beneath an unseen tread") or True,
                "2": lambda: adjust_health(5, "A warmth suffuses thee, a flicker of divine radiance") and adjust_faith(2, "Thy prayer fortifies thy soul") or True,
                "3": lambda: type_text("The whispers weave through the leaves: 'Beware the shadow that stalks the light.' A riddle, perchance, or a warning from the ether.") or True,
                "4": lambda: type_text("Thine eyes pierce the mist, spying a faint golden gleam to the east—a beacon or a snare in this forsaken wood.") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            As thou steady thy breath, the mist swirls and parts, revealing a sight both wondrous and strange. A stag strides forth, its coat aglow with an unearthly sheen that rends the forest’s gloom. Betwixt its antlers, a cross of molten gold blazes, casting a halo about its noble crown. Its eyes, deep and wise, fix upon thee, unblinking, as if gazing into the depths of thy spirit. The air grows still, the whispers fading to a reverent silence. This is no mere beast, but a vision—mayhap a herald of the Almighty, or a guile woven by this enchanted realm.
            """,
            "choices": ["1. Approach with reverence", "2. Bow in humble obeisance", "3. Turn aside, wary of deceit", "4. Challenge it with a shout, blade aloft"],
            "outcomes": {
                "1": lambda: adjust_health(10, "The stag’s cross grazeth thy brow, vitality surging through thy veins") and story_flags.update({"stag_spared": True}) or True,
                "2": lambda: adjust_faith(3, "Thy humility afore this creature bolstereth thy spirit") or True,
                "3": lambda: True,
                "4": lambda: adjust_health(-5, "The stag fleeth, its hooves shaking the earth beneath thee") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The forest closeth in as thou pressest onward, its branches clawing at thy armor like the hands of the damned. A sudden sound shatters the stillness—footfalls, heavy and deliberate, crunching through the underbrush behind thee. Thy grip tightens on thy sword hilt, memories of ambushes in the Holy Land flashing afore thine eyes. The air thickens with menace, and thy pulse quickens beneath thy breastplate. What stalketh thee is no wraith of mist, but a foe of flesh and malice.
            """,
            "choices": ["1. Turn and face the unseen foe", "2. Slip behind a tree to conceal thyself", "3. Climb a nearby oak", "4. Beseech the Lord’s protection"],
            "outcomes": {
                "1": lambda: combat("Orc Ambush", 25, 5, 1),
                "2": lambda: True,
                "3": lambda: adjust_fatigue(2, "The climb straineth thy weary sinews") or True,
                "4": lambda: adjust_health(5, "A faint glow enshrouds thee, warding off the unseen") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            Thy path windeth deeper into the wood, where the trees grow dense, their branches entwined like the vault of a shadowed cathedral. Amidst the roots, a glint catcheth thine eye—a rusted dagger, its blade marred by age, half-buried in the earth. Beside it, the soil is disturbed, as if clawed by desperate hands. The air groweth heavy, laden with the weight of forgotten sorrow. Thy crusader’s heart wrestleth betwixt caution and curiosity, the Bible at thy chest a silent testament to thy sacred charge.
            """,
            "choices": ["1. Claim the dagger as thine own", "2. Leave it untouched", "3. Dig beneath its resting place", "4. Bury it with a prayer"],
            "outcomes": {
                "1": lambda: inventory.append("rusted dagger") or True,
                "2": lambda: True,
                "3": lambda: inventory.append("Aramaic scroll") or True,
                "4": lambda: adjust_faith(1, "A prayer for the lost sootheth thy soul") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A tremor rippleth through the forest floor, leaves raining from the canopy like tears of the lost. The whispers swell into a chorus of dread: 'The beast stirs… the shadow nears…' The trees bend inward, their gnarled forms bowing to an unseen presence. Thy breath fogs in the chill air, and the weight of thy armor becometh both shield and burden. From the underbrush riseth a low growl, primal and deep, kindling the embers of thy crusader’s fire.
            """,
            "choices": ["1. Draw thy sword and stand resolute", "2. Carve a cross into a tree", "3. Recite Psalm 23 aloud", "4. Move silent as a shade"],
            "outcomes": {
                "1": lambda: True,
                "2": lambda: adjust_faith(2, "The cross’s sanctity steadyeth thy heart") or True,
                "3": lambda: adjust_health(5, "The words of scripture renew thy strength") or True,
                "4": lambda: story_flags.update({"stealthy": True}) or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The forest’s heart beateth louder, a primal rhythm shaking the earth beneath thy boots. From the shadows emergeth a figure—a hermit, clad in tattered robes, his eyes wild with fervor or madness. He clutchth a staff crowned with a crude cross, and his voice raspeth like dry leaves: 'The beast cometh, knight! Wilt thou face it, or flee as the weak?' His gaze boreth into thee, demanding judgment, whilst the growl draweth nigh, a storm upon the horizon.
            """,
            "choices": ["1. Proclaim thy resolve to fight", "2. Seek his blessing", "3. Pass him by in silence", "4. Demand his aid"],
            "outcomes": {
                "1": lambda: adjust_faith(1, "Thy vow strengtheneth thy spirit") or True,
                "2": lambda: adjust_health(5, "His trembling hand bestoweth a blessing") or True,
                "3": lambda: True,
                "4": lambda: adjust_health(-5, "He swingeth his staff in wrath") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A sudden trial striketh! The forest shifteth, its mysteries unfolding in ways unforeseen.
            """,
            "choices": [],
            "outcomes": {"default": lambda: random_event()}
        },
        {
            "text": """
            Thou stumblest into a clearing where the mist thinneth, revealing a slab of weathered stone sunk into the earth. Its surface is graven with jagged runes that pulse faintly with a sickly green light: 'The Beast Cometh.' The air hums with ancient power, and the ground trembleth beneath thy feet, as if the prophecy stirreth to life. Thy Bible presseth against thy chest, a bulwark ‘gainst the dread coiling in thy gut. This be no mere relic, but a harbinger of the trial to come.
            """,
            "choices": ["1. Lay thy hand upon the stone", "2. Pass it by", "3. Offer a prayer o’er it", "4. Smite it with thy sword"],
            "outcomes": {
                "1": lambda: True,
                "2": lambda: True,
                "3": lambda: adjust_health(5, "A warm light floweth from thy prayer") or True,
                "4": lambda: adjust_health(-5, "The blade’s impact jarreth thy arms") and story_flags.update({"slab_smashed": True}) or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The forest erupteth into chaos as the trees part with a groan, their roots torn asunder by a monstrous form. A Chimera riseth—its lion’s head roareth with primal fury, its serpent tail hisseth venom, and its shadowy wings beat a tempest into the air. Its eyes blaze like hellfire, fixing upon thee with a hunger born of prophecy. Thy sword trembleth in thy grip, not from fear, but from the weight of this hour—a trial sent by powers beyond mortal ken. The battle commenceth ‘neath the canopy of shadow.

            .-------.
            |  ***  |
            |  ***  |
            '-------'
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("the Chimera", 40, 8, 1) and inventory.append("golden key")
            }
        }
    ]
    for s in scenes:
        if not scene(s["text"], s["choices"], s["outcomes"]):
            return False
    save_game(2)
    return True

def chapter_two():
    type_text("\n--- Chapter II: The Tower of Judgment ---")
    scenes = [
        {
            "text": """
            The forest dwindles as thou emergest onto a windswept plain, the air sharp with the tang of coming rain. Afore thee riseth a tower of black stone, its jagged spire piercing the storm-laden sky like a lance thrust into the firmament. At its peak, a golden cross glinteth faintly through the gathering clouds, a beacon amidst the desolation—or perchance a taunt to the unworthy. The ground crunchth beneath thy boots with gravel, and the golden key in thy pack hums faintly, as if drawn to this place of judgment. The wind howleth, bearing echoes of distant thunder, and thou feelest the weight of unseen eyes upon thee.
            """,
            "choices": ["1. Approach the iron gate", "2. Circle the tower’s base", "3. Kneel and pray", "4. Examine the stonework"],
            "outcomes": {
                "1": lambda: "golden key" in inventory and type_text("The key vibrateth against thy chest as thou near’st the gate.") or True,
                "2": lambda: inventory.append("rusted grate knowledge") or True,
                "3": lambda: adjust_health(5, "A flicker of divine favor warmeth thy weary frame") or True,
                "4": lambda: type_text("Faint runes scar the stone: 'Judgment awaiteth the pure.' A riddle from ages past.") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            Thou standest afore the iron gate, its bars rusted yet unyielding, forged in some ancient fire. The golden key trembleth in thy pack, its light pulsing like a heartbeat ‘gainst the gloom. The tower loometh above, its black walls etched with the scars of forgotten battles. Above the gate, the golden cross gleamth through the storm, a silent witness to thy fate. The wind tuggeth at thy cloak, and thou sensest the tower’s judgment drawing nigh—a test of thy worthiness.
            """,
            "choices": ["1. Insert the golden key", "2. Pound upon the iron", "3. Shout a proclamation", "4. Step back and reconsider"],
            "outcomes": {
                "1": lambda: "golden key" in inventory and type_text("The key slideth into the lock with a soft click, and the gate groaneth open, revealing a dark stair.") or True,
                "2": lambda: True,
                "3": lambda: adjust_health(-5, "Wraiths stir from the shadows, grazing thy soul") or True,
                "4": lambda: True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The gate—if thou hast opened it—yieldeth to a spiral stair that twisteth upward into darkness, its steps worn smooth by countless treaders. Torchlight flickereth faintly along the walls, casting shadows that dance like specters of the damned. The air groweth colder with each step, the stone closing in like the maw of a great beast. Thy breath foggeth afore thee, and the clank of thy armor echoeth in the narrow passage. The tower’s heart lieth above, but its secrets guard the way.
            """,
            "choices": ["1. Climb boldly upward", "2. Search for traps", "3. Pray for protection", "4. Listen for sounds above"],
            "outcomes": {
                "1": lambda: adjust_fatigue(1, "The ascent straineth thy legs") or True,
                "2": lambda: True,
                "3": lambda: adjust_health(5, "A mantle of peace settleth o’er thee") or True,
                "4": lambda: type_text("Slow, deliberate footfalls echo from above, clad in iron—a guardian awaiteth.") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A sudden trial striketh! The tower’s ancient stones shift, unveiling its hidden perils or boons.
            """,
            "choices": [],
            "outcomes": {"default": lambda: random_event()}
        },
        {
            "text": """
            The stair climbeth steeper now, and a chill wind gusteth downward, tugging at thy cloak like the grasp of unseen hands. The stone groweth slick with moisture, glistening in the torchlight, and the air thickeneth with the scent of decay—an ancient rot that seepeth from the walls. Thy grip tighteneth on thy sword, memories of Jerusalem’s sieges flashing through thy mind. Each step feeleth a trial, the tower testing thy resolve with every breath.
            """,
            "choices": ["1. Press through the wind", "2. Raise thy shield", "3. Recite scripture", "4. Retreat a few steps"],
            "outcomes": {
                "1": lambda: adjust_fatigue(1, "The wind battereth thy weary form") or True,
                "2": lambda: True,
                "3": lambda: adjust_faith(2, "Thy words cut through the storm") or True,
                "4": lambda: adjust_health(-5, "The cold seepeth into thy bones as thou falterest") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A landing interrupteth the stair, a narrow shelf carved into the tower’s heart. From the shadows emergeth a wraith, its form a tattered shroud of darkness, its eyes aglow with malevolent light. It drifteth forward, claws outstretched, a guardian of this forsaken place. Thy sword arm tenseth, the weight of thy crusade pressing down as the air groweth heavy with its presence.
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("Wraith Guard", 30, 6, 2)
            }
        },
        {
            "text": """
            The wraith’s defeat revealeth a crevice in the stone, where a cluster of herbs gloweth with a faint, verdant light. Their leaves shimmer ‘gainst the black wall, a stark contrast to the tower’s decay. They smell of life, a whisper of grace in this stern place, yet thou wonderest if they be a gift—or a lure set by unseen hands. Thy weary body acheth for their promise, but caution lingereth in thy mind.
            """,
            "choices": ["1. Take the herbs", "2. Leave them be", "3. Consume them now", "4. Study them closely"],
            "outcomes": {
                "1": lambda: inventory.append("healing herbs") or True,
                "2": lambda: True,
                "3": lambda: adjust_health(10, "The herbs’ bitter taste floodeth thee with renewed vigor") or True,
                "4": lambda: type_text("These be monk’s wort, known to the healers of old—a rare find indeed.") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The stair resumeth, its steps narrower now, and a faint click echoeth ahead—a trap, perchance, or the shifting of ancient stone. The walls gleam with moisture, reflecting the torchlight in eerie patterns that dance like specters. Thy breath foggeth in the frigid air, and each step feeleth a gamble ‘gainst the tower’s cruel design. The sound groweth louder, a warning or a challenge.
            """,
            "choices": ["1. Attempt to disarm it", "2. Step carefully over", "3. Pray for safe passage", "4. Fall back briefly"],
            "outcomes": {
                "1": lambda: True,
                "2": lambda: adjust_health(-5, "A dart whistleth past, grazing thine arm") or True,
                "3": lambda: adjust_faith(1, "Thy prayer steadyeth thine hand") or True,
                "4": lambda: adjust_fatigue(1, "Retreating taxeth thy strength") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The stair endeth at a vast platform, the tower’s summit open to a sky wracked by storm. Lightning splitteth the clouds, illuminating the golden cross above—a symbol of salvation or condemnation. From the shadows descendeth a Watcher, half-angel, half-beast, its form a blasphemy of divine and profane. Its eyes burn with judgment, its flaming whip cracketh like thunder, and its voice boometh: 'Prove thy worth, knight, or perish!' The platform trembleth as it lasheth out, and the battle beginneth ‘neath the storm’s wrath.
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("the Watcher", 50, 6, 2, {"name": "Whip Charge", "max": 3}) and inventory.append("silver chalice")
            }
        }
    ]
    for s in scenes:
        if not scene(s["text"], s["choices"], s["outcomes"]):
            return False
    save_game(3)
    return True

def chapter_three():
    type_text("\n--- Chapter III: The River of Grace ---")
    scenes = [
        {
            "text": """
            The tower fadeth into memory as thou steppest onto a cliff’s edge, overlooking a vast river that shimmereth with a holy light. Its waters flow like molten gold, reflecting the golden city that riseth on the far shore—its spires pierce the heavens, a vision of Zion reborn. Yet beneath the surface, dark shapes twist and writhe, a reminder that grace here is tempered by peril. The wind carrieth a soft hymn, and thy boots crunch ‘gainst the rocky ledge as thou descendest toward the bank, drawn by the city’s promise.
            """,
            "choices": ["1. Approach the riverbank", "2. Kneel and pray", "3. Scan the horizon", "4. Touch the water"],
            "outcomes": {
                "1": lambda: type_text("A rickety bridge swayeth in the breeze, its planks weathered and frail.") or True,
                "2": lambda: adjust_health(5, "The river’s light bathes thee in grace") or True,
                "3": lambda: type_text("The city gleameth across the water, a path winding down the cliff to thy left.") or True,
                "4": lambda: adjust_health(10, "The warm water washeth away thy weariness") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            Thou reachest the riverbank, where the golden waters lap at the shore with a gentle, ceaseless rhythm. The bridge loometh closer now, its ropes frayed and boards creaking ‘neath the wind’s push. Across the river, the city’s light beckoneth, a promise of rest after thy trials. Yet the churning beneath the surface warneth of dangers unseen, and thy crusader’s heart weigheth valor ‘gainst wisdom. The hymn groweth louder, a call to cross—or a lure to thy doom.
            """,
            "choices": ["1. Cross the bridge cautiously", "2. Seek a ford downstream", "3. Reinforce the bridge", "4. Swim the river"],
            "outcomes": {
                "1": lambda: adjust_health(-5, "A plank snappeth, nigh plunging thee in") or True,
                "2": lambda: inventory.append("ford knowledge") or True,
                "3": lambda: adjust_fatigue(1, "The labor wearieth thee") or True,
                "4": lambda: adjust_health(-15, "The current draggeth at thine armor") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            As thou steady thyself, a dove soareth overhead, its wings a flash of white ‘gainst the golden sky. It circleth once above the river, a symbol of peace—or a guide sent from the city beyond. Its flight is graceful, cutting through the mist that riseth from the water, and it banketh toward the river’s heart, its path a silent invitation. The hymn swelleth, and thou feelest the weight of thy choices pressing upon thee.
            """,
            "choices": ["1. Follow the dove’s path", "2. Pray to it for guidance", "3. Ignore it and press on", "4. Watch its flight closely"],
            "outcomes": {
                "1": lambda: True,
                "2": lambda: adjust_health(5, "A peace settleth o’er thy soul") or True,
                "3": lambda: True,
                "4": lambda: adjust_faith(1, "Its grace sharpeneth thy senses") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A sudden trial striketh! The river’s banks shift, unveiling the land’s hidden trials or treasures.
            """,
            "choices": [],
            "outcomes": {"default": lambda: random_event()}
        },
        {
            "text": """
            The riverbank yieldeth a new discovery—a driftwood raft, its timbers lashed together with vines, resting half in the water. It beareth the marks of some lost traveler, its wood weathered by the current’s embrace. The golden city glimmereth across the waves, and thou ponderest the raft’s worth ‘gainst the crossing ahead—or the one thou hast made. The hymn hums in the air, a reminder of the grace that surroundeth thee.
            """,
            "choices": ["1. Claim the raft", "2. Repair it with thy tools", "3. Leave it behind", "4. Push it into the river"],
            "outcomes": {
                "1": lambda: inventory.append("driftwood raft") or True,
                "2": lambda: adjust_fatigue(1, "The work tireth thy hands") or True,
                "3": lambda: True,
                "4": lambda: True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A howl splitteth the air, sharp and guttural, echoing from the far bank like the wolves of Rohan’s plains. Wargs burst from the mist, their fur matted with river mud, their fangs gleaming as they charge toward thee. Their eyes burn with feral hunger, drawn by the scent of thy blood and steel. Thy hand flieth to thy sword, the memory of battle stirring thy crusader’s fire as the pack closeth in.
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("Warg Pack", 35, 7, 3)
            }
        },
        {
            "text": """
            The silver chalice—if thou bear’st it—gloweth faintly as thou near’st the river’s heart, its light reflecting on the golden waves like a mirror of grace. The waters ripple in response, as though recognizing the relic’s sanctity. Thou feelest its power stirring, a gift from the tower now turned to salvation—or a tool for the trials ahead. The city’s spires shimmer closer, their promise within reach.
            """,
            "choices": ["1. Fill the chalice with river water", "2. Drink from it", "3. Offer it to the river", "4. Raise it high"],
            "outcomes": {
                "1": lambda: "silver chalice" in inventory and inventory.append("holy water") or True,
                "2": lambda: "silver chalice" in inventory and adjust_health(15, "The water floodeth thee with divine renewal") or True,
                "3": lambda: adjust_faith(2, "The river accepteth thine offering") or True,
                "4": lambda: True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The river’s calm shattereth as the waters churn violently, waves crashing ‘gainst the bank with a roar like Judgment Day. Dark shapes surge beneath, their forms obscured but menacing—scales glint, and eyes like embers pierce the surface. Thy shield arm tenseth, the tales of Leviathan echoing in thy mind as the current groweth wilder. The city’s light flickereth across the waves, a distant hope amidst this rising peril.
            """,
            "choices": ["1. Dive into the fray", "2. Launch the raft", "3. Pray for calm", "4. Stand and watch"],
            "outcomes": {
                "1": lambda: adjust_health(-5, "A dark shape brusheth thee, chilling thy blood") or True,
                "2": lambda: "driftwood raft" in inventory and True,
                "3": lambda: adjust_faith(1, "Thy prayer stilleth the waters") or True,
                "4": lambda: True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The river erupteth in a final fury as a Leviathan breachth the surface, its scales gleaming like burnished armor, its jaws snapping with the hunger of ages. Its eyes burn with the fires of Job’s ancient foe, and its roar shaketh the earth, a beast of prophecy barring thy path to the golden city. Thy sword gleamth in the fading light, the chalice’s glow—if thou hold’st it—flaring beside thee. This be a trial of steel and faith, and the battle beginneth on the shores of grace.
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("the Leviathan", 60, 8, 3, {"name": "Submerged", "max": 3}) and inventory.append("pearl of grace")
            }
        }
    ]
    for s in scenes:
        if not scene(s["text"], s["choices"], s["outcomes"]):
            return False
    save_game(4)
    return True

def chapter_four():
    type_text("\n--- Chapter IV: The Gates of Zion ---")
    scenes = [
        {
            "text": """
            The river falleth behind thee, its golden waters fading into a shimmering memory as thou steppest onto a shore of radiant sand. Afore thee rise the gates of Zion, their walls of jasper and pearl towering like the New Jerusalem of Revelation’s promise. The air hums with a celestial song, a choir of unseen voices that lifteth thy weary spirit. Yet a shadow loometh—a dark rider astride a pale horse, its eyes fixed upon thee with a gaze that chills thy soul. The ground beneath thy boots gleamth with holy light, and thy armor clanketh softly, a testament to the battles that brought thee hither.
            """,
            "choices": ["1. Stride boldly to the gates", "2. Kneel in reverence", "3. Look to the ramparts", "4. Examine the walls"],
            "outcomes": {
                "1": lambda: True,
                "2": lambda: adjust_health(5, "The sand’s warmth reneweth thee") or True,
                "3": lambda: type_text("Angelic figures stand atop the walls, their wings folded, their eyes stern yet serene.") or True,
                "4": lambda: inventory.append("wall breach knowledge") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The pearl of grace—if thou claim’dst it—pulseth warmly in thy pack, its light syncing with the celestial hymn that filleth the air. The gates tower above, their surface smooth as glass yet radiant with an inner fire. The rider shifteth atop its steed, a silhouette of dread ‘gainst the golden glow, and thou feelest the weight of judgment pressing down—a final test of all thou hast endured. The song groweth louder, a call to prove thy worth.
            """,
            "choices": ["1. Offer the pearl to the gates", "2. Clutch it close", "3. Pray with it in hand", "4. Ignore its glow"],
            "outcomes": {
                "1": lambda: "pearl of grace" in inventory and story_flags.update({"pearl_offered": True}) or True,
                "2": lambda: True,
                "3": lambda: adjust_health(5, "The pearl’s grace floweth through thee") or True,
                "4": lambda: adjust_faith(-1, "Thou spurn’st the relic’s call") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            A sudden trial striketh! The golden shore trembleth, unveiling the final twists of thy crusade.
            """,
            "choices": [],
            "outcomes": {"default": lambda: random_event()}
        },
        {
            "text": """
            The dark rider moveth now, its pale horse snorting wisps of shadow that curl like smoke. It dismounteth with a grace both terrible and serene, revealing Death itself—the Fourth Horseman of Revelation’s dread pages. Its scythe gleamth with unholy power, and its voice whispereth through the air like a blade o’er stone: 'Thy soul is mine, crusader.' The gates tremble behind it, as though the city holdeth its breath, and thy heart poundeth with a mix of fear and defiance.
            """,
            "choices": ["1. Challenge Death directly", "2. Bow in submission", "3. Pray for deliverance", "4. Flank via the breach"],
            "outcomes": {
                "1": lambda: adjust_health(-5, "The scythe grazeth thee as thou advancest") or True,
                "2": lambda: True,
                "3": lambda: adjust_faith(2, "Thy prayer pierceth the shadow") or True,
                "4": lambda: "wall breach knowledge" in inventory and story_flags.update({"flanked": True}) or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The angels above stir, their wings rustling like a storm of feathers ‘cross the golden sky. One descendeth, its armor gleaming with celestial fire, and extendeth a hand. In its grasp is a sword of radiant flame, its blade alive with holy wrath—a gift from the heavenly host, or a challenge to wield it rightly. The rider watcheth, its scythe still, as the air thickeneth with the weight of this moment.
            """,
            "choices": ["1. Call for the sword", "2. Refuse their aid", "3. Pray to receive it", "4. Salute in honor"],
            "outcomes": {
                "1": lambda: inventory.append("sword of light") or True,
                "2": lambda: True,
                "3": lambda: adjust_health(5, "A surge of strength blesseth thee") or True,
                "4": lambda: adjust_faith(1, "Thine honor bindeth thee to their cause") or True,
                "default": lambda: True
            }
        },
        {
            "text": """
            From the shadows beyond the gates, a legion of shades emergeth—souls lost to time, their forms wreathed in darkness. They advance with silent menace, claws of shadow outstretched, a final barrier afore the city’s embrace. Death standeth apart, watching as its minions test thy mettle. Thy blade gleamth, ready to carve a path through this last gauntlet.
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("Shadow Legion", 40, 8, 4)
            }
        },
        {
            "text": """
            The gates shudder now, their light pulsing like a living heart. Dust falleth from their frame, and the angels’ song crescendoth, a hymn of judgment or welcome that shaketh the air. Death advanceth, its scythe raised, a crescent of shadow ‘gainst the radiance. Thou feelest the climax of thy crusade drawing nigh, the weight of every step from Acre to this moment pressing upon thy shoulders.
            """,
            "choices": ["1. Push ‘gainst the gates", "2. Pray for them to open", "3. Stand and wait", "4. Seek the breach"],
            "outcomes": {
                "1": lambda: adjust_fatigue(2, "The gates resist thy might") or True,
                "2": lambda: adjust_faith(2, "The light flareth at thy prayer") or True,
                "3": lambda: adjust_health(-5, "Arrows of shadow rain from above") or True,
                "4": lambda: "flanked" in story_flags and True,
                "default": lambda: True
            }
        },
        {
            "text": """
            The air groweth thick with power as the gates pulse brighter, their song a melody of triumph or lament. Death closeth in, its scythe slashing the air with a sound like tearing silk. The ground quaketh ‘neath its steps, and the angels’ voices weave a chorus of light ‘gainst shadow. Thou grippest thy sword—or the sword of light, if it be thine—its steel or flame a testament to thy journey. The final battle loometh, a clash of mortal and eternal.
            """,
            "choices": ["1. Charge with fury", "2. Raise thy shield", "3. Pray for aid", "4. Dodge its strike"],
            "outcomes": {
                "1": lambda: adjust_fatigue(1, "The charge taxeth thy strength") or True,
                "2": lambda: True,
                "3": lambda: adjust_health(5, "A divine hand bolstereth thee") or True,
                "4": lambda: True,
                "default": lambda: True
            }
        },
        {
            "text": """
            Death, the Pale Rider, loometh larger now, its form towering ‘gainst the gates’ radiance. The angels fall silent, the storm holdeth its breath, and the Horseman striketh—a tempest of shadow and steel. Thy blade meeteth its scythe, a clash of crusader and apocalypse ‘neath Zion’s walls. The air crackleth with power, and thou feelest the threads of thy fate weaving shut in this moment.

            |  ***  |
            |  ***  |
            '-------'
            """,
            "choices": [],
            "outcomes": {
                "default": lambda: combat("the Pale Rider", 70, 10, 4, {"name": "Desperation", "max": float('inf')})
            }
        }
    ]
    for s in scenes:
        if not scene(s["text"], s["choices"], s["outcomes"]):
            return False
    return True

# Main Game Loop
def main():
    print("\033[93m" + "="*50 + "\033[0m")
    type_text("The Chronicles of the Crusader")
    print("\033[93m" + "="*50 + "\033[0m")
    
    # Show instructions until player is ready
    while not instructions():
        pass
    
    starting_chapter = intro()
    
    chapters = [chapter_one, chapter_two, chapter_three, chapter_four]
    for chapter_num, chapter_func in enumerate(chapters, 1):
        if starting_chapter <= chapter_num:
            print("\033[93m" + "-"*50 + "\033[0m")
            if not chapter_func():
                type_text(f"\nThy quest ends in Chapter {chapter_num}, O valiant one.")
                break
            elif chapter_num == 4:
                print("\033[93m" + "="*50 + "\033[0m")
                type_text("The End. Thy crusade triumphs, Sir Gideon, blessed be thy name!")
                print("\033[93m" + "="*50 + "\033[0m")
    
    type_text(f"Thy final relics: {', '.join(inventory)}")

if __name__ == "__main__":
    main()
