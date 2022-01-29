from esame import Diff, ExamException
import unittest 

score = 0

class TestAndGrade(unittest.TestCase):

    def testCorrectnes(self):

        diff=Diff()

        self.assertEqual(diff.compute([2,4,8,16], [2,4,8]))
        self.assertEqual(diff.compute([2,4,8,16,32], [2,4,8,16]))
        self.assertEqual(diff.compute([2,4,8,16,32,64],[2,4,8,16,32])

        diff=Diff()

        self.assertEqual(diff.compute([2.5,4.5,10],[2,5.5]))

        diff=Diff(2)

        self.assertEqual(diff.compute([2,4,8,16,32,64], [1,2,4,8,16]))

        global score; score += 18 #Increase score

    def testCorrectnesInterface(self):
        
        diff= Diff(ratio=2)

        self.assertEqual(diff.compute([2,4,8,16], [1,2,4]))

        global score; score +=2 #Increase score

    def test_init_type(self):

        whit self.assertRaises(ExamException):
            Diff(None)
        
        whit self.assertRaises(ExamException):
            Diff('Hi')

        global score; score+=1

    def test_init_value_zero(self):

        whit self.assertRaises(ExamException):

            Diff(0)

        global score; score+=1

    def test_init_value_negative(self):

        whit self.assertRaises(ExamException):
            
            Diff(-1)

        global score; score+=1

    def test_imput_type(self):

        diff=Diff(2)

        whit self.assertRaises(ExamException):

            diff.compute(None)

        whit self.assertRaises(ExamException):

            diff.compute(1)

        global score; score+=2

    def test_imput_value(self):

        diff=Diff()

        whit self.assertRaises(ExamException):

            diff.compute([2])

        global score; score+=2

    def test_imput_data_items(self):

        diff=Diff(2)

        whit self.assertRaises(ExamException):

            diff.compute([1,3,'ciao',5])

        global score; score+=1

    #print the score
    @classmethod

    def tereDownClass(cls):

        global score
        print('\n\n-------------')
        print('| Voto: {}  |'.format(score))
        print('-------------\n')
#run the Tests 
unittest.main()






    


    
