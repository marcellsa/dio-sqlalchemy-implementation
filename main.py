from sqlalchemy import creat_engine, Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(9), nullable=False, unique=True)
    endereco = Column(String(100))

    contas = relationship(
        "Conta", back_populates="cliente"
    )

    def __repr__(self):
        return f"""
        <Cliente(id={self.id},
        nome={self.nome},
        cpf={self.cpf},
        endereco={self.endereco})
        >"""


class Conta(Base):
    __tablename__ = "contas"
    # atributos
    id = Column(Integer, primary_key=True)
    tipo = Column(String(10), nullable=False)
    agencia = Column(String(10), nullable=False)
    num = Column(String(10), nullable=False)
    saldo = Column(Float, default=0.0)
    id_cliente = Column(Integer, ForeignKey("clientes.id"))

    clientes = relationship(
        "Cliente", back_populates="contas"
    )

    def __repr__(self):
        return f"""
        <Conta(id={self.id},
                   tipo={self.tipo},
                   cliente_id={self.id_cliente},
                   saldo={self.saldo!r},
                   agencia={self.agencia!r},
                   num={self.num})
        >"""


# Configurando o banco de dados SQLite
engine = creat_engine('sqlite:///banco_de_dados.db')
Base.metadata.create_all(engine)


# Criando uma sessão de banco de dados
Session = sessionmaker(blind=engine)
session = Session()

# Criando algumas contas relacionadas aos cliente
cliente1 = Cliente(nome='João', cpf='111.111.111-11', endereco='R JB, 111')
cliente2 = Cliente(nome='Martim', cpf='222.222.222-22', endereco='R MB, 222')
cliente3 = Cliente(nome='Aurora', cpf='333.333.333-33', endereco='R AB, 333')
cliente4 = Cliente(nome='Violeta', cpf='444.444.444-44', endereco='R VB, 444')

# Adicionando os clientes à sessão e commitnado para persistir no BD
session.add_all([cliente1, cliente2, cliente3, cliente4])
session.commit()
