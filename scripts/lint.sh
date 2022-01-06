#!/usr/bin/env bash

set -e
set -x

#mypy asyncer
flake8 cli docs_src
black cli docs_src --check
#isort asyncer tests docs_src scripts --check-only
