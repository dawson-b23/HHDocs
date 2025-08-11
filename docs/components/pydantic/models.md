# Models — Pydantic Patterns

Concise
- Use Pydantic `BaseModel` to define structured inputs and outputs for prompts.

Example
```
from pydantic import BaseModel

class DefectReport(BaseModel):
    id: int
    description: str
    severity: int
```

Comprehensive
- Use validators for normalization and custom parsing
- Use `Field(..., description="...")` to annotate fields which can be used in prompts
- Consider `Annotated` and constrained types for stricter schemas

Pattern: Prompt → Parse
- Build a prompt template that requests a JSON blob matching your model
- Use Pydantic to parse the LLM output and validate types

Troubleshooting
- If parsing fails, add more explicit instructions and examples in the prompt, or use `pydantic.parse_obj_as` for flexible parsing.
