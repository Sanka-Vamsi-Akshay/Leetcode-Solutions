class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinationList = []
        self.n = len(characters)
        self.characters = characters
        self.combinationLength = combinationLength
        self.allCombinations('', 0)

    def next(self) -> str:
        return self.combinationList.pop(0)        

    def hasNext(self) -> bool:
        return bool(self.combinationList)

    def allCombinations(self, word: str, idx: int) -> list[str]:
        if len(word) == self.combinationLength:
            self.combinationList.append(word)
            return
        for i in range(idx, self.n):
            self.allCombinations(word + self.characters[i], i + 1)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()