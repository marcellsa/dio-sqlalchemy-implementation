from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    telefone = Column(Integer(11))

    contas = relationship(
        "Conta", back_populates="cliente"
    )

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nome={self.nome!r}, cpf={self.cpf!r}, endereco={self.endereco!r}, telefone={self.telefone!r})"


class Conta(Base):
    __tablename__ = "conta"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(Float)
    agencia = Column(String)
    num = Column(Integer)

    clientes = relationship(
        "Cliente", back_populates="contas"
    )

    def __repr__(self):
        return f"Conta(id={self.id!r}, tipo={self.tipo!r}, cliente_id={self.cliente_id!r}, saldo={self.saldo!r}, agencia={self.agencia!r}, num={self.num!r})"
