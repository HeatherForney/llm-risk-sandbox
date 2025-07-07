import json
import datetime

# Simulated user database and role-based access control
USER_ROLES = {
    "alice": "engineering",
    "bob": "hr",
    "charles": "finance"
}

# Simulate cloud document fetch
def fetch_document(role):
    with open("data/mock_documents.json") as f:
        docs = json.load(f)
    return docs.get(role, "No document found.")

# Simple log function
def log_interaction(user, prompt, response):
    timestamp = datetime.datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "user": user,
        "prompt": prompt,
        "response": response
    }
    with open("logs/interactions.log", "a") as log_file:
        log_file.write(json.dumps(entry) + "\n")

# Simulated LLM response with naive filtering
def process_prompt(user, prompt):
    role = USER_ROLES.get(user)
    if role is None:
        return "Access denied: Unknown user."

    # Simple leakage check
    if any(other_role in prompt.lower() for other_role in USER_ROLES.values() if other_role != role):
        return "Access denied: Cross-role data access attempt blocked."

    doc = fetch_document(role)
    if doc == "No document found.":
        return "These documents may not exist or your role does not have permission to access them."
    response = f"[LLM] Based on {role} docs: {doc}"

    log_interaction(user, prompt, response)
    return response

# CLI runner
if __name__ == "__main__":
    print("Welcome to LLM Risk Sandbox")
    user = input("Enter your username: ").strip().lower()
    while True:
        prompt = input(f"{user}> ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        print(process_prompt(user, prompt))

