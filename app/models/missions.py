from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class Mission(Base):
    __tablename__ = 'missions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cat_id = Column(Integer, ForeignKey('spy_cats.id', ondelete='SET NULL'), nullable=True)
    complete = Column(Boolean, default=False)

    cat = relationship('SpyCat', back_populates='missions')
    targets = relationship('Target', back_populates='mission', cascade="all, delete-orphan")
