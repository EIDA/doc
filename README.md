# doc

Central documentation for end users, published at https://eida.github.io/doc/.

Built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Preview locally

With [uv](https://docs.astral.sh/uv/):

```bash
uv run --no-project --with-requirements requirements.txt python scripts/fetch_services.py
uv run --no-project --with-requirements requirements.txt mkdocs serve
```

Then open http://127.0.0.1:8000/doc/. The first command fetches the service docs;
run it again to pick up changes in the service repositories.

To check the build the way CI does:

```bash
uv run --no-project --with-requirements requirements.txt mkdocs build
```

The build is strict: broken links, broken anchors and unknown tags fail it.

## How it is organised

| Path | What it is |
|---|---|
| `docs/` | Pages of this site. Page order comes from `.nav.yml` files. |
| `services.yml` | The list of services shown on the site. |
| `scripts/fetch_services.py` | Copies each service's docs into `docs/services/<name>/` and writes the menu: one tab per role, built from the `user/`, `operator/` and `developer/` folders. |
| `hooks/services.py` | Points the edit button of service pages at the service's own repository. |
| `doc_template/` | Docs folder for service repositories to copy. |
| `.github/workflows/build.yml` | Builds and deploys the site on push to `main` and every night. |

`docs/services/` and `docs/.nav.yml` are generated and not committed.

## Add a service

1. In the service's repository, copy the template and fill it in:
   `cp -r doc_template my-repo/docs`.
   See the [service docs template](https://eida.github.io/doc/contributing/service-docs-template/).
2. Add the service to `services.yml` and open a pull request.

## Conventions

- A page's folder (`user/`, `operator/`, `developer/`) decides which tab it appears in. Tags are only `user`, `operator` and `developer`.
- Dependencies in `requirements.txt` are pinned on purpose. Do not loosen them.
 