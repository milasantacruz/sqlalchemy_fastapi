from sqlalchemy import Boolean, Integer, Column, ForeignKey, String, Table, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index = True)
    price = Column(Integer)
    is_offer = Column(Boolean)
    orders = relationship("Order", secondary="order_items", back_populates="items")


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index = True)
    phone = Column(String)
    orders = relationship("Order", back_populates="client")



class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="orders")
    items = relationship("Item", secondary="order_items", back_populates="orders")