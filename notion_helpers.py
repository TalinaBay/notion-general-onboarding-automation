from notion_client import Client
import os
from dotenv import load_dotenv
import json

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
onboarding_db = os.getenv("CURRENT_ONBOARDING_DB")
tasks_db = os.getenv("TASKS_DB")



def create_onboarding_page(onboardee_data):
    response = notion.pages.create(
        parent={"database_id": onboarding_db},
        properties={
            "Onboardee ID": {
                "title": [
                    {"text": {"content": onboardee_data["onboardee_id"]}}
                ]
            },
            "Onboardee Name": {
                "rich_text": [
                    {"text": {"content": onboardee_data["onboardee_name"]}}
                ]
            },
            "Role": {
                "rich_text": [
                    {"text": {"content": onboardee_data["role"]}}
                ]
            },
            "DOB": {
                "date": {
                    "start": onboardee_data["dob"]
                    }
            }
        }
    )
    page_id = response["id"]
    return page_id


def create_task(task_name, onboardee_page_id):
    notion.pages.create(
        parent={"database_id": tasks_db},
        properties={
            "Task": {
                "title": [
                    {"text": {"content": task_name}}
                ]
            },
            "Onboardee ID": {
                "relation": [{"id": onboardee_page_id}]
            }
        }
    )

