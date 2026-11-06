"""Scarica le notizie italiane da NewsAPI e le salva in un CSV con data e ora.

Riscritto a partire dal formato del CSV di esempio. Richiede la variabile NEWSAPI_KEY.
"""
import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests

API_URL = "https://newsapi.org/v2/everything"
FONTI = "ansa.it,repubblica.it,ilsole24ore.com,ilfattoquotidiano.it,ilgiornale.it,ilpost.it"
COLONNE = ["publishedAt", "source_name", "title", "url"]


def scarica(chiave, quante=100, sessione=requests):
    risposta = sessione.get(
        API_URL,
        params={"domains": FONTI, "language": "it", "sortBy": "publishedAt", "pageSize": quante},
        headers={"X-Api-Key": chiave},
        timeout=30,
    )
    if risposta.status_code != 200:
        raise RuntimeError(f"NewsAPI ha risposto {risposta.status_code}: {risposta.text[:200]}")
    return risposta.json().get("articles", [])


def pulisci(articoli):
    """Tiene le colonne utili, toglie articoli rimossi, titoli vuoti e duplicati."""
    righe = [
        {
            "publishedAt": a.get("publishedAt"),
            "source_name": (a.get("source") or {}).get("name"),
            "title": (a.get("title") or "").strip(),
            "url": a.get("url"),
        }
        for a in articoli
    ]
    tabella = pd.DataFrame(righe, columns=COLONNE)
    tabella = tabella[(tabella.title != "") & (tabella.title != "[Removed]")]
    return tabella.drop_duplicates("title").reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quante", type=int, default=100, help="Numero di notizie da chiedere (massimo 100)")
    parser.add_argument("--cartella", type=Path, default=Path("."), help="Dove salvare il CSV")
    args = parser.parse_args()

    chiave = os.environ.get("NEWSAPI_KEY")
    if not chiave:
        sys.exit("Imposta la variabile NEWSAPI_KEY con la tua chiave di newsapi.org")
    try:
        tabella = pulisci(scarica(chiave, args.quante))
    except (requests.RequestException, RuntimeError) as errore:
        sys.exit(f"Estrazione non riuscita: {errore}")

    args.cartella.mkdir(parents=True, exist_ok=True)
    percorso = args.cartella / f"notizie_italia_{datetime.now():%Y-%m-%d_%H-%M}.csv"
    tabella.to_csv(percorso, index=False, encoding="utf-8-sig")
    print(f"Salvate {len(tabella)} notizie in {percorso}")


if __name__ == "__main__":
    main()
