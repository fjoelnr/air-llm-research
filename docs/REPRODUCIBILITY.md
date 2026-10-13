# Reproduzierbarkeit

## Was heute reproduzierbar ist

Offline-Validierung der Projektstruktur, Quellen- und Claim-Referenzen sowie Evidenzstatus. Python >=3.11, Standardbibliothek; keine Paketinstallation, keine Netzverbindung und kein Seed erforderlich.
Aus dem Repository-Stamm ausführen:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

CI führt dieselben Prüfungen aus. Es existiert derzeit keine AIR-LLM-Simulation. Leere Register sind kein positives Forschungsergebnis.

## Vertrag für zukünftige Läufe

Jeder Lauf benötigt:
- Experiment-ID und vorab versioniertes Protokoll;
- vollständigen Git-Commit und Information über lokale Änderungen;
- Betriebssystem, Hardware, Interpreter sowie exakt fixierte Abhängigkeiten;
- Datenquelle, Rechte, unveränderte Eingabe-Hashes und Vorverarbeitung;
- Konfiguration, Einheiten und Seeds oder Begründung deterministischen Verhaltens;
- ausführbaren Startbefehl, Start-/Endzeit, Exitstatus und Logs;
- Rohresultate, Auswertung, Unsicherheiten, Baseline und negative Ergebnisse;
- SHA-256 für relevante Artefakte und konkrete Zuordnung zu Claims.

Versions-/Hardwareunterschiede und nichtdeterministische Operationen müssen benannt werden. Behauptete Replikation benötigt unabhängigen Lauf mit Vergleichskriterium.
Große Daten und Modellgewichte nicht in Git einchecken; freigegebene Bezugsquelle und Checksummen nutzen. Vertrauliche Daten bleiben außerhalb des öffentlichen Projekts.

## Ordnerkonvention

Protokoll: experiments/<experiment-id>/PROTOCOL.md.
Freigegebene Laufartefakte: results/<experiment-id>/<run-id>/.
Eintrag in registries/experiments.json erst mit passendem Status; `completed` erfordert vorhandene Artefakte. Ein Registry-Eintrag allein belegt keine wissenschaftliche Güte.
