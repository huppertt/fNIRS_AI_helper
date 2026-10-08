# fNIRS AI Helper

This separate project is for developing a local-first, AI-assisted helper for
Brain Analyzer / pyNIRS_toolbox. The initial focus is documentation of existing
pipeline operations. The helper should explain and orchestrate Brain Analyzer
functionality rather than replace it.

## Current scope

- [Basic pipeline context](docs/basic-pipeline-context.md) records the pipeline
  modules currently shown by the Pipeline Manager when advanced modules are
  hidden.
- [Basic modality workflows](docs/basic-modality-workflows.md) summarizes
  workflows shown by Python tests/examples and MATLAB demos, with evidence
  limits and differences called out.
- [Event annotation context](docs/event-annotation-context.md) documents the
  existing event pairing behavior relevant to the initial prototype.
- [Video-lecture context](docs/video-lecture-context.md) condenses six
  timestamped transcript files into analysis guidance, with caveats separating
  lecture recommendations and historical MATLAB examples from current Python
  behavior.
- The initial GUI is a documentation-grounded, one-turn Q&A prototype with
  Google Gemini and OpenRouter provider options. It does not read datasets,
  execute tools, or modify annotations.

## Run the GUI

Use Python 3.10 or newer. From this folder, create an isolated environment,
install the project, and start the application:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m fnirs_ai_helper
```

Select a provider in the app and use its API-key button to save a key:

- **OpenRouter (default):** Create a key in
  [OpenRouter settings](https://openrouter.ai/settings/keys). The default
  `openrouter/free` model routes to an available free model. You can enter
  another OpenRouter model ID in the editable **Model ID** field.
- **Google Gemini:** Create a key in
  [Google AI Studio](https://aistudio.google.com/apikey).

Keys are stored separately in a supported native OS credential store (macOS
Keychain, Windows Credential Locker, or supported Linux Secret Service/KWallet
backends). They are not written to this repository or a plaintext
configuration file. If a supported backend is unavailable, the application
will report that and will not fall back to a file-based keyring.

This is an API key (not a ChatGPT subscription or a reusable Google sign-in
token). Google provides an unpaid Gemini API tier for certain models and
regions, with usage limits that can change; it is not an academic-specific
entitlement or guaranteed unlimited service. Check the current
[pricing and quota details](https://ai.google.dev/gemini-api/docs/pricing).

Each question and the selected local documentation are sent directly to the
selected API service. OpenRouter routes each request to the chosen model; its
data handling, retention, and pricing can depend on OpenRouter and the selected
model provider. Review current [OpenRouter privacy information](https://openrouter.ai/privacy)
and [model/provider routing information](https://openrouter.ai/docs/guides/routing)
before use. For Gemini, Google's unpaid-tier terms may allow submitted content
and generated responses to be used to improve products and reviewed by humans.
Google's terms require users to be 18 or older and prohibit clinical use and
medical advice. Review [Gemini API terms](https://ai.google.dev/gemini-api/terms)
and institutional requirements before use. Google's terms may require paid
services for API clients made available in the EEA, Switzerland, or UK.
Never submit sensitive, confidential, or personal information, including PHI
or identifying study details, to any provider. This prototype does not send
recordings because it does not load them, but users can still type sensitive
information into the question box.

The default question is the odd/even marker example from
`ChatGPT_interface/Example_001_odd_even_stimulus_markers.txt`. Submitted
questions appear in blue in the read-only transcript, and the question field
clears for the next question. The transcript retains earlier exchanges in the
current app session.
Requests run asynchronously with a 60-second total deadline; the GUI displays
elapsed time and reports provider errors.

For development, each successful question and response is appended to a
date-named JSON Lines file in `development_logs/`; submitted ratings are
appended as separate entries. These local logs are excluded from Git. They do
not contain API keys or the documentation context, but they do contain the
question and response, so do not include sensitive or identifying information.

## Development

Run the tests with:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest
```

The provider boundary is deliberately small so providers can be added without
changing the GUI or context assembly. Gemini uses Google's official
`google-genai` SDK, and OpenRouter uses its OpenAI-compatible chat-completions
endpoint.

## Privacy and contributions

Keep this repository limited to software architecture, public scientific
references, and de-identified or synthetic examples. Do not add human-subject
data, PHI, credentials, API keys, or private study details.

For future knowledge entries, document the problem, observed marker pattern,
interpretation, proposed operation(s), assumptions, exceptions, and validation
steps. Keep case-specific facts clearly distinguished from general rules.

## Sharing this context with ChatGPT and Copilot

The Markdown files in this repository are the canonical, version-controlled
context. Copilot can use them when this repository is open in the workspace.
To use the same material with ChatGPT, connect the GitHub repository if a
GitHub connector is available for the user's ChatGPT account, or provide the
public repository/document link in the conversation. Availability and write
capabilities depend on the account and product configuration; a copied or
uploaded document is a snapshot and may become stale.

Prefer making substantive changes as reviewable Git commits or pull requests.
The repository owner must create/publish the GitHub repository and configure
access; this local project does not include credentials or provider setup.
