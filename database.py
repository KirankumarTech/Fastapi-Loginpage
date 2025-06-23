from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:kiran@localhost/Kiran',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()