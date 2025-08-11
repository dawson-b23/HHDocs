# Troubleshooting

Common issues and steps to resolve them.

## No response / 404
- Verify network (H&H Secure or Quality) or wired connection.
- Restart services: `python start_services.py`.
- Check Docker container health: `docker ps`, `docker logs <container>`.

## Slow responses
- Monitor GPU/CPU (`btop`).
- Restart model host (Ollama) and Streamlit app.

## Supabase connection issues
- Verify service keys and test queries in Supabase dashboard.

## Agent routing problems
- Confirm prefixes (e.g., `press20_data`) are used correctly.

<!-- New supporting page created by assistant -->