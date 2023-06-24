from card import Card


class DuplicatedObject():

    def __init__(self, card: Card, count: int) -> None:
        self.card = card
        self.count = count


class Hand:

    def __init__(self, cards: list[Card]) -> None:
        if (len(cards) != 5):
            raise ValueError("len(cards) must be 5")
        self.cards = cards


    def get_card_numbers(self):
        return list(map(lambda x: x.number, self.cards))
    

    def get_card_patterns(self):
        return list(map(lambda x: x.pattern, self.cards))
    

    def get_duplicateds(self) -> list[DuplicatedObject]:
        # 被っているカードを返す
        r = []
        for card in self.cards:
            c = self.get_card_numbers().count(card.number)
            # 最低一つでも被っているかどうか
            if c > 1:
                r.append((card.number, c))       
        return [DuplicatedObject(Card(None, t[0]), t[1]) for t in set(r)]
    

    def get_most_duplicated(self):
        dupls = self.get_duplicateds()
        l = [d.count for d in dupls]
        for d in dupls:
            if d.count == max(l):
                return d


    def inspect(self):
        # TODO 役を判定
        pass


    def is_straight(self) -> bool:
        # ストレートかどうか
        card_numbers = sorted(self.get_card_numbers())
        return card_numbers == list(range(card_numbers[0], card_numbers[-1]+1))
    

    def is_flush(self) -> bool:
        # フラッシュかどうか
        card_patterns = self.get_card_patterns()
        return len(set(card_patterns)) == 1
    

    def is_fourcard(self) -> bool:
        dupl = self.get_most_duplicated()
        return dupl.count == 4
    

    def is_threecard(self) -> bool:
        dupl = self.get_most_duplicated()
        return dupl.count == 3
    


h = Hand([
    Card("spade", 10),
    Card("heart", 10),
    Card("clover", 10),
    Card("diamond", 10),
    Card("spade", 14),
])


print(h.cards[-1].to_str())

print(h.get_most_duplicated())

print(h.is_fourcard())