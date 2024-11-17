import tkinter as tk
from tkinter import messagebox
import time

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is 5 + 3?", "options": ["5", "8", "12", "15"], "answer": "8"},
    {"question": "Which programming language is named after a comedy group?", "options": ["Python", "Java", "C++", "Ruby"], "answer": "Python"},
]

score = 0
current_question = 0
start_time = time.time()

def submit_answer():
    global score, current_question

    selected = answer_var.get()
    if selected == questions[current_question]["answer"]:
        score += 1

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        end_time = time.time()
        elapsed_time = int(end_time - start_time)
        messagebox.showinfo("Quiz Finished", f"Your score: {score}/{len(questions)}\nTime taken: {elapsed_time} seconds")
        root.quit()

def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        radio_buttons[i].config(text=option, value=option)
    answer_var.set(None)

# GUI setup
root = tk.Tk()
root.title("Quiz App")

question_label = tk.Label(root, text="", font=("Helvetica", 16))
question_label.pack(pady=10)

answer_var = tk.StringVar()
radio_buttons = [tk.Radiobutton(root, text="", variable=answer_var, value="", font=("Helvetica", 14)) for _ in range(4)]
for rb in radio_buttons:
    rb.pack(anchor="w")

submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=10)

show_question()
root.mainloop()
