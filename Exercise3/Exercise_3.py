import tkinter as tk
from tkinter import ttk

def load_data():
    students = []
    try:
        with open(r'C:\Users\cymon\WebProgramming\portfolio_questions\studentMarks.txt', 'r') as f:
            lines = f.readlines()
        num_students = int(lines[0].strip())
        for line in lines[1:]:
            parts = line.strip().split(',')
            code = int(parts[0])
            name = parts[1]
            course1 = int(parts[2])
            course2 = int(parts[3])
            course3 = int(parts[4])
            exam = int(parts[5])
            total_course = course1 + course2 + course3
            overall = total_course + exam
            percentage = (overall / 160) * 100
            if percentage >= 70:
                grade = 'A'
            elif percentage >= 60:
                grade = 'B'
            elif percentage >= 50:
                grade = 'C'
            elif percentage >= 40:
                grade = 'D'
            else:
                grade = 'F'
            students.append({
                'code': code,
                'name': name,
                'total_course': total_course,
                'exam': exam,
                'percentage': percentage,
                'grade': grade,
                'overall': overall
            })
    except FileNotFoundError:
        print("File not found.")
    return students

def view_all(students, text):
    text.delete(1.0, tk.END)
    total_percentage = 0
    for student in students:
        text.insert(tk.END, f"Student's Name: {student['name']}\n")
        text.insert(tk.END, f"Student's Number: {student['code']}\n")
        text.insert(tk.END, f"Total coursework mark: {student['total_course']}\n")
        text.insert(tk.END, f"Exam Mark: {student['exam']}\n")
        text.insert(tk.END, f"Overall percentage: {student['percentage']:.2f}%\n")
        text.insert(tk.END, f"Student grade: {student['grade']}\n\n")
        total_percentage += student['percentage']
    avg_percentage = total_percentage / len(students) if students else 0
    text.insert(tk.END, f"Number of students: {len(students)}\n")
    text.insert(tk.END, f"Average percentage mark: {avg_percentage:.2f}%\n")

def view_individual(students, combo, text):
    selected = combo.get()
    if selected:
        for student in students:
            if f"{student['code']} - {student['name']}" == selected:
                text.delete(1.0, tk.END)
                text.insert(tk.END, f"Student's Name: {student['name']}\n")
                text.insert(tk.END, f"Student's Number: {student['code']}\n")
                text.insert(tk.END, f"Total coursework mark: {student['total_course']}\n")
                text.insert(tk.END, f"Exam Mark: {student['exam']}\n")
                text.insert(tk.END, f"Overall percentage: {student['percentage']:.2f}%\n")
                text.insert(tk.END, f"Student grade: {student['grade']}\n")
                break

def view_highest(students, text):
    if not students:
        return
    highest = max(students, key=lambda s: s['overall'])
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Student's Name: {highest['name']}\n")
    text.insert(tk.END, f"Student's Number: {highest['code']}\n")
    text.insert(tk.END, f"Total coursework mark: {highest['total_course']}\n")
    text.insert(tk.END, f"Exam Mark: {highest['exam']}\n")
    text.insert(tk.END, f"Overall percentage: {highest['percentage']:.2f}%\n")
    text.insert(tk.END, f"Student grade: {highest['grade']}\n")

def view_lowest(students, text):
    if not students:
        return
    lowest = min(students, key=lambda s: s['overall'])
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Student's Name: {lowest['name']}\n")
    text.insert(tk.END, f"Student's Number: {lowest['code']}\n")
    text.insert(tk.END, f"Total coursework mark: {lowest['total_course']}\n")
    text.insert(tk.END, f"Exam Mark: {lowest['exam']}\n")
    text.insert(tk.END, f"Overall percentage: {lowest['percentage']:.2f}%\n")
    text.insert(tk.END, f"Student grade: {lowest['grade']}\n")

students = load_data()
root = tk.Tk()
root.title("Student Marks Manager")
root.configure(bg='#e0f7fa')  

title_label = tk.Label(root, text="Student Manager", font=("Arial", 18, "bold"), bg='#e0f7fa', fg='#00695c')
title_label.pack(pady=15)

top_frame = tk.Frame(root, bg='#b2dfdb', bd=2, relief='ridge')
top_frame.pack(pady=10, padx=20, fill='x')
btn1 = tk.Button(top_frame, text="View all student records", font=("Arial", 10, "bold"), bg='#4db6ac', fg='white', relief='raised', command=lambda: view_all(students, text))
btn2 = tk.Button(top_frame, text="Show highest score", font=("Arial", 10, "bold"), bg='#4db6ac', fg='white', relief='raised', command=lambda: view_highest(students, text))
btn3 = tk.Button(top_frame, text="Show lowest score", font=("Arial", 10, "bold"), bg='#4db6ac', fg='white', relief='raised', command=lambda: view_lowest(students, text))
btn1.pack(side=tk.LEFT, padx=10, pady=5, expand=True)
btn2.pack(side=tk.LEFT, padx=10, pady=5, expand=True)
btn3.pack(side=tk.LEFT, padx=10, pady=5, expand=True)

ind_frame = tk.Frame(root, bg='#b2dfdb', bd=2, relief='ridge')
ind_frame.pack(pady=10, padx=20, fill='x')
ind_label = tk.Label(ind_frame, text="View individual student record:", font=("Arial", 10, "bold"), bg='#b2dfdb', fg='#00695c')
ind_label.pack(side=tk.LEFT, padx=5, pady=5)
combo = ttk.Combobox(ind_frame, values=[f"{s['code']} - {s['name']}" for s in students], state="readonly", font=("Arial", 10))
combo.pack(side=tk.LEFT, padx=5, pady=5)
btn_view = tk.Button(ind_frame, text="View record", font=("Arial", 10, "bold"), bg='#4db6ac', fg='white', relief='raised', command=lambda: view_individual(students, combo, text))
btn_view.pack(side=tk.LEFT, padx=5, pady=5)


text_frame = tk.Frame(root, bg='#e0f7fa')
text_frame.pack(pady=10, padx=20, fill='both', expand=True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(text_frame, height=20, width=80, font=("Arial", 10), bg='#ffffff', fg='#000000', bd=2, relief='sunken', yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill='both', expand=True)
scrollbar.config(command=text.yview)

root.mainloop()
