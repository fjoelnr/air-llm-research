# AIR-LLM Research

Öffentliches Forschungsprojekt, initialisiert am 13.10.2026. **Keine validierten Forschungsergebnisse, keine nachgewiesenen Simulationen.**

## Stand Phase 00/01

- Phase 00: Projektauftrag, Governance, Zugriffsaudit und reproduzierbare Struktur eingerichtet.
- Phase 01: Quelleninventar und Review-Verfahren eingerichtet; inhaltlicher Dossier-Review **blockiert**, bis die drei Originaltexte vorliegen.
- MUNIN-General: MCP erreichbar und nach Live-Prüfung **nur lesbar**. Keine MUNIN-Schreiboperation und keine Synchronisierung durchgeführt.
- Das Akronym AIR-LLM, die technische Forschungsfrage und mögliche Abgrenzungen zu gleichnamiger Software werden erst anhand der Originaldossiers festgelegt.

## Einstieg

1. [Charter](docs/CHARTER.md)
2. [Research Plan](docs/RESEARCH_PLAN.md)
3. [Dossier-Review und Quellenlücke](docs/DOSSIER_REVIEW.md)
4. [Claims Register](docs/CLAIMS_REGISTER.md), [maschinelles Register](registries/claims.json)
5. [MUNIN-Zugriff und Synchronisierungsregeln](docs/MUNIN_ACCESS.md)
6. [Backlog](docs/BACKLOG.md)
7. [Reproduzierbarkeit](docs/REPRODUCIBILITY.md)
8. [Verifikationsbericht](docs/VERIFICATION.md)

## Lokale Prüfung

Python 3.11 oder neuer, ausschließlich Standardbibliothek:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

Diese Prüfungen validieren Register, Provenienz und Projektstruktur. Sie führen **keine wissenschaftliche Simulation** aus. Ein grüner CI-Status belegt keine AIR-LLM-Hypothese.

## Struktur

```text
docs/               Auftrag, Forschungsplan, Review, Zugriffe, Entscheidungen
registries/         Quellen, Claims, Experimente mit explizitem Evidenzstatus
data/               Richtlinien; keine ungeprüften Rohdaten
experiments/        Protokollvorlage, noch keine ausgeführten Experimente
results/            Richtlinien; noch keine wissenschaftlichen Resultate
scripts/            Offline-Validator
tests/              Validierung von Evidenz- und Integritätsregeln
.github/            CI und Issue-Vorlage
```

Beiträge folgen [CONTRIBUTING.md](CONTRIBUTING.md). Für Dossier-Volltexte und fremde Daten werden keine Nutzungsrechte unterstellt; siehe [RIGHTS.md](RIGHTS.md).
