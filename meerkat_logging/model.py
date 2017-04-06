"""
Logging database model definition
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class Log(Base):
    __tablename__ = 'log'
    
    uuid = Column(String, primary_key=True)
    timestamp = Column(DateTime, index=True)
    type = Column(String, index=True)
    source = Column(String, index=True)
    source_type = Column(String, index=True)
    implementation = Column(String, index=True)
    event_data = Column(JSONB)

