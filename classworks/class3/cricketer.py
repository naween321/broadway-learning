class Cricketer:
    def __init__(self, name, age, number_of_matches):
        self.name = name
        self.age = age
        self.number_of_matches = number_of_matches

    def get_info(self):
        print(f"Name of the cricketer is {self.name}")
        print(f"Age of the cricketer is {self.age}")
        print(f"Matches played by the cricketer is {self.number_of_matches}")


class Batsman(Cricketer):
    def __init__(self, name, age, number_of_matches, runs, centuries):
        self.runs = runs
        self.centuries = centuries
        super().__init__(name, age, number_of_matches)

    def get_info(self):
        super().get_info()
        print(f"Number of runs made is {self.runs}")
        print(f"Centuries made is {self.centuries}")


class Bowler(Cricketer):
    def __init__(self, name, age, number_of_matches, wickets):
        self.wickets = wickets
        super().__init__(name, age, number_of_matches)

    def get_info(self):
        super().get_info()
        print(f"Number of wickets taken is {self.wickets}")


batsman1 = Batsman("Virat", 29, 1000, 12, 50)
bowler = Bowler("Malla", 30, 500, 100)
batsman1.get_info()
bowler.get_info()