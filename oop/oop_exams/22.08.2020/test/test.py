import unittest

from project.student_report_card import StudentReportCard


class StudentReportTest(unittest.TestCase):

    def test_initialization(self):
        student = StudentReportCard("Deli", 1)
        self.assertEqual("Deli", student.student_name)
        self.assertEqual(1, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_student_name_error(self):
        student = StudentReportCard("Deli", 1)
        with self.assertRaises(ValueError) as ex:
            student.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_student_name_success(self):
        student = StudentReportCard("Deli", 1)
        student.student_name = "Kaloyan"
        self.assertEqual("Kaloyan", student.student_name)

    def test_school_year_error(self):
        student = StudentReportCard("Deli", 1)
        with self.assertRaises(ValueError) as ex:
            student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_error_2(self):
        student = StudentReportCard("Deli", 1)
        with self.assertRaises(ValueError) as ex:
            student.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_success(self):
        student = StudentReportCard("Deli", 1)
        student.school_year = 10
        self.assertEqual(10, student.school_year)
        self.assertEqual("Deli", student.student_name)

    def test_school_year_success_2(self):
        student = StudentReportCard("Deli", 12)
        student.school_year = 12
        self.assertEqual(12, student.school_year)
        self.assertEqual("Deli", student.student_name)

    def test_add_grade_name_there(self):
        student = StudentReportCard("Deli", 1)
        student.grades_by_subject = {"Deli": [4]}
        student.add_grade("Deli", 5)
        self.assertEqual({"Deli": [4, 5]}, student.grades_by_subject)

    def test_add_grade_name_not_there(self):
        student = StudentReportCard("Kaloyan", 1)
        student.grades_by_subject = {"Kaloyan": [4]}
        student.add_grade("Deli", 5)
        self.assertEqual({"Kaloyan": [4], "Deli": [5]}, student.grades_by_subject)

    def test_average_grade_by_subject(self):
        student = StudentReportCard("Deli", 1)
        student.grades_by_subject = {"Deli": [4, 5]}
        result = student.average_grade_by_subject()
        self.assertEqual(f"Deli: 4.50", result)
        self.assertEqual({"Deli": [4, 5]}, student.grades_by_subject)

    def test_average_grade_for_all_subjects(self):
        student = StudentReportCard("Deli", 1)
        student.grades_by_subject = {"Deli": [5, 5], "Kaloyan": [5, 5]}
        result = student.average_grade_for_all_subjects()
        self.assertEqual(f"Average Grade: 5.00", result)

    def test_repr_success(self):
        student = StudentReportCard("Deli", 1)
        student.grades_by_subject = {"Deli": [5, 5]}
        expected = f"Name: Deli" + "\n"
        expected += f"Year: 1" + "\n"
        expected += f"----------" + "\n"
        expected += f"Deli: 5.00" + "\n"
        expected += f"----------" + "\n"
        expected += f"Average Grade: 5.00"
        self.assertEqual(expected, student.__repr__())

    def test_repr_success_2(self):
        student = StudentReportCard("Deli", 1)
        student.grades_by_subject = {"History": [5, 5], "Math": [5, 5]}
        expected = ""
        expected += f"Name: Deli" + "\n"
        expected += f"Year: 1" + "\n"
        expected += f"----------" + "\n"
        expected += f"History: 5.00" + "\n"
        expected += f"Math: 5.00" + "\n"
        expected += f"----------" + "\n"
        expected += f"Average Grade: 5.00"
        self.assertEqual(expected, student.__repr__())


if __name__ == '__main__':
    unittest.main()

