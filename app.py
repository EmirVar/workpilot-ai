from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'dein_sicherer_schlüssel'  # Für Produktion ändern

# Chat-Verlauf initialisieren
def get_history():
    if "chat_history" not in session:
        session["chat_history"] = []
    return session["chat_history"]

# Ollama-Abfrage
def query_ollama(messages):
    url = "http://localhost:11434/api/chat"  # Dein lokaler Ollama-Endpunkt
    payload = {
        "model": "llama3.1:8b",
        "messages": messages,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Fehler bei der Verbindung zur KI: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    history = get_history()
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            # User-Nachricht hinzufügen
            history.append({"role": "user", "content": user_input})
            # Placeholder für Thinking
            history.append({"role": "bot", "content": "Thinking..."})
            session.modified = True
            # Antwort von Ollama abfragen
            messages = [{"role": "user", "content": user_input}]
            bot_response = query_ollama(messages)
            # Thinking ersetzen
            history[-1]["content"] = bot_response
            session.modified = True
        return redirect(url_for("index"))
    return render_template("index.html", chat_history=history)

@app.route("/clear", methods=["POST"])
def clear():
    session["chat_history"] = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
