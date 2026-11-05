"""The live tests' masking (tests/live/recorder.py), proven without a server:
docs/live is public, so what names the lab must not reach it."""

from __future__ import annotations

import base64

import pytest
from live.recorder import Masker


@pytest.fixture
def masker() -> Masker:
    m = Masker()
    m.prefixes = ["lab01"]
    m.add("backup01", "primary")
    m.add("Finance-Policy", "policy")
    return m


def test_known_names_anywhere(masker: Masker) -> None:
    text = masker.text("backup01 runs Finance-Policy; STU 1M_BACKUP01_DS3")
    assert text == "primary-01 runs policy-01; STU 1M_primary-01_DS3"


def test_prefixes_also_after_underscores(masker: Masker) -> None:
    assert "lab01" not in masker.text("slp 1M_LAB01BCK02_DS3, host lab01esx4").lower()


def test_fqdns_addresses_and_emails(masker: Masker) -> None:
    text = masker.text("vc01.corp.local at 10.1.2.3 mailed ops@corp.local")
    assert "corp" not in text and "10.1.2.3" not in text
    assert "192.0.2." in text


def test_code_is_not_a_host_name(masker: Masker) -> None:
    masker.learn("nbu.policies.list and nbu.raw.config")
    assert masker.text("nbu.policies.list") == "nbu.policies.list"


def test_identifying_keys_are_learned(masker: Masker) -> None:
    masker.learn({"vCenter": "vcenter-prod", "clientName": "payroll-db"})
    assert masker.text("payroll-db on vcenter-prod") == "host-01 on vcenter-01"


def test_secrets_by_key(masker: Masker) -> None:
    data = masker.data({"apiKey": "abc", "caCertificate": "-----BEGIN", "count": 3})
    assert data == {"apiKey": "<masked>", "caCertificate": "<masked>", "count": 3}


def test_inside_hex_ids(masker: Masker) -> None:
    hex_id = b"backup01_cloud".hex().upper()
    masked = masker.text(f"id {hex_id}")
    assert bytes.fromhex(masked.split()[1]).decode() == "primary-01_cloud"


def test_leaks_found_even_encoded(masker: Masker) -> None:
    encoded = base64.b64encode(b"host backup01 here").decode()
    assert masker.leaks(f"blob {encoded}")
    assert masker.leaks("text BACKUP01")
    assert not masker.leaks("primary-01 only")


def test_pem_blocks(masker: Masker) -> None:
    pem = "-----BEGIN PUBLIC KEY-----\nMIIBIjAN\n-----END PUBLIC KEY-----"
    assert masker.text(f"key: {pem}") == "key: <public key masked>"
