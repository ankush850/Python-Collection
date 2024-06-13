import tkinter as tk
import os
from time import strftime

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Theme configurations
        self.themes = {
            'light': {
                'bg': 'white',
                'fg': 'black',
                'frame_bg': 'white'
            },
            'dark': {
                'bg': '#22478a',
                'fg': 'white',
                'frame_bg': '#22478a'
            }
        }
        
        self.current_theme = 'dark'
        self.time_label = None
        self.main_frame = None
        
        self.setup_ui()
        self.update_time()
    
    def setup_ui(self):
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]['frame_bg'])
        self.main_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        
        # Create time label
        self.time_label = tk.Label(
            self.main_frame, 
            font=('calibri', 40, 'bold'),
            bg=self.themes[self.current_theme]['bg'],
            fg=self.themes[self.current_theme]['fg']
        )
        self.time_label.pack(expand=True)
        
        # Create menu
        self.create_menu()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        theme_menu = tk.Menu(menubar, tearoff=0)
        
        theme_menu.add_command(label="Light Theme", command=lambda: self.switch_theme('light'))
        theme_menu.add_command(label="Dark Theme", command=lambda: self.switch_theme('dark'))
        theme_menu.add_separator()
        theme_menu.add_command(label="Exit", command=self.root.quit)
        
        menubar.add_cascade(label="Theme", menu=theme_menu)
        self.root.config(menu=menubar)
    
    def switch_theme(self, theme_name):
        """Switch between light and dark themes"""
        if theme_name not in self.themes:
            return
        
        self.current_theme = theme_name
        
        # Destroy old frame and label
        if self.main_frame:
            self.main_frame.destroy()
        
        # Create new frame with new theme
        self.main_frame = tk.Frame(
            self.root, 
            bg=self.themes[self.current_theme]['frame_bg']
        )
        self.main_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        
        # Create new label with new theme colors
        self.time_label = tk.Label(
            self.main_frame,
            font=('calibri', 40, 'bold'),
            bg=self.themes[self.current_theme]['bg'],
            fg=self.themes[self.current_theme]['fg']
        )
        self.time_label.pack(expand=True)
    
    def update_time(self):
        """Update time every second"""
        string = strftime('%I:%M:%S %p')
        if self.time_label:
            self.time_label.config(text=string)
        self.root.after(1000, self.update_time)
    
    def run(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = DigitalClock()
    app.run()
