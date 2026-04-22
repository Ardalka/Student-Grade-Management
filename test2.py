import unittest
from Task6.1.py import rank_students_by_average

class TestRankStudents(unittest.TestCase):

    # -------------------------
    # Input–Output Tests
    # -------------------------
    def test_correct_ranking(self):
        students = [
            {"name": "A", "scores": [100, 90]},
            {"name": "B", "scores": [70, 80]},
            {"name": "C", "scores": [50, 60]}
        ]
        ranked = rank_students_by_average(students)
        self.assertEqual(ranked[0]["name"], "A")
        self.assertEqual(ranked[-1]["name"], "C")

    # -------------------------
    # Edge Cases
    # -------------------------
    def test_empty_scores(self):
        students = [{"name": "A", "scores": []}]
        ranked = rank_students_by_average(students)
        self.assertEqual(ranked[0]["average"], 0)

    def test_missing_scores_key(self):
        students = [{"name": "A"}]
        ranked = rank_students_by_average(students)
        self.assertEqual(ranked[0]["average"], 0)

    def test_same_average(self):
        students = [
            {"name": "A", "scores": [80, 80]},
            {"name": "B", "scores": [80, 80]}
        ]
        ranked = rank_students_by_average(students)
        self.assertEqual(len(ranked), 2)

if __name__ == "__main__":
    unittest.main()
