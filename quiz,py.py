import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "London", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
                "correct_answer": "Blue Whale"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.create_widgets()
        self.display_question()
    
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(fill=tk.X, padx=20, pady=5)
        
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next Question", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=10)
    
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            
            self.score_label.config(text=f"Score: {self.score}")
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if self.option_buttons[selected_option].cget("text") == correct_answer:
            self.score += 1
        self.current_question += 1
        self.display_question()
    
    def next_question(self):
        self.current_question += 1
        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
