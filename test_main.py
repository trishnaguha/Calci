import unittest
import main
 
class TestCalci(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_add(self):
        self.assertEqual(main.add(3, 4), 7, 'addition is not correct')
 
    def test_sub(self):
        self.assertEqual(main.sub(6, 4), 2, 'subtraction is not correct')

    def test_div(self):
        self.assertEqual(main.div(6, 3), 2, 'division is not correct')

    def test_multi(self):
        self.assertEqual(main.multi(6, 2), 12, 'multiplication is not correct')
 	
 	def test_perc(self):
		self.assertEqual(main.perc(38), 0.38, 'percentage is not correct')

 	def test_fact(self):
		self.assertEqual(main.fact(3), 6, 'factorial is not correct')
        
    def test_squarert(self):
		self.assertEqual(main.squarert(4), 2, 'square root is not correct')

    def test_power(self):
        self.assertEqual(main.power(3, 3), 27, 'power is not correct') 

 	def test_logarithm(self):
		self.assertEqual(main.log(5), 0.69897000433, 'logarithm is not correct')

    def test_sine(self):
        self.assertEqual(main.sin(90), 1, 'sine is not correct')

	def test_cosine(self):
		self.assertEqual(main.cos(0), 1, 'cosine is not correct')

	def test_tangent(self):
		self.assertEqual(main.tan(45), 1, 'tangent is not correct')

	def test_degrees(self):
		self.assertEqual(main.deg(1), 57.2957795131, 'radians to degrees is not correct')

	def test_radians(self):
		self.assertEqual(main.rad(1), 0.0174532925199, 'degrees to radians is not correct')

	def tearDown(self):
		pass
		
if __name__ == '__main__':
    unittest.main()