import tkinter as tk
import random


jokes = []

with open(r'C:\Users\cymon\WebProgramming\portfolio_questions\randomjokes.txt', 'r') as f:
        jokes = [line.strip().split('?', 1) for line in f if '?' in line and len(line.strip().split('?', 1)) == 2]
        print(f"Loaded {len(jokes)} jokes.") 

root = tk.Tk()
root.title("Joke Teller")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  #

custom_font = ("Arial", 12)

output = tk.Text(root, height=10, width=50, font=custom_font, bg="#ffffff", fg="#000000", wrap=tk.WORD)
output.pack(pady=10, padx=10)

entry = tk.Entry(root, font=custom_font, bg="#e6f3ff", fg="#000000")
entry.pack(pady=5, padx=10)


reveal_button = tk.Button(root, text="Reveal Punchline", font=custom_font, bg="#4CAF50", fg="white", command=lambda: reveal_punchline())
reveal_button.pack(pady=5)
reveal_button.config(state=tk.DISABLED)

state = 'waiting'
current_joke = None

def process_input(event=None):
    global state, current_joke
    user_input = entry.get().strip()
    entry.delete(0, tk.END)
    if user_input.lower() == 'quit':
        root.quit()
    elif user_input == "Alexa tell me a Joke" and state == 'waiting':
        if not jokes:
            output.insert(tk.END, "No jokes available. Check randomjokes.txt at the specified path.\n")
            return
        current_joke = random.choice(jokes)
        output.insert(tk.END, current_joke[0] + "?\n")
        reveal_button.config(state=tk.NORMAL)
        state = 'punchline'
    else:
        output.insert(tk.END, "Invalid command. Type 'Alexa tell me a Joke' or 'quit'.\n")

def reveal_punchline():
    global state
    if state == 'punchline' and current_joke:
        output.insert(tk.END, current_joke[1] + "\nType 'Alexa tell me a Joke' for another or 'quit' to exit.\n")
        reveal_button.config(state=tk.DISABLED)
        state = 'waiting'

entry.bind('<Return>', process_input)
output.insert(tk.END, "Type 'Alexa tell me a Joke' to start or 'quit' to exit.\n")
root.mainloop()
