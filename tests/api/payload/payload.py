valid_user_payload = {
   "username": "anna68",
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
   "title": "task3",
    "description": "test task",
    "completed": True
}

invalid_task_payload = {
    "description": "test task",
    "completed": False

}


valid_update_task_payload = {
   "title": "task1",
    "description": "change ID",
    "completed": True
}

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}


