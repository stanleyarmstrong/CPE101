import unittest
import poly


class TestPoly(unittest.TestCase):
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_poly(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
        poly1 = [3, 4, 5]
        poly2 = [8, 11, 14]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [11, 15, 19])
    def test_poly_mult(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_mult2(poly1, poly2)
        polytest = []
        polytest.append(poly1[0] * poly2[0])
        polytest.append((poly1[0] * poly2[1]) + (poly1[1] + poly2[0]))
        polytest.append((poly1[0] * poly2[2]) + (poly1[1] * poly2[1]) + (poly1[2] * poly2[0]))
        polytest.append((poly1[1] * poly2[2]) + (poly1[2] * poly2[1]))
        polytest.append(poly1[2] * poly2[2])
        self.assertListAlmostEqual(poly3, polytest)
        poly1 = [3, 4, 5]
        poly2 = [8, 11, 14]
        poly3 = poly.poly_mult2(poly1, poly2)
        polytest = []
        polytest.append(poly1[0] * poly2[0])
        polytest.append((poly1[0] * poly2[1]) + (poly1[1] + poly2[0]))
        polytest.append((poly1[0] * poly2[2]) + (poly1[1] * poly2[1]) + (poly1[2] * poly2[0]))
        polytest.append((poly1[1] * poly2[2]) + (poly1[2] * poly2[1]))
        polytest.append(poly1[2] * poly2[2])
        self.assertListAlmostEqual(poly3, polytest)





if __name__ == '__main__':
    unittest.main()
