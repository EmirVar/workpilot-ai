
# WorkPilot

**Author:** Varka Emir  

WorkWorkPilot ist eine lokale Chat-Anwendung, die das **Llama3.1:8b** Modell über **Ollama** verwendet. Nutzer können direkt mit dem Modell chatten, der Chat-Verlauf wird angezeigt und kann gelöscht werden.  

---

## Features

- Chat mit **Llama3.1:8b** über **Ollama**  
- Echtzeit-Anzeige des Chatverlaufs  
- "Thinking..." Platzhalter während das Modell antwortet  
- Verlauf löschen  
- Unterstützt **lokale Installation** oder **Docker**  

---
## Lokale Installation (Python)

1. **Repository klonen:**
   ```bash
   git clone https://github.com/EmirVar/workpilot-ai.git
   cd workpilot-ai
   
2. **Python-Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   
2. **Ollama Image herunterladen:**
   ```bash
   ollama pull llama3.1:8b
   
## Voraussetzungen

- Ollama muss heruntergeladen sein 
-  mit "ollama serve" starten
- Danach den Pull-Command machen


