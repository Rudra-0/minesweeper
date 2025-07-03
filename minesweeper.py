import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class Minesweeper:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Minesweeper")
        
        # Theme colors
        self.themes = {
            "light": {
                "bg": "#f0f0f0",
                "button": "#e0e0e0",
                "button_hover": "#d0d0d0",
                "text": "#000000",
                "revealed": "#cccccc",
                "mine": "#ff4444",
                "flag": "#ff8800",
                "numbers": ["#0000ff", "#008000", "#ff0000", "#000080",
                           "#800000", "#008080", "#000000", "#808080"]
            },
            "dark": {
                "bg": "#2c2c2c",
                "button": "#3c3c3c",
                "button_hover": "#4c4c4c",
                "text": "#ffffff",
                "revealed": "#505050",
                "mine": "#ff6666",
                "flag": "#ffaa33",
                "numbers": ["#6666ff", "#66ff66", "#ff6666", "#6666ff",
                           "#ff8080", "#66ffff", "#ffffff", "#aaaaaa"]
            }
        }
        self.current_theme = "light"
        
        # Game parameters
        self.difficulties = {
            "Easy": {"size": 12, "mines": 20},
            "Medium": {"size": 16, "mines": 40},
            "Hard": {"size": 24, "mines": 99}
        }
        
        self.current_difficulty = "Easy"
        self.size = self.difficulties[self.current_difficulty]["size"]
        self.mines = self.difficulties[self.current_difficulty]["mines"]
        
        # Game state
        self.buttons = []
        self.mines_grid = []
        self.flags = set()
        self.revealed = set()
        self.game_over = False
        self.start_time = None
        self.timer = 0
        
        # Configure window
        self.window.configure(bg=self.themes[self.current_theme]["bg"])
        self.window.resizable(False, False)
        
        # Create UI elements
        self.create_top_frame()
        self.create_game_board()
        self.init_game()
        
    def create_top_frame(self):
        # Main top frame
        main_frame = tk.Frame(self.window, bg=self.themes[self.current_theme]["bg"])
        main_frame.pack(pady=10)
        
        # Theme toggle
        self.theme_button = tk.Button(
            main_frame,
            text="🌙" if self.current_theme == "light" else "☀️",
            command=self.toggle_theme,
            font=("Arial", 12),
            width=3,
            bg=self.themes[self.current_theme]["button"],
            fg=self.themes[self.current_theme]["text"]
        )
        self.theme_button.pack(pady=5)
        
        # Difficulty buttons frame
        diff_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]["bg"])
        diff_frame.pack(pady=5)
        
        for diff in self.difficulties.keys():
            btn = tk.Button(
                diff_frame,
                text=diff,
                command=lambda d=diff: self.change_difficulty(d),
                width=8,
                font=("Arial", 10, "bold"),
                bg=self.themes[self.current_theme]["button"],
                fg=self.themes[self.current_theme]["text"]
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.bind_hover_events(btn)
        
        # Info frame
        info_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]["bg"])
        info_frame.pack(pady=10)
        
        # Stylish labels with icons
        self.mine_label = tk.Label(
            info_frame,
            text=f"💣 {self.mines}",
            font=("Arial", 12, "bold"),
            bg=self.themes[self.current_theme]["bg"],
            fg=self.themes[self.current_theme]["text"]
        )
        self.mine_label.pack(side=tk.LEFT, padx=20)
        
        self.time_label = tk.Label(
            info_frame,
            text="⏱️ 0",
            font=("Arial", 12, "bold"),
            bg=self.themes[self.current_theme]["bg"],
            fg=self.themes[self.current_theme]["text"]
        )
        self.time_label.pack(side=tk.LEFT, padx=20)
        
        # Reset button with icon
        self.reset_button = tk.Button(
            info_frame,
            text="🔄 Reset",
            command=self.reset_game,
            font=("Arial", 10, "bold"),
            bg=self.themes[self.current_theme]["button"],
            fg=self.themes[self.current_theme]["text"]
        )
        self.reset_button.pack(side=tk.LEFT, padx=20)
        self.bind_hover_events(self.reset_button)
        
    def create_game_board(self):
        # Main game grid with modern styling
        self.game_frame = tk.Frame(
            self.window,
            bg=self.themes[self.current_theme]["bg"],
            padx=10,
            pady=10
        )
        self.game_frame.pack()
        
        # Adjust button size based on grid size for better fit
        button_size = 2 if self.size <= 16 else 1
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(
                    self.game_frame,
                    width=button_size,
                    height=1,
                    font=("Arial", 9 if self.size <= 16 else 8, "bold"),
                    bg=self.themes[self.current_theme]["button"],
                    fg=self.themes[self.current_theme]["text"]
                )
                btn.grid(row=i, column=j, padx=1, pady=1)
                btn.bind('<Button-1>', lambda e, x=i, y=j: self.click(x, y))
                btn.bind('<Button-3>', lambda e, x=i, y=j: self.flag(x, y))
                self.bind_hover_events(btn)
                row.append(btn)
            self.buttons.append(row)
            
    def bind_hover_events(self, button):
        button.bind('<Enter>', lambda e: button.config(
            bg=self.themes[self.current_theme]["button_hover"]))
        button.bind('<Leave>', lambda e: button.config(
            bg=self.themes[self.current_theme]["button"]))
            
    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.theme_button.config(
            text="🌙" if self.current_theme == "light" else "☀️",
            bg=self.themes[self.current_theme]["button"],
            fg=self.themes[self.current_theme]["text"]
        )
        self.update_theme()
        
    def update_theme(self):
        # Update window
        self.window.configure(bg=self.themes[self.current_theme]["bg"])
        
        # Update all frames
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=self.themes[self.current_theme]["bg"])
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.configure(
                            bg=self.themes[self.current_theme]["button"],
                            fg=self.themes[self.current_theme]["text"]
                        )
                    elif isinstance(child, tk.Label):
                        child.configure(
                            bg=self.themes[self.current_theme]["bg"],
                            fg=self.themes[self.current_theme]["text"]
                        )
                        
        # Update game buttons
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in self.revealed:
                    self.buttons[i][j].configure(
                        bg=self.themes[self.current_theme]["button"],
                        fg=self.themes[self.current_theme]["text"]
                    )
                else:
                    self.buttons[i][j].configure(
                        bg=self.themes[self.current_theme]["revealed"],
                        fg=self.get_number_color(self.mines_grid[i][j])
                    )
                    
    def get_number_color(self, number):
        if number <= 0:
            return self.themes[self.current_theme]["text"]
        return self.themes[self.current_theme]["numbers"][number - 1]
        
    def init_game(self):
        # Initialize mines grid
        self.mines_grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.flags = set()
        self.revealed = set()
        self.game_over = False
        self.start_time = None
        self.timer = 0
        
        # Place mines randomly
        mines_placed = 0
        while mines_placed < self.mines:
            x, y = random.randrange(self.size), random.randrange(self.size)
            if self.mines_grid[x][y] != -1:
                self.mines_grid[x][y] = -1
                mines_placed += 1
                
        # Calculate numbers
        for i in range(self.size):
            for j in range(self.size):
                if self.mines_grid[i][j] != -1:
                    self.mines_grid[i][j] = self.count_adjacent_mines(i, j)
                    
        self.update_mine_counter()
        self.start_timer()
        
    def count_adjacent_mines(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.mines_grid[nx][ny] == -1:
                        count += 1
        return count
    
    def click(self, x, y):
        if self.game_over or (x, y) in self.flags:
            return
            
        if not self.start_time:
            self.start_time = time.time()
            
        if self.mines_grid[x][y] == -1:
            self.game_over = True
            self.reveal_all()
            messagebox.showinfo("Game Over", "You hit a mine!")
            return
            
        self.reveal(x, y)
        
        if len(self.revealed) == self.size * self.size - self.mines:
            self.game_over = True
            messagebox.showinfo("Congratulations", "You won!")
            
    def reveal(self, x, y):
        if (x, y) in self.revealed or (x, y) in self.flags:
            return
            
        self.revealed.add((x, y))
        self.buttons[x][y].config(
            relief=tk.SUNKEN,
            bg=self.themes[self.current_theme]["revealed"]
        )
        
        if self.mines_grid[x][y] == 0:
            self.buttons[x][y].config(text="")
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.reveal(nx, ny)
        else:
            self.buttons[x][y].config(
                text=str(self.mines_grid[x][y]),
                fg=self.get_number_color(self.mines_grid[x][y])
            )
            
    def flag(self, x, y):
        if self.game_over or (x, y) in self.revealed:
            return
            
        if (x, y) in self.flags:
            self.flags.remove((x, y))
            self.buttons[x][y].config(text="")
        else:
            self.flags.add((x, y))
            self.buttons[x][y].config(text="🚩")
            
        self.update_mine_counter()
        
    def reveal_all(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.mines_grid[i][j] == -1:
                    self.buttons[i][j].config(text="💣", background="red")
                elif (i, j) not in self.revealed:
                    self.buttons[i][j].config(text=str(self.mines_grid[i][j]) if self.mines_grid[i][j] > 0 else "")
                    
    def change_difficulty(self, difficulty):
        self.current_difficulty = difficulty
        self.size = self.difficulties[difficulty]["size"]
        self.mines = self.difficulties[difficulty]["mines"]
        
        # Clear existing board
        self.game_frame.destroy()
        
        # Recreate buttons array
        self.buttons = []
        
        # Create new board
        self.create_game_board()
        self.init_game()
        
    def reset_game(self):
        # Clear existing board
        for row in self.buttons:
            for button in row:
                button.config(text="", relief=tk.RAISED, background=self.themes[self.current_theme]["button"])
        self.init_game()
        
    def update_mine_counter(self):
        remaining_mines = self.mines - len(self.flags)
        self.mine_label.config(text=f"💣 {remaining_mines}")
        
    def start_timer(self):
        def update_timer():
            if self.start_time and not self.game_over:
                self.timer = int(time.time() - self.start_time)
                self.time_label.config(text=f"⏱️ {self.timer}")
            self.window.after(1000, update_timer)
        update_timer()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Minesweeper()
    game.run()
