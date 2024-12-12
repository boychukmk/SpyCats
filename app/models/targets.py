from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Target(Base):
    __tablename__ = 'targets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String)
    complete = Column(Boolean, default=False)
    mission_id = Column(Integer, ForeignKey('missions.id'), nullable=False)

    mission = relationship('Mission', back_populates='targets')
