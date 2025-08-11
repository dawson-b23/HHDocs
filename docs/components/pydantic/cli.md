# CLI — Running Examples

Concise
- Activate venv and run example scripts: `source .venv/bin/activate && python examples/run_example.py`

Comprehensive
- Use `argparse` or `click` for small CLIs

Example (argparse)
```
import argparse
from examples.example_agent import run_agent, Task

parser = argparse.ArgumentParser()
parser.add_argument("--query", required=True)
args = parser.parse_args()

task = Task(query=args.query)
result = run_agent(task)
print(result.json())
```

Packaging
- For reusable CLI, expose entry points in `setup.cfg` or `pyproject.toml`.
