# Estrazione di notizie italiane tramite API

> **Stato:** lo script `estrai_notizie.py` non è ancora pubblicato. Il repository contiene per ora un esempio dell'output.

L'obiettivo è scaricare le notizie italiane tramite API e salvarle in un CSV con data e ora dell'estrazione.

## Output di esempio

`notizie_italia_2026-05-14_11-31.csv` contiene 100 notizie con quattro colonne: `publishedAt`, `source_name`, `title` e `url`.

Controllando il file risulta che:

- le notizie arrivano da 19 fonti, con Tuttomercatoweb (23), ANSA (19) e Il Fatto Quotidiano (17) in testa;
- 5 titoli sono duplicati;
- l'estrazione è del 14 maggio alle 11:31, ma le notizie sono state pubblicate il 13 maggio tra le 05:33 e le 09:30 UTC, quindi con oltre un giorno di ritardo.

<img width="926" height="495" alt="Output dello script nel terminale" src="https://github.com/user-attachments/assets/301183f3-43bb-47ed-9248-b0d6000c1a98" />
