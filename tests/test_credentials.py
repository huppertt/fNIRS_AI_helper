import sys
from types import SimpleNamespace

import pytest

from fnirs_ai_helper.credentials import (
    ACCOUNT_NAMES,
    ACCOUNT_NAME,
    SERVICE_NAME,
    CredentialStore,
    CredentialStoreError,
)


class MemoryKeyring:
    def __init__(self, priority=1):
        self.priority = priority
        self.values = {}

    def get_password(self, service, account):
        return self.values.get((service, account))

    def set_password(self, service, account, value):
        self.values[(service, account)] = value

    def delete_password(self, service, account):
        del self.values[(service, account)]


NativeTestKeyring = type(
    "Keyring", (MemoryKeyring,), {"__module__": "keyring.backends.macOS"}
)


def install_fake_keyring(monkeypatch, backend):
    module = SimpleNamespace(
        get_keyring=lambda: backend,
        get_password=backend.get_password,
        set_password=backend.set_password,
        delete_password=backend.delete_password,
    )
    monkeypatch.setitem(sys.modules, "keyring", module)


def test_credentials_use_keyring_and_never_write_to_project_files(monkeypatch, tmp_path):
    backend = NativeTestKeyring()
    install_fake_keyring(monkeypatch, backend)
    credentials = CredentialStore()

    credentials.save_api_key("  user-secret  ")

    assert credentials.get_api_key() == "user-secret"
    assert backend.values == {(SERVICE_NAME, ACCOUNT_NAME): "user-secret"}
    assert list(tmp_path.iterdir()) == []
    credentials.delete_api_key()
    assert credentials.get_api_key() is None


def test_provider_api_keys_are_stored_separately(monkeypatch):
    backend = NativeTestKeyring()
    install_fake_keyring(monkeypatch, backend)
    credentials = CredentialStore()

    credentials.save_api_key("gemini-secret", "gemini")
    credentials.save_api_key("openrouter-secret", "openrouter")

    assert credentials.get_api_key("gemini") == "gemini-secret"
    assert credentials.get_api_key("openrouter") == "openrouter-secret"
    assert ACCOUNT_NAMES["gemini"] != ACCOUNT_NAMES["openrouter"]
    credentials.delete_api_key("openrouter")
    assert credentials.get_api_key("openrouter") is None
    assert credentials.get_api_key("gemini") == "gemini-secret"


def test_credentials_fail_closed_without_secure_backend(monkeypatch):
    install_fake_keyring(monkeypatch, MemoryKeyring(priority=0))

    with pytest.raises(CredentialStoreError, match="No supported native OS"):
        CredentialStore().save_api_key("user-secret")


def test_credentials_reject_plaintext_file_keyring(monkeypatch):
    class PlaintextKeyring(MemoryKeyring):
        __module__ = "keyrings.alt.file"

    install_fake_keyring(monkeypatch, PlaintextKeyring(priority=1))

    with pytest.raises(CredentialStoreError, match="No supported native OS"):
        CredentialStore().save_api_key("user-secret")


def test_credentials_reject_blank_keys():
    with pytest.raises(ValueError, match="Enter an API key"):
        CredentialStore().save_api_key("  ")
