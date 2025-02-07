import unittest
from snake_game import SnakeGame, Direction, Point, BLOCK_SIZE

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = SnakeGame(640, 480)

    def test_initialization(self):
        self.assertEqual(self.game.width, 640)
        self.assertEqual(self.game.height, 480)
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.direction, Direction.RIGHT)
        self.assertEqual(self.game.score, 0)

    def test_place_food(self):
        food = self.game._place_food()
        self.assertIsInstance(food, Point)
        self.assertTrue(0 <= food.x < self.game.width)
        self.assertTrue(0 <= food.y < self.game.height)
        self.assertTrue(food.x % BLOCK_SIZE == 0)
        self.assertTrue(food.y % BLOCK_SIZE == 0)

    def test_collision_with_boundary(self):
        # Test collision with right wall
        self.game.head = Point(self.game.width, self.game.height//2)
        self.assertTrue(self.game._is_collision())

        # Test collision with left wall
        self.game.head = Point(-BLOCK_SIZE, self.game.height//2)
        self.assertTrue(self.game._is_collision())

        # Test collision with top wall
        self.game.head = Point(self.game.width//2, -BLOCK_SIZE)
        self.assertTrue(self.game._is_collision())

        # Test collision with bottom wall
        self.game.head = Point(self.game.width//2, self.game.height)
        self.assertTrue(self.game._is_collision())

    def test_collision_with_self(self):
        self.game.head = self.game.snake[1]
        self.assertTrue(self.game._is_collision())

    def test_movement(self):
        initial_head = self.game.head
        
        # Test RIGHT movement
        self.game._move(Direction.RIGHT)
        self.assertEqual(self.game.head.x, initial_head.x + BLOCK_SIZE)
        self.assertEqual(self.game.head.y, initial_head.y)

        # Test LEFT movement
        self.game._move(Direction.LEFT)
        self.assertEqual(self.game.head.x, initial_head.x)
        self.assertEqual(self.game.head.y, initial_head.y)

        # Test UP movement
        self.game._move(Direction.UP)
        self.assertEqual(self.game.head.x, initial_head.x)
        self.assertEqual(self.game.head.y, initial_head.y - BLOCK_SIZE)

        # Test DOWN movement
        self.game._move(Direction.DOWN)
        self.assertEqual(self.game.head.x, initial_head.x)
        self.assertEqual(self.game.head.y, initial_head.y)

    def test_reset(self):
        # Change some game state
        self.game.score = 10
        self.game.direction = Direction.LEFT
        
        # Reset the game
        self.game.reset()
        
        # Verify reset state
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.direction, Direction.RIGHT)
        self.assertEqual(len(self.game.snake), 3)

if __name__ == '__main__':
    unittest.main() 