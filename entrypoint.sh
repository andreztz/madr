#!/bin/bash

alembic upgrade head

uvicorn --host 0.0.0.0 --port 8000 madr.app:app
