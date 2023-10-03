def playing_domino(cards, deck):
    for card in cards:
        if card[0] == deck[0] or card[0] == deck[1] or card[1] == deck[0] or card[1] == deck[1]:
            return card
    return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []