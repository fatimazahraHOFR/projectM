import tkinter as tk
from tkinter import messagebox
import time

# Classe pour le Quiz avec Chrono
class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Qui a écrit la théorie de la relativité ?",
                "choices": ["Isaac Newton", "Albert Einstein", "Galilée", "Nikola Tesla"],
                "correct": "Albert Einstein"
            },
            {
                "question": "Quel est le plus grand océan du monde ?",
                "choices": ["Océan Atlantique", "Océan Pacifique", "Océan Indien", "Océan Arctique"],
                "correct": "Océan Pacifique"
            },
            {
                "question": "Quel élément chimique a pour symbole 'Fe' ?",
                "choices": ["Fer", "Fluor", "Francium", "Fermium"],
                "correct": "Fer"
            },
            {
                "question": "Quel est le pays le plus peuplé du monde ?",
                "choices": ["Chine", "Inde", "États-Unis", "Indonésie"],
                "correct": "Chine"
            },
            {
                "question": "En quelle année l'homme a-t-il marché sur la Lune pour la première fois ?",
                "choices": ["1969", "1959", "1979", "1989"],
                "correct": "1969"
            }
        ]
        self.score = 0
        self.current_question = 0
        self.time_left = 30  # Temps par question en secondes
        self.start_time = time.time()

    def get_question(self):
        return self.questions[self.current_question]["question"]

    def get_choices(self):
        return self.questions[self.current_question]["choices"]

    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question]["correct"]
        if answer == correct_answer:
            self.score += 1
        self.current_question += 1

    def is_end(self):
        return self.current_question >= len(self.questions)

    def get_score(self):
        return self.score

    def time_remaining(self):
        elapsed_time = time.time() - self.start_time
        return max(0, self.time_left - int(elapsed_time))

# Fonction pour afficher la question suivante
def next_question():
    if quiz.is_end():
        messagebox.showinfo("Quiz terminé", f"Votre score est : {quiz.get_score()}/{len(quiz.questions)}")
        show_main_menu()  # Retour au menu principal après le quiz
    else:
        question_label.config(text=quiz.get_question())
        choice1_button.config(text=quiz.get_choices()[0], command=lambda: answer_question(quiz.get_choices()[0]))
        choice2_button.config(text=quiz.get_choices()[1], command=lambda: answer_question(quiz.get_choices()[1]))
        choice3_button.config(text=quiz.get_choices()[2], command=lambda: answer_question(quiz.get_choices()[2]))
        choice4_button.config(text=quiz.get_choices()[3], command=lambda: answer_question(quiz.get_choices()[3]))
        update_timer()

# Fonction pour vérifier la réponse
def answer_question(answer):
    quiz.check_answer(answer)
    quiz.start_time = time.time()  # Reset the timer for the next question
    next_question()

# Fonction pour mettre à jour le timer
def update_timer():
    remaining_time = quiz.time_remaining()
    timer_label.config(text=f"Temps restant : {remaining_time}s")
    if remaining_time == 0:
        messagebox.showwarning("Temps écoulé", "Le temps est écoulé pour cette question.")
        quiz.check_answer("")  # Automatically mark as incorrect if time is up
        quiz.start_time = time.time()  # Reset the timer for the next question
        next_question()
    else:
        # Actualisation toutes les 1000 ms (1 seconde)
        root.after(1000, update_timer)

# Fonction pour afficher le menu principal
def show_main_menu():
    # Cacher l'interface de quiz
    quiz_frame.pack_forget()
    # Afficher le menu principal
    main_menu_frame.pack()

# Fonction pour démarrer le quiz
def start_quiz():
    global quiz
    quiz = Quiz()  # Re-initialiser le quiz à chaque début
    # Cacher le menu principal
    main_menu_frame.pack_forget()
    # Afficher l'interface du quiz
    quiz_frame.pack()
    next_question()

# Fonction pour quitter l'application
def quit_app():
    root.quit()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Quiz avec Menu Principal")
root.geometry("500x350")
root.config(bg="#f5f5f5")

# Frame pour le menu principal
main_menu_frame = tk.Frame(root, bg="#f5f5f5")

# Titre du menu principal
main_menu_title = tk.Label(main_menu_frame, text="Menu Principal", font=("Arial", 16, "bold"), bg="grey")
main_menu_title.pack(pady=10)

# Bouton pour démarrer le quiz
start_button = tk.Button(main_menu_frame, text="Commencer le Quiz", font=("Arial", 12), bg="#4caf50", fg="white", width=20, command=start_quiz)
start_button.pack(pady=10)

# Bouton pour voir les scores (fonctionnalité à ajouter plus tard)
scores_button = tk.Button(main_menu_frame, text="Voir les Scores", font=("Arial", 12), bg="#4caf50", fg="white", width=20, command=lambda: messagebox.showinfo("Scores", "Les scores seront enregistrés ici"))
scores_button.pack(pady=10)

# Bouton pour quitter l'application
quit_button = tk.Button(main_menu_frame, text="Quitter", font=("Arial", 12), bg="#f44336", fg="white", width=20, command=quit_app)
quit_button.pack(pady=10)

# Frame pour le quiz
quiz_frame = tk.Frame(root, bg="#f5f5f5")

# Titre du quiz
title_label = tk.Label(quiz_frame, text="Quiz de Culture Générale", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# Affichage de la question
question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), bg="pink", wraplength=450)
question_label.pack(pady=10)

# Boutons pour les choix
choice1_button = tk.Button(quiz_frame, text="", font=("Arial", 12), bg="blue", fg="white", width=30)
choice1_button.pack(pady=5)

choice2_button = tk.Button(quiz_frame, text="", font=("Arial", 12), bg="brown", fg="white", width=30)
choice2_button.pack(pady=5)

choice3_button = tk.Button(quiz_frame, text="", font=("Arial", 12), bg="yellow", fg="white", width=30)
choice3_button.pack(pady=5)

choice4_button = tk.Button(quiz_frame, text="", font=("Arial", 12), bg="green", fg="white", width=30)
choice4_button.pack(pady=5)

# Affichage du timer
timer_label = tk.Label(quiz_frame, text="Temps restant : 30s", font=("Arial", 12), bg="#f5f5f5")
timer_label.pack(pady=5)

# Afficher le menu principal au démarrage
show_main_menu()

# Lancer l'interface graphique
root.mainloop()
