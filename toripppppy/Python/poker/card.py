class Card:

    def __init__(self, pattern: str, number: int) -> None:
        if pattern not in pattern_icon_dict.keys():
            if pattern is not None:
                raise ValueError(f"\"{pattern}\" is not trump pattern")
            
        self.pattern = pattern

        if number < 1 or 14 < number:
            raise ValueError(f"{number} is out of range")
        
        if number == 1:
            number = 14
            
        self.number = number


    ### magic methods

    def __eq__(self, __value: object) -> bool:
        return self.number == __value.number and self.pattern == __value.pattern
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __lt__(self, __value: object):
        return self.number < __value.number

    def __le__(self, __value: object):
        return self.number <= __value.number
    
    def __hash__(self) -> int:
        return hash(self.to_str())
    
    ###

    def get_icon_from_pattern(self):
        return pattern_icon_dict[self.pattern]
    
    def adjust_number_notation(self):
        res = ""
        if self.number in number_char_dict.keys():
            res = number_char_dict[self.number]
        else:
            res = str(self.number)

        return res.rjust(2)


    def to_str(self) -> str:
        # カードの文字列として完成させて返す
        def colored_red(text: str) -> str:
            return "\033[107m\033[31m" + text + "\033[0m"

        def colored_black(text: str) -> str:
            return "\033[107m\033[30m" + text + "\033[0m"
        
        res = self.get_icon_from_pattern()
        res += self.adjust_number_notation()

        if self.pattern in ["diamond", "heart"]:
            return colored_red(res)
        else:
            return colored_black(res)
        


pattern_icon_dict = {
    "clover": "♣︎",
    "diamond": "◆",
    "heart": "❤︎",
    "spade": "♠︎",
}

number_char_dict = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
}