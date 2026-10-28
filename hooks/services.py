"""Point fetched service pages back to their own repository.

For pages under docs/services/<name>/ listed in services.yml, the edit button opens
the file in the service's repository and a source line is added at the end.
"""

from pathlib import Path

import yaml

_services = {}


def on_config(config):
    services_file = Path(config.config_file_path).parent / "services.yml"
    if services_file.exists():
        for service in yaml.safe_load(services_file.read_text())["services"]:
            if "repo" in service:
                _services[service["name"]] = service
    return config


def _service_for(page):
    parts = page.file.src_uri.split("/")
    if len(parts) > 2 and parts[0] == "services" and parts[1] in _services:
        return _services[parts[1]], "/".join(parts[2:])
    return None, None


def on_page_markdown(markdown, page, config, files):
    service, rel = _service_for(page)
    if not service:
        return markdown
    if rel.startswith("overview-"):
        rel = "index.md"  # per-tab copy of the Overview, see scripts/fetch_services.py
    repo, ref, path = service["repo"], service["ref"], service["path"]
    page.edit_url = f"https://github.com/{repo}/edit/{ref}/{path}/{rel}"
    source = f"https://github.com/{repo}/blob/{ref}/{path}/{rel}"
    return markdown + f"\n\n---\n\nSource: [{repo} ({ref})]({source})\n"
