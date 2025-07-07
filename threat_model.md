# LLM Risk Sandbox

This is a small simulation of what can go wrong when a large language model is given access to internal business documents without proper constraints. It’s not a real LLM—it mimics the flow of data and response behavior to demonstrate how leakage happens and how to block it.

## Why This Exists

LLMs are increasingly being embedded into internal tools, sometimes with direct access to sensitive company data. That’s a problem.

This app shows what happens when:
- The LLM has access to docs across departments (engineering, HR, finance)
- A user tries to ask questions outside their role
- No logging or filtering is in place

The goal isn’t to stop people from using LLMs—it’s to show how to wrap them in guardrails before letting them touch real data.

## How It Works

- Each user is hardcoded to a department (`alice`, `bob`, `charles`)
- Prompts are checked for role violations
- Only department-specific documents are available
- All interactions are logged
- Documents are stored in a local JSON file to simulate cloud storage

## What It’s Simulating

- LLMs hooked up to internal cloud buckets (e.g., S3, GCS)
- Prompt leakage and role overreach
- Logging and traceability requirements
- What a minimal containment layer might look like

## Running the App

Run from the project root:

```bash
python app.py
