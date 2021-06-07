# NLP-Projekt: Klassifikation von Unternehmenssnippets
## Datenquellen
Im Rahmen eines Praktikums wurden die Unternehmensdaten zunächst mithilfe einer Web-Scaper Extension von relevanten Webseiten gezogen, um eine Datenbasis für Sales-Aktivitäten zu haben. Mithilfe dieser Anwendung kann in kurzer Zeit eine hohe Anzahl an Unternehmensdaten angereichert werden, indem beispielweise Ausstellerlisten von Messen oder öffentliche Mitgliederdaten von Verbänden heruntergeladen werden. Zur Klassifizierung wurden den Unternehmenseinträgen zunächst händisch Segmente und Subsegmente zugeordnet.

| Unternehmensname  | Straße | PLZ | Land | TelefonNr. | Webseite | E-Mail | Segment   | Subsegment |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| XY AG  | Musterstr. 69  | 65283  | DE  | 0443 582  | www.xyag.de  | info@xyag.de | Industrial & Services | Service Bureau |  

Im Prinzip wurde eine manuelle Textklassifikation vorgenommen, um die Unternehmen in vorgegebene Kategorien einzuordnen. Im Zuge des Praktikums sind knapp 2000 klssifizierte Datensätze entstanden, die von der Salesabteilung und dem Marketing für die Neukundenakquise verwendet werden. 
Für das Projekt können die gelabelten Datensätze für das Training des Klassifizierungsalgorithmus verwendet werden. 
Für das Natural Language Processing nutzen wir sogenannte Snippets, das ist die Kurzbeschreibung der Suchmaschine (in dem Fall Bing). Diese enthalten meist alle relevnaten Informationen und Begriffe, da der Suchmaschinennutzer darüber auf die Webseite gelockt werden soll.
## Datentransformation 
Die Daten, die man über den Web-Scraper erhält, müssen zunächst vorverarbeitet werden, um einheitliche, durch Semikolon getrennte Datensätze zu erhalten. Für diese vorgeschobene Bearbeitung wurde die search and replace Funktion im Text Editor verwendet.
Nachdem die Daten, vernünftig angezeigt werden konnten, wurden unvollständige Einträge aus den Trainingsdaten entfernt. Diese Vorbereitung erfolgte noch manuell.
