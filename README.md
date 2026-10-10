# praxisnachbereitung-ws25

A. Git - Vorbereitung
GitRepository angelegt

B. Datenimport & Bereinigung 

Anlegen der Exel Arbeitsmappe und importieren der einszelnen CSV-Dateien. Dabei konnten wir bei der Vorschau den Import prüfen und konnten das Trennzeichen und die UTF-8 Codierung auswählen. Nach dem Import Versuch das Datum in die TT.MM.JJJJ Form zu bringen wobei es Probleme gab. 

Probleme: 
Formatieren des Datum in folgende Form TT.MM.JJJJ lückenhaft da bei fehlender erster 0 Exel es nicht als valide Zahl zum umformatieren erkannt hat. Beispiel bei 6012024 hat er aufgrund der ersten fehlenden 0 --> 06012024 das zu formatierende Datum nicht erkannt. 

C. Datenzusammenführung 

Unsicherheit mit der zu verwendeten JOIN Anweisung, dadurch fehlerhafte zusammengeführte Tabelle. 



D. Visuelle Analyse in Excel 
1) Mit den gegebenen Spalten konnten wir nicht herausfinden, welche Geräte nicht verliehen waren. Da man nicht nur nach Rückgabedatum filtern konnte, da manche Geräte mehrmals ausgeliehen wurden. Daher haben wir eine Hilfsspalte benötigt welche überprüft ob das Gerät noch aktuell ausgeliehen ist, bzw irgendwann nicht zurückgegeben wurde.

2) Beim Filtern werden einzelne Geräte mehrfach angezeigt, da sie mehrfach verliehen wurden.

3+4) Säulendiagramm erstellt welches Verteilung von Gerätetyp und Standort darstellt

E. Export und Git

2) Code funktioniert an sich. Stellt noch das Problem der Daten dar welche nie richtig importiert wurden. 

