#!/usr/bin/bash
celery worker -A picha.celery -B -Q default -n default@%h -l info 2>/dev/null
