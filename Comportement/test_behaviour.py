import unittest
from behaviour import Behaviour
from obstacle import Obstacle
from can import Can

class TestBehaviour(unittest.TestCase):
    def setUp(self):
        self.behaviour = Behaviour()

    def test_dodgeLeft(self):
        element = self.behaviour.avoidObstacle( Obstacle(0, -50) )
        self.assertEqual(element, 'Dodge Gauche')
    
    def test_dodgeRight(self):
        element = self.behaviour.avoidObstacle( Obstacle(0, 20))
        self.assertEqual(element, 'Dodge Droit')

    def test_catchObject(self):
        element = self.behaviour.catchObject( Can(20000) )
        self.assertEqual(element, 'Object grabed')

    def test_catchObjectThatIsTooFar(self):
        element = self.behaviour.catchObject( Can() )
        self.assertEqual(element, 'Object is too far to be grabed')

    def test_uncatchableObject(self):
        element = self.behaviour.catchObject( Obstacle() )
        self.assertEqual(element, 'Object can\'t be grabed')

if __name__ == '__main__':
    unittest.main()