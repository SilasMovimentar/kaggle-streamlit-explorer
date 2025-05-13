# Lego-Datenset-Explorer mit Streamlit

Dieses kleine Webtool ermöglicht es dir, den "Lego-Database"-Datensatz von Kaggle interaktiv zu erkunden. Du kannst die angezeigten Lego-Sets nach Erscheinungsjahr und Thema filtern und dir die Anzahl der Teile als Balkendiagramm anzeigen lassen.

## Voraussetzungen

Bevor du das Tool ausführen kannst, stelle sicher, dass du folgende Voraussetzungen erfüllst:

* **Python 3.6 oder höher** ist auf deinem System installiert.
* Die folgenden Python-Bibliotheken sind installiert. Du kannst sie mit `pip` installieren:
    ```bash
    pip install streamlit pandas kaggle python-dotenv
    ```
* Du hast einen **Kaggle-Account** und ein **API-Token** erstellt.

## Einrichtung

1.  **Klonen des Repositorys (optional):** Wenn dieser Code Teil eines Git-Repositorys ist, klone es auf deinen lokalen Rechner.

2.  **Erstellen der `.env`-Datei:**
    * Im Hauptverzeichnis des Projekts (dort, wo sich auch dein Python-Skript befindet) erstelle eine Datei namens `.env`.
    * Füge in diese Datei deine Kaggle-Benutzername und deinen API-Schlüssel ein, die du von deiner `kaggle.json`-Datei erhalten hast:
        ```env
        KAGGLE_USERNAME=DEIN_KAGGLE_BENUTZERNAME
        KAGGLE_KEY=DEIN_KAGGLE_API_SCHLÜSSEL
        ```
        **Wichtig:** Ersetze `DEIN_KAGGLE_BENUTZERNAME` und `DEIN_KAGGLE_API_SCHLÜSSEL` durch deine tatsächlichen Werte.

3.  **`.gitignore`-Datei (empfohlen):**
    * Erstelle im Hauptverzeichnis eine Datei namens `.gitignore` (falls noch nicht vorhanden).
    * Füge die Zeile `.env` zu dieser Datei hinzu, um zu verhindern, dass deine sensiblen Kaggle-Zugangsdaten versehentlich in dein Git-Repository hochgeladen werden.

## Ausführung

1.  **Navigiere zum Projektverzeichnis:** Öffne dein Terminal oder deine Kommandozeile und wechsle in den Ordner, in dem sich dein Python-Skript (`.py`-Datei) befindet.

2.  **Starte die Streamlit-App:** Führe den folgenden Befehl aus:
    ```bash
    streamlit run dein_skriptname.py
    ```
    Ersetze `dein_skriptname.py` durch den tatsächlichen Namen deiner Python-Datei.

3.  **Interaktion mit der App:** Streamlit wird automatisch einen neuen Tab in deinem Webbrowser öffnen und die Lego-Datenset-Explorer-Anwendung anzeigen.
    * Wähle ein **Jahr** aus dem Dropdown-Menü, um die Lego-Sets dieses Jahres anzuzeigen.
    * Wähle ein **Thema** aus dem Dropdown-Menü, um die Lego-Sets mit diesem Thema anzuzeigen.
    * Unter den Auswahlfeldern wird eine Tabelle mit den gefilterten Lego-Sets angezeigt.
    * Ein Balkendiagramm unter der Tabelle visualisiert die Anzahl der Teile der gefilterten Sets.

## Code-Übersicht

* **`import streamlit as st`**: Importiert die Streamlit-Bibliothek für die Erstellung der Webanwendung.
* **`import pandas as pd`**: Importiert die Pandas-Bibliothek für die Datenmanipulation.
* **`import os`**: Importiert das `os`-Modul für Interaktionen mit dem Betriebssystem (z.B. Überprüfen des Datei-Exists).
* **`from kaggle.api.kaggle_api_extended import KaggleApi`**: Importiert die notwendige Klasse für die Interaktion mit der Kaggle-API.
* **`from dotenv import load_dotenv`**: Importiert die Funktion zum Laden von Umgebungsvariablen aus der `.env`-Datei.
* **`load_dotenv()`**: Lädt die Umgebungsvariablen aus der `.env`-Datei.
* **`username = os.getenv("KAGGLE_USERNAME")`** und **`key = os.getenv("KAGGLE_KEY")`**: Ruft deinen Kaggle-Benutzernamen und API-Schlüssel aus den Umgebungsvariablen ab.
* **`api = KaggleApi()`** und **`api.authenticate()`**: Erstellt eine Instanz der Kaggle-API und authentifiziert sich mit deinen Anmeldeinformationen.
* **`DATASET_ID = "anderas/lego-database"`**: Definiert die ID des zu verwendenden Kaggle-Datasets.
* **`CSV_FILE = "lego/sets.csv"`**: Definiert den Namen der CSV-Datei innerhalb des heruntergeladenen Datasets.
* **`if not os.path.exists("lego"): ...`**: Überprüft, ob der Ordner "lego" existiert. Falls nicht, wird das Kaggle-Dataset heruntergeladen und entpackt.
* **`df = pd.read_csv(CSV_FILE)`**: Lädt die Daten aus der CSV-Datei in einen Pandas DataFrame.
* **`st.title(...)`**: Zeigt den Titel der Streamlit-Anwendung an.
* **`year = st.selectbox(...)`** und **`theme = st.selectbox(...)`**: Erstellen Dropdown-Menüs zur Auswahl von Jahr und Thema.
* **`filtered = df[(df['year'] == year) & (df['theme_id'] == theme)]`**: Filtert den DataFrame basierend auf den ausgewählten Jahr und Thema.
* **`st.dataframe(filtered)`**: Zeigt den gefilterten DataFrame als interaktive Tabelle an.
* **`st.bar_chart(filtered['num_parts'])`**: Erstellt ein Balkendiagramm der Spalte 'num\_parts' für die gefilterten Daten.

## Hinweise

* Stelle sicher, dass deine Kaggle-Anmeldeinformationen in der `.env`-Datei korrekt sind.
* Die Anwendung lädt das Kaggle-Dataset nur dann herunter, wenn der Ordner "lego" noch nicht existiert. Wenn du das Dataset erneut herunterladen möchtest, lösche den Ordner "lego" im Projektverzeichnis.
* Die Dropdown-Menüs zeigen nur eindeutige Werte aus den Spalten 'year' und 'theme\_id' an, bei denen keine fehlenden Werte vorhanden sind.
* Das Balkendiagramm zeigt die Anzahl der Teile (`num_parts`) für die gefilterten Lego-Sets.

Viel Spaß beim Erkunden der Lego-Daten!