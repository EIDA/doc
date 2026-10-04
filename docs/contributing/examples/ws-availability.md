# Example: ws-availability

[ws-availability](../../tools/ws-availability/index.md) follows this template.
Its `README.md` and `BETA.md` were split into pages without rewriting the text.

`docs/.nav.yml`:

```yaml
title: ws-availability
nav:
  - index.md
  - install.md
  - usage.md
  - configuration.md
  - troubleshooting.md
  - development.md
```

Where each README section went:

| README section | Page | Tags |
|---|---|---|
| Intro, References | [index.md](../../tools/ws-availability/index.md) | data-user, node-operator |
| Deployment, Upgrading from v1.0.x, First-time database setup, `BETA.md` | [install.md](../../tools/ws-availability/install.md) | node-operator |
| Endpoints, What runs daily | [usage.md](../../tools/ws-availability/usage.md) | data-user, node-operator |
| Configuration, Tuning | [configuration.md](../../tools/ws-availability/configuration.md) | node-operator |
| Troubleshooting | [troubleshooting.md](../../tools/ws-availability/troubleshooting.md) | node-operator |
| Development | [development.md](../../tools/ws-availability/development.md) | developer |
