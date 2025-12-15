# WorkPilot

**Author:** Varka Emir

WorkPilot ist eine lokale Chat-Anwendung, die das Llama3.1:8b Modell über Ollama verwendet. Nutzer können direkt mit dem Modell chatten, der Chat-Verlauf wird angezeigt und kann gelöscht werden.

## Features

- Chat mit Llama3.1:8b über Ollama
- Echtzeit-Anzeige des Chatverlaufs
- "Thinking..." Platzhalter während das Modell antwortet
- Verlauf löschen
- Unterstützt lokale Installation oder Docker

## Ordnerstruktur

workpilot-ai/
│
├── app.py # Flask-Anwendung
├── requirements.txt # Python-Abhängigkeiten
├── Dockerfile # Docker-Image
├── LICENSE # MIT-Lizenz
├── README.md # Projektbeschreibung
├── templates/
│ └── index.html # HTML-Frontend
└── static/
├── style.css # CSS-Styles
└── logo.png # Logo
## Lokale Installation (Python)

1. Repository klonen:
   ```bash
   git clone https://github.com/EmirVar/workpilot-ai.git
   cd workpilot-ai
