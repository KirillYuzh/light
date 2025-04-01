import tkinter as tk

class ClickCounter:
    def __init__(self):
        self.count = 0
        self.root = tk.Tk()
        self.root.title("Click Counter")
        
        self.label = tk.Label(self.root, text="Clicks: 0", font=("Arial", 20))
        self.label.pack(pady=20)
        
        self.button = tk.Button(
            self.root, 
            text="Click Me!", 
            command=self.increment,
            font=("Arial", 14),
            padx=20,
            pady=10
        )
        self.button.pack()
        
    def increment(self):
        self.count += 1
        self.label.config(text=f"Clicks: {self.count}")

app = ClickCounter()
app.root.mainloop()