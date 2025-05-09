import json
import os

RESULTS_FILE = "results.json"
QUESTIONS_FILE = "questions.json"

def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_results(username, score, total_questions):
    results = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            try:
                results = json.load(file)
            except json.JSONDecodeError:
                results = []

    results.append({
        "nom": username,
        "score": score,
        "total": total_questions
    })

    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

def view_results():
    if not os.path.exists(RESULTS_FILE):
        return "Aucun résultat enregistré pour le moment."

    with open(RESULTS_FILE, "r", encoding="utf-8") as file:
        try:
            results = json.load(file)
        except json.JSONDecodeError:
            return "Erreur de lecture du fichier des résultats."

    if not results:
        return "Aucun résultat enregistré."

    result_lines = []
    for r in results:
        line = f"{r['nom']} : {r['score']} / {r['total']}"
        result_lines.append(line)

    return "\n".join(result_lines)
