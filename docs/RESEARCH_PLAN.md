# Research Plan — Phase 00/01

Stand: 2026-10-13. Dieser Plan wurde für die Initialisierung erstellt. Frühere Phasendefinitionen waren im Gesprächsabruf nicht lesbar; historische Übereinstimmung wird nicht behauptet.

## Phase 00 — Foundation

Lieferungen: Charter, Quellen- und Claim-Schema, öffentlicher Projektstand, Backlog, MUNIN-Audit, Offline-Prüfung und CI.
Gate G00: Repository öffentlich; Commit abrufbar; Dokumente und Register geprüft; Issues vorhanden; Zugriffsbeschränkungen dokumentiert.
Owner: fjoelnr; operative Dokumentation durch beauftragte Assistenz.

## Phase 01 — Evidence and dossier review

### 01.1 Originalquellen sichern — blockiert

Drei Originaldossiers als Text/Markdown/PDF beschaffen. Pro Dokument Titel, Version, Datum, Autor/Entstehung, Herkunft, Rechte, SHA-256 und Fundstellenkonvention erfassen. Keine Platzhalter als Beleg akzeptieren. Die Zuordnung der Gesprächs-Nachrichten zu einzelnen Dossiers muss bestätigt werden.
Gate: D01–D03 verfügbar und auf Vollständigkeit geprüft.

### 01.2 Aussagen atomisieren

Pro prüfbarer Aussage eine Claim-ID. Kategorien: Definition, Hypothese, Literaturbehauptung, analytische Herleitung, Modellrechnung, Simulation, empirischer Befund.
Erfassen: exakte Aussage, Fundstelle, Einheiten, Voraussetzungen, Evidenzstatus, Unsicherheit, Gegenbelege, Prüfmethode und Owner.
Gate: Jede wesentliche Schlussfolgerung auf belegte Einzelclaims zurückführbar.

### 01.3 Modellrechnungen prüfen

Für jeden Zahlenwert Eingaben, Einheiten, Gleichungen, Parameterquellen und Gültigkeitsbereich dokumentieren. Rechenschritte unabhängig nachvollziehen; Dimensionsanalyse, Grenzfälle, Sensitivität und alternative Annahmen prüfen.
Unbelegte Inputs bleiben als Annahmen markiert. Rechenrichtigkeit allein validiert die zugrunde liegende Hypothese nicht.
Gate: Jede Zahl reproduzierbar oder als unbelegt/nicht reproduzierbar markiert.

### 01.4 Simulationen und Messungen auditieren

Nur vorhandener ausführbarer Code plus Konfiguration, Umgebung, Seed soweit relevant, Eingabedaten und Laufartefakte zählt als überprüfbarer Lauf.
Im verfügbaren Material fehlen solche Artefakte. Das beweist nicht, dass niemals simuliert wurde; es verhindert die Verifikation.
Gate: Claims ohne Laufnachweis bleiben unvalidiert; fehlende Läufe erhalten Issues.

### 01.5 Experimentprotokolle vorbereiten

Erst nach fachlicher Klärung festlegen: falsifizierbare Hypothese; Zielgröße mit Einheit; Baseline und Nullmodell; kontrollierte Variablen; Datenaufteilung; Parameterraum; Replikate/Seeds; Unsicherheitsauswertung; Erfolgsschwelle; Abbruchregeln; Rechenbudget.
Kein nachträgliches Optimieren der Erfolgsschwelle anhand der Ergebnisse.
Gate G01: Review aller drei Dossiers, Claims abgedeckt, offene Evidenzlücken bekannt, mindestens ein fachlich spezifiziertes Protokoll zur Freigabe vorbereitet.

## Anschließende Forschung — noch nicht gestartet

Phase 02: begrenzter Pilot gegen Baseline, inklusive negativer Ergebnisse.
Phase 03: Replikation, Robustheit, Sensitivität und unabhängiger Reproduktionsversuch.
Diese Phasen sind Vorschläge, keine rekonstruierten Zusagen aus den Dossiers.

## Priorisierung und Abhängigkeiten

P0 Originaltexte → technische Begriffe → Claims/Modellrechnungen → Baseline → Protokoll → Lauf.
MUNIN-Leseverknüpfung kann parallel gepflegt werden; MUNIN-Schreibintegration ist kein implizites Gate und wird nicht vorausgesetzt.
Zeit- und Kostenplanung nach Kenntnis von Modell, Daten und Hardwarebedarf. Keine erfundene Laufzeit oder Rechenkostenprognose.
