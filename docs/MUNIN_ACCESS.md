# MUNIN/Obsidian — Zugriffsstatus und sichere Synchronisierung

Prüfung: 2026-10-13T21:39:42.054803+00:00 (2026-10-13, 23:39 MESZ).
Scope: ausschließlich konfigurierter MUNIN-MCP und MUNIN-General.

## Verifizierter Live-Status

| Prüfung | Ergebnis | Aussagegrenze |
|---|---|---|
| health | status=ok; service=munin-mcp; version=0.1.0 | Dienst erreichbar |
| sichtbarer Vault | MUNIN-General | keine Aussage über weitere Vaults |
| Schreibstatus | read_only=true | kein Schreibzugriff über diese Integration |
| project_context AIR-LLM | project_not_found | kein passendes Projektverzeichnis aufgelöst |
| exakte knowledge_search AIR-LLM | 0 Treffer; Backend sqlite_fts5; index_documents=36 | begrenzter Indexbefund, kein Vollständigkeitsbeweis |
| knowledge_read Policy | 12 Zeilen aus 00-System/Prompts/Brain-First.md erfolgreich gelesen | praktischer, begrenzter Markdown-Lesezugriff bestätigt |
| vorhandene Werkzeuge | health, vault_info, project_context, knowledge_search, knowledge_read | ausschließlich lesende Werkzeuge |
| MUNIN-Schreibtest | nicht durchgeführt | Mutationswerkzeug fehlt; Policy untersagt Umgehung |
| Obsidian-Anwendung/lokales Vault-Dateisystem | nicht geprüft | keine Schreibfähigkeit daraus abgeleitet |

Maschinenlesbare, minimierte Prüfdaten: [access-audit.json](../registries/access-audit.json).
Es wurde kein Projekt-Wissensdokument geöffnet oder öffentlich exportiert. Als Leseprobe wurden ausschließlich zwölf Zeilen der bekannten Systempolicy gelesen: `00-System/Prompts/Brain-First.md`, Zeilen 1–12. Suchtreffer wären vor Verwendung stets mit knowledge_read zu prüfen.

MUNIN-Restricted wurde nicht angefragt, gelesen, durchsucht oder anderweitig berührt.
Ein erfolgreiches health ist kein Schreibnachweis. Vorhandene Dateisystemrechte des Computers würden ebenfalls keine autorisierte Vault-Schreibintegration belegen.

## Aktuell zulässiger Ablauf

GitHub hält freigegebene Forschungsartefakte und ihre Versionen. MUNIN wird bei Bedarf gezielt als lesende Wissensquelle genutzt.
**Kein automatischer Sync, kein behaupteter Ingest, keine bidirektionale Replikation.**
Nur Projekt-ID, Claim-IDs und freigegebene GitHub-Links können für einen späteren manuellen Wissenseintrag vorbereitet werden. Ein vorbereiteter Text ist noch kein gespeicherter MUNIN-Eintrag.

## Regeln für einen späteren, separat autorisierten Ingest

1. Dedizierte, erlaubte Schreibschnittstelle und Ziel in MUNIN-General festlegen. Kein direkter Dateisystem- oder Shell-Umweg.
2. Erlaubte Zielpfade auf einen Projektbereich begrenzen. Restricted bleibt vollständig ausgeschlossen.
3. Vor Übertragung Inhalte prüfen: keine Tokens, Zugangsdaten, personenbezogenen Informationen, ungeprüften Vault-Auszüge oder Rohgespräche.
4. Daten pro Richtung explizit freigeben. Ein lesbarer MUNIN-Inhalt ist nicht automatisch für das öffentliche GitHub-Repository freigegeben.
5. Herkunft dokumentieren: freigegebener Repository-Pfad, Commit-SHA, Claim-IDs, Quellversion, Prüfer und Zeitpunkt.
6. Erst Dry-run/Diff und Backup; dann kleine idempotente Änderungen mit Versionsprüfung. Keine pauschale Spiegelung und keine propagierten Löschungen.
7. Bei konkurrierenden Änderungen anhalten, beide Versionen erhalten und den Konflikt zur Entscheidung vorlegen.
8. Nach erlaubtem Schreiben über die Schnittstelle zurücklesen, Inhalt/Hash vergleichen und einen minimierten Receipt speichern. Erst dann „synchronisiert“ melden.
9. Fehler dürfen nie zu stillen Wiederholungen, Doppeleinträgen oder erweiterten Zielpfaden führen.

Diese Regeln beschreiben einen möglichen zukünftigen Workflow. Er ist weder eingerichtet noch ausgeführt; Änderungen am kanonischen Konfliktverfahren benötigen eigene Klärung.
