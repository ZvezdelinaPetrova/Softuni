import unittest

from project.team import Team


class TeamTest(unittest.TestCase):

    def test_initialization(self):
        team = Team("Deli")
        self.assertEqual("Deli", team.name)
        self.assertEqual({}, team.members)

    def test_name_error(self):
        team = Team("Deli")
        with self.assertRaises(ValueError) as ex:
            team.name = "123D"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_success(self):
        team = Team("Deli")
        team.name = "Kaloyan"
        self.assertEqual("Kaloyan", team.name)

    def test_add_member(self):
        team = Team("Deli")
        result = team.add_member(Kaloyan=30, Mima=20)
        self.assertEqual({"Kaloyan": 30, "Mima": 20}, team.members)
        self.assertEqual(f"Successfully added: Kaloyan, Mima", result)

    def test_remove_member(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30, "Mima": 20}
        result = team.remove_member("Mima")
        self.assertEqual(f"Member Mima removed", result)
        self.assertEqual({"Kaloyan": 30}, team.members)

    def test_remove_member_not_exist(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30, "Mima": 20}
        result = team.remove_member("Georgi")
        self.assertEqual(f"Member with name Georgi does not exist", result)

    def test_gt(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 15, "Deli": 20}
        team2 = Team("BBB")
        team2.members = {"Grigor": 14}
        result = team.__gt__(team2)
        self.assertEqual(True, result)
        # team.members["pesho"] = 21
        # team.members["goso"] = 22
        # another_team = Team("Another")
        # another_team.members["mem1"] = 22
        # another_team.members["mem2"] = 24
        # another_team.members["mem3"] = 25
        # self.assertEqual(True, another_team > team)
        # self.assertEqual(False, another_team < team)

    def test_gt_false(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30}
        team2 = Team("BBB")
        team2.members = {"Grigor": 14, "Mima": 20}
        result = team.__gt__(team2)
        self.assertEqual(False, result)

    def test_len(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30}
        result = team.__len__()
        self.assertEqual(1, result)

    def test_add(self):
        team = Team("Deli")
        team2 = Team("BBB")
        team.members = {"Kaloyan": 30, "Mima": 20}
        team2.members = {"Grigor": 14}
        new_team_name = f"{team.name}{team2.name}"
        team3 = team.__add__(team2)
        self.assertEqual({"Kaloyan": 30, "Mima": 20, "Grigor": 14}, team3.members)
        self.assertEqual("DeliBBB", new_team_name)
        self.assertEqual("DeliBBB", team3.name)

    def test_str_success(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30}
        expected = f"Team name: {team.name}" + "\n"
        expected += f"Member: Kaloyan - 30-years old"
        self.assertEqual(expected, team.__str__())

    def test_str_years(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30, "Mima": 32}
        expected = f"Team name: {team.name}" + "\n"
        expected += f"Member: Mima - 32-years old" + "\n"
        expected += f"Member: Kaloyan - 30-years old"
        self.assertEqual(expected, team.__str__())

    def test_str_years_equal(self):
        team = Team("Deli")
        team.members = {"Kaloyan": 30, "Ari": 30}
        expected = f"Team name: {team.name}" + "\n"
        expected += f"Member: Ari - 30-years old" + "\n"
        expected += f"Member: Kaloyan - 30-years old"
        self.assertEqual(expected, team.__str__())

    def test_team_str__without_members__expected_correct_str(self):
        team = Team("Deli")
        expected = "Team name: Deli"
        actual = team.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()















