from datetime import datetime

import sqlalchemy.exc
from fastapi import HTTPException, status

from task_model import session, TaskModel
from task_model import TaskJson, TaskTitle, TaskContent


def list_all_tasks_impl():
    return session.query(TaskModel).all()


def get_task_by_id_impl(task_id: int):
    task = session.query(TaskModel).get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return task


def create_task_impl(task_json: TaskJson):
    task = TaskModel(
        title=task_json.title,
        content=task_json.content
    )
    try:
        session.add(task)
        session.commit()
    except sqlalchemy.exc.IntegrityError as ex:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(ex))


def change_title_by_id_impl(task_id: int, task_title: TaskTitle):
    task: TaskModel = get_task_by_id_impl(task_id=task_id)
    task.title = task_title.title
    session.commit()


def change_content_by_id_impl(task_id: int, task_content: TaskContent):
    task: TaskModel = get_task_by_id_impl(task_id=task_id)
    task.content = task_content.content
    session.commit()


def done_task_by_id_impl(task_id):
    task: TaskModel = get_task_by_id_impl(task_id=task_id)
    task.done = True
    task.done_at = datetime.now()
    session.commit()


def delete_task_by_id_impl(task_id):
    task: TaskModel = get_task_by_id_impl(task_id=task_id)
    session.delete(task)
    session.commit()
