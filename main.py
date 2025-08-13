import notion_helpers
import csv_helpers
from config import ONBOARDING_TASKS


onboardees = csv_helpers.get_onboardees_from_csv("to_be_onboarded.csv", "onboarded.csv")
for onboardee in onboardees:
    print(f'Creating onboarding page for {onboardee["onboardee_id"]} ({onboardee["onboardee_name"]}) with role {onboardee["role"]}')
    onboardee_id = notion_helpers.create_onboarding_page(onboardee)
    for task in ONBOARDING_TASKS[onboardee["role"]]:
        notion_helpers.create_task(task, onboardee_id)


print("Done✅")