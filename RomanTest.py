import unittest

class RomanTest(unittest.TestCase):

	def test_1shouldBeI(self):
		self.assertEqual(self.roman(1), "I")

	def test_2shouldBeII(self):
		self.assertEqual(self.roman(2), "II")

	def test_3shouldBeIII(self):
		self.assertEqual(self.roman(3), "III")

	def test_4shouldBeIV(self):
		self.assertEqual(self.roman(4), "IV")

	def test_5shouldBeV(self):
		self.assertEqual(self.roman(5), "V")

	def test_6shouldBeVI(self):
		self.assertEqual(self.roman(6), "VI")

	def test_8shouldBeVI(self):
		self.assertEqual(self.roman(8), "VIII")

	def test_10shouldBeX(self):
		self.assertEqual(self.roman(10), "X")

	def test_7shouldBeVII(self):
		self.assertEqual(self.roman(7), "VII")

	def test_9shouldBeIX(self):
		self.assertEqual(self.roman(9), "IX")

	def test_11shouldBeXI(self):
		self.assertEqual(self.roman(11), "XI")

	def test_12shouldBeXII(self):
		self.assertEqual(self.roman(12), "XII")

	def test_1KshouldBeM(self):
		self.assertEqual(self.roman(1000), "M")

	def test_2KshouldBe(self):
		self.assertEqual(self.roman(2000), "MM")

	def test_100shoudl

	def roman_thousands(self, nb):
		m = nb / 1000
		t = ""
		i = 1

		while i <= m:
			t += "M"
			i += 1

		return t

	def roman_hundreds(self, nb):
		return "C"

	def roman_unit(self, nb):
		result = ""

		rest = nb % 10
		if rest > 0 and rest < 4:
			i = 1;
			while i<= nb:
				i += 1
				result = result + "I"
		elif rest == 4:
			result = "IV"
		elif nb == 5:
			result = "V"
		elif nb > 5 and nb < 9:
			rest = nb % 5
			result = "V"
			i = 1;
			while i<= rest:
				i += 1
				result = result + "I"
		elif rest == 9:
			result = "IX"
		elif rest == 0:
			result = "X"

		return result

	def roman(self, nb):
		t = ""

		if nb > 10:
			if nb == 11:
				return "XI"
			elif nb == 12:
				return "XII"
			else:
				return self.roman_thousands(nb)


		else:
			t = self.roman_unit(nb)

		return t

if __name__ == '__main__':
	unittest.main()