import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))

class planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    surface_water = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(String(250))


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(character)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')