from models import User, Task
from models.db import session
from sqlalchemy import select, or_


# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#querying

# Query all of the users:
query = select(User).order_by(User.id)
# users = session.execute(query)
users = session.scalars(query)

# Output all of the users using regular Python:
print(query)  # prints the SQL
for user in users:
    print(user.username)

# Query all of the tasks:
query = select(Task).order_by(Task.id)
print(query)
# users = session.execute(query)
tasks = session.scalars(query)

# Print them:
for task in tasks:
    print(task.name, task.user.username)

# Query all of the tasks owned by Keith Taylor:
query = (
    select(Task)
    .join(User)
    .filter(User.username == "keith_taylor")
    .order_by(Task.id)
)
print(query)
tasks = session.scalars(query)

for task in tasks:
    print(task.name, task.user.username)

# Query all of the tasks owned by Keith Taylor or Misty Baker:
query = (
    select(Task)
    .join(User)
    .filter(
        or_(User.username == "keith_taylor",
            User.username == "misty_baker")
    )
    .order_by(Task.id)
)
print(query)
tasks = session.scalars(query)
for task in tasks:
    print(task.name, task.user.username)
