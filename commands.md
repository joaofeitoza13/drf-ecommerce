# General commands for better development environment

## Some function

  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())

## Some commands

  Describes some useful and most used commands

### Tests

  pytest -k "function_name"  |-> runs tests only for the passed function
  pytest -X                  |-> runs the tests and stops at the first fail
  pytest --cov               |-> runs the tests and shows it's coverage

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

## errors, bugs and it's references

  obs: errors are defined in the description of the link.

  [Ignore specific flake8 rule in entire files](https://stackoverflow.com/questions/48153886/flake8-ignore-specific-warning-for-entire-file "Repeating the same warning/error ignore command")

  [Apps aren't loaded yet](https://stackoverflow.com/questions/34114427/django-upgrading-to-1-9-error-appregistrynotready-apps-arent-loaded-yet  "ERROR - django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet")

  [define DJANGO_SETTINGS_MODULE](https://stackoverflow.com/questions/62094296/django-settings-module-or-call-settings-configure-before-accessing-settings "ERROR - django.core.exceptions.ImproperlyConfigured: You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings")

  [Configure Make for Windows](https://www.technewstoday.com/install-and-use-make-in-windows/)

  [Passing args to Makefile custom commands](https://stackoverflow.com/questions/2826029/passing-additional-variables-from-command-line-to-make)

  [Especify which context coverage is using](https://coverage.readthedocs.io/en/7.3.1/source.html)

  [Missing separatos in Makefile custom commands](https://stackoverflow.com/questions/70146594/makefile6-missing-separator-stop-error)

  [drf_spectacular generates .yml or .yaml](https://stackoverflow.com/questions/22268952/what-is-the-difference-between-yaml-and-yml-extension)

  [Configurations for .editorconfig](https://editorconfig.org/#file-format-details)

  [Configure black, isort and pre-commit](http://www.sefidian.com/2021/08/03/how-to-use-black-flake8-and-isort-to-format-python-codes/)

  [Setup SSH on Windows Powershell](https://evidencen.com/how-to-setup-ssh-on-windows-powershell-for-github/)

  [Omit folders or files from coverage](https://pytest-cov.readthedocs.io/en/latest/config.html?highlight=exclude)
