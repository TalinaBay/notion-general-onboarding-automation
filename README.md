# Notion Onboarding Automation

A Python script that connects to your existing Notion workspace to automate onboarding for multiple role types (e.g. intern, freelance, minijob, part-time, full-time).

## Requirements

- Python **3.9+**
- A Notion account
- A Notion integration with the correct permissions
- API key from Notion

## What it does

- Reads a CSV list of onboardees with their roles
- Creates pages for each onboardee in your Notion **Onboarding** database
- Adds role-specific onboarding tasks linked to each onboardee in a separate **Tasks** database
- Moves onboarded people from `to_be_onboarded.csv` to `onboarded.csv`

## Notion Setup

1. **Create a Notion integration:**

   - Go to [Notion Integrations](https://www.notion.so/profile/integrations)
   - Create a new integration for your workspace
   - Enable read/write permissions
   - Copy the **Internal Integration Secret**

2. **Create Notion databases** with these property names:
   <img width="975" height="679" alt="Screenshot 2025-08-14 at 1 01 58 PM" src="https://github.com/user-attachments/assets/6d52f681-8732-4d28-8b03-b0e7eb0f66e0" />

⚠ **Property names must match exactly** as above, or the script will fail.

3. (Optional) Add a **Progress Bar** property to the `Current Onboarding` database using a **Rollup** of the task completion checkboxes.

4. **Get your database IDs:**
   - Share the databases publicly (or via integration)
   - From the shared URL, copy the 32-character alphanumeric ID between the workspace name and any query parameters (before any `?`)
     <img width="1502" height="128" alt="image" src="https://github.com/user-attachments/assets/4eeba417-7ee1-4137-8750-cb008aaf047b" />

## Getting Started

1. Clone the repository
2. Create a `.env` file with your Notion API token and the database IDs:

```
NOTION_TOKEN=your_secret_token
CURRENT_ONBOARDING_DB=your_current_onboarding_db_id
TASKS_DB=your_tasks_db_id
```

3. Put your onboardees in `data/to_be_onboarded.csv` with columns:

- `onboardee_id` (a unique onboardee ID)
- `onboardee_name` (their full name)
- `dob` (their date of birth)
- `role` (their employment role)  
  **Notes:**
- `dob` must be in `YYYY-MM-DD` format for Notion compatibility.

## Run the script

1. Create a Virtual Environment.
   **Notes:**
   This keeps your project’s Python packages separate.

```bash
python3 -m venv venv
```

2. Activate it.

```bash
source venv/bin/activate
```

3. Install Required Packages.

```bash
pip install notion-client python-dotenv
```

4. Run the script.

```bash
python3  main.py
```

## Project Structure

```
.
├── config.py                    # Config and onboarding tasks per role
├── csv_helpers.py               # CSV reading utilities
├── notion_helpers.py            # Notion API helper functions
├── data/                        # CSV data files
│   └── to_be_onboarded.csv
│   └── onboarded.csv
├── main.py                      # Main script
├── .env                         # Notion API tokens (not committed)
└── .gitignore
```
