#!/bin/bash

set -e


cleanup() {
	pkill -f "uvicorn.*app.main:app" 2>/dev/null || true
}


cleanup
trap cleanup EXIT SIGINT SIGTERM

if [[ -z "${VIRTUAL_ENV}" ]]; then
	python -m venv .venv
	if [[ "$SHELL" == "/bin/bash" ]] || [[ "$SHELL" == "/bin/zsh" ]]; then
		source .venv/bin/activate
	else
		source .venv/bin/activate.fish
	fi
fi

pip install -r requirements.txt

pytest -v

uvicorn --port 8080 app.main:app &
sleep 3

curl -sf http://127.0.0.1:8080/health > /dev/null

curl -sf http://127.0.0.1:8080/octocat > /dev/null

