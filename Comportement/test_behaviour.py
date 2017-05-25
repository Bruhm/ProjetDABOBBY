import unittest
from behaviour import Behaviour
from obstacle import Obstacle

class TestBehaviour(unittest.TestCase):
    def setUp(self):
        self.behaviour = Behaviour()

    def test_dodgeLeft(self):
        element = self.behaviour.avoidObstacle( Obstacle(0, 100) )
        self.assertEqual(element, 'Dodge Gauche')
    
    def test_dodgeRight(self):
        element = self.behaviour.avoidObstacle( Obstacle(200, 100))
        self.assertEqual(element, 'Dodge Droit')

if __name__ == '__main__':
    unittest.main()