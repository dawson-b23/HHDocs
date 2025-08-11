#!/usr/bin/env bash
# Simple health-check script for local AI services
set -euo pipefail

echo "Checking Docker status..."
docker ps --format 'table {{.Names}}	{{.Status}}	{{.Ports}}'

check_url(){
  url=$1
  name=$2
  echo -n "Checking $name ($url)... "
  if curl -sSf --max-time 3 "$url" >/dev/null; then
    echo "OK"
  else
    echo "FAILED"
  fi
}

# Common endpoints (adjust if your setup maps ports differently)
check_url "http://localhost:5678" "n8n"
check_url "http://localhost:3000" "Open WebUI"
check_url "http://localhost:11434" "Ollama (may be internal)"
check_url "http://localhost:8000" "Docs (if served)"

echo "Done. Review failures above and inspect container logs with 'docker logs <name>'" 
