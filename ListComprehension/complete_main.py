def create_minion(summoner_stats):
    minion_stats = [stat * 0.5 for stat in summoner_stats]
    return minion_stats

# don't touch below this line

# [Health, Armor, Damage]
summoner = [100.0, 50.0, 120.0] 
minion = create_minion(summoner)

print("Minion Health:", minion[0])
print("Minion Armor:", minion[1])
print("Minion Damage:", minion[2])