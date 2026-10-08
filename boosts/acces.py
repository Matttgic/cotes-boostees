"""Accès aux sites des bookmakers : IP française (proxy Bright Data, zone ISP) + empreinte de Chrome.

Sans IP française, Winamax, Unibet et PMU renvoient 403 aux serveurs GitHub (américains).
Avec l'IP française mais le client Python standard, Winamax renvoie encore 403 (pare-feu
CloudFront) : il faut l'empreinte TLS/HTTP2 d'un vrai Chrome (curl_cffi).
"""
from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote

CA_BRIGHTDATA = Path(__file__).resolve().parent.parent / "certs" / "brightdata_proxy_ca.crt"
PORT_DEFAUT = "44445"          # port affiché dans le panneau Bright Data pour la zone ISP


class SecretsManquants(RuntimeError):
    pass


def proxy_francais(session: str) -> dict:
    """URL du proxy, sortie en France ; `session` garde la même IP pour tout un passage."""
    client = os.environ.get("BRIGHTDATA_CUSTOMER_ID", "").strip().removeprefix("brd-customer-")
    zone = os.environ.get("BRIGHTDATA_ZONE", "").strip()
    mdp = os.environ.get("BRIGHTDATA_PASSWORD", "").strip()
    if not (client and zone and mdp):
        raise SecretsManquants("BRIGHTDATA_CUSTOMER_ID, BRIGHTDATA_ZONE et BRIGHTDATA_PASSWORD sont requis")
    port = os.environ.get("BRIGHTDATA_PORT", "").strip() or PORT_DEFAUT
    url = (f"http://brd-customer-{client}-zone-{zone}-country-fr-session-{session}:"
           f"{quote(mdp, safe='')}@brd.superproxy.io:{port}")
    return {"http": url, "https": url}


def bundle_certificats(dossier: Path) -> str:
    """Certificats publics + Bright Data (valable que la zone intercepte le TLS ou non)."""
    import certifi
    chemin = dossier / "ca_bundle.pem"
    chemin.write_text(Path(certifi.where()).read_text() + "\n" + CA_BRIGHTDATA.read_text())
    return str(chemin)


def masquer(texte: str) -> str:
    """Retire le mot de passe du proxy d'un texte (message d'erreur contenant l'URL du proxy)."""
    v = os.environ.get("BRIGHTDATA_PASSWORD", "").strip()
    if len(v) >= 4:
        texte = texte.replace(v, "***").replace(quote(v, safe=""), "***")
    return texte


class Navigateur:
    """Client HTTP « Chrome » passant par le proxy français, avec comptage des octets reçus."""

    def __init__(self, dossier_tmp: Path):
        from curl_cffi import requests as creq
        self._creq = creq
        self.proxies = proxy_francais(os.urandom(4).hex())
        self.verif = bundle_certificats(dossier_tmp)
        self.octets = 0
        self.requetes = 0

    def get(self, url: str, timeout: int = 60):
        self.requetes += 1
        r = self._creq.get(url, impersonate="chrome", proxies=self.proxies, verify=self.verif,
                           timeout=timeout, headers={"Accept-Language": "fr-FR,fr;q=0.9"})
        self.octets += len(r.content)
        return r
