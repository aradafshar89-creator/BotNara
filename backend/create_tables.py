from app.db.database import engine
from app.models.upload import Base
from app.models.sale import Sale

Base.metadata.create_all(bind=engine)

print("TABLES CREATED")
