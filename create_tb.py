from db import engine, Base
from models import Movie, Rating

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")

