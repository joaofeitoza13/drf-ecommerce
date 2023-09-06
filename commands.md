# General commands for better development environment

## Some function

  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())

## settings.json adjustments to auto-format and auto-lint

  python -m pip install --upgrade pip

  python -m pip install -U flake8

  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length",
    "95"
  ],
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--max-line-length",
    "95"
  ],
