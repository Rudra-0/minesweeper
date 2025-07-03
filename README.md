# 🎮 Modern Minesweeper

A feature-rich, modern implementation of the classic Minesweeper game built with Python and Tkinter. This version includes themes, multiple difficulty levels, and an enhanced user interface with icons and modern styling.

## ✨ Features

### 🎯 Gameplay Features
- **Three Difficulty Levels**: Easy (12x12, 20 mines), Medium (16x16, 40 mines), Hard (24x24, 99 mines)
- **Smart Reveal**: Auto-reveal adjacent empty cells
- **Flag System**: Right-click to flag suspected mines
- **Timer**: Track your solving time
- **Mine Counter**: Shows remaining unflagged mines
- **Win/Loss Detection**: Clear victory and defeat conditions

### 🎨 Modern UI Features
- **Dual Themes**: Light and dark mode with smooth transitions
- **Icon Integration**: Emojis for mines (💣), flags (🚩), timer (⏱️), and reset (🔄)
- **Hover Effects**: Interactive button hover states
- **Responsive Design**: Adaptive button sizing based on grid size
- **Color-Coded Numbers**: Different colors for different mine counts
- **Modern Styling**: Sleek, contemporary interface design

### 🎮 Controls
- **Left Click**: Reveal tile
- **Right Click**: Toggle flag on tile
- **Theme Button**: Switch between light/dark themes (🌙/☀️)
- **Difficulty Buttons**: Change game difficulty (Easy/Medium/Hard)
- **Reset Button**: Start new game (🔄 Reset)

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Tkinter (included with most Python installations)

### Installation

1. **Clone or download the repository**:
   ```bash
   git clone <your-repo-url>
   cd minesweaper
   ```

2. **Run the game**:
   ```bash
   python minesweeper.py
   ```

## 🎯 How to Play

1. **Start the Game**: Run `python minesweeper.py`
2. **Choose Difficulty**: Click Easy, Medium, or Hard buttons
3. **Toggle Theme**: Click the moon/sun button for dark/light theme
4. **Reveal Tiles**: Left-click on tiles to reveal them
5. **Flag Mines**: Right-click to flag suspected mines
6. **Win Condition**: Reveal all non-mine tiles
7. **Lose Condition**: Click on a mine

### 🏆 Game Rules
- Numbers indicate how many mines are adjacent to that tile
- Use logic and deduction to avoid mines
- Flag tiles you suspect contain mines
- Clear all safe tiles to win

## 🎨 Themes

### Light Theme
- Clean, bright interface
- High contrast for easy visibility
- Professional appearance

### Dark Theme
- Easy on the eyes for long gaming sessions
- Modern dark UI
- Vibrant accent colors

## 🎮 Difficulty Levels

| Difficulty | Grid Size | Mines | Ideal For |
|------------|-----------|-------|-----------|
| Easy       | 12x12     | 20    | Beginners |
| Medium     | 16x16     | 40    | Intermediate |
| Hard       | 24x24     | 99    | Experts |

## 🛠️ Technical Features

- **Object-Oriented Design**: Clean, maintainable code structure
- **Event-Driven Architecture**: Responsive user interactions
- **Dynamic UI Updates**: Real-time theme switching
- **Recursive Reveal Algorithm**: Efficient empty cell revelation
- **State Management**: Proper game state tracking

## 📁 Project Structure

```
minesweaper/
├── minesweeper.py      # Main game implementation
├── README.md           # Project documentation
└── requirements.txt    # Dependencies (optional)
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Classic Minesweeper game by Microsoft
- Python Tkinter community
- Modern UI/UX design principles

---

**Enjoy playing! 🎮** If you find any bugs or have suggestions, please open an issue.
