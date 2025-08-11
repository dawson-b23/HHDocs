# Agents — Examples

Concise
- Define agent behaviors as functions that accept Pydantic models and return models.

Example
```
from pydantic import BaseModel

class Task(BaseModel):
    query: str

class Result(BaseModel):
    answer: str

def run_agent(task: Task) -> Result:
    # call LLM here with task.query and return Result
    return Result(answer=f"Echo: {task.query}")
```

Comprehensive
- Implement retries and error handling around LLM calls
- Use background workers or asyncio for long-running agents
- Keep I/O (LLM calls) isolated for easier testing

Repo examples
- I will pull short snippets from `Work/` and `scripts/` to demonstrate agent implementations used in this repo.
