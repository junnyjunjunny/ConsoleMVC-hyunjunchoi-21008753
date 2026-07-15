import unittest

from app.models.sample import Sample, SampleModel


class SampleModelTest(unittest.TestCase):
    def setUp(self):
        self.model = SampleModel()
        self.model.add(Sample("S-001", "실리콘 웨이퍼-8인치", 0.5, 0.92, 480))

    def test_add_duplicate_raises(self):
        with self.assertRaises(ValueError):
            self.model.add(Sample("S-001", "dup", 0.1, 0.9, 0))

    def test_get_missing_raises(self):
        with self.assertRaises(KeyError):
            self.model.get("S-999")

    def test_search_by_name(self):
        results = self.model.search_by_name("실리콘")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].sample_id, "S-001")

    def test_list_all(self):
        self.assertEqual(len(self.model.list_all()), 1)


if __name__ == "__main__":
    unittest.main()
