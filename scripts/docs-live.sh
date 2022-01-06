#!/usr/bin/env bash

set -e

mkdocs serve --config-file mkdocs.insiders.yml -a localhost:24687
