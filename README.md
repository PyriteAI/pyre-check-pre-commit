# Pyre pre-commit Hook

[pre-commit](https://pre-commit.com/) hook for [Pyre](https://pyre-check.org/).

## Prerequisites

`pyre-check-pre-commit` is a script hook, meaning that pre-commit does not create a virtual environment for it, nor does it install any dependencies on your behave. As such, you must have `pyre-check` installed.

## Usage

In your `.pre-commit-config.yaml`, add:

```yaml
repos:
  - repo: https://github.com/PyriteAI/pyre-check-pre-commit
    rev: 0.1.0
    hooks:
      - id: pyre-check
```

### Arguments

`pyre-check-pre-commit` supports the following arguments:

- `-d | --work-dir`: move to the given directory before executing pyre.

Any additional arguments will be passed to `pyre`.
