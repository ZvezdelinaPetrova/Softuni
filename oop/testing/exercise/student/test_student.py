import unittest

from project.student import Student


class StudentTest(unittest.TestCase):

    def test_initialization(self):
        student = Student("Deli")
        self.assertEqual("Deli", student.name)
        self.assertEqual({}, student.courses)

    def test_init_curse(self):
        student = Student("Deli", {"Java": ["n1", "n2"]})
        self.assertEqual("Deli", student.name)
        self.assertEqual({"Java": ["n1", "n2"]}, student.courses)

    def test_if_enroll_success(self):
        student = Student("Deli", {"Java": ["n1", "n2"]})
        result = student.enroll("Java", "n", "b")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Java": ["n1", "n2", "n"]}, student.courses)

    def test_if_enroll_success_one(self):
        student = Student("Deli", {"Java": ["n1"]})
        result = student.enroll("Python", ["n1"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Java": ["n1"], "Python": ["n1"]}, student.courses)

    def test_if_enroll_success_one_empty(self):
        student = Student("Deli", {"Java": ["n1"]})
        result = student.enroll("Python", ["n1"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Java": ["n1"], "Python": ["n1"]}, student.courses)

    def test_if_enroll_empty_list(self):
        student = Student("Deli", {"Java": ["n1"]})
        result = student.enroll("Python", "n4", "ddd")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Java": ["n1"], "Python": []}, student.courses)

    def test_add_notes(self):
        student = Student("Deli", {"Java": ["n1"]})
        result = student.add_notes("Java", "n4")
        self.assertEqual("Notes have been updated", result)

    def test_if_make_empty(self):
        student = Student("Deli", {"Java": ["n1"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Python", "n4")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        student = Student("Deli", {"Java": ["n1"]})
        result = student.leave_course("Java")
        self.assertEqual("Course has been removed", result)

    def test_leave_not_found(self):
        student = Student("Deli", {"Java": ["n1"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    unittest.main()





# import unittest
#
#
# from project.student import Student
# # from oop.testing.exercise.student.student import Student
#
#
# class TestStudent(unittest.TestCase):
#     def test_initialization(self):
#         student = Student("Deli", courses=None)
#         self.assertEqual("Deli", student.name)
#         self.assertEqual({}, student.courses)
#
#     def test_initialization_2(self):
#         student = Student("Deli", {})
#         self.assertEqual("Deli", student.name)
#         self.assertEqual({}, student.courses)
#
#     # def test_initialization(self):
#     #     student = Student("Deli")
#     #     self.assertEqual("Deli", student.name)
#     #     self.assertEqual({}, student.courses)
#     #
#     # def test_init_curse(self):
#     #     student = Student("Deli", {"Java": ["n1", "n2"]})
#     #     self.assertEqual("Deli", student.name)
#     #     self.assertEqual({"Java": ["n1", "n2"]}, student.courses)
#
#     def test_enroll_course_already_added(self):
#         student = Student("Deli", {})
#         student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#         for i in student.courses.keys():
#             if i == "Python":
#                 expected = student.enroll("Python", "d", "v")
#                 self.assertEqual("Course already added. Notes have been updated.", expected)
#
#     def test_enroll_notes_y(self):
#         student = Student("Deli", {})
#         student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#         actual = student.enroll("PHP", "d", "Y")
#         student.courses["PHP"] = "d"
#         self.assertEqual("Course and course notes have been added.", actual)
#
#     def test_enroll_notes_empty(self):
#         student = Student("Deli", {})
#         student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#         actual = student.enroll("PHP", "d", "")
#         student.courses["PHP"] = "d"
#         self.assertEqual("Course and course notes have been added.", actual)
#
#     def test_enroll_new_course(self):
#         student = Student("Deli", {})
#         expected = student.enroll("PHP", ["T"], "N")
#         self.assertEqual("Course has been added.", expected)
#         self.assertEqual([], student.courses["PHP"])
#
#     # def test_add_notes(self):
#     #     student = Student("Deli", {})
#     #     student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#     #     actual = student.add_notes("Python", "d")
#     #     student.courses["Python"].append("d")
#     #     self.assertEqual("Notes have been updated", actual)
#
#     # def test_leave_course(self):
#     #     student = Student("Deli", {})
#     #     student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#     #     actual = student.leave_course("Python")
#     #     # student.courses["Python"].append("d")
#     #     self.assertEqual("Course has been removed", actual)
#
#     def test_add_notes_error(self):
#         student = Student("Deli", {})
#         student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#         with self.assertRaises(Exception) as ex:
#             student.add_notes("PHP", "d")
#         self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
#
#     def test_leave_course_error(self):
#         student = Student("Deli", {})
#         student.courses = {"Python": ["shit", "hard"], "JS": ["more_shits", "damn"]}
#         with self.assertRaises(Exception) as ex:
#             student.leave_course("PHP")
#         self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
#
#
# if __name__ == '__main__':
#     unittest.main()