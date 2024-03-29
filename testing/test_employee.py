import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Runs before everything"""
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """Runs after everything"""
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("John", "Doe", 50000)
        self.emp_2 = Employee("Jane", "Doe", 60000)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "John.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Doe@email.com")
        self.emp_1.first = "Corey"
        self.emp_2.first = "Janet"
        self.assertEqual(self.emp_1.email, "Corey.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Janet.Doe@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "John Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Doe")
        self.emp_1.first = "Corey"
        self.emp_2.first = "Janet"
        self.assertEqual(self.emp_1.fullname, "Corey Doe")
        self.assertEqual(self.emp_2.fullname, "Janet Doe")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def tearDown(self):
        print("tearDown\n")

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("https://company.com/Doe/May")
            self.assertEqual(schedule, "Success")

            # Testing bad response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("https://company.com/Doe/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
