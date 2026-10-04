# Tool docs template

Copy [`doc_template`](https://github.com/EIDA/doc/tree/main/doc_template) into
your repository as `docs/`:

```bash
cp -r doc_template my-repo/docs
```

1. Replace `TOOL-NAME` in `.nav.yml` and in every page title.
2. Move your existing text into the pages, replacing the `<!-- ... -->` comments.
3. Delete the pages you have no content for, and their lines in `.nav.yml`.
4. Keep only the tags that apply on each page.

## Rules

- Move existing text into the pages. Do not rewrite it.
- Page titles start with the tool name, for example `# ws-availability: Install`.
- Tags are only `data-user`, `node-operator` and `developer`.
- Links between pages are relative; links to anything else use a full URL.
- For tools made of several parts, fill in Components on the overview page and
  use the same names as headings on the other pages.

## Examples

- [eida-statistics](examples/eida-statistics.md): a tool made of several parts
- [ws-availability](examples/ws-availability.md): a README split into pages
