def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x: x != "", [line.strip() for line in lines]))
    return lines

def get_winner_nums(winners):
    res = set()
    for i in range(0, len(winners), 3):
        first = winners[i]
        second = winners[i + 1]
        if first == " ":
            first = 0
        else:
            first = int(first)
        second = int(second)
        res.add(first * 10 + second)
    return res

def get_chosen_nums(chosen):
    res = []
    for i in range(0, len(chosen), 3):
        first = chosen[i]
        second = chosen[i + 1]
        if first == " ":
            first = 0
        else:
            first = int(first)
        second = int(second)
        res.append(first * 10 + second)
    return res

def part1():
    cards = get_input("p4-1.txt")
    sum = 0
    for card in cards:
        nums = card.split(": ")[1]
        winners, chosen = nums.split(" | ")
        # Each number is two chars long, with a space
        # instead of a leading zero for single digit numbers
        winner_nums = get_winner_nums(winners)
        chosen_nums = get_chosen_nums(chosen)
        num_winners = 0
        for num in chosen_nums:
            if num in winner_nums:
                num_winners += 1
        if num_winners > 0:
            sum += 2 ** (num_winners - 1)
    print(sum)

def part2():
    cards = get_input("p4-1.txt")
    total_cards = 0
    # Problem constraints say that if I have matching numbers, that the
    # cards I win will never run off the table
    i = 0
    card_count_map = {j: 1 for j in range(len(cards))}
    for card in cards:
        card_count = card_count_map[i]
        nums = card.split(": ")[1]
        winners, chosen = nums.split(" | ")
        winner_nums = get_winner_nums(winners)
        chosen_nums = get_chosen_nums(chosen)
        num_winners = 0
        for num in chosen_nums:
            if num in winner_nums:
                num_winners += 1
        for j in range(num_winners):
            card_count_map[i + j + 1] += card_count
        total_cards += card_count
        i += 1
    print(total_cards)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
