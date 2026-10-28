#!/usr/bin/env bash
# Builds doc_template/ in strict mode the way services use it:
# once as a single-part service and once as a service with several parts.
set -euo pipefail
cd "$(dirname "$0")/.."

DOCS=.cache/template-check
rm -rf "$DOCS" && mkdir -p "$DOCS/services"

# Single-part service
cp -r doc_template "$DOCS/services/single"

# Service with several parts: overview at the top, one template copy per part
mkdir -p "$DOCS/services/multi"
cp doc_template/index.md "$DOCS/services/multi/index.md"
cat >>"$DOCS/services/multi/index.md" <<'MD'

## Components

| Component | Docs | What it does | For |
|---|---|---|---|
| Part one | [Part one](part-one/index.md) | Description | operator |
| Part two | [Part two](part-two/index.md) | Description | developer |
MD
cp -r doc_template "$DOCS/services/multi/part-one"
cp -r doc_template "$DOCS/services/multi/part-two"

mkdocs build -f mkdocs.template.yml
