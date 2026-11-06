# Estrazione di notizie italiane tramite API

Scarica le notizie italiane da [NewsAPI](https://newsapi.org), toglie titoli vuoti e duplicati e le salva in un CSV con data e ora dell'estrazione.

## Avvio

```bash
pip install -r requirements.txt
export NEWSAPI_KEY=la_tua_chiave   # Windows PowerShell: $env:NEWSAPI_KEY="la_tua_chiave"
python estrai_notizie.py
```

Per un'esecuzione quotidiana si può usare l'Utilità di pianificazione di Windows o cron. Con il piano gratuito NewsAPI può fornire le notizie in ritardo.

Lo script è stato riscritto a partire dal formato del CSV di esempio, generato da una versione precedente non conservata. I test simulano l'API.

## Output di esempio della versione precedente

`notizie_italia_2026-05-14_11-31.csv` contiene 100 notizie con quattro colonne: `publishedAt`, `source_name`, `title` e `url`.

Controllando il file risulta che:

- le notizie arrivano da 19 fonti, con Tuttomercatoweb (23), ANSA (19) e Il Fatto Quotidiano (17) in testa;
- 5 titoli sono duplicati;
- l'estrazione è del 14 maggio alle 11:31, ma le notizie sono state pubblicate il 13 maggio tra le 05:33 e le 09:30 UTC, quindi con oltre un giorno di ritardo.

<img width="926" height="495" alt="Output dello script nel terminale" src="https://github.com/user-attachments/assets/301183f3-43bb-47ed-9248-b0d6000c1a98" />
