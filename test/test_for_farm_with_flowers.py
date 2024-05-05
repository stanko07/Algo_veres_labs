import unittest
import os
from farm_with_flowers import max_flow

cur_path = os.path.dirname(__file__)


class TestMaxCarsDelivery(unittest.TestCase):

    def test_max_cars_delivery(self):
        """Test case with normal data"""
        with open(cur_path + "/roads2.csv", 'w') as file:
            file.write("""F1,F2
S1,S2
F2,S1,8
F1,R1,3
F1,R2,10
F1,R3,5
R1,R4,3
R2,R4,2
R2,S2,3
R3,R2,6
R3,S1,4
R4,S1,8
R4,R3,6""")

        max_cars = max_flow(
            cur_path + "/roads2.csv"
        )
        print("Max cars:", max_cars)
        self.assertEqual(max_cars, 12)


    def test_max_cars_delivery2(self):
        with open(cur_path + "/roads.csv", 'w') as file:
            file.write("""F1,F2
S1,S2
F1,R1,3
F1,R2,10
F1,R3,5
R3,R2,6
R4,S1,8
R4,R3,6""")

        max_cars = max_flow(
            cur_path + "/roads.csv"
        )

        print("Max cars:", max_cars)
        self.assertEqual(max_cars, 0)


if __name__ == "__main__":
    unittest.main()
