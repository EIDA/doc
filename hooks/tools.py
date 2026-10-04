"""Point fetched tool pages back to their own repository.

For pages under docs/tools/<name>/ listed in tools.yml, the edit button opens
the file in the tool's repository and a source line is added at the end.
"""

from pathlib import Path

import yaml

_tools = {}


def on_config(config):
    tools_file = Path(config.config_file_path).parent / "tools.yml"
    if tools_file.exists():
        for tool in yaml.safe_load(tools_file.read_text())["tools"]:
            if "repo" in tool:
                _tools[tool["name"]] = tool
    return config


def _tool_for(page):
    parts = page.file.src_uri.split("/")
    if len(parts) > 2 and parts[0] == "tools" and parts[1] in _tools:
        return _tools[parts[1]], "/".join(parts[2:])
    return None, None


def on_page_markdown(markdown, page, config, files):
    tool, rel = _tool_for(page)
    if not tool:
        return markdown
    repo, ref, path = tool["repo"], tool["ref"], tool["path"]
    page.edit_url = f"https://github.com/{repo}/edit/{ref}/{path}/{rel}"
    source = f"https://github.com/{repo}/blob/{ref}/{path}/{rel}"
    return markdown + f"\n\n---\n\nSource: [{repo} ({ref})]({source})\n"
