# Threat Model: LLM Risk Sandbox

This sandbox simulates what can go wrong when a large language model is given access to internal business documents without guardrails. It's not a real LLM, but it mimics behavior well enough to explore what breaks when access is poorly scoped.

## Modeled Risks

- Cross-role prompt leakage
- Overexposed internal documents
- Lack of prompt-response logging
- Absence of role-based filtering

## Security Assumptions

- Each user is assigned a role (engineering, HR, finance)
- Prompts may refer to departments outside that role
- There’s no natural language understanding—just simple string matching
- All documents live in one shared location (mocked JSON)

## Containment Measures

- Role-based access to documents
- Prompt filtering blocks cross-department references
- Logging of prompt and response pairs to a file
- Cloud storage is simulated but structurally accurate (single-source, untagged data)

## Limitations

- No authentication or identity validation
- No detection of indirect leakage (rephrased or obfuscated queries)
- No real LLM behavior—responses are fixed
- No encryption or document classification

## Purpose

The goal isn’t to simulate a working product, but to show how things fail by default—and what even minimal containment looks like. It’s a testbed for discussing security boundaries before plugging anything into an actual LLM.

