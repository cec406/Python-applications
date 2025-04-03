import random
from main import type_text, get_choice, Enemy

def play_year(wizard, year):
    wizard.year = year
    if year == 1:
        year_1(wizard)
    elif year == 2:
        year_2(wizard)
    elif year == 3:
        year_3(wizard)
    elif year == 4:
        year_4(wizard)
    elif year == 5:
        year_5(wizard)
    elif year == 6:
        year_6(wizard)
    elif year == 7:
        year_7(wizard)

def year_1(wizard):
    type_text("\n=== Year 1: The Philosopher’s Stone ===", "yellow")

    # Chapter 1: A Muggle’s Mundane Summer
    type_text("\nChapter 1: A Muggle’s Mundane Summer", "yellow")
    type_text("The summer sun blazes over your quiet Muggle town, a relentless tyrant baking the cracked pavements and wilting the patchy lawns into a brittle, faded yellow.", "white")
    type_text(f"You’re eleven, {wizard.name}, sprawled across the threadbare carpet of your small bedroom, flipping through a dog-eared comic book whose pages curl from countless readings.", "white")
    type_text("Life here is a relentless cycle—school drones on with its arithmetic and spelling, chores stack like unwashed dishes, and the neighbor’s terrier yaps incessantly at shadows.", "white")
    type_text("Yet beneath this monotony, a restless spark flickers within you—a whisper of something vast and untamed, yearning for a world beyond these peeling walls.", "white")
    type_text("Downstairs, your parents’ voices drift up—‘That fence needs fixing,’ your dad grumbles over a chipped teacup, while your mum sighs about grocery prices, a familiar hum against the buzz of flies.", "white")
    choice = get_choice(["daydream", "read", "explore"], "How will you escape this stifling day?", wizard)
    if choice == "daydream":
        type_text(f"You flop back, {wizard.name}, gazing at the water-stained ceiling, your mind conjuring castles of stone and dragons with wings that blot out the sun.", "white")
    elif choice == "read":
        type_text("You delve deeper into the comic, its tales of heroes and hidden realms a fleeting escape from the dull grey of your reality.", "white")
    else:
        type_text("You slip outside, the overgrown garden a tangle of weeds—nothing stirs, yet the air hums with a strange, unspoken promise.", "white")
    type_text("As twilight drapes the sky in bruised purples, a faint rustle at your window breaks the stillness—something extraordinary approaches.", "white")

    # Chapter 2: The Owl’s Mysterious Gift
    type_text("\nChapter 2: The Owl’s Mysterious Gift", "yellow")
    type_text("Rain hammers your bedroom window that night, a ceaseless tattoo against the glass, thunder growling like a beast in the distance.", "white")
    type_text(f"You’re half-dozing, {wizard.name}, cocooned in a thin blanket, the room bathed in the streetlamp’s flickering glow, when a sharp *tap-tap-tap* snaps you awake.", "white")
    type_text("An owl clings to the sill, its feathers sodden, amber eyes gleaming through the storm—a letter swings from its beak, sealed with crimson wax bearing an ornate ‘H.’", "white")
    type_text("Your pulse quickens as you unlatch the window—a blast of cold, wet air sweeps in, scattering your comics as the owl drops its burden and vanishes into the tempest.", "white")
    type_text(f"The parchment crackles in your hands, {wizard.name}, emerald ink shimmering: ‘Dear {wizard.name}, We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.’", "green")
    choice = get_choice(["shout", "read", "hide"], "How do you greet this wondrous news?", wizard)
    if choice == "shout":
        type_text(f"‘Mum! Dad!’ you cry, {wizard.name}, tumbling downstairs in a tangle of blanket, clutching the letter as if it might vanish.", "green")
        type_text("Your parents freeze—‘A wizard?’ your dad chokes, teacup clattering, while your mum envelops you in a bewildered, joyful hug.", "green")
        wizard.align_with_good()
    elif choice == "read":
        type_text(f"You perch on your bed, {wizard.name}, tracing each word—‘Hogwarts… magic…’—a thrill blooming as reality shifts beneath you.", "white")
    else:
        type_text(f"You slip the letter under your pillow, {wizard.name}, heart racing—‘Not yet,’ you murmur, a secret too vast to share.", "white")
    type_text("Sleep flees as your mind dances with visions of cloaked figures and enchanted halls—a new world beckons.", "white")

    # Chapter 3: A Family’s Bewilderment
    type_text("\nChapter 3: A Family’s Bewilderment", "yellow")
    type_text("Dawn breaks grey and humid, the air heavy with last night’s rain—your parents sit at the kitchen table, the letter unfurled between them like a relic.", "white")
    type_text(f"‘Diagon Alley, London,’ your mum reads, voice quivering with awe, while your dad adjusts his glasses—‘Never heard of it!’", "white")
    type_text("A stern owl swoops in mid-breakfast, dropping a second note—‘The Leaky Cauldron,’ it instructs, listing robes, books, a wand—your parents exchange wide-eyed glances.", "white")
    type_text("‘We’ll drive,’ your dad declares, voice firm despite his confusion—‘Can’t have owls sorting our lives!’—your mum nods, clutching the Galleons.", "white")
    type_text(f"You’re ushered to the car, {wizard.name}, the sack of coins clinking—‘What’s happening?’ your dad mutters, the engine sputtering to life.", "white")
    choice = get_choice(["explain", "silence"], "Address their confusion?", wizard)
    if choice == "explain":
        type_text("‘It’s magic school!’ you say—‘Magic?’ your mum echoes, half-laughing, half-dazed.", "white")
    else:
        type_text("You stay quiet—‘He’s in a mood,’ your dad grumbles, driving on.", "white")
    type_text("London looms ahead—your world teeters on the brink of the unknown.", "white")

    # Chapter 4: The Leaky Cauldron’s Veil
    type_text("\nChapter 4: The Leaky Cauldron’s Veil", "yellow")
    type_text("London pulses with Muggle clamor—horns blare, pigeons scatter—but the Leaky Cauldron crouches in a shadowed alley, its sign swaying unnoticed by the crowds.", "white")
    type_text(f"You step from the car, {wizard.name}, your parents trailing—‘This it?’ your dad frowns as you push the oak door, revealing a smoky, bustling inn.", "white")
    type_text("Tom, the toothless innkeeper, grins—‘First time, eh? Back way!’—witches in pointed hats sip ale, wizards mutter over parchment.", "white")
    type_text("He leads you to a brick wall—*tap-tap-tap*—it groans, parting to unveil Diagon Alley, a riot of color and sound.", "white")
    type_text(f"Your jaw drops, {wizard.name}—‘Blimey!’ your dad gasps, your mum clutching his arm.", "white")
    choice = get_choice(["marvel", "rush"], "Enter this new realm?", wizard)
    if choice == "marvel":
        type_text("‘It’s… alive!’—you breathe, drinking in the chaos.", "white")
    else:
        type_text("You rush—‘Let’s go!’—eager to dive in.", "white")
    type_text("Cobblestones hum beneath your feet—magic unfurls like a dream.", "white")

    # Chapter 5: Gringotts’ Gilded Secrets
    type_text("\nChapter 5: Gringotts’ Gilded Secrets", "yellow")
    type_text("Gringotts towers over Diagon Alley, its marble facade a gleaming fortress, goblins with claw-like hands guarding its secrets.", "white")
    type_text(f"You enter, {wizard.name}, the hall echoing—goblins scribble, eyeing you as you slide a golden key—‘Vault 687,’—to Griphook.", "white")
    type_text("‘This way,’ he growls—a cart rockets you down twisting tracks, torches flaring past vaults of gold and dust.", "white")
    type_text("Your vault opens—Galleons cascade, a treasure trove—‘Whose?’ you wonder.", "white")
    choice = get_choice(["grab", "count", "ask"], "Claim your fortune?", wizard)
    if choice == "grab":
        type_text(f"You scoop coins, {wizard.name}—‘Loads!’—their weight thrilling.", "white")
    elif choice == "count":
        type_text("‘Just enough,’—you tally, calm amid the gleam.", "green")
        wizard.align_with_good()
    else:
        type_text("‘Whose gold?’—‘Yours now,’ Griphook snaps.", "white")
    type_text("The cart ascends—your pockets sing with magic’s wealth.", "white")

    # Chapter 6: Ollivanders’ Whispering Wands
    type_text("\nChapter 6: Ollivanders’ Whispering Wands", "yellow")
    type_text("Diagon Alley thrums—potions bubble, brooms hover—but Ollivanders’ sits hushed, its windows clouded with age.", "white")
    type_text(f"You enter, {wizard.name}, a bell tinkling—Ollivander emerges—‘{wizard.name}, at last,’—his silver eyes gleam.", "white")
    type_text("‘Holly, phoenix feather,’—you wave, sparks shower—‘Curious!’—he hands it over.", "cyan")
    wizard.modify_house_points(5)
    choice = get_choice(["thank", "test", "ask"], "Embrace your wand?", wizard)
    if choice == "thank":
        type_text("‘Thank you,’—‘Well chosen,’ he smiles.", "green")
        wizard.align_with_good()
    elif choice == "test":
        type_text("You flick—sparks dance!", "white")
    else:
        type_text("‘Why me?’—‘It chose you,’ he murmurs.", "white")
    type_text("You leave, wand alive in your grip.", "white")

    # Chapter 7: The Menagerie’s Call
    type_text("\nChapter 7: The Menagerie’s Call", "yellow")
    type_text("The Magical Menagerie buzzes—owls hoot, cats purr, toads croak.", "white")
    type_text(f"You step in, {wizard.name},—‘Pet?’—the shopkeep grunts.", "white")
    choice = get_choice(["owl", "cat", "toad", "none"], "Choose a friend?", wizard)
    if choice == "owl":
        type_text("‘Shadow,’—it hoots—‘Wise,’ the shopkeep nods.", "green")
        wizard.inventory.append("Owl: Shadow")
    elif choice == "cat":
        type_text("‘Midnight,’—it purrs—‘Sly,’ he says.", "white")
        wizard.inventory.append("Cat: Midnight")
    elif choice == "toad":
        type_text("‘Hopper,’—it croaks—‘Steady,’ he grunts.", "white")
        wizard.inventory.append("Toad: Hopper")
    else:
        type_text("‘No thanks,’—‘Suit yerself,’ he shrugs.", "white")
    type_text("You exit, supplies in tow—magic hums.", "white")

    # Chapter 8: Platform 9¾
    type_text("\nChapter 8: Platform 9¾", "yellow")
    type_text("September 1st—King’s Cross teems—‘9¾!’—you spot red hair vanish.", "white")
    type_text(f"You push, {wizard.name},—stone parts, the Express gleams!", "white")
    choice = get_choice(["board", "watch"], "Step aboard?", wizard)
    if choice == "board":
        type_text("You climb—‘Here we go!’—velvet seats await.", "white")
    else:
        type_text("You watch—‘Magic!’—owls flutter.", "white")
    type_text("The whistle blows—Hogwarts calls!", "white")

    # Chapter 9: Train Companions
    type_text("\nChapter 9: Train Companions", "yellow")
    type_text("Fields blur—‘Sweets?’—the trolley witch offers.", "white")
    type_text(f"‘{wizard.name}!’—Ron and Hermione enter!", "white")
    choice = get_choice(["welcome", "refuse"], "Friends?", wizard)
    if choice == "welcome":
        type_text("‘Sure!’—Ron chats, Hermione lectures—friends!", "green")
        wizard.align_with_good()
    else:
        type_text("‘No,’—‘Odd,’ Ron says, leaving.", "white")
    type_text("Hogwarts nears—towers rise!", "white")

    # Chapter 10: The Sorting Hat
    type_text("\nChapter 10: The Sorting Hat", "yellow")
    type_text("Boats glide—‘Hagrid!’—the castle glows.", "white")
    type_text(f"‘{wizard.name}!’—McGonagall calls, hat on—‘Where?’ it asks.", "white")
    choice = get_choice(["valor", "ambition", "wisdom", "kindness"], "Your heart?", wizard)
    houses = {"valor": "Gryffindor", "ambition": "Slytherin", "wisdom": "Ravenclaw", "kindness": "Hufflepuff"}
    wizard.house = houses[choice]
    type_text(f"‘{wizard.house}!’—cheers erupt!", "green")
    wizard.modify_house_points(10)

    # Chapter 11: First Lessons
    type_text("\nChapter 11: First Lessons", "yellow")
    type_text(f"{wizard.house} dorm—‘Potions!’—Snape looms.", "white")
    choice = get_choice(["brew", "cheat"], "Potion?", wizard)
    if choice == "brew":
        type_text("‘Gold!’—‘Passable,’ Snape sneers.", "cyan")
        wizard.inventory.append("Healing Potion")
        wizard.advance_skill("potions")
    else:
        type_text("‘Steal!’—‘Points!’—Snape snaps.", "red")
        wizard.modify_house_points(-5)
    type_text("‘Next!’—you flee the chill.", "white")

    # Chapter 12: Troll’s Chaos
    type_text("\nChapter 12: Troll’s Chaos", "yellow")
    type_text("‘Troll!’—Quirrell gasps—‘Hermione!’—Harry runs!", "white")
    choice = get_choice(["help", "flee"], "Save her?", wizard)
    if choice == "help":
        type_text("‘Go!’—you dash!", "white")
        enemy = Enemy("Mountain Troll", 100, 25)
        while enemy.is_alive() and wizard.is_alive():
            type_text(f"\n{wizard.name}: {wizard.health} | Troll: {enemy.health}", "white")
            choice = get_choice(["attack", "use spell"], "Fight!", wizard)
            if choice == "attack":
                type_text(f"{wizard.name} swings!", "white")
                enemy.take_damage(10)
            else:
                spell = get_choice(wizard.spells_known, "Cast?", wizard)
                wizard.use_magic(spell, enemy, "troll")
            if enemy.is_alive():
                enemy.use_ability(wizard)
        if wizard.is_alive():
            type_text("‘Saved!’—points soar!", "green")
            wizard.modify_house_points(20)
    else:
        type_text("‘Run!’—guilt!", "white")

def year_2(wizard):
    type_text("\n=== Year 2: Chamber of Secrets ===", "yellow")

    # Chapter 1: Summer’s Stagnation
    type_text("\nChapter 1: Summer’s Stagnation", "yellow")
    type_text("Summer smothers your Muggle town in a thick, sticky haze—heat ripples off the pavement, and flies buzz against your window, trapped in the stagnant air.", "white")
    type_text(f"You’re twelve, {wizard.name}, sprawled across your bed, a fan whirring uselessly as sweat beads on your brow—Hogwarts feels like a distant dream.", "white")
    type_text("Shadow delivers letters—‘Wish you were here!’ Hermione writes, ‘Pranks!’ Ron scrawls—but the magic fades under this oppressive sun.", "white")
    choice = get_choice(["reply", "ignore"], "Break the monotony?", wizard)
    if choice == "reply":
        type_text(f"‘Miss you!’—Shadow soars!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Too hot,’—you toss them aside.", "white")
    type_text("Days blur—magic dims.", "white")

    # Chapter 2: Dobby’s Plea
    type_text("\nChapter 2: Dobby’s Plea", "yellow")
    type_text("A *pop*—Dobby trembles—‘{wizard.name} mustn’t go!’—his eyes glisten.", "white")
    choice = get_choice(["listen", "shoo"], "Hear him?", wizard)
    if choice == "listen":
        type_text("‘Chamber!’—he whispers, vanishing.", "white")
    else:
        type_text("‘Out!’—pudding crashes!", "red")
        wizard.align_with_dark()
    type_text("‘What!’—chaos downstairs!", "white")

    # Chapter 3: The Flying Escape
    type_text("\nChapter 3: The Flying Escape", "yellow")
    type_text("A car hovers—‘Ron!’—‘In!’", "white")
    choice = get_choice(["join", "stay"], "Fly?", wizard)
    if choice == "join":
        type_text("‘Up!’—stars blur!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Wait,’—they go!", "white")
        return
    type_text("‘Freedom!’—night soars!", "white")

    # Chapter 4: The Burrow
    type_text("\nChapter 4: The Burrow", "yellow")
    type_text("‘Home!’—Mrs. Weasley hugs!", "white")
    choice = get_choice(["eat", "help"], "Settle?", wizard)
    if choice == "eat":
        type_text("‘Tart!’—sweet!", "white")
    else:
        type_text("‘Sweep!’—‘Thanks!’", "green")
        wizard.align_with_good()
    type_text("‘School!’—Ron beams!", "white")

    # Chapter 5: Barrier Trouble
    type_text("\nChapter 5: Barrier Trouble", "yellow")
    type_text("‘Blocked!’—‘Fly!’—car hums!", "white")
    choice = get_choice(["fly", "wait"], "Go?", wizard)
    if choice == "fly":
        type_text("‘Up!’—Willow looms!", "white")
    else:
        type_text("‘Missed!’—stranded!", "white")
        return
    type_text("‘Crash!’—branches thrash!", "white")

    # Chapter 6: Willow’s Wrath
    type_text("\nChapter 6: Willow’s Wrath", "yellow")
    type_text("‘Out!’—Willow slams!", "white")
    choice = get_choice(["blast", "run"], "Escape?", wizard)
    if choice == "blast":
        type_text("‘Stupefy!’—free!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Run!’—Snape!", "red")
    type_text("‘Detention!’—back!", "white")

    # Chapter 7: Lockhart’s Swagger
    type_text("\nChapter 7: Lockhart’s Swagger", "yellow")
    type_text("‘Me!’—Lockhart preens!", "white")
    choice = get_choice(["admire", "doubt"], "Trust?", wizard)
    if choice == "admire":
        type_text("‘Famous!’—clap!", "white")
    else:
        type_text("‘Fraud!’—doubt!", "white")
    type_text("‘Pixies!’—chaos!", "white")

    # Chapter 8: Petrified Omen
    type_text("\nChapter 8: Petrified Omen", "yellow")
    type_text("‘Mrs. Norris!’—‘Chamber!’", "white")
    choice = get_choice(["search", "report"], "Act?", wizard)
    if choice == "search":
        type_text("‘Hiss!’—chill!", "cyan")
        wizard.advance_skill("herbology")
    else:
        type_text("‘Tell!’—‘Safe!’", "green")
    type_text("‘Fear!’—whispers!", "white")

    # Chapter 9: Pixie Fiasco
    type_text("\nChapter 9: Pixie Fiasco", "yellow")
    type_text("‘Pixies!’—Lockhart flails!", "white")
    choice = get_choice(["catch", "hide"], "Chaos?", wizard)
    if choice == "catch":
        type_text("‘Stupefy!’—nab!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Duck!’—Hermione!", "white")
    type_text("‘Out!’—wreck!", "white")

    # Chapter 10: Dueling Drama
    type_text("\nChapter 10: Dueling Drama", "yellow")
    type_text("‘Duel!’—Snape smirks!", "white")
    choice = get_choice(["duel", "watch"], "Step?", wizard)
    if choice == "duel":
        type_text("‘Stupefy!’—Draco trips!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Snake!’—Harry hisses!", "white")
    type_text("‘End!’—whispers!", "white")

    # Chapter 11: Riddle’s Voice
    type_text("\nChapter 11: Riddle’s Voice", "yellow")
    type_text("‘Tom!’—diary speaks!", "white")
    choice = get_choice(["write", "burn"], "Use?", wizard)
    if choice == "write":
        type_text("‘Who?’—‘Riddle!’", "white")
    else:
        type_text("‘Burn!’—sizzle!", "green")
        wizard.align_with_good()
    type_text("‘Creepy!’—dread!", "white")

    # Chapter 12: Chamber’s Depths
    type_text("\nChapter 12: Chamber’s Depths", "yellow")
    type_text("‘Ginny!’—‘Down!’", "white")
    enemy = Enemy("Basilisk", 150, 30, "shadow")
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Basilisk: {enemy.health}", "white")
        choice = get_choice(["attack", "use spell"], "Fight!", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} slashes!", "white")
            enemy.take_damage(10)
        else:
            spell = get_choice(wizard.spells_known, "Cast?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
    if wizard.is_alive():
        type_text("‘Fawkes!’—‘Saved!’", "green")
        wizard.modify_house_points(30)

def year_3(wizard):
    type_text("\n=== Year 3: Prisoner of Azkaban ===", "yellow")

    # Chapter 1: Summer’s Heavy Veil
    type_text("\nChapter 1: Summer’s Heavy Veil", "yellow")
    type_text("Summer drapes your Muggle town in a suffocating veil—humid air clings like a second skin, and the streets lie still under a hazy sun that offers no mercy.", "white")
    type_text(f"You’re thirteen, {wizard.name}, stretched across your bed in a room that shrinks with each passing day, your Hogwarts trunk a dusty relic in the corner.", "white")
    type_text("Memories of trolls and serpents flicker like distant embers, but here, the world is a dull hum—the lawnmower’s drone, the telly’s faint chatter from below.", "white")
    type_text("Your parents whisper—‘He’s odd lately,’ your dad mutters over his newspaper—unaware of the magic pulsing beneath your restless surface.", "white")
    choice = get_choice(["reflect", "pack", "write"], "Endure the stillness?", wizard)
    if choice == "reflect":
        type_text(f"You lie back, {wizard.name}, staring at the ceiling—‘Hogwarts,’—a beacon in the haze.", "white")
    elif choice == "pack":
        type_text("You sift through your trunk—‘Wand, robes…’—yearning for escape.", "white")
    else:
        type_text("‘Ron!’—you scribble—Shadow waits to fly.", "green")
        wizard.align_with_good()
    type_text("‘Soon,’—the promise holds you steady.", "white")

    # Chapter 2: Aunt Marge’s Bluster
    type_text("\nChapter 2: Aunt Marge’s Bluster", "yellow")
    type_text("August creeps—Aunt Marge arrives, her bulldogs snuffling as she barges in—‘Boy!’—her voice a bellow.", "white")
    type_text(f"‘Dinner, {wizard.name}!’—she jabs, wine sloshing—‘Your parents, layabouts!’—rage simmers.", "white")
    choice = get_choice(["snap", "stay"], "Face her?", wizard)
    if choice == "snap":
        type_text("‘Wizard!’—she bloats, floating—‘What!’—chaos!", "red")
        wizard.align_with_dark()
    else:
        type_text("‘Calm,’—you grit, enduring.", "green")
        wizard.align_with_good()
    type_text("‘Trouble!’—magic flares!", "white")

    # Chapter 3: The Knight Bus
    type_text("\nChapter 3: The Knight Bus", "yellow")
    type_text("‘Run!’—trunk drags, a bus screeches—‘Stan!’—‘Where?’—‘Anywhere!’", "white")
    choice = get_choice(["board", "walk"], "Ride?", wizard)
    if choice == "board":
        type_text("‘Lurch!’—‘Leaky!’", "white")
    else:
        type_text("‘Trudge!’—Fudge!", "white")
        return
    type_text("‘Sirius!’—Stan hisses!", "white")

    # Chapter 4: Leaky Refuge
    type_text("\nChapter 4: Leaky Refuge", "yellow")
    type_text("‘Tom!’—‘Stay!’—Fudge nods!", "white")
    choice = get_choice(["rest", "snoop"], "Settle?", wizard)
    if choice == "rest":
        type_text("‘Bed!’—creak!", "white")
    else:
        type_text("‘Whispers!’—magic!", "white")
    type_text("‘Black!’—Fudge warns!", "white")

    # Chapter 5: Diagon Reunions
    type_text("\nChapter 5: Diagon Reunions", "yellow")
    type_text("‘Ron! Hermione!’—‘Flying?’—‘Reckless!’", "white")
    choice = get_choice(["shop", "chat"], "Day?", wizard)
    if choice == "shop":
        type_text("‘Books!’—Blotts!", "white")
    else:
        type_text("‘Black?’—whispers!", "white")
    type_text("‘School!’—buzz!", "white")

    # Chapter 6: Dementors’ Chill
    type_text("\nChapter 6: Dementors’ Chill", "yellow")
    type_text("‘Frost!’—Dementors!", "white")
    choice = get_choice(["fight", "faint"], "Face?", wizard)
    if choice == "fight":
        type_text("‘Resist!’—Lupin!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Dark!’—‘Chocolate!’", "white")
    type_text("‘Sirius!’—Lupin!", "white")

    # Chapter 7: Boggart’s Jest
    type_text("\nChapter 7: Boggart’s Jest", "yellow")
    type_text("‘Boggarts!’—Lupin!", "white")
    choice = get_choice(["face", "watch"], "Fear?", wizard)
    if choice == "face":
        type_text("‘Riddikulus!’—laugh!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Neville!’—lace!", "white")

    # Chapter 8: Divination’s Doom
    type_text("\nChapter 8: Divination’s Doom", "yellow")
    type_text("‘Death!’—Trelawney!", "white")
    choice = get_choice(["believe", "scoff"], "Fate?", wizard)
    if choice == "believe":
        type_text("‘Maybe…’—omens!", "white")
        wizard.advance_skill("divination")
    else:
        type_text("‘Rubbish!’—Ron!", "white")

    # Chapter 9: Buckbeak’s Wings
    type_text("\nChapter 9: Buckbeak’s Wings", "yellow")
    type_text("‘Bow!’—Hagrid!", "white")
    choice = get_choice(["bow", "stare"], "Greet?", wizard)
    if choice == "bow":
        type_text("‘Fly!’—soar!", "green")
        wizard.modify_house_points(10)
    else:
        type_text("‘Ow!’—claws!", "red")
        wizard.take_damage(10)

    # Chapter 10: Stormy Quidditch
    type_text("\nChapter 10: Stormy Quidditch", "yellow")
    type_text("‘Rain!’—Dementors!", "white")
    choice = get_choice(["cheer", "help"], "Game?", wizard)
    if choice == "cheer":
        type_text("‘{wizard.house}!’—go!", "green")
        wizard.modify_house_points(5)
    else:
        type_text("‘Harry!’—Lupin!", "white")

    # Chapter 11: Sirius’s Shadow
    type_text("\nChapter 11: Sirius’s Shadow", "yellow")
    type_text("‘Slash!’—Fat Lady!", "white")
    choice = get_choice(["search", "guard"], "Hunt?", wizard)
    if choice == "search":
        type_text("‘Clues!’—marks!", "white")
    else:
        type_text("‘Guard!’—tense!", "white")

    # Chapter 12: Patronus Light
    type_text("\nChapter 12: Patronus Light", "yellow")
    type_text("‘Expecto!’—Lupin!", "white")
    choice = get_choice(["try", "pass"], "Cast?", wizard)
    if choice == "try":
        type_text("‘Wisp!’—shine!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Later!’—fear!", "white")

    # Chapter 13: Shack’s Truth
    type_text("\nChapter 13: Shack’s Truth", "yellow")
    type_text("‘Innocent!’—Sirius!", "white")
    choice = get_choice(["trust", "doubt"], "Believe?", wizard)
    if choice == "trust":
        type_text("‘Right!’—stand!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Prove!’—tension!", "white")

    # Chapter 14: Time’s Turn
    type_text("\nChapter 14: Time’s Turn", "yellow")
    type_text("‘Twist!’—Hermione!", "white")
    choice = get_choice(["buckbeak", "sirius"], "Save?", wizard)
    if choice == "buckbeak":
        type_text("‘Fly!’—free!", "green")
        wizard.modify_house_points(10)
    else:
        type_text("‘Run!’—Sirius!", "green")
        wizard.modify_house_points(10)
    type_text("‘Stag!’—Dementors flee!", "cyan")
    wizard.modify_house_points(20)

def year_4(wizard):
    type_text("\n=== Year 4: Goblet of Fire ===", "yellow")

    # Chapter 1: The Quidditch World Cup’s Roar
    type_text("\nChapter 1: The Quidditch World Cup’s Roar", "yellow")
    type_text("Summer bursts into a cacophony of life—‘Quidditch World Cup!’ Mr. Weasley exclaims, his eyes alight as he unveils a battered old boot pulsing with hidden magic.", "white")
    type_text(f"‘Hold tight, {wizard.name}!’—the Portkey whirls you into a sprawling campsite, tents shimmering under a sky alive with the thunder of brooms and the roar of thousands.", "white")
    type_text("‘Ireland versus Bulgaria!’ Ron bellows over the din—Krum dives, a streak of shadow, as emerald-clad chasers weave through the air like emerald flames.", "white")
    type_text("The crowd surges—‘Don’t wander!’ Mrs. Weasley shouts, her voice swallowed by the cheers as banners snap in the wind.", "white")
    choice = get_choice(["cheer", "watch", "explore"], "Dive into the World Cup’s frenzy?", wizard)
    if choice == "cheer":
        type_text(f"‘Krum!’ you shout, {wizard.name}, voice raw as he snatches the Snitch in a breathtaking plunge—‘Legend!’—the stands quake with applause!", "green")
        wizard.modify_house_points(5)
    elif choice == "watch":
        type_text("You perch on a rickety bench—‘They’re like birds!’—marveling at the players’ grace, a symphony of speed and skill.", "white")
    else:
        type_text("You slip through the tents—‘Wands for sale!’ vendors call—until a chilling ‘Dark Mark!’ splits the sky, green and serpentine!", "white")
    type_text("A skull blazes above—‘Run!’—panic erupts as dark magic stains the night!", "white")

    # Chapter 2: Whispers on the Hogwarts Express
    type_text("\nChapter 2: Whispers on the Hogwarts Express", "yellow")
    type_text("The Hogwarts Express chugs through rolling fields, steam curling like dragon’s breath as the familiar scarlet engine hums beneath your feet.", "white")
    type_text(f"‘Back again!’ Ron sprawls across the seat, grinning—‘Triwizard Tournament!’ Hermione announces, her nose buried in a tome, {wizard.name}.", "white")
    type_text("‘Foreign schools, champions!’ Neville chimes in, wide-eyed—rumors ripple through the compartment like wildfire.", "white")
    type_text("The trolley witch trundles by—‘Anything sweet?’—her cart groans with treats as the landscape shifts to misty hills.", "white")
    choice = get_choice(["speculate", "relax", "buy"], "Prepare for the year ahead?", wizard)
    if choice == "speculate":
        type_text("‘Dangerous, you reckon?’ you ask—‘Thrilling!’ Ron counters, eyes gleaming.", "white")
    elif choice == "relax":
        type_text("You lean back—‘Rest now,’—savoring the gentle sway of the train.", "white")
    else:
        type_text("‘Chocolate Frog!’—you snag one, Dumbledore’s card winking—‘Nice!’", "green")
        wizard.modify_house_points(5)
    type_text("Hogwarts looms closer—‘Home!’—its towers pierce the dusk like sentinels.", "white")

    # Chapter 3: The Arrival of Rivals
    type_text("\nChapter 3: The Arrival of Rivals", "yellow")
    type_text("The Great Hall glows with candlelight—‘Welcome!’ Dumbledore’s voice rings as Beauxbatons sweep in, silken robes flowing like water, led by the ethereal Fleur Delacour.", "white")
    type_text(f"Durmstrang follows, {wizard.name}, their heavy boots thudding—Viktor Krum strides among them—‘Blimey!’ Ron gasps, starstruck.", "white")
    type_text("‘The Triwizard Tournament!’ Dumbledore proclaims—‘A test of courage and skill!’—the hall erupts in cheers.", "white")
    type_text("The Goblet of Fire flickers blue—‘Eternal glory awaits!’—his words spark a fire in the air.", "white")
    choice = get_choice(["excite", "worry", "doubt"], "Feel the tournament’s pull?", wizard)
    if choice == "excite":
        type_text("‘This’ll be brilliant!’—you clap, swept up in the thrill.", "green")
        wizard.align_with_good()
    elif choice == "worry":
        type_text("‘Sounds risky,’—you murmur, unease prickling.", "white")
    else:
        type_text("‘All show,’—you scoff, skeptical.", "white")
    type_text("‘Champions!’—the hall holds its breath!", "white")

    # Chapter 4: The Goblet’s Unexpected Choice
    type_text("\nChapter 4: The Goblet’s Unexpected Choice", "yellow")
    type_text("The Goblet’s flames dance—‘Fleur Delacour!’—cheers—‘Viktor Krum!’—roars—‘Cedric Diggory!’—Hufflepuff explodes!", "white")
    type_text(f"Then—‘{wizard.name}!’—the hall falls silent, a gasp—‘What!’ Harry chokes, eyes wide as every head turns.", "white")
    type_text("‘A fourth?’—Dumbledore’s voice is steel—‘Impossible!’ Snape snarls.", "white")
    choice = get_choice(["accept", "protest", "freeze"], "Answer the Goblet’s call?", wizard)
    if choice == "accept":
        type_text("‘I’ll compete!’—you stand, cheers and boos clashing!", "green")
        wizard.align_with_good()
    elif choice == "protest":
        type_text("‘I didn’t enter!’—your shout is drowned by murmurs!", "white")
    else:
        type_text("You freeze—‘How?’—stares pierce!", "white")
    type_text("‘To the champions’ room!’—Dumbledore commands!", "white")

    # Chapter 5: The Dragon’s Fiery Trial
    type_text("\nChapter 5: The Dragon’s Fiery Trial", "yellow")
    type_text("The first task dawns—‘Dragons!’—a Hungarian Horntail roars, its scales glinting, guarding a golden egg as flames sear the air.", "white")
    type_text(f"‘{wizard.name}, your turn!’—the crowd holds its breath, the beast’s eyes locking onto you.", "white")
    type_text("‘Get the egg!’—Bagman’s voice booms—‘Now!’", "white")
    choice = get_choice(["fly", "transfigure", "distract"], "Face the dragon?", wizard)
    if choice == "fly":
        type_text("‘Accio broom!’—you soar, dodging fire—‘Got it!’—the egg’s yours!", "cyan")
        wizard.advance_skill("charms")
    elif choice == "transfigure":
        type_text("‘Rocks to dogs!’—they bark, distracting—‘Mine!’—you snatch!", "cyan")
        wizard.advance_skill("transfiguration")
    else:
        type_text("‘Stupefy!’—it staggers—‘Run!’—egg secured!", "cyan")
        wizard.advance_skill("defense")
    type_text("‘Alive!’—the stands thunder with relief!", "white")

    # Chapter 6: The Yule Ball’s Elegance
    type_text("\nChapter 6: The Yule Ball’s Elegance", "yellow")
    type_text("Winter cloaks Hogwarts—‘Yule Ball!’—the castle sparkles, snow dusting the turrets as whispers of dresses and dates fill the halls.", "white")
    type_text(f"‘{wizard.name}, got a partner?’ Ron frets, red-faced—‘Need one!’—panic edges his voice.", "white")
    type_text("The Great Hall transforms—icicles gleam, music swells!", "white")
    choice = get_choice(["invite", "solo", "help"], "Prepare for the ball?", wizard)
    if choice == "invite":
        type_text("‘Parvati, dance?’—‘Yes!’—she beams, relief washing over!", "green")
        wizard.modify_house_points(10)
    elif choice == "solo":
        type_text("‘I’ll go alone,’—you shrug, content.", "white")
    else:
        type_text("‘Ron, ask her!’—you nudge—‘Thanks!’—he stammers.", "green")
        wizard.align_with_good()
    type_text("‘Dance!’—the night glitters!", "white")

    # Chapter 7: Secrets of the Egg
    type_text("\nChapter 7: Secrets of the Egg", "yellow")
    type_text("‘The egg!’—you turn it, a screech—‘What!’—Harry winces.", "white")
    type_text(f"‘{wizard.name}, clues!’—Hermione insists—‘Second task!’", "white")
    choice = get_choice(["bathe", "study"], "Unlock it?", wizard)
    if choice == "bathe":
        type_text("‘Bath!’—water reveals—‘Mermaids!’", "cyan")
        wizard.advance_skill("charms")
    else:
        type_text("‘Books!’—‘Songs?’—close!", "white")
    type_text("‘Lake!’—the next looms!", "white")

    # Chapter 8: The Black Lake’s Depths
    type_text("\nChapter 8: The Black Lake’s Depths", "yellow")
    type_text("‘Second task!’—the Black Lake shimmers—‘Ron!’—he’s below!", "white")
    type_text(f"‘{wizard.name}, dive!’—the whistle shrieks!", "white")
    choice = get_choice(["bubble", "gillyweed"], "Rescue him?", wizard)
    if choice == "bubble":
        type_text("‘Bubble-Head!’—you plunge—‘Free!’", "cyan")
        wizard.advance_skill("charms")
    else:
        type_text("‘Gillyweed!’—webs grow—‘Got him!’", "cyan")
        wizard.advance_skill("herbology")
    type_text("‘Saved!’—cheers resound!", "white")

    # Chapter 9: The Maze’s Treachery
    type_text("\nChapter 9: The Maze’s Treachery", "yellow")
    type_text("‘Third task!’—hedges twist, a labyrinth—‘Sphinx!’—riddles hiss!", "white")
    type_text(f"‘{wizard.name}, solve!’—it stares!", "white")
    choice = get_choice(["solve", "blast", "trick"], "Pass the maze?", wizard)
    if choice == "solve":
        type_text("‘East!’—path clears!", "cyan")
        wizard.advance_skill("transfiguration")
    elif choice == "blast":
        type_text("‘Stupefy!’—vines part!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Feint!’—slip by!", "white")
    type_text("‘Cup!’—it nears!", "white")

    # Chapter 10: The Graveyard’s Horror
    type_text("\nChapter 10: The Graveyard’s Horror", "yellow")
    type_text("‘Cup!’—a Portkey—‘Cedric!’—he falls, Voldemort rises!", "white")
    type_text(f"‘{wizard.name}, duel!’—his wand glows!", "white")
    enemy = Enemy("Voldemort", 150, 30, "shadow")
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Voldemort: {enemy.health}", "white")
        choice = get_choice(["attack", "defend", "use spell"], "Survive the Dark Lord?", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} lunges—‘Take that!’—sparks fly!", "white")
            enemy.take_damage(10)
        elif choice == "defend":
            wizard.use_magic("protego")
            type_text("‘Shield holds!’—green light rebounds!", "cyan")
        elif choice == "use spell":
            spell = get_choice(wizard.spells_known, "Which spell?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
            type_text("‘Avada!’—you dodge!", "red")
    if wizard.is_alive():
        type_text("‘Priori Incantatem!’—‘Flee!’—ghosts aid!", "green")
        wizard.modify_house_points(30)
        type_text("‘He’s back!’—you gasp, trembling!", "white")
    else:
        type_text("‘No!’—darkness claims!", "red")

    # Chapter 11: Mourning and Resolve
    type_text("\nChapter 11: Mourning and Resolve", "yellow")
    type_text("Hogwarts mourns—‘Cedric…’—silence cloaks the hall.", "white")
    type_text(f"‘{wizard.name}, he’s back,’—Dumbledore’s voice is grave—‘War looms!’", "white")
    choice = get_choice(["grieve", "resolve", "rage"], "Face the aftermath?", wizard)
    if choice == "grieve":
        type_text("‘Gone…’—tears fall, heavy!", "white")
    elif choice == "resolve":
        type_text("‘We fight!’—fire ignites!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Curse him!’—anger burns!", "red")
        wizard.align_with_dark()
    type_text("‘Prepare!’—the world shifts!", "white")

def year_5(wizard):
    type_text("\n=== Year 5: Order of the Phoenix ===", "yellow")

    # Chapter 1: Shadows of Doubt
    type_text("\nChapter 1: Shadows of Doubt", "yellow")
    type_text("Summer cloaks your Muggle town in a oppressive stillness—humid air presses against your skin, and the world feels smaller, tighter, after Voldemort’s return.", "white")
    type_text(f"You’re fifteen, {wizard.name}, pacing your room—your trunk lies ready, but dread gnaws at you, whispers of the Dark Lord’s shadow lingering from the graveyard.", "white")
    type_text("The Daily Prophet screeches lies—‘Potter delusional!’—your name smeared alongside Harry’s, the Ministry’s denial a bitter pill.", "white")
    type_text("Downstairs, your parents mutter—‘He’s brooding again,’ your dad sighs—unaware of the war brewing beyond their quiet lives.", "white")
    choice = get_choice(["write", "brood", "prepare"], "Face the uncertain dawn?", wizard)
    if choice == "write":
        type_text(f"‘Harry,’ you pen—‘Truth?’—Shadow flutters off, a lifeline to allies.", "green")
        wizard.align_with_good()
    elif choice == "brood":
        type_text("‘Lies,’—you pace, anger simmering in the silence.", "white")
    else:
        type_text("‘Wand ready,’—you check spells, steeling yourself.", "white")
    type_text("The air hums—‘Something’s coming,’ you sense.", "white")

    # Chapter 2: Dementors in the Alley
    type_text("\nChapter 2: Dementors in the Alley", "yellow")
    type_text("Night falls—‘Out!’—you storm from the house, the weight of lies too much, wandering alleys until frost bites the air.", "white")
    type_text(f"‘Dementors!’—two glide toward you, {wizard.name}, cloaks billowing—cold seeps, despair claws!", "white")
    type_text("‘Help!’—a neighbor screams—‘Now!’", "white")
    choice = get_choice(["fight", "flee"], "Confront the darkness?", wizard)
    if choice == "fight":
        type_text("‘Expecto Patronum!’—a wisp flares—‘Away!’—they retreat!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Run!’—you stumble—‘Dudley?’—Harry saves!", "white")
    type_text("‘Ministry!’—owls loom!", "white")

    # Chapter 3: Grimmauld’s Sanctuary
    type_text("\nChapter 3: Grimmauld’s Sanctuary", "yellow")
    type_text("‘Order!’—you’re whisked to 12 Grimmauld Place, a shadowed house creaking with secrets—‘Sirius!’—he grins.", "white")
    type_text(f"‘{wizard.name}, safe!’—Mrs. Weasley hugs—‘Stay!’", "white")
    choice = get_choice(["listen", "snoop"], "Settle in?", wizard)
    if choice == "listen":
        type_text("‘Voldemort!’—Sirius warns—‘He’s moving!’", "white")
    else:
        type_text("‘Kreacher!’—‘Filth!’—he hisses!", "red")
    type_text("‘Fight!’—the Order hums!", "white")

    # Chapter 4: Umbridge’s Reign
    type_text("\nChapter 4: Umbridge’s Reign", "yellow")
    type_text("Hogwarts—‘Umbridge!’—pink and poison—‘No magic!’—she smirks!", "white")
    type_text(f"‘{wizard.name}, behave!’—her quill gleams!", "white")
    choice = get_choice(["rebel", "obey"], "Defy her?", wizard)
    if choice == "rebel":
        type_text("‘No!’—you glare—‘We learn!’", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Yes,’—rage simmers!", "white")
    type_text("‘Rules!’—she croons!", "white")

    # Chapter 5: Dumbledore’s Army
    type_text("\nChapter 5: Dumbledore’s Army", "yellow")
    type_text("‘DA!’—Harry calls—‘Fight!’—Room of Requirement!", "white")
    choice = get_choice(["join", "pass"], "Stand?", wizard)
    if choice == "join":
        type_text("‘Expelliarmus!’—you pledge!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Watch,’—you linger!", "white")
    type_text("‘Ready!’—spells flare!", "white")

    # Chapter 6: Hogsmeade’s Pact
    type_text("\nChapter 6: Hogsmeade’s Pact", "yellow")
    type_text("‘Hog’s Head!’—‘We fight!’—secret meeting!", "white")
    choice = get_choice(["lead", "follow"], "Role?", wizard)
    if choice == "lead":
        type_text("‘Stand!’—you rally!", "cyan")
        wizard.modify_house_points(10)
    else:
        type_text("‘Harry!’—you nod!", "white")
    type_text("‘Signed!’—rebellion!", "white")

    # Chapter 7: Occlumency’s Pain
    type_text("\nChapter 7: Occlumency’s Pain", "yellow")
    type_text("‘Mind!’—Snape probes!", "white")
    choice = get_choice(["resist", "open"], "Guard?", wizard)
    if choice == "resist":
        type_text("‘Out!’—push!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Memories!’—sneer!", "white")
    type_text("‘Focus!’—Snape snaps!", "white")

    # Chapter 8: The Ministry Trap
    type_text("\nChapter 8: The Ministry Trap", "yellow")
    type_text("‘Sirius!’—Harry’s vision—‘Go!’", "white")
    choice = get_choice(["fly", "stay"], "Rescue?", wizard)
    if choice == "fly":
        type_text("‘Thestrals!’—to London!", "white")
    else:
        type_text("‘Trap!’—wait!", "white")
        return
    type_text("‘Death Eaters!’—ambush!", "red")

    # Chapter 9: Battle of Prophecies
    type_text("\nChapter 9: Battle of Prophecies", "yellow")
    type_text("‘Bellatrix!’—spells clash!", "white")
    enemy = Enemy("Bellatrix Lestrange", 120, 25, "shadow")
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Bellatrix: {enemy.health}", "white")
        choice = get_choice(["attack", "use spell"], "Battle!", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} strikes!", "white")
            enemy.take_damage(10)
        else:
            spell = get_choice(wizard.spells_known, "Cast?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
    if wizard.is_alive():
        type_text("‘Flee!’—‘Sirius!’—he falls!", "red")
        wizard.modify_house_points(25)

    # Chapter 10: The Truth Unveiled
    type_text("\nChapter 10: The Truth Unveiled", "yellow")
    type_text("‘He’s back!’—Dumbledore confirms!", "white")
    choice = get_choice(["rally", "mourn"], "Face it?", wizard)
    if choice == "rally":
        type_text("‘Fight!’—resolve!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Sirius…’—grief!", "white")
    type_text("‘War!’—Hogwarts braces!", "white")

def year_6(wizard):
    type_text("\n=== Year 6: Half-Blood Prince ===", "yellow")

    # Chapter 1: Shadows Lengthen
    type_text("\nChapter 1: Shadows Lengthen", "yellow")
    type_text("Summer fades—‘War!’—the Prophet screams, Death Eaters strike!", "white")
    type_text(f"You’re sixteen, {wizard.name},—‘Safe?’—you pace!", "white")
    choice = get_choice(["train", "wait"], "Prepare?", wizard)
    if choice == "train":
        type_text("‘Spells!’—you practice!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Soon,’—you watch!", "white")
    type_text("‘Hogwarts!’—hope!", "white")

    # Chapter 2: Slughorn’s Return
    type_text("\nChapter 2: Slughorn’s Return", "yellow")
    type_text("‘Potions!’—Slughorn waddles!", "white")
    choice = get_choice(["brew", "cheat"], "Excel?", wizard)
    if choice == "brew":
        type_text("‘Perfect!’—gold!", "cyan")
        wizard.advance_skill("potions")
    else:
        type_text("‘Caught!’—shame!", "red")
        wizard.align_with_dark()
    type_text("‘Talent!’—Slughorn beams!", "white")

    # Chapter 3: The Prince’s Tome
    type_text("\nChapter 3: The Prince’s Tome", "yellow")
    type_text("‘Prince!’—book whispers!", "white")
    choice = get_choice(["use", "discard"], "Trust?", wizard)
    if choice == "use":
        type_text("‘Sectumsempra!’—dark!", "cyan")
        wizard.advance_skill("dark arts")
    else:
        type_text("‘Risky!’—toss!", "white")
    type_text("‘Secrets!’—power!", "white")

    # Chapter 4: Draco’s Burden
    type_text("\nChapter 4: Draco’s Burden", "yellow")
    type_text("‘Draco!’—pale, plotting!", "white")
    choice = get_choice(["follow", "ignore"], "Watch?", wizard)
    if choice == "follow":
        type_text("‘Sneak!’—clues!", "white")
    else:
        type_text("‘Busy!’—pass!", "white")
    type_text("‘Something!’—dread!", "white")

    # Chapter 5: Horcrux Hunt
    type_text("\nChapter 5: Horcrux Hunt", "yellow")
    type_text("‘Soul!’—Dumbledore reveals!", "white")
    choice = get_choice(["probe", "trust"], "Seek?", wizard)
    if choice == "probe":
        type_text("‘Locket!’—dark!", "cyan")
        wizard.advance_skill("dark arts")
    else:
        type_text("‘Lead!’—follow!", "white")
    type_text("‘Danger!’—truth!", "white")

    # Chapter 6: The Cave’s Trial
    type_text("\nChapter 6: The Cave’s Trial", "yellow")
    type_text("‘Drink!’—Dumbledore pleads!", "white")
    choice = get_choice(["help", "refuse"], "Aid?", wizard)
    if choice == "help":
        type_text("‘Force!’—pain!", "green")
        wizard.align_with_good()
    else:
        type_text("‘No!’—alone!", "white")
    type_text("‘Inferi!’—rise!", "red")

    # Chapter 7: Inferi Assault
    type_text("\nChapter 7: Inferi Assault", "yellow")
    type_text("‘Fight!’—Inferi swarm!", "white")
    enemy = Enemy("Inferi Horde", 100, 20)
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Inferi: {enemy.health}", "white")
        choice = get_choice(["attack", "use spell"], "Battle!", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} slashes!", "white")
            enemy.take_damage(10)
        else:
            spell = get_choice(wizard.spells_known, "Cast?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
    if wizard.is_alive():
        type_text("‘Fire!’—‘Locket!’", "green")
        wizard.modify_house_points(20)

    # Chapter 8: Tower’s Fall
    type_text("\nChapter 8: Tower’s Fall", "yellow")
    type_text("‘Draco!’—‘Avada!’—Snape!", "white")
    choice = get_choice(["fight", "flee"], "Act?", wizard)
    if choice == "fight":
        type_text("‘Stupefy!’—flee!", "cyan")
        wizard.take_damage(20)
    else:
        type_text("‘Run!’—‘No!’", "white")
    type_text("‘Dumbledore!’—grief!", "white")

    # Chapter 9: Mourning’s Silence
    type_text("\nChapter 9: Mourning’s Silence", "yellow")
    type_text("‘Gone…’—hall weeps!", "white")
    choice = get_choice(["honor", "rage"], "React?", wizard)
    if choice == "honor":
        type_text("‘For him!’—resolve!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Curse!’—dark!", "red")
    type_text("‘War!’—echoes!", "white")

    # Chapter 10: The Prince Revealed
    type_text("\nChapter 10: The Prince Revealed", "yellow")
    type_text("‘Snape!’—‘Prince!’", "white")
    choice = get_choice(["forgive", "hate"], "Judge?", wizard)
    if choice == "forgive":
        type_text("‘Why?’—light!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Traitor!’—shadow!", "red")
        wizard.align_with_dark()
    type_text("‘End!’—prepare!", "white")

def year_7(wizard):
    type_text("\n=== Year 7: Deathly Hallows ===", "yellow")

    # Chapter 1: Flight from Shadows
    type_text("\nChapter 1: Flight from Shadows", "yellow")
    type_text("‘War!’—Death Eaters strike!", "white")
    type_text(f"‘{wizard.name}, flee!’—Order!", "white")
    choice = get_choice(["fight", "fly"], "Escape?", wizard)
    if choice == "fight":
        type_text("‘Stupefy!’—hold!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Broom!’—soar!", "white")
    type_text("‘Safe!’—for now!", "white")

    # Chapter 2: The Wedding Crash
    type_text("\nChapter 2: The Wedding Crash", "yellow")
    type_text("‘Fleur!’—‘Attack!’—Death Eaters!", "white")
    choice = get_choice(["defend", "flee"], "Stand?", wizard)
    if choice == "defend":
        type_text("‘Stupefy!’—off!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Apparate!’—run!", "white")
    type_text("‘Chaos!’—scattered!", "white")

    # Chapter 3: Horcrux Quest
    type_text("\nChapter 3: Horcrux Quest", "yellow")
    type_text("‘Locket!’—tents!", "white")
    choice = get_choice(["destroy", "hide"], "Locket?", wizard)
    if choice == "destroy":
        type_text("‘Stab!’—gone!", "cyan")
        wizard.advance_skill("dark arts")
    else:
        type_text("‘Bury!’—safe!", "white")
    type_text("‘Next!’—hunt!", "white")

    # Chapter 4: Godric’s Hollow
    type_text("\nChapter 4: Godric’s Hollow", "yellow")
    type_text("‘Graves!’—Nagini!", "white")
    enemy = Enemy("Nagini", 100, 25, "shadow")
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Nagini: {enemy.health}", "white")
        choice = get_choice(["attack", "use spell"], "Battle!", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} slashes!", "white")
            enemy.take_damage(10)
        else:
            spell = get_choice(wizard.spells_known, "Cast?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
    if wizard.is_alive():
        type_text("‘Flee!’—close!", "green")
        wizard.modify_house_points(20)

    # Chapter 5: The Silver Doe
    type_text("\nChapter 5: The Silver Doe", "yellow")
    type_text("‘Doe!’—‘Sword!’", "white")
    choice = get_choice(["dive", "wait"], "Retrieve?", wizard)
    if choice == "dive":
        type_text("‘Cold!’—grab!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Watch!’—Ron!", "white")
    type_text("‘Horcrux!’—closer!", "white")

    # Chapter 6: Lovegood’s Tale
    type_text("\nChapter 6: Lovegood’s Tale", "yellow")
    type_text("‘Hallows!’—Luna’s dad!", "white")
    choice = get_choice(["believe", "doubt"], "Trust?", wizard)
    if choice == "believe":
        type_text("‘Maybe…’—hope!", "white")
    else:
        type_text("‘Mad!’—skeptic!", "white")
    type_text("‘Ambush!’—flee!", "white")

    # Chapter 7: Malfoy Manor
    type_text("\nChapter 7: Malfoy Manor", "yellow")
    type_text("‘Caught!’—‘Bellatrix!’", "white")
    choice = get_choice(["fight", "talk"], "Escape?", wizard)
    if choice == "fight":
        type_text("‘Stupefy!’—clash!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Wait!’—Dobby!", "white")
    type_text("‘Free!’—loss!", "white")

    # Chapter 8: Gringotts’ Heist
    type_text("\nChapter 8: Gringotts’ Heist", "yellow")
    type_text("‘Break!’—‘Cup!’", "white")
    choice = get_choice(["charm", "blast"], "Steal?", wizard)
    if choice == "charm":
        type_text("‘Imperio!’—in!", "cyan")
        wizard.advance_skill("dark arts")
    else:
        type_text("‘Blast!’—chaos!", "white")
    type_text("‘Dragon!’—fly!", "white")

    # Chapter 9: Hogwarts Siege
    type_text("\nChapter 9: Hogwarts Siege", "yellow")
    type_text("‘War!’—‘Defend!’", "white")
    choice = get_choice(["front", "support"], "Fight?", wizard)
    if choice == "front":
        type_text("‘Stupefy!’—frontline!", "cyan")
        wizard.advance_skill("defense")
    else:
        type_text("‘Heal!’—aid!", "green")
        wizard.align_with_good()
    type_text("‘Hold!’—battle!", "white")

    # Chapter 10: The Final Duel
    type_text("\nChapter 10: The Final Duel", "yellow")
    type_text("‘Voldemort!’—‘End!’", "white")
    enemy = Enemy("Voldemort", 200, 40, "shadow")
    while enemy.is_alive() and wizard.is_alive():
        type_text(f"\n{wizard.name}: {wizard.health} | Voldemort: {enemy.health}", "white")
        choice = get_choice(["attack", "use spell"], "End it!", wizard)
        if choice == "attack":
            type_text(f"{wizard.name} charges!", "white")
            enemy.take_damage(10)
        else:
            spell = get_choice(wizard.spells_known, "Cast?", wizard)
            wizard.use_magic(spell, enemy)
        if enemy.is_alive():
            enemy.use_ability(wizard)
    if wizard.is_alive():
        type_text("‘Over!’—‘Victory!’", "green")
        wizard.modify_house_points(50)

    # Chapter 11: Dawn of Peace
    type_text("\nChapter 11: Dawn of Peace", "yellow")
    type_text("‘Light!’—‘Rebuild!’", "white")
    choice = get_choice(["heal", "honor"], "After?", wizard)
    if choice == "heal":
        type_text("‘Help!’—restore!", "green")
        wizard.align_with_good()
    else:
        type_text("‘Fallen!’—honor!", "white")
    type_text("‘Peace!’—end!", "white")
