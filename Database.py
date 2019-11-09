#!/usr/bin/env python3

import sqlalchemy as sq

class Equipment(Base):
    __tablename__ = 'equipment'

    name = Column(String, primary_key=True)
    count = Colum(Integer)

    def __repr__(self):
        return "Equipment: %s" %self.name

engine = create_engine('sqlite:///:memory:', echo=True)

def get_name():
    pass

def enter_equip(tag_name, ownership, description):
    pass
