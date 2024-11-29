import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self, time):
        self.distance += self.speed * time

    def walk(self, time):
        self.distance += (self.speed / 2) * time

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

class Tournament:
    def __init__(self, distance):
        self.distance = distance
        self.runners = []

    def add_runner(self, runner):
        self.runners.append(runner)

    def start(self):
        results = {}
        for runner in self.runners:
            time = self.distance / runner.speed
            runner.run(time)
            results[runner.name] = runner.distance
        return results


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrei = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты всех тестов:")
        for name, result in cls.all_results.items():
            print(f"{name}: {result}")

    def test_race_usain_nik(self):
        tournament = Tournament(distance=90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.nik)
        results = tournament.start()
        self.all_results[(90, "Усэйн, Ник")] = results
        self.assertTrue(max(results, key=lambda k: results[k]) == "Усэйн")

    def test_race_andrei_nik(self):
        tournament = Tournament(distance=90)
        tournament.add_runner(self.andrei)
        tournament.add_runner(self.nik)
        results = tournament.start()
        self.all_results[(90, "Андрей, Ник")] = results
        self.assertTrue(max(results, key=lambda k: results[k]) == "Андрей")

    def test_race_usain_andrei_nik(self):
        tournament = Tournament(distance=90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.andrei)
        tournament.add_runner(self.nik)
        results = tournament.start()
        self.all_results[(90, "Усэйн, Андрей, Ник")] = results
        self.assertTrue(max(results, key=lambda k: results[k]) == "Усэйн")


if __name__ == "__main__":
    unittest.main()