valid_user_payload = {
   "username": "anna92",
    "password": "test"
}

invalid_user_payload = {
    "password": "test1"

}


invalid_user_payload1 = {
    "username": "anna64",
    "password": "test1"

}

valid_task_payload = {
   "title": "task5",
    "description": "test task",
    "completed": True
}

changed_status_valid_task_payload = {
   "title": "task5",
    "description": "test task",
    "completed": False
}

invalid_task_payload = {
    "description": "test task",
    "completed": False

}


valid_update_task_payload = {
   "title": "task2",
    "description": "change ID",
    "completed": True
}

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}


