# Browser Agent Bibliothek

Diese Projekt ist ein leistungsstarker Browser-Automatisierungsagent, der Gemini 2.0 Flash für intelligentes Webbrowsing und Aufgabenausführung nutzt. Es kombiniert die Möglichkeiten der Browser-Automatisierung mit fortschrittlicher KI, um webbasierte Aufgaben autonom auszuführen.

## Funktionen

- 🤖 KI-gesteuerte Browser-Automatisierung mit Gemini 2.0 Flash
- 🌐 Anpassbare Browsersteuerung und -konfiguration
- 📝 Gesprächsprotokollierung und Verlaufsverfolgung
- 🎯 Aufgabenorientierte Automatisierung mit Bilderkennungsfähigkeiten
- 🛠 Erweiterbare Systemaufforderungen und Controller-Funktionalität

## Voraussetzungen

- Python 3.11 oder höher
- Google API-Schlüssel für Gemini 2.0 Flash
- Moderner Webbrowser (Chrome empfohlen)

## Installation

1. Repository klonen:
```bash
git clone [your-repository-url]
cd browser-use-libary
```

2. Virtuelle Umgebung erstellen und aktivieren:
```bash
# Unter macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Unter Windows
python -m venv .venv
.venv\Scripts\activate
```

3. Erforderliche Pakete installieren:
```bash
pip install -r requirements.txt
```

4. Erstellen Sie eine `.env`-Datei im Projektstamm mit folgendem Inhalt:
```env
GOOGLE_API_KEY=your_google_api_key_here
ANONYMIZED_TELEMETRY=false
```

## Verwendung

Das Hauptskript zeigt, wie man den Browser-Agenten verwendet:

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller, Browser, BrowserConfig, SystemPrompt
import asyncio
import os
from dotenv import load_dotenv

# Umgebungsvariablen laden
load_dotenv()

# Gemini 2.0 Flash initialisieren
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Browser konfigurieren
config = BrowserConfig(
    headless=False  # Browserfenster anzeigen
)

# Benutzerdefinierten Controller und Browser erstellen
custom_controller = Controller()
browser = Browser(config=config)

async def main():
    agent = Agent(
        task="your_task_here",
        llm=llm,
        browser=browser,
        controller=custom_controller,
        use_vision=True,
        save_conversation_path="logs/conversation.json"
    )
    result = await agent.run(max_steps=200)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

Um das Beispiel auszuführen:
```bash
python main.py
```

## Projektstruktur

- `main.py`: Haupteinstiegspunkt und Beispielimplementierung
- `requirements.txt`: Projektabhängigkeiten
- `logs/`: Verzeichnis für Gesprächsprotokolle und Verlauf
- `.env`: Konfiguration der Umgebungsvariablen

## Konfiguration

Das Projekt kann über verschiedene Parameter konfiguriert werden:

- `BrowserConfig`: Browserfunktionen konfigurieren (Headless-Modus usw.)
- `SystemPrompt`: Verhalten und Regeln des KI-Agenten anpassen
- `Controller`: Browser-Steuerungsfunktionalität erweitern oder modifizieren

## Protokollierung

Gesprächsprotokolle werden im Verzeichnis `logs` gespeichert. Jeder Durchlauf erstellt eine neue JSON-Datei mit dem vollständigen Interaktionsverlauf.

## Umgebungsvariablen

- `GOOGLE_API_KEY`: Ihr Google API-Schlüssel für Gemini 2.0 Flash
- `ANONYMIZED_TELEMETRY`: Auf 'false' setzen, um Telemetrie zu deaktivieren

## Mitwirken

Beiträge sind willkommen! Bitte reichen Sie einen Pull Request ein.

## Lizenz

[Ihre Lizenz hier]