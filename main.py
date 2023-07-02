from fastapi import FastAPI


app = FastAPI(
    title='Trading App'
)


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'Jonh'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
]


@app.get('/users/{user_id}')
def get_user(user_id):
    return user_id
