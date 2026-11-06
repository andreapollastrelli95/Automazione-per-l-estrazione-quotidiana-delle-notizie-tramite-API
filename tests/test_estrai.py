import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import estrai_notizie as e


def articolo(titolo):
    return {"publishedAt": "2026-05-13T09:30:50Z", "source": {"name": "ANSA.it"}, "title": titolo, "url": "https://x"}


def test_pulisci_toglie_duplicati_e_rimossi():
    t = e.pulisci([articolo("A"), articolo(" A "), articolo("[Removed]"), articolo(None), articolo("B")])
    assert list(t.title) == ["A", "B"]
    assert list(t.columns) == e.COLONNE


def test_errore_api_chiaro():
    class Risposta:
        status_code = 401
        text = "chiave non valida"

    class Sessione:
        def get(self, *a, **k):
            return Risposta()

    with pytest.raises(RuntimeError, match="401"):
        e.scarica("x", sessione=Sessione())
