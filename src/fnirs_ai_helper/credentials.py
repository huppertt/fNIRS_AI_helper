"""OS credential-store access for LLM provider API keys."""

SERVICE_NAME = "org.brainanalyzir.fnirs-ai-helper"
ACCOUNT_NAMES = {
    "gemini": "gemini-api-key",
    "openrouter": "openrouter-api-key",
}
ACCOUNT_NAME = ACCOUNT_NAMES["gemini"]
_SECURE_BACKENDS = {
    ("keyring.backends.SecretService", "Keyring"),
    ("keyring.backends.Windows", "WinVaultKeyring"),
    ("keyring.backends.kwallet", "DBusKeyring"),
    ("keyring.backends.macOS", "Keyring"),
}


class CredentialStoreError(RuntimeError):
    """Raised when a secure operating-system credential store is unavailable."""


class CredentialStore:
    """Store the API key only in a keyring backend with positive priority."""

    @staticmethod
    def _keyring():
        try:
            import keyring
        except ImportError as exc:
            raise CredentialStoreError(
                "The keyring package is unavailable. Install the app dependencies."
            ) from exc

        try:
            backend = keyring.get_keyring()
            backend_type = (type(backend).__module__, type(backend).__name__)
            if (
                backend is None
                or backend.priority <= 0
                or backend_type not in _SECURE_BACKENDS
            ):
                raise CredentialStoreError(
                    "No supported native OS credential-store backend is available. "
                    "The API key was not saved."
                )
        except CredentialStoreError:
            raise
        except Exception as exc:
            raise CredentialStoreError(
                f"Could not access the OS credential store: {exc}"
            ) from exc
        return keyring

    @staticmethod
    def _account_name(provider: str) -> str:
        try:
            return ACCOUNT_NAMES[provider]
        except KeyError as exc:
            raise ValueError(f"Unsupported API-key provider: {provider}") from exc

    def get_api_key(self, provider: str = "gemini") -> str | None:
        keyring = self._keyring()
        account_name = self._account_name(provider)
        try:
            return keyring.get_password(SERVICE_NAME, account_name)
        except Exception as exc:
            raise CredentialStoreError(
                f"Could not read the {provider} API key from the OS credential store: {exc}"
            ) from exc

    def save_api_key(self, api_key: str, provider: str = "gemini") -> None:
        value = api_key.strip()
        if not value:
            raise ValueError("Enter an API key before saving.")
        keyring = self._keyring()
        account_name = self._account_name(provider)
        try:
            keyring.set_password(SERVICE_NAME, account_name, value)
        except Exception as exc:
            raise CredentialStoreError(
                f"Could not save the API key to the OS credential store: {exc}"
            ) from exc

    def delete_api_key(self, provider: str = "gemini") -> None:
        keyring = self._keyring()
        account_name = self._account_name(provider)
        try:
            if keyring.get_password(SERVICE_NAME, account_name) is not None:
                keyring.delete_password(SERVICE_NAME, account_name)
        except Exception as exc:
            raise CredentialStoreError(
                f"Could not remove the {provider} API key from the OS credential store: {exc}"
            ) from exc
