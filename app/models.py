from sqlalchemy import Column, Integer, String, Date
from db import Base, engine


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    company = Column(String())

    qliq_1_fact = Column(Integer)
    qliq_2_fact = Column(Integer)
    qoil_1_fact = Column(Integer)
    qoil_2_fact = Column(Integer)
    
    qliq_1_frcst = Column(Integer)
    qliq_2_frcst = Column(Integer)
    qoil_1_frcst = Column(Integer)
    qoil_2_frcst = Column(Integer)

    created_at = Column(Date)
    
    def __repr__(self):
        return f"Check for {self.company} at the date"

# direct call cleans table
if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)