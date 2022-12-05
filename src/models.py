import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name= Column(String(80), nullable=False)
    telephone= Column(Integer)
    email= Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)

class Favorito(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,ForeignKey('user.id'))
    id_planets= Column(Integer,ForeignKey('planets.id'))
    id_characters=Column(Integer,ForeignKey('characters.id'))
    
   # person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name= Column(String(80), nullable=False)
    population= Column(Integer)
    climate= Column(String(80), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name= Column(String(80), nullable=False)
    gender= Column(String(80), nullable=False)
    birth_years= Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
