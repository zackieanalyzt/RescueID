from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    thai_id = Column(String)
    emergency_contact = Column(String)

class HealthRecord(Base):
    __tablename__ = 'health_records'
    record_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    medical_history = Column(String)
    allergies = Column(String)
