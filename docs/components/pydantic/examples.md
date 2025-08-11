# Examples — Runnable snippets

This file contains small, copy-paste examples you can run in a venv.

Example: echo agent (`examples/run_example.py`)

```
# run_example.py
from pydantic import BaseModel

class Task(BaseModel):
    query: str

class Result(BaseModel):
    answer: str

def run_agent(task: Task) -> Result:
    return Result(answer=f"Echo: {task.query}")

if __name__ == '__main__':
    t = Task(query='hello world')
    r = run_agent(t)
    print(r.json())
```

Create an `examples/` folder under the components path or repo root for these scripts.
