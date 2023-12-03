import re

limit_mapping = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def collect_bag(line: str):
    # Regular expression patterns
    game_id_pattern = r"Game (\d+):"
    counts_pattern = r"(\d+) (\w+)"

    # Find the game ID
    game_id_match = re.search(game_id_pattern, line)
    if game_id_match:
        game_id = int(game_id_match.group(1))
    
    rounds = line.split(":")[1]
    for round in rounds.split(";"):
        counts_matches = re.findall(counts_pattern, round)
        for match in counts_matches:
            count = int(match[0])
            color = match[1].lower()
            if count > limit_mapping[color]:
                return False, game_id

    return True, game_id

def collect_bag2(line: str):
    mapping = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    # Regular expression patterns
    game_id_pattern = r"Game (\d+):"
    counts_pattern = r"(\d+) (\w+)"

    # Find the game ID
    game_id_match = re.search(game_id_pattern, line)
    if game_id_match:
        game_id = int(game_id_match.group(1))
    
    rounds = line.split(":")[1]
    for round in rounds.split(";"):
        counts_matches = re.findall(counts_pattern, round)
        for match in counts_matches:
            count = int(match[0])
            color = match[1].lower()
            mapping[color] = max(mapping[color], count)

    ans = 1
    for value in mapping.values():
        ans *= value

    return ans


with open("input2.txt", "r") as f:
    game_id_sum = 0
    powers_game = 0
    lines = [line.rstrip() for line in f]
    for line in lines:
        possible, game_id = collect_bag(line)
        powers_game += collect_bag2(line)
        if possible:
            game_id_sum += game_id
    print(game_id_sum)
    print(powers_game)