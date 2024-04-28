import unittest
import functions as f


class Test_functions(unittest.TestCase):
    
    def test_create_acc(self):
        self.assertTrue(f.create_account("Luis", "Garcia", "01/22/2006", "13455 NoName Rd", "luis@gmail.com", "1234"))

    def test_log_in(self):
        self.assertTrue(f.log_in("sebastianmes2007@gmail.com", "4444"))
        self.assertFalse(f.log_in("sebastianmes2007@gmail.com", "8888"))
    
    def test_get_id(self):
        self.assertEqual(f.get_id(["sebastianmes2007@gmail.com"]), (4,))
    
    
    def test_update_acc(self):
        self.assertFalse(f.update_acc((4,),"balance", "100"))
    
if __name__ == '__main__':
    unittest.main()