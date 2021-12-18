class Statistic():
    def __init__(self):
        self.numbers = [12, 37, 6, 9, 17,7]
        self.min = None
        self.max = None
        self.mean = None
        self.median = None
    def set_number(self):
        self.numbers.append(int(input("Enter number:")))

    def display_numbers(self):
        for i in self.numbers:
            print(i, end=" ")
        print()

    def get_min_number(self):
        self.min = min(self.numbers)

    def get_max_number(self):
        self.max = max(self.numbers)

    def get_mean(self):
        summary = 0
        for i in self.numbers:
            summary += i
        self.mean = summary/len(self.numbers)

    def get_median(self):
        sorted = []
        sorted.extend(self.numbers)
        sorted.sort()
        if len(self.numbers) % 2 == 0:
            self.median = ((sorted[len(self.numbers)//2] + sorted[(len(self.numbers)//2)+1])/2)
        else:
            self.median = sorted[len(self.numbers)//2]

    def display_min(self):
        print(self.min)

    def dsiplay_max(self):
        print(self.max)

    def display_mean(self):
        print(self.mean)

    def display_median(self):
        print(self.median)

