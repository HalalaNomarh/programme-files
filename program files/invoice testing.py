import unittest, INVOICEGENERATOR
class TestInvoiceGen(unittest.TestCase):
    def test_add_item(self):
        self.assertEqual(INVOICEGENERATOR.invoiceGenarator.mult(2,4),8)
        self.assertTrue(INVOICEGENERATOR.invoiceGenarator.mult(2,4) == 8)

if __name__ == "__main__":
    unittest.main()