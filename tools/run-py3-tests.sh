#!/usr/bin/env bash

testr init
testr run --concurrency=5 --parallel `cat py3-testlist`
