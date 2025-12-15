WorkPilot

Author: Varka Emir

WorkPilot ist eine lokale Chat-Anwendung, die das Llama3.1:8b Modell über Ollama verwendet. Nutzer können direkt mit dem Modell chatten, der Chat-Verlauf wird angezeigt und kann gelöscht werden.

Features

Chat mit Llama3.1:8b über Ollama

Echtzeit-Anzeige des Chatverlaufs

"Thinking..." Platzhalter während das Modell antwortet

Verlauf löschen

Unterstützt lokale Installation oder Docker

Ordnerstruktur
workpilot-ai/
│
├── app.py                  # Flask-Anwendung
├── requirements.txt        # Python-Abhängigkeiten
├── Dockerfile              # Docker-Image
├── LICENSE                 # MIT-Lizenz
├── README.md               # Projektbeschreibung
├── templates/
│   └── index.html          # HTML-Frontend
└── static/
    ├── style.css           # CSS-Styles
    └── logo.png            # Logo

Lokale Installation (Python)

Repository klonen:

git clone https://github.com/EmirVar/workpilot-ai.git
cd workpilot-ai


Python-Abhängigkeiten installieren:

pip install -r requirements.txt


Ollama einrichten

Offizielle Dokumentation: https://ollama.com/docs

Modell herunterladen:

ollama pull llama3.1:8b


Ollama-Daemon starten:

ollama serve


App starten:

python app.py


Browser öffnen:

http://localhost:5000

Docker-Installation

Dockerfile erstellen (bereits im Repo vorhanden).

Docker-Image bauen:

docker build -t workpilot-ai .


Docker-Container starten:

docker run -p 5000:5000 workpilot-ai


Browser öffnen:

http://localhost:5000

Hinweise

Der aktuelle app.secret_key ist im Code hardcoded. Für Produktion empfiehlt sich, einen eigenen Secret Key zu setzen oder eine .env Datei zu verwenden.

Das Modell llama3.1:8b muss auf jedem Rechner vorhanden sein, der die App nutzen will.

Lizenz

MIT License – siehe LICENSE
