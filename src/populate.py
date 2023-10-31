from models import User
from models import Task
from models.db import Base, engine, session
from faker import Faker
import random

fake = Faker()


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_user():
    profile = fake.simple_profile()
    tokens = profile['name'].split(' ')
    first_name = tokens.pop(0)
    last_name = ' '.join(tokens)
    username = '{0}_{1}'.format(
        first_name, last_name.replace(' ', '_')).lower()
    provider = profile['mail'].split('@')[1]
    email = '{0}@{1}'.format(username, provider)
    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email)
    return user


def create_fake_users(n=5):
    users = []
    for _ in range(n):
        user = create_user()
        users.append(user)
        session.add(user)
    session.commit()
    return users


def create_fake_tasks(users, n=25):
    for _ in range(n):
        user = random.choice(users)
        task = create_task(user)
        session.add(task)
    session.commit()


tasks = [
    ['Dishes', 'Do the dishes'],
    ['Sweep', 'Sweep the floor'],
    ['Mow', 'Mow the lawn'],
    ['Trash', 'Take out the trash'],
    ['Groceries', 'Buy groceries'],
    ['Exercise', 'Do some jumping jax'],
]


def create_task(user):
    dummy_task = random.choice(tasks)
    task = Task(
        name=dummy_task[0],
        description=dummy_task[1],
        done=False,
        user=user
    )
    return task


if __name__ == '__main__':

    # drop all tables:
    step = 1
    print('{0}. Dropping all tables...'.format(step))
    drop_tables()
    step += 1

    # create all tables:
    print('{0}. creating DB tables (if they don\'t already exist)...'.format(step))
    create_tables()
    step += 1

    # fake users:
    print('{0}. creating some fake users...'.format(step))
    users = create_fake_users(5)
    step += 1

    # fake tasks
    create_fake_tasks(users, n=25)
    print('{0}. creating some fake tasks...'.format(step))
