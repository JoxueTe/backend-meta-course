class MyFirstClass:
    print("Who wrote this?")
    index = "Autho-Book"

    def __init__(self, philosopher, book) -> None:
        self.philosopher = philosopher
        self.book = book

    def hand_list(self):
        print(self.philosopher + " wrote the book: " + self.book)


whodunnit = MyFirstClass("Sun Tzu", "The art of war")
print(whodunnit.hand_list())
