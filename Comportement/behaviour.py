class Behaviour:
    MAX_WIDTH = 320
    MAX_HEIGHT = 240

    def __init__(self):
        self.data = []

    def avoidObstacle(self, obstacle):
        if obstacle.posX > (Behaviour.MAX_WIDTH / 2):
            return 'Dodge Droit'
        else:
            return 'Dodge Gauche'

