#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place cli docs_src --exclude=__init__.py
black cli docs_src
isort cli docs_src
