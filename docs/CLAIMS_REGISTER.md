# Claims Register

Maschinenlesbare Quelle: [registries/claims.json](../registries/claims.json).

## Aktueller Stand

| ID | Aussage | Art | Status |
|---|---|---|---|
| C-0001 | MUNIN-General meldete beim Zugriffsaudit read_only=true | Zugriffsbefund | verified_access |
| C-0002 | AIR-LLM wurde über project_context und exakte Suche nicht gefunden | begrenzter Suchbefund | verified_access |
| C-0003 | Die drei Dossier-Volltexte waren im verfügbaren Abruf nicht enthalten | Quellenverfügbarkeit | source_missing |

**Keine wissenschaftlichen AIR-LLM-Claims extrahiert oder validiert.** Die drei Einträge dokumentieren Projektzustand und Zugriff; sie sind keine Forschungsergebnisse. Der Suchbefund behauptet keine vollständige Abwesenheit aus allen Obsidian-Daten.

## Schema und zulässige Zustände

Jeder Eintrag besitzt ID, präzise Aussage, Typ, Status, Quellen-IDs, Fundstellen, Annahmen, Unsicherheit, Prüfmethode und Experimentverweise.
Wissenschaftliche Zustände: `hypothesis`, `model_unverified`, `simulation_unverified`, `empirical_unverified`, `validated`, `refuted`, `contested`, `source_missing`.
`validated` erfordert verfügbare Quellen mit Fundstelle und mindestens einen abgeschlossenen Experimentdatensatz mit vorhandenen Artefakten. Das ist eine Mindestregel der Registerprüfung, keine automatische wissenschaftliche Begutachtung.
Reine Herleitungen verbleiben bis zur manuellen Prüfung als unvalidierte Modellclaims; das Schema kann bei fachlichem Bedarf mit dokumentierter Entscheidung erweitert werden.

## Reviewregeln

Gesprächsaussage ≠ Primärbeleg. Modellrechnung ≠ Simulation. Simulation ≠ Realweltmessung.
Unbelegte Parameter, Extrapolationen und angenommene Wirkungsgrade müssen explizit markiert werden.
Widersprüche erhalten getrennte Belege und den Status `contested`; keine stille Zusammenführung.
Statusänderungen benötigen Commit, Begründung und Nachweis. Keine leeren Platzhalter mit Status „validated“.
