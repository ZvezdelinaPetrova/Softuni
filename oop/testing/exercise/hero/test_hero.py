import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def test_initialization(self):
        hero = Hero("Deli", 100, 50, 5)
        self.assertEqual("Deli", hero.username)
        self.assertEqual(100, hero.level)
        self.assertEqual(50, hero.health)
        self.assertEqual(5, hero.damage)

    def test_battle(self):
        hero = Hero("Deli", 100, 50, 5)
        hero2 = Hero("Deli", 1001, 504, 5)
        with self.assertRaises(Exception) as ex:
            hero.battle(hero2)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_less_than_zero(self):
        hero = Hero("Deli", 100, 0, 5)
        hero2 = Hero("B", 1001, 504, 5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_less_than_zero_enemy(self):
        hero = Hero("Deli", 100, 50, 5)
        hero2 = Hero("B", 1001, 0, 5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(hero2)
        self.assertEqual(f"You cannot fight B. He needs to rest", str(ex.exception))

    def test_if_battle_draw(self):
        hero = Hero("Deli", 30, 50, 5)
        hero2 = Hero("B", 30, 30, 5)
        actual = hero.battle(hero2)
        self.assertEqual("Draw", actual)

    def test_if_hero_win(self):
        hero = Hero("Deli", 10, 50, 5)
        hero2 = Hero("B", 2, 20, 2)
        actual = hero.battle(hero2)
        self.assertEqual("You win", actual)
        self.assertEqual(11, hero.level)
        self.assertEqual(51, hero.health)
        self.assertEqual(10, hero.damage)

    def test_you_lose(self):
        hero = Hero("Deli", 2, 20, 2)
        hero2 = Hero("B", 52, 1000, 30)
        actual = hero.battle(hero2)
        self.assertEqual("You lose", actual)
        self.assertEqual(53, hero2.level)
        self.assertEqual(1001, hero2.health)
        self.assertEqual(35, hero2.damage)

    def test_str(self):
        hero = Hero("Deli", 2, 20, 2)
        actual = hero.__str__()
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
               f"Health: {hero.health}\n" \
               f"Damage: {hero.damage}\n"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()