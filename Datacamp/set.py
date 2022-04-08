# Set theory
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = misty_set.symmetric_difference(ash_set)
print(unique_to_set)

brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix', 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)


# %timeit 'Psyduck' in ash_pokedex
# %timeit 'Psyduck' in brock_pokedex_set
#
# %timeit 'Machop' in ash_pokedex
# %timeit 'Machop' in brock_pokedex_set

names = ['Forretress', 'WormadamSandy Cloak', 'Croagunk', 'Mime Jr.', 'Camerupt', 'Alomomola', 'Munchlax', 'Tauros', 'Victini', 'Salamence', 'Flygon', 'Cottonee', 'Pachirisu', 'Caterpie', 'Avalugg', 'Beldum', 'Foongus', 'Zigzagoon', 'Buizel', 'Octillery', 'Seviper', 'Charmeleon', 'Torkoal', 'Doublade', 'Grovyle', 'Maractus', 'Tynamo', 'Magikarp', 'Beautifly', 'Parasect', 'Frogadier', 'Clefairy', 'Doduo', 'Aggron', 'Conkeldurr', 'Volbeat', 'Whimsicott', 'Sentret', 'Lairon', 'Jirachi', 'Cloyster', 'Dragalge', 'Hitmonlee', 'Gothitelle', 'Delphox', 'Magmortar', 'Talonflame', 'Victini', 'Feebas', 'Rampardos', 'Marowak', 'Pelipper', 'Espurr', 'MeowsticMale', 'Stunfisk', 'Cascoon', 'Metang', 'Scizor', 'Chimecho', 'Anorith', 'Heatmor', 'Shieldon', 'Doduo', 'Mesprit', 'Nidoran♀', 'Wartortle', 'Wooper', 'Mr. Mime', 'Mightyena', 'Mankey', 'Golbat', 'Azurill', 'Bagon', 'Leafeon', 'Electivire', 'Milotic', 'Elekid', 'Chimecho', 'Delphox', 'Gabite', 'Scizor', 'Budew', 'Haxorus', 'Porygon-Z', 'Beldum', 'Torterra', 'Volcanion', 'Chimecho', 'Pidove', 'Entei', 'WormadamPlant Cloak', 'Azelf', 'Galvantula', 'Tirtouga', 'Gible', 'Primeape', 'Zweilous', 'Shellder', 'Ho-oh', 'Emboar', 'Rotom', 'Solosis', 'Vigoroth', 'Frogadier', 'Ampharos', 'Gastly', 'Riolu', 'Doublade', 'Kirlia', 'Lickitung', 'Aromatisse', 'Mandibuzz', 'Happiny', 'Chandelure', 'Gorebyss', 'Barboach', 'Eevee', 'Ho-oh', 'Duosion', 'Sewaddle', 'Hippopotas', 'Seaking', 'Butterfree', 'Mew', 'Bronzor', 'Suicune', 'Herdier', 'Xerneas', 'Mareep', 'Slakoth', 'Uxie', 'Samurott', 'Dewgong', 'Togekiss', 'Pichu', 'Vanillish', 'Zapdos', 'Floette', 'Fletchling', 'Vigoroth', 'Umbreon', 'Conkeldurr', 'Phantump', 'Shellder', 'WormadamTrash Cloak', 'Rampardos', 'Electabuzz', 'Clawitzer', 'Dedenne', 'Regigigas', 'Xatu', 'Wartortle', 'Growlithe', 'Gulpin', 'Weezing', 'Starly', 'Scraggy', 'Skrelp', 'Wynaut', 'Carvanha', 'Solrock', 'Heatmor', 'KyogrePrimal Kyogre', 'Swinub', 'Mothim', 'Eelektrik', 'Yanma', 'Piplup', 'Chespin', 'Shellos', 'Cradily', 'Chatot', 'Burmy', 'Groudon', 'Inkay', 'Azumarill', 'Spinarak', 'Surskit', 'Azelf', 'Chandelure', 'Ariados', 'Gloom', 'Toxicroak', 'Teddiursa', 'Forretress', 'Onix', 'Musharna', 'Carbink', 'Phantump', 'Ledyba', 'Escavalier', 'Misdreavus', 'Nuzleaf', 'Drilbur', 'Staravia', 'Garbodor', 'Slakoth', 'Glalie', 'Minccino', 'Cottonee', 'Feraligatr', 'Munna', 'Ditto', 'Feraligatr', 'Igglybuff', 'Electrike', 'Tropius', 'Muk', 'Froslass', 'Huntail', 'Pidove', 'Shellder', 'Regice', 'Sealeo', 'Chinchou', 'Absol', 'Skrelp', 'Volcarona', 'Minun', 'Magnezone', 'Feraligatr', 'Marowak', 'Mantine', 'Shelmet', 'Abra', 'Musharna', 'Chespin', 'Victreebel', 'Sudowoodo', 'Grotle', 'Hawlucha', 'Ivysaur', 'Mew', 'Hawlucha', 'Porygon', 'Qwilfish', 'Skrelp', 'Natu', 'Clefable', 'Anorith', 'RotomWash Rotom', 'Swoobat', 'Floette', 'Corsola', 'Marowak', 'Glalie', 'Buneary', 'Zweilous', 'Arceus', 'Ponyta', 'Sandslash', 'Dugtrio', 'Kingler', 'Breloom', 'Lilligant', 'Entei', 'Carbink', 'Audino', 'Dewott', 'Golem', 'Victreebel', 'Shiftry', 'Swirlix', 'Caterpie', 'Krabby', 'Nosepass', 'Roggenrola', 'Gligar', 'Sceptile', 'Sunflora', 'Leavanny', 'Froakie', 'Girafarig', 'Exeggcute', 'Simipour', 'Archeops', 'Kadabra', 'Chikorita', 'Chansey', 'Onix', 'Cottonee', 'Muk', 'Chimecho', 'Victini', 'Gastrodon', 'Cradily', 'Exeggcute', 'Celebi', 'Eelektross', 'Sliggoo', 'Haunter', 'Bouffalant', 'Crobat', 'Solrock', 'Whismur', 'Sudowoodo', 'Durant', 'Articuno', 'Minun', 'Rhyperior', 'Ho-oh', 'Electrode', 'Lombre', 'Mesprit', 'Goodra', 'Numel', 'Castform', 'Drifblim', 'Bastiodon', 'Helioptile', 'Aggron', 'Scolipede', 'Sandslash', 'Cherrim', 'Mantyke', 'Golduck', 'Wingull', 'Froslass', 'Seismitoad', 'Manaphy', 'Jynx', 'Gallade', 'Karrablast', 'Rampardos', 'Haxorus', 'Sandshrew', 'Bayleef', 'Ludicolo', 'Blitzle', 'Venonat', 'Chingling', 'Flygon', 'Raticate', 'Espeon', 'Lileep', 'Durant', 'Surskit', 'Wynaut', 'Slowking', 'Abomasnow', 'Larvesta', 'Registeel', 'Hoppip', 'Drilbur', 'Aggron', 'Murkrow', 'Fennekin', 'Archen', 'Klink', 'Pignite', 'Golduck', 'Sableye', 'Wartortle', 'Sliggoo', 'Trapinch', 'Vanilluxe', 'Gengar', 'Carracosta', 'Espurr', 'Golett', 'Tropius', 'Weepinbell', 'Krabby', 'Talonflame', 'Hippopotas', 'Simisear', 'Slowbro', 'Manectric', 'Lugia', 'Gligar', 'Claydol', 'Tangela', 'Duskull', 'Buneary', 'Altaria', 'Cryogonal', 'Elekid', 'Toxicroak', 'Zapdos', 'Ralts', 'KyogrePrimal Kyogre', "Farfetch'd", 'Duskull', 'Mesprit', 'Mightyena', 'Manaphy', 'Zebstrika', 'Vileplume', 'Smeargle', 'Ludicolo', 'Numel', 'Snover', 'Totodile', 'Reuniclus', 'Panpour', 'Pyroar', 'Qwilfish', 'Manaphy', 'Tyranitar', 'Kyurem', 'Honchkrow', 'Tympole', 'Azurill', 'Pikachu', 'Forretress', 'Marshtomp', 'Persian', 'Gigalith', 'Clamperl', 'Poliwag', 'Reuniclus', 'Kricketot', 'Exeggcute', 'Infernape', 'Chingling', 'Gulpin', 'Yveltal', 'Porygon-Z', 'Cascoon', 'Donphan', 'Duosion', 'Natu', 'Lombre', 'Phantump', 'Spheal', 'Corsola', 'Bastiodon', 'Spritzee', 'Nincada', 'Beheeyem', 'Quagsire', 'Combusken', 'Vespiquen', 'DarmanitanStandard Mode', 'Scizor', 'Swanna', 'Pidgeotto', 'Cradily', 'Blissey', 'Clefable', 'Numel', 'Virizion', 'Chesnaught', 'Yamask', 'Burmy', 'Butterfree', 'Garchomp', 'Masquerain', 'Ursaring', 'Servine', 'Infernape', 'Ludicolo', 'Gastrodon', 'Ducklett', 'Bergmite', 'Espurr', 'Moltres', 'Butterfree', 'Arcanine', 'Chansey', 'Chespin', 'Snover', 'Shroomish', 'Mightyena', 'Swoobat', 'Grumpig', 'Bellsprout', 'Cyndaquil', 'Gabite', 'Bibarel', 'Zorua', 'WormadamPlant Cloak', 'Roggenrola', 'Arcanine', 'Slakoth', 'Dewott', 'Scizor', 'Crawdaunt', 'Fearow', 'Buizel', 'Tentacruel', 'Azumarill', 'Espeon', 'Watchog', 'Staravia', 'Amaura', 'Exeggutor', 'Gible', 'Marowak', 'Ekans', 'Bastiodon', 'Shelgon', 'Roserade', 'Scrafty', 'Machamp', 'Shuppet', 'Mawile', 'Boldore', 'Krookodile', 'Sudowoodo']
primary_types = ['Bug', 'Bug', 'Poison', 'Psychic', 'Fire', 'Water', 'Normal', 'Normal', 'Psychic', 'Dragon', 'Ground', 'Grass', 'Electric', 'Bug', 'Ice', 'Steel', 'Grass', 'Normal', 'Water', 'Water', 'Poison', 'Fire', 'Fire', 'Steel', 'Grass', 'Grass', 'Electric', 'Water', 'Bug', 'Bug', 'Water', 'Fairy', 'Normal', 'Steel', 'Fighting', 'Bug', 'Grass', 'Normal', 'Steel', 'Steel', 'Water', 'Poison', 'Fighting', 'Psychic', 'Fire', 'Fire', 'Fire', 'Psychic', 'Water', 'Rock', 'Ground', 'Water', 'Psychic', 'Psychic', 'Ground', 'Bug', 'Steel', 'Bug', 'Psychic', 'Rock', 'Fire', 'Rock', 'Normal', 'Psychic', 'Poison', 'Water', 'Water', 'Psychic', 'Dark', 'Fighting', 'Poison', 'Normal', 'Dragon', 'Grass', 'Electric', 'Water', 'Electric', 'Psychic', 'Fire', 'Dragon', 'Bug', 'Grass', 'Dragon', 'Normal', 'Steel', 'Grass', 'Fire', 'Psychic', 'Normal', 'Fire', 'Bug', 'Psychic', 'Bug', 'Water', 'Dragon', 'Fighting', 'Dark', 'Water', 'Fire', 'Fire', 'Electric', 'Psychic', 'Normal', 'Water', 'Electric', 'Ghost', 'Fighting', 'Steel', 'Psychic', 'Normal', 'Fairy', 'Dark', 'Normal', 'Ghost', 'Water', 'Water', 'Normal', 'Fire', 'Psychic', 'Bug', 'Ground', 'Water', 'Bug', 'Psychic', 'Steel', 'Water', 'Normal', 'Fairy', 'Electric', 'Normal', 'Psychic', 'Water', 'Water', 'Fairy', 'Electric', 'Ice', 'Electric', 'Fairy', 'Normal', 'Normal', 'Dark', 'Fighting', 'Ghost', 'Water', 'Bug', 'Rock', 'Electric', 'Water', 'Electric', 'Normal', 'Psychic', 'Water', 'Fire', 'Poison', 'Poison', 'Normal', 'Dark', 'Poison', 'Psychic', 'Water', 'Rock', 'Fire', 'Water', 'Ice', 'Bug', 'Electric', 'Bug', 'Water', 'Grass', 'Water', 'Rock', 'Normal', 'Bug', 'Ground', 'Dark', 'Water', 'Bug', 'Bug', 'Psychic', 'Ghost', 'Bug', 'Grass', 'Poison', 'Normal', 'Bug', 'Rock', 'Psychic', 'Rock', 'Ghost', 'Bug', 'Bug', 'Ghost', 'Grass', 'Ground', 'Normal', 'Poison', 'Normal', 'Ice', 'Normal', 'Grass', 'Water', 'Psychic', 'Normal', 'Water', 'Normal', 'Electric', 'Grass', 'Poison', 'Ice', 'Water', 'Normal', 'Water', 'Ice', 'Ice', 'Water', 'Dark', 'Poison', 'Bug', 'Electric', 'Electric', 'Water', 'Ground', 'Water', 'Bug', 'Psychic', 'Psychic', 'Grass', 'Grass', 'Rock', 'Grass', 'Fighting', 'Grass', 'Psychic', 'Fighting', 'Normal', 'Water', 'Poison', 'Psychic', 'Fairy', 'Rock', 'Electric', 'Psychic', 'Fairy', 'Water', 'Ground', 'Ice', 'Normal', 'Dark', 'Normal', 'Fire', 'Ground', 'Ground', 'Water', 'Grass', 'Grass', 'Fire', 'Rock', 'Normal', 'Water', 'Rock', 'Grass', 'Grass', 'Fairy', 'Bug', 'Water', 'Rock', 'Rock', 'Ground', 'Grass', 'Grass', 'Bug', 'Water', 'Normal', 'Grass', 'Water', 'Rock', 'Psychic', 'Grass', 'Normal', 'Rock', 'Grass', 'Poison', 'Psychic', 'Psychic', 'Water', 'Rock', 'Grass', 'Psychic', 'Electric', 'Dragon', 'Ghost', 'Normal', 'Poison', 'Rock', 'Normal', 'Rock', 'Bug', 'Ice', 'Electric', 'Ground', 'Fire', 'Electric', 'Water', 'Psychic', 'Dragon', 'Fire', 'Normal', 'Ghost', 'Rock', 'Electric', 'Steel', 'Bug', 'Ground', 'Grass', 'Water', 'Water', 'Water', 'Ice', 'Water', 'Water', 'Ice', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Ground', 'Grass', 'Water', 'Electric', 'Bug', 'Psychic', 'Ground', 'Normal', 'Psychic', 'Rock', 'Bug', 'Bug', 'Psychic', 'Water', 'Grass', 'Bug', 'Steel', 'Grass', 'Ground', 'Steel', 'Dark', 'Fire', 'Rock', 'Steel', 'Fire', 'Water', 'Dark', 'Water', 'Dragon', 'Ground', 'Ice', 'Ghost', 'Water', 'Psychic', 'Ground', 'Grass', 'Grass', 'Water', 'Fire', 'Ground', 'Fire', 'Water', 'Electric', 'Psychic', 'Ground', 'Ground', 'Grass', 'Ghost', 'Normal', 'Dragon', 'Ice', 'Electric', 'Poison', 'Electric', 'Psychic', 'Water', 'Normal', 'Ghost', 'Psychic', 'Dark', 'Water', 'Electric', 'Grass', 'Normal', 'Water', 'Fire', 'Grass', 'Water', 'Psychic', 'Water', 'Fire', 'Water', 'Water', 'Rock', 'Dragon', 'Dark', 'Water', 'Normal', 'Electric', 'Bug', 'Water', 'Normal', 'Rock', 'Water', 'Water', 'Psychic', 'Bug', 'Grass', 'Fire', 'Psychic', 'Poison', 'Dark', 'Normal', 'Bug', 'Ground', 'Psychic', 'Psychic', 'Water', 'Ghost', 'Ice', 'Water', 'Rock', 'Fairy', 'Bug', 'Psychic', 'Water', 'Fire', 'Bug', 'Fire', 'Bug', 'Water', 'Normal', 'Rock', 'Normal', 'Fairy', 'Fire', 'Grass', 'Grass', 'Ghost', 'Bug', 'Bug', 'Dragon', 'Bug', 'Normal', 'Grass', 'Fire', 'Water', 'Water', 'Water', 'Ice', 'Psychic', 'Fire', 'Bug', 'Fire', 'Normal', 'Grass', 'Grass', 'Grass', 'Dark', 'Psychic', 'Psychic', 'Grass', 'Fire', 'Dragon', 'Normal', 'Dark', 'Bug', 'Rock', 'Fire', 'Normal', 'Water', 'Bug', 'Water', 'Normal', 'Water', 'Water', 'Water', 'Psychic', 'Normal', 'Normal', 'Rock', 'Grass', 'Dragon', 'Ground', 'Poison', 'Rock', 'Dragon', 'Grass', 'Dark', 'Fighting', 'Ghost', 'Steel', 'Rock', 'Ground', 'Rock']
generations = [2, 4, 4, 4, 3, 5, 4, 1, 5, 3, 3, 5, 4, 1, 6, 3, 5, 3, 4, 2, 3, 1, 3, 6, 3, 5, 5, 1, 3, 1, 6, 1, 1, 3, 5, 3, 5, 2, 3, 3, 1, 6, 1, 5, 6, 4, 6, 5, 3, 4, 1, 3, 6, 6, 5, 3, 3, 2, 3, 3, 5, 4, 1, 4, 1, 1, 2, 1, 3, 1, 1, 3, 3, 4, 4, 3, 2, 3, 6, 4, 2, 4, 5, 4, 3, 4, 6, 3, 5, 2, 4, 4, 5, 5, 4, 1, 5, 1, 2, 5, 4, 5, 3, 6, 2, 1, 4, 6, 3, 1, 6, 5, 4, 5, 3, 3, 1, 2, 5, 5, 4, 1, 1, 1, 4, 2, 5, 6, 2, 3, 4, 5, 1, 4, 2, 5, 1, 6, 6, 3, 2, 5, 6, 1, 4, 4, 1, 6, 6, 4, 2, 1, 1, 3, 1, 4, 5, 6, 3, 3, 3, 5, 3, 2, 4, 5, 2, 4, 6, 4, 3, 4, 4, 3, 6, 2, 2, 3, 4, 5, 2, 1, 4, 2, 2, 1, 5, 6, 6, 2, 5, 2, 3, 5, 4, 5, 3, 3, 5, 5, 2, 5, 1, 2, 2, 3, 3, 1, 4, 3, 5, 1, 3, 3, 2, 3, 6, 5, 3, 4, 2, 1, 2, 5, 1, 5, 6, 1, 2, 4, 6, 1, 1, 6, 1, 2, 6, 2, 1, 3, 4, 5, 6, 2, 1, 3, 4, 5, 4, 1, 1, 1, 1, 3, 5, 2, 6, 5, 5, 1, 1, 3, 6, 1, 1, 3, 5, 2, 3, 2, 5, 6, 2, 1, 5, 5, 1, 2, 1, 1, 5, 1, 3, 5, 4, 3, 1, 2, 5, 6, 1, 5, 2, 3, 3, 2, 5, 1, 3, 4, 2, 1, 3, 4, 6, 3, 3, 4, 4, 6, 3, 5, 1, 4, 4, 1, 3, 4, 5, 4, 1, 4, 5, 4, 5, 1, 2, 3, 5, 1, 4, 3, 1, 2, 3, 5, 3, 3, 2, 4, 5, 3, 2, 5, 3, 2, 6, 5, 5, 5, 1, 3, 1, 6, 3, 5, 1, 5, 6, 5, 3, 1, 1, 6, 4, 5, 1, 3, 2, 2, 3, 1, 3, 4, 3, 5, 2, 4, 1, 3, 3, 1, 3, 4, 3, 4, 5, 1, 2, 3, 3, 4, 2, 5, 5, 6, 2, 4, 2, 5, 4, 5, 3, 1, 2, 3, 1, 5, 3, 1, 5, 4, 1, 4, 4, 3, 6, 4, 3, 2, 5, 2, 3, 6, 3, 2, 4, 6, 3, 5, 2, 3, 4, 5, 2, 5, 1, 3, 2, 1, 3, 5, 6, 5, 4, 1, 4, 3, 2, 5, 4, 3, 4, 5, 6, 6, 1, 1, 1, 1, 6, 4, 3, 3, 5, 3, 1, 2, 4, 4, 5, 4, 5, 1, 3, 5, 2, 3, 1, 4, 1, 2, 2, 5, 4, 6, 1, 4, 1, 1, 4, 3, 4, 5, 1, 3, 3, 5, 5, 2]


def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques


# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')

