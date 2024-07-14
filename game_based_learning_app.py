import tkinter as tk
from tkinter import messagebox
import random

class GameBasedLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game-Based Learning App")
        self.score = 0
        self.leaderboard = {}
        self.time_left = 60  # Game duration in seconds
        self.max_score = 50
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        self.title_label = tk.Label(self.root, text="Welcome to the Game-Based Learning App", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # User Name
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(pady=10)

        self.name_label = tk.Label(self.name_frame, text="Enter your name:", font=("Helvetica", 12))
        self.name_label.pack(side=tk.LEFT)

        self.name_entry = tk.Entry(self.name_frame, font=("Helvetica", 12))
        self.name_entry.pack(side=tk.LEFT, padx=10)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        # Change User Button
        self.change_user_button = tk.Button(self.root, text="Change User", command=self.change_user)
        self.change_user_button.pack(pady=10)

        # Back Button
        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_user_entry)

        # Hint Button
        self.hint_button = tk.Button(self.root, text="Hint", command=self.show_hint)
        
        # Timer Label
        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}", font=("Helvetica", 12))
        
        # Question Area
        self.question_frame = tk.Frame(self.root)
        
        self.question_label = tk.Label(self.question_frame, text="Solve this problem:", font=("Helvetica", 12))
        self.question_label.pack(side=tk.LEFT)
        
        self.question_text = tk.Label(self.question_frame, font=("Helvetica", 12))
        self.question_text.pack(side=tk.LEFT, padx=10)
        
        # Answer Area
        self.answer_frame = tk.Frame(self.root)
        
        self.answer_label = tk.Label(self.answer_frame, text="Your Answer:", font=("Helvetica", 12))
        self.answer_label.pack(side=tk.LEFT)
        
        self.answer_entry = tk.Entry(self.answer_frame, font=("Helvetica", 12))
        self.answer_entry.pack(side=tk.LEFT, padx=10)
        
        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        
        # Feedback Area
        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        
        # Score Area
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 12))
        
        # Leaderboard Area
        self.leaderboard_label = tk.Label(self.root, text="Leaderboard", font=("Helvetica", 12))
        self.leaderboard_text = tk.Text(self.root, height=10, width=40)
    
    def start_game(self):
        self.user_name = self.name_entry.get().strip()
        if not self.user_name:
            messagebox.showwarning("Input Error", "Please enter your name to start the game.")
            return
        
        self.name_frame.pack_forget()
        self.start_button.pack_forget()
        self.change_user_button.pack_forget()

        self.question_frame.pack(pady=10)
        self.answer_frame.pack(pady=10)
        self.submit_button.pack(pady=20)
        self.feedback_label.pack(pady=10)
        self.score_label.pack(pady=10)
        self.leaderboard_label.pack(pady=10)
        self.leaderboard_text.pack(pady=10)
        self.back_button.pack(pady=10)
        self.hint_button.pack(pady=10)
        self.timer_label.pack(pady=10)

        self.load_question()
        self.update_timer()
    
    def change_user(self):
        # Reset the game
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.feedback_label.config(text="")
        self.time_left = 60
        self.timer_label.config(text=f"Time Left: {self.time_left}")
        self.name_frame.pack(pady=10)
        self.start_button.pack(pady=10)
        self.change_user_button.pack(pady=10)
        
        self.question_frame.pack_forget()
        self.answer_frame.pack_forget()
        self.submit_button.pack_forget()
        self.feedback_label.pack_forget()
        self.score_label.pack_forget()
        self.leaderboard_label.pack_forget()
        self.leaderboard_text.pack_forget()
        self.back_button.pack_forget()
        self.hint_button.pack_forget()
        self.timer_label.pack_forget()

        self.answer_entry.delete(0, tk.END)
    
    def back_to_user_entry(self):
        # Hide the game interface and show the user name entry fields
        self.question_frame.pack_forget()
        self.answer_frame.pack_forget()
        self.submit_button.pack_forget()
        self.feedback_label.pack_forget()
        self.score_label.pack_forget()
        self.leaderboard_label.pack_forget()
        self.leaderboard_text.pack_forget()
        self.back_button.pack_forget()
        self.hint_button.pack_forget()
        self.timer_label.pack_forget()

        self.name_frame.pack(pady=10)
        self.start_button.pack(pady=10)
        self.change_user_button.pack(pady=10)
    
    def show_hint(self):
        hint_message = ""
        if self.operation == '+':
            hint_message = f"Try breaking it down: {self.num1} + {self.num2}."
        elif self.operation == '-':
            hint_message = f"Think about how many more you need to get from {self.num2} to {self.num1}."
        elif self.operation == '*':
            hint_message = f"Use repeated addition: {self.num1} times {self.num2} is the same as adding {self.num1} to itself {self.num2} times."
        elif self.operation == '/':
            hint_message = f"Remember, {self.num1} divided by {self.num2} means how many times does {self.num2} fit into {self.num1}."
        
        messagebox.showinfo("Hint", hint_message)
    
    def load_question(self):
        operations = ['+', '-', '*', '/']
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operation = random.choice(operations)
        
        if self.operation == '/':
            self.num1 = self.num1 * self.num2  # Ensure the division is always an integer
        
        self.question = f"{self.num1} {self.operation} {self.num2}"
        self.question_text.config(text=self.question)
    
    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = float(user_answer)
            if self.operation == '+':
                correct_answer = self.num1 + self.num2
            elif self.operation == '-':
                correct_answer = self.num1 - self.num2
            elif self.operation == '*':
                correct_answer = self.num1 * self.num2
            elif self.operation == '/':
                correct_answer = self.num1 / self.num2

            if user_answer == correct_answer:
                self.feedback_label.config(text="Correct! Well done.", fg="green")
                self.score += 4
            else:
                self.feedback_label.config(text=f"Incorrect. The correct answer was {correct_answer}. Try again.", fg="red")
                self.score -= 1
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

        self.answer_entry.delete(0, tk.END)
        self.score_label.config(text=f"Score: {self.score}")
        self.update_leaderboard()
        self.load_question()

        if self.score >= self.max_score:
            self.end_game("You reached the maximum score of 50!")
    
    def update_leaderboard(self):
        self.leaderboard[self.user_name] = self.score
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        
        self.leaderboard_text.delete("1.0", tk.END)
        for name, score in sorted_leaderboard:
            self.leaderboard_text.insert(tk.END, f"{name}: {score}\n")
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game("Time's up!")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.change_user()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameBasedLearningApp(root)
    root.mainloop()
