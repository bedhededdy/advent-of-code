from collections import Counter

def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def classify_hand(hand):
    # Optimizations can definitely be made to this, but for now I will just
    # implement the most straightforward solution.
    hand = hand.split(" ")[0]
    # 5 of a kind
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 6
    # 4 of a kind
    card_counts = Counter(hand)
    if any([count == 4 for count in card_counts.values()]):
        return 5
    # Full house
    three_of_a_kind = any([count == 3 for count in card_counts.values()])
    pairs = [count > 1 for count in card_counts.values()]
    pairs = [pair for pair in pairs if pair] # Filter out the False values
    if three_of_a_kind and len(pairs) > 1: # Can't double count the 3 of a kind as a pair
        return 4
    # 3 of a kind
    if three_of_a_kind:
        return 3
    # 2 pair
    if len(pairs) > 1:
        return 2
    # 1 pair
    if len(pairs) > 0:
        return 1
    # High card
    return 0

def rank_card(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 11
    if card == "T":
        return 10
    return int(card)

def rank_bids(hand_bids):
    # Python's use of a key scoring function is sort of a drawback here,
    # because what we really want is a comparator function that makes handling
    # ties more elegant.
    # As a consequence, I will just end up doing a bubble sort for simplicity.
    hand_to_class = {}
    for i in range(len(hand_bids)):
        hand_to_class[hand_bids[i].split(" ")[0]] = classify_hand(hand_bids[i])
    n = len(hand_bids)
    while True:
        swapped = False
        for i in range(1, n):
            # Inefficient to not just do the split once when we classify the hand
            # but it's fine
            hand1 = hand_bids[i-1].split(" ")[0]
            hand2 = hand_bids[i].split(" ")[0]
            class1 = hand_to_class[hand1]
            class2 = hand_to_class[hand2]
            if class1 > class2:
                hand_bids[i-1], hand_bids[i] = hand_bids[i], hand_bids[i-1]
                swapped = True
            if class1 == class2:
                for j in range(len(hand1)):
                    card1_rank = rank_card(hand1[j])
                    card2_rank = rank_card(hand2[j])
                    if card1_rank > card2_rank:
                        hand_bids[i-1], hand_bids[i] = hand_bids[i], hand_bids[i-1]
                        swapped = True
                        break
                    if card1_rank < card2_rank:
                        break
        n = n - 1 # We know that the last element is sorted, so we needn't check it again
        if not swapped:
            break
    return [int(hand_bid.split(" ")[1]) for hand_bid in hand_bids]

def is_four_of_a_kind(hand):
    hand = hand.split(" ")[0]
    card_counts = Counter(hand)
    if any([count == 4 for count in card_counts.values()]):
        return True
    return False

def is_three_of_a_kind(hand):
    hand = hand.split(" ")[0]
    card_counts = Counter(hand)
    if any([count == 3 for count in card_counts.values()]):
        return True
    return False

def is_two_pair(hand):
    hand = hand.split(" ")[0]
    card_counts = Counter(hand)
    pairs = [count > 1 for count in card_counts.values()]
    pairs = [pair for pair in pairs if pair] # Filter out the False values
    if len(pairs) > 1:
        return True
    return False

def is_pair(hand):
    hand = hand.split(" ")[0]
    card_counts = Counter(hand)
    pairs = [count > 1 for count in card_counts.values()]
    pairs = [pair for pair in pairs if pair] # Filter out the False values
    if len(pairs) > 0:
        return True
    return False

def classify_hand_without_jokers(hand):
    hand_without_jokers = ""
    for card in hand:
        if card != "J":
            hand_without_jokers += card
    # Can't have a full house with a joker
    if is_four_of_a_kind(hand_without_jokers):
        return 5
    if is_three_of_a_kind(hand_without_jokers):
        return 3
    if is_two_pair(hand_without_jokers):
        return 2
    if is_pair(hand_without_jokers):
        return 1
    return 0

def classify_hand2(hand):
    # the key here is to figure out what hand we have with just the 4 cards
    # and then to see what the best hand we can make is when we add in the 5th
    # card assuming that there is a joker in the hand
    if not "J" in hand:
        return classify_hand(hand)
    class_without_jokers = classify_hand_without_jokers(hand)
    num_jokers = hand.count("J")
    if num_jokers == 1:
        if class_without_jokers == 5:
            # If we have a four of a kind, then make a 5 of a kind
            return 6
        if class_without_jokers == 3:
            # If we have a 3 pair, then make a 4 of a kind
            return 5
        if class_without_jokers == 2:
            # If we have a 2 pair, then make a full house
            return 4
        if class_without_jokers == 1:
            # If we have a pair, then make a three of a kind
            return 3
        # Turn high card into a pair
        return 1
    elif num_jokers == 2:
        if class_without_jokers == 3:
            # If we have a three of a kind, then make a 5 of a kind
            return 6
        if class_without_jokers == 1:
            # If we have a pair, then make a 4 of a kind
            return 5
        # If we have a high card, then make a three of a kind
        return 3
    elif num_jokers == 3:
        if class_without_jokers == 1:
            # If we have a pair, then make a 5 of a kind
            return 6
        # If we have a high card, then make a four of a kind
        return 5
    elif num_jokers == 4:
        # Turn high card into 5 of a kind
        return 6
    elif num_jokers == 5:
        # Get the best hand (5 of a kind)
        return 6

def rank_card2(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 1
    if card == "T":
        return 10
    return int(card)

def rank_bids2(hand_bids):
    hand_to_class = {}
    for i in range(len(hand_bids)):
        hand_to_class[hand_bids[i].split(" ")[0]] = classify_hand2(hand_bids[i])
    n = len(hand_bids)
    while True:
        swapped = False
        for i in range(1, n):
            # Inefficient to not just do the split once when we classify the hand
            # but it's fine
            hand1 = hand_bids[i-1].split(" ")[0]
            hand2 = hand_bids[i].split(" ")[0]
            class1 = hand_to_class[hand1]
            class2 = hand_to_class[hand2]
            if class1 > class2:
                hand_bids[i-1], hand_bids[i] = hand_bids[i], hand_bids[i-1]
                swapped = True
            if class1 == class2:
                for j in range(len(hand1)):
                    card1_rank = rank_card2(hand1[j])
                    card2_rank = rank_card2(hand2[j])
                    if card1_rank > card2_rank:
                        hand_bids[i-1], hand_bids[i] = hand_bids[i], hand_bids[i-1]
                        swapped = True
                        break
                    if card1_rank < card2_rank:
                        break
        n = n - 1 # We know that the last element is sorted, so we needn't check it again
        if not swapped:
            break
    return [int(hand_bid.split(" ")[1]) for hand_bid in hand_bids]


def part1():
    hand_bids = get_input("p7-1.txt")
    sorted_bids = rank_bids(hand_bids)
    winnings = 0
    for i in range(len(sorted_bids)):
        winnings += sorted_bids[i] * (i + 1)
    print(winnings)


def part2():
    hand_bids = get_input("p7-1.txt")
    sorted_bids = rank_bids2(hand_bids)
    winnings = 0
    for i in range(len(sorted_bids)):
        winnings += sorted_bids[i] * (i + 1)
    print(winnings)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
