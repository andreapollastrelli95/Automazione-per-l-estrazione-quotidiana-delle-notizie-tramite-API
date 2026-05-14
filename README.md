# Automazione-per-l-estrazione-quotidiana-delle-notizie-tramite-API
Questo progetto automatizza il download delle notizie italiane aggiornate utilizzando un sistema basato su API. Lo script estrae i titoli dai principali quotidiani nazionali, li pulisce, li organizza e genera automaticamente un file CSV con data e ora dell’estrazione.

🎯 Obiettivi del progetto
Automatizzare la raccolta delle notizie italiane da più fonti
Salvare i risultati in un file CSV con timestamp
Rendere il processo eseguibile con un singolo comando
Creare una pipeline semplice, veloce e riutilizzabile

⚙️ Come funziona l’automazione
Lo script:
Si connette ai server delle news tramite API
Recupera un numero configurabile di notizie (es. 100)
Estrae:
nome della fonte
titolo della notizia
URL (se disponibile)
data di pubblicazione

Genera un file CSV con nome automatico:
notizie_italia_YYYY-MM-DD_HH-MM.csv
Esempio reale generato:
notizie_italia_2026-05-14_11-31.csv

🧪 Esempio di output (console)
Connessione ai server delle notizie...
✅ Successo! Creato il file: notizie_italia_2026-05-14_11-31.csv
--- ESTRATTE 100 NOTIZIE ---
    source_name                title
0   Ilpost.it                  Al ministero della Giustizia la gestione dell’...
1   Tuttomercatoweb.com        Lotito su Malagò: "Kant parlava di fenomeno e ...
2   Ilgiornale.it              Una voragine da 174 miliardi
3   La Repubblica              Obesità: aumenta il peso medio, in ascensore e...
...
Premi Invio per chiudere...

🛠️ Tecnologie utilizzate
Python
Requests (per chiamate API)
Pandas (per la creazione del CSV)
JSON (gestione delle risposte API)
Batch / CMD (per esecuzione automatizzata)

▶️ Come eseguire lo script
Clona il repository
Installa le dipendenze:

Codice
pip install -r requirements.txt
Esegui lo script:

Codice
python estrai_notizie.py

Troverai il CSV generato nella cartella del progetto.

📌 Funzionalità aggiuntive (opzionali)
Pianificazione giornaliera tramite Windows Task Scheduler
Invio automatico via email
Integrazione con Power BI per dashboard aggiornate
