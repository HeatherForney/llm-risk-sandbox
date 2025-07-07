# LLM Risk Sandbox

This project simulates a common design flaw: giving a large language model (LLM) access to internal business documents without proper containment. It’s a controlled testbed to show how prompts can leak information across roles and how to stop it.

## Why This Exists

LLMs are being embedded into internal tools, often with too much visibility into sensitive data. This sandbox demonstrates basic defenses against that:

- Role-based document access
- Prompt filtering to block cross-role leakage
- Logging of all user interactions

It’s not a real LLM. It mimics LLM behavior to demonstrate access patterns and failures.

## How It Works

- Users (`alice`, `bob`, `charles`) each map to a department (engineering, hr, finance)
- Prompts are filtered for forbidden department references
- Responses are drawn from role-appropriate mock docs
- All interactions are logged with timestamps
- Docs are loaded from JSON to simulate cloud storage

## Running the App

From your terminal:

```bash
python app.py
