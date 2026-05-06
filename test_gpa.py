import unittest
from grades import grades_to_gpa


class TestGradesToGPA(unittest.TestCase):


    def test_fail_grade(self):
        self.assertEqual(grades_to_gpa(45), 0.0)

    def test_pass_grade(self):
        self.assertEqual(grades_to_gpa(55), 1.0)

    def test_average_grade(self):
        self.assertEqual(grades_to_gpa(65), 2.0)

    def test_good_grade(self):
        self.assertEqual(grades_to_gpa(75), 3.0)

    def test_very_good_grade(self):
        self.assertEqual(grades_to_gpa(85), 4.0)

    def test_excellent_grade(self):
        self.assertEqual(grades_to_gpa(95), 5.0)


    def test_boundary_50(self):
        self.assertEqual(grades_to_gpa(50), 1.0)

    def test_boundary_60(self):
        self.assertEqual(grades_to_gpa(60), 2.0)

    def test_boundary_70(self):
        self.assertEqual(grades_to_gpa(70), 3.0)

    def test_boundary_80(self):
        self.assertEqual(grades_to_gpa(80), 4.0)

    def test_boundary_90(self):
        self.assertEqual(grades_to_gpa(90), 5.0)


    def test_negative_score(self):
        self.assertIsNone(grades_to_gpa(-5))

    def test_score_above_100(self):
        self.assertIsNone(grades_to_gpa(105))


if __name__ == "__main__":
    unittest.main()