from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()

class Solution(Base):
  __tablename__ = 'solutions'
  id = Column(Integer, primary_key=True)
  n = Column(Integer)
  solution = Column(ARRAY(Integer))

  def __repr__(self):
    return "<Solution(n={}, label='{}')>".format(self.n, self.label)