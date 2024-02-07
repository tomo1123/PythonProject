"""バリューが高い順に辞書型を並べ替える"""
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(sorted(ranking, key=ranking.get, reverse=True))