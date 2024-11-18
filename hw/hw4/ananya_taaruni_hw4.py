import tkinter as tk
from tkinter import messagebox
import os
import math  

os.environ['TK_SILENCE_DEPRECATION'] = '1'

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_circular_linked_list(n):
    head = Node(0)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    current.next = head 
    return head

class CountingOutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Counting-Out Game")

        self.n = None
        self.k = None
        self.head = None
        self.remaining_players = None

        self.label_n = tk.Label(root, text="Enter N (2-11):")
        self.label_n.grid(row=0, column=0, padx=10, pady=5)
        self.entry_n = tk.Entry(root)
        self.entry_n.grid(row=0, column=1, padx=10, pady=5)

        self.label_k = tk.Label(root, text="Enter K (more than one):")
        self.label_k.grid(row=1, column=0, padx=10, pady=5)
        self.entry_k = tk.Entry(root)
        self.entry_k.grid(row=1, column=1, padx=10, pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.grid(row=2, columnspan=2, pady=10)

        self.eliminate_button = tk.Button(root, text="Eliminate", command=self.eliminate_player, state=tk.DISABLED)
        self.eliminate_button.grid(row=3, columnspan=2, pady=10)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=4, columnspan=2, padx=10, pady=10)

        self.text_widget = tk.Text(root, height=10, width=40)
        self.text_widget.grid(row=5, columnspan=2, padx=10, pady=10)

    def start_game(self):
        try:
            n_input = self.entry_n.get()
            k_input = self.entry_k.get()

            self.n = int(n_input)
            self.k = int(k_input)

            if not (1 < self.n < 12) or self.k < 1:
                raise ValueError("Invalid range")

        except ValueError:
            messagebox.showinfo("Error", "Please enter valid integers:\nN (2-11), K (more than or equal to 1).")
            return

        self.head = create_circular_linked_list(self.n)
        self.remaining_players = self.n

        self.text_widget.delete("1.0", tk.END)
        self.canvas.delete("all")
        self.text_widget.insert(tk.END, f"Game started. N={self.n}, K={self.k}\n")

        self.display_players()

        self.eliminate_button.config(state=tk.NORMAL)

    def display_players(self):
        """Display players on the canvas in a circular formation."""
        center_x, center_y = 200, 200
        radius = 150

        current = self.head
        angle_step = 2 * math.pi / self.remaining_players

        self.canvas.delete("all")

        for i in range(self.remaining_players):
            angle = i * angle_step
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue")
            self.canvas.create_text(x, y, text=str(current.value))
            current = current.next

    def eliminate_player(self):
        if self.remaining_players == 1:
            return

        previous = None
        current = self.head
        for _ in range(self.k - 1):
            previous = current
            current = current.next

        previous.next = current.next
        self.head = previous.next
        self.remaining_players -= 1

        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, f"Eliminated Player {current.value}\n")
        self.display_players()

        if self.remaining_players == 1:
            messagebox.showinfo("Winner", f"Player {self.head.value} wins!")
            self.reset_game()

    def reset_game(self):
        self.text_widget.delete("1.0", tk.END)
        self.entry_n.delete(0, tk.END)
        self.entry_k.delete(0, tk.END)
        self.canvas.delete("all")
        self.eliminate_button.config(state=tk.DISABLED)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    game = CountingOutGame(root)
    root.mainloop()