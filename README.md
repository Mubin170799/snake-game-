# 🐍 Python Snake Game

A classic Snake game implementation using Pygame. Control the snake, eat food to grow longer, and avoid hitting the walls or yourself!

## 🎮 Game Features

- Smooth snake movement with arrow key controls
- Score tracking
- Collision detection
- Food spawning system
- Clean object-oriented design
- Comprehensive test suite

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mubin170799/snake-game-.git
cd snake-game
```

2. Create and activate virtual environment:

For Windows:
```bash
python -m venv snake_env
snake_env\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv snake_env
source snake_env/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 🎯 How to Play

1. Run the game:
```bash
python snake_game.py
```

2. Controls:
- ⬆️ Up Arrow: Move up
- ⬇️ Down Arrow: Move down
- ⬅️ Left Arrow: Move left
- ➡️ Right Arrow: Move right

3. Game Rules:
- Eat the red food blocks to grow and increase your score
- Avoid hitting the walls
- Don't collide with yourself
- Try to achieve the highest score possible!

## 🧪 Running Tests

```bash
python -m unittest test_snake_game.py
```

## 🛠️ Project Structure

```
snake-game/
├── snake_game.py      # Main game implementation
├── test_snake_game.py # Test suite
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## 🔧 Technical Details

- **Language**: Python 3
- **Game Engine**: Pygame
- **Testing**: Python unittest framework
- **Architecture**: Object-oriented design
- **Key Components**:
  - Snake movement system
  - Collision detection
  - Food spawning mechanism
  - Score tracking
  - Game state management

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

