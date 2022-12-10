# post -> create
# get -> read
# put -> update
# delete -> delete

from fastapi import FastAPI
from task_model import \
    TaskJson, \
    TaskTitle, \
    TaskContent


from endpoint_impl import \
    list_all_tasks_impl, \
    get_task_by_id_impl, \
    create_task_impl, \
    change_title_by_id_impl, \
    change_content_by_id_impl, \
    done_task_by_id_impl, \
    delete_task_by_id_impl


app = FastAPI()


@app.post('/')
def create_task(task_json: TaskJson):
    return create_task_impl(task_json=task_json)


@app.get('/list')
def list_all_tasks():
    return list_all_tasks_impl()


@app.get('/{task_id}')
def get_task_by_id(task_id: int):
    return get_task_by_id_impl(task_id=task_id)


@app.put('/title/{task_id}')
def change_title_by_id(task_id: int, task_title: TaskTitle):
    return change_title_by_id_impl(task_id=task_id, task_title=task_title)


@app.put('/content/{task_id}')
def change_content_by_id(task_id: int, task_content: TaskContent):
    return change_content_by_id_impl(task_id=task_id, task_content=task_content)


@app.put('/done/{task_id}')
def done_task_by_id(task_id: int):
    return done_task_by_id_impl(task_id=task_id)


@app.delete('/delete/{task_id}')
def delete_task_by_id(task_id: int):
    return delete_task_by_id_impl(task_id=task_id)


def main():
    print('started!')


if __name__ == '__main__':
    main()
