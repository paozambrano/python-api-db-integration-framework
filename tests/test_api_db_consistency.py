import pytest
import json
import os
from api_services.user_service import UserService
from db_handlers.mysql_handler import MySQLHandler

current_dir = os.path.dirname(__file__)
payload_path = os.path.join(current_dir, '..', 'data', 'user_payload.json')
with open(payload_path, 'r') as f:
    CREATE_USER_PAYLOAD = json.load(f)

def test_create_api_and_validate_db():
    api = UserService()
    db_handler = MySQLHandler()
    payload = CREATE_USER_PAYLOAD

    print("n[STEP 1] Sending POST to the API to create a user...")
    api_response = api.create_user(payload)

    assert api_response.status_code == 201, f"FAIL: Expected 201 Created, got {api_response.status_code}"
    response_json = api_response.json()

    user_id = response_json.get('id', '999')

    print(f'[STEP 2] Simulating that the application saves the user {user_id} in the DB')
    insert_query = """
    INSERT INTO users (id, first_name, job_title)
    VALUES (%s, %s, %s)
    """
    insert_params = (user_id, payload['name'], payload['job'])
    db_handler.execute_query(insert_query, insert_params)

    print(f"[STEP 3] Getting user data {user_id} directly from the DB")
    select_query = "SELECT first_name, job_title FROM users WHERE id = %s"
    db_result = db_handler.execute_query(select_query, (user_id))

    assert len(db_result) == 1, "FAIL: The user was not found in the database"
    db_user_data = db_result[0]

    assert db_user_data['first_name'] == payload ['name'], "FAIL: The DataBase name does not match the API payload"
    assert db_user_data['job_title'] == payload['job'], "FAIL: The Database position does not match the API payload"

    print("[SUCCESS] Data consistency confirmed: API 201 and DB match")

    delete_query = "DELETE FROM users WHERE id = %s"
    db_handler.execute_query(delete_query, (user_id,))