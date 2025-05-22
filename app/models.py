from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando a base do banco de dados
Base = declarative_base()

# Definindo o modelo da tabela "users"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# Criando a conexão com o banco (SQLite por enquanto)
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criando a sessão do banco
SessionLocal = sessionmaker(bind=engine)

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)