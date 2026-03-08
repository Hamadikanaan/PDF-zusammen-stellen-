
```md
# PDF Zusammenführen

Dieses Projekt ist ein kleines Python-Programm mit einer grafischen Oberfläche.  
Mit dem Programm kann man mehrere PDF-Dateien auswählen und zu einer PDF-Datei zusammenführen.

## Funktionen

- Mehrere PDF-Dateien auswählen
- PDF-Dateien zusammenführen
- Neue PDF-Datei speichern
- Die fertige PDF-Datei automatisch öffnen
- Einfache Bedienung mit Fenster

## Benötigte Programme

Du brauchst:

- Python 3
- das Modul `pypdf`

`tkinter` ist oft schon in Python installiert.

## Installation

Zuerst musst du das Modul `pypdf` installieren.

```bash
pip install pypdf
```

## Projekt starten

Starte das Programm mit diesem Befehl:

```bash
python main.py
```

Wenn deine Datei anders heißt, musst du `main.py` durch den richtigen Dateinamen ersetzen.

## So funktioniert das Programm

1. Klicke auf **Dateien auswählen**
2. Wähle eine oder mehrere PDF-Dateien
3. Klicke auf **OK - Zusammenführen**
4. Wähle den Speicherort für die neue Datei
5. Die neue PDF-Datei wird gespeichert und geöffnet

## Verwendete Bibliotheken

- `tkinter`
- `pypdf`
- `os`
- `subprocess`
- `platform`

## Unterstützte Systeme

Das Programm funktioniert auf:

- Windows
- macOS
- Linux

## Hinweise

- Es können nur PDF-Dateien ausgewählt werden.
- Wenn keine Datei ausgewählt wurde, zeigt das Programm eine Warnung.
- Nach dem Zusammenführen wird die Auswahl zurückgesetzt.

## Mögliche Verbesserungen

- Namen der ausgewählten Dateien anzeigen
- Reihenfolge der Dateien ändern
- Einzelne Dateien aus der Liste löschen
- Drag-and-drop hinzufügen
- Besseres Design

## Autor

Hamadi Alkanaan
```
