#!/usr/bin/env bash
# Builds doc_template/ in strict mode the way tools use it:
# once as a single-part tool and once as a tool with several parts.
set -euo pipefail
cd "$(dirname "$0")/.."

DOCS=.cache/template-check
rm -rf "$DOCS" && mkdir -p "$DOCS/tools"

# Single-part tool
cp -r doc_template "$DOCS/tools/single"

# Tool with several parts: overview at the top, one template copy per part
mkdir -p "$DOCS/tools/multi"
cp doc_template/index.md "$DOCS/tools/multi/index.md"
cat >> "$DOCS/tools/multi/index.md" <<'MD'

## Components

| Component | Docs | What it does | For |
|---|---|---|---|
| Part one | [Part one](part-one/index.md) | Description | node-operator |
| Part two | [Part two](part-two/index.md) | Description | developer |
MD
cp -r doc_template "$DOCS/tools/multi/part-one"
cp -r doc_template "$DOCS/tools/multi/part-two"
cat > "$DOCS/tools/multi/.nav.yml" <<'NAV'
title: TOOL-NAME
nav:
  - Overview: index.md
  - part-one
  - part-two
NAV

mkdocs build -f mkdocs.template.yml
