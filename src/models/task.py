from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .db import Base, engine
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    done = Column(Boolean, default=False)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    user = relationship("User")
