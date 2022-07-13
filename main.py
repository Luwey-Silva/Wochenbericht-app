#----------------------Importiert Biblioteken-------------#

from pathlib import Path
from docxtpl import DocxTemplate


#----------------------Speichern der datei----------------#

schueler_name = str(input("Gib dein Name ein: "))
kalenderwoche = str(input("Kalenderwoche eingeben: "))
dateiname_ende = "Arbeitsbericht_KW_" + kalenderwoche +"_"+ schueler_name + ".docx"

#----------------------Daten eingabe----------------------#

user_name = str(input("Bitte Name eingeben: "))
user_beschreibung_montag = str(input("Was würde am Montag gemacht? "))
user_stunden_montag = float(input("Gib die Stunden für Montag ein: "))
user_beschreibung_dienstag = str(input("Was würde am Montag gemacht? "))
user_stunden_dienstag = float(input("Gib die Stunden für Montag ein: "))
user_beschreibung_mittwoch = str(input("Was würde am Montag gemacht? "))
user_stunden_mittwoch = float(input("Gib die Stunden für Montag ein: "))
user_beschreibung_donnerstag = str(input("Was würde am Montag gemacht? "))
user_stunden_donnerstag = float(input("Gib die Stunden für Montag ein: "))
user_beschreibung_freitag = str(input("Was würde am Montag gemacht? "))
user_stunden_freitag = float(input("Gib die Stunden für Montag ein: "))

#tag_der_unterschrift =
#von_bis_tag = 



#----------------------Datei Vorlage----------------------#

document_path = Path(__file__).parent / "Arbeitsbericht.docx"
doc = DocxTemplate(document_path)


#---------------------Wörterbuch (Context)----------------#

context = {
    "NAME": user_name,
    "USER_STUNDEN_MONTAG" : user_stunden_montag, 
    "USER_STUNDEN_DIENSTAG" : user_stunden_dienstag,
    "USER_STUNDEN_MITTWOCH" : user_stunden_mittwoch,
    "USER_STUNDEN_DONNERSTAG" : user_stunden_donnerstag,
    "USER_STUNDEN_FREITAG" :  user_stunden_freitag,
    "USER_BESCHREIBUNG_MONTAG" : user_beschreibung_montag,
    "USER_BESCHREIBUNG_DIENSTAG" : user_beschreibung_dienstag,
    "USER_BESCHREIBUNG_MITTWOCH" : user_beschreibung_mittwoch,
    "USER_BESCHREIBUNG_DONNERSTAG" : user_beschreibung_donnerstag,
    "USER_BESCHREIBUNG_FREITAG" : user_beschreibung_freitag,
    }


#----------------------Speichern der datei----------------#

doc.render(context)
doc.save(Path(__file__).parent / dateiname_ende)

#----------------------Progamm Ende-----------------------#