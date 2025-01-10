# Browser-Automatisierungsbibliothek 🚀

Eine leistungsstarke Bibliothek zur Browser-Automatisierung mit KI-gestützter Interaktion, basierend auf Google Gemini 2.0.

## 🌟 Hauptfunktionen

- 🤖 KI-gesteuerte Browser-Automatisierung
- 🎯 Präzise Webseiten-Interaktion
- 👁️ Visuelle Erkennungsfähigkeiten
- 📝 Ausführliche Protokollierung
- 🔄 Anpassbare Systemanweisungen

## 🛠️ Installation

1. Repository klonen:
   ```bash
   git clone [repository-url]
   cd browser-use-libary
   ```

2. Python-Umgebung einrichten:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Unter Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## ⚙️ Konfiguration

1. Umgebungsvariablen einrichten:
   ```bash
   cp .env.example .env
   ```

2. `.env` Datei konfigurieren:
   - Google API-Schlüssel von der [Google Cloud Console](https://console.cloud.google.com/apis/credentials) besorgen
   - Einstellungen in der `.env` Datei anpassen:
     ```
     GOOGLE_API_KEY=ihr_api_schlüssel
     ANONYMIZED_TELEMETRY=false
     ```

## 💻 Verwendung

```python
from browser_use import Agent, Controller, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI

# Browser konfigurieren
config = BrowserConfig(headless=False)
browser = Browser(config=config)
controller = Controller()

# Gemini-Modell initialisieren
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

# Agent erstellen und ausführen
agent = Agent(
    task="Ihre Aufgabe hier",
    llm=llm,
    browser=browser,
    controller=controller,
    use_vision=True,
    save_conversation_path="logs/conversation.json"
)

# Ausführen
result = await agent.run(max_steps=200)
```

## 🔒 Sicherheitshinweise

- API-Schlüssel niemals im Versionskontrollsystem speichern
- `.env` Datei ist in `.gitignore` aufgeführt
- Bei Verdacht auf kompromittierte API-Schlüssel sofort neue generieren

## 📦 Abhängigkeiten

- google-generativeai >= 0.3.0
- python-dotenv >= 1.0.0
- aiohttp >= 3.9.0
- browser-use >= 0.1.0
- langchain >= 0.1.0

## 🤝 Beitragen

Verbesserungsvorschläge und Pull Requests sind willkommen! Bitte stellen Sie sicher, dass Sie:

1. Tests für neue Funktionen hinzufügen
2. Die Dokumentation aktualisieren
3. Den Code-Style einhalten

## 📝 Protokollierung

- Konversationsprotokolle werden im `logs/` Verzeichnis gespeichert
- Browser-Aktivitäten werden automatisch aufgezeichnet
- Fehler werden detailliert protokolliert

## 🔧 Anpassung

Sie können das Verhalten des Agents durch Anpassung der `SystemPrompt`-Klasse modifizieren:

```python
class CustomSystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        existing_rules = super().important_rules()
        custom_rules = "Ihre benutzerdefinierten Regeln hier"
        return f'{existing_rules}\n{custom_rules}'
```

## 📫 Kontakt & Support

Bei Fragen oder Problemen erstellen Sie bitte ein Issue im Repository. 