import tkinter as tk
from tkinter import messagebox
import json_utils

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("800x600")
        self.root.minsize(400, 300)

        self.username = ""
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.IntVar()
        self.timer_id = None
        self.time_left = 20

        # Charger et afficher l’image de fond
        self.bg = tk.PhotoImage(file="image.png")
        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_menu()

    def create_menu(self):
        self.clear_window()
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(self.root, text="Menu Principal", font=("Arial", 18), bg="#ffffff").pack(pady=20, expand=True)
        tk.Button(self.root, text="Jouer au quiz", command=self.start_quiz).pack(pady=5, fill="x", padx=100)
        tk.Button(self.root, text="Voir les résultats", command=self.view_results).pack(pady=5, fill="x", padx=100)
        tk.Button(self.root, text="Quitter", command=self.root.quit).pack(pady=(5, 30), fill="x", padx=100)

    def start_quiz(self):
        self.questions = json_utils.load_questions()
        if not self.questions:
            messagebox.showerror("Erreur", "Aucune question trouvée.")
            return
        self.ask_username()

    def ask_username(self):
        self.clear_window()
        tk.Label(self.root, text="Entrez votre nom :", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5, fill="x", padx=50)
        tk.Button(self.root, text="Commencer", command=self.begin_quiz).pack(pady=10)

    def begin_quiz(self):
        self.username = self.username_entry.get()
        if not self.username.strip():
            messagebox.showwarning("Nom requis", "Veuillez entrer un nom.")
            return
        self.score = 0
        self.current_question = 0
        self.show_question()

    def show_question(self):
        self.clear_window()
        self.time_left = 20
        question = self.questions[self.current_question]

        tk.Label(self.root, text=f"Question {self.current_question + 1}:", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.root, text=question['question'], wraplength=600, bg="#ffffff").pack(pady=5, fill="x", padx=50)

        self.selected_option.set(-1)
        for i, option in enumerate(question['options']):
            tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=i, bg="#ffffff").pack(anchor="w", padx=50)

        self.timer_label = tk.Label(self.root, text=f"Temps restant : {self.time_left} secondes", fg="red", bg="#ffffff")
        self.timer_label.pack(pady=5)

        tk.Button(self.root, text="Valider", command=self.check_answer).pack(pady=10)

        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Temps restant : {self.time_left} secondes")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.check_answer(auto=True)

    def check_answer(self, auto=False):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        choice = self.selected_option.get()
        correct_answer = self.questions[self.current_question]['reponse']

        if not auto and choice == -1:
            messagebox.showwarning("Choix requis", "Veuillez sélectionner une réponse.")
            self.update_timer()
            return

        if not auto and self.questions[self.current_question]['options'][choice] == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        json_utils.save_results(self.username, self.score, len(self.questions))
        if self.score >= 9:
            message = "Félicitations 🎉 !"
        elif self.score >= 6:
            message = "Bien joué 👍 !"
        else:
            message = "Peut mieux faire 😕"
        messagebox.showinfo("Résultat", f"Score : {self.score}/{len(self.questions)}\n{message}")
        self.create_menu()

    def view_results(self):
        self.clear_window()
        tk.Label(self.root, text="Résultats", font=("Arial", 16), bg="#ffffff").pack(pady=10)
        results_text = tk.Text(self.root, height=15, width=80)
        results_text.pack(padx=20, pady=10, expand=True, fill="both")

        try:
            results = json_utils.view_results()
        except Exception as e:
            results = "Erreur lors du chargement des résultats : " + str(e)

        results_text.insert("1.0", results)
        results_text.config(state="disabled")
        tk.Button(self.root, text="Retour", command=self.create_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        # Recréation de bg_label
        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
