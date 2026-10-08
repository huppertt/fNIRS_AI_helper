# fNIRS AI Helper

This separate project is for developing a local-first, AI-assisted helper for
Brain Analyzer / pyNIRS_toolbox. The initial focus is documentation of existing
pipeline operations. The helper should explain and orchestrate Brain Analyzer
functionality rather than replace it.

## Current scope

- [Basic pipeline context](docs/basic-pipeline-context.md) records the pipeline
  modules currently shown by the Pipeline Manager when advanced modules are
  hidden.
- No AI provider, tool execution, dataset access, or annotation modification
  code is implemented yet.

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
