import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .model import Base, Solution

db_uri = os.environ['DB_URI']
db = create_engine(db_uri)
Base.metadata.create_all(db)

Session = sessionmaker(bind=db)

def storeSolutions(solutions, n):
  s = Session()
  for i in range(len(solutions)):
    solution = Solution(
      n = n,
      solution = solutions[i]
    )
    s.add(solution)
  s.commit()
  s.close()
  print('Done')