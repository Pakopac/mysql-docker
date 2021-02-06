from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
import subprocess
import logging
import datetime

import conn

engine = conn.engine
connection = engine.connect()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = MetaData()

print('- - - MySQL Docker Container Python connection ok - - - \n')

print('- - - docker ps info - - -')
bashCommand = "docker ps"
output = subprocess.check_output(bashCommand, shell=True)
print(output)
print('\n')

print('- - - Tables into database - - -')
print(engine.table_names())

Payments = Table('payments', metadata,
    Column('customerNumber', Integer, primary_key=True, nullable=False),
    Column('checkNumber', String(50), primary_key=True, nullable=False),
    Column('paymentDate', Date, nullable=False),
    Column('amount', Float(10,2), nullable=False)
)

Offices = Table('offices', metadata,
    Column('officeCode', String(10), primary_key=True, nullable=False),
    Column('city', String(50), nullable=False),
    Column('phone', String(50), nullable=False),
    Column('addressLine1', String(50), nullable=False),
    Column('addressLine2', String(50), nullable=True),
    Column('state', String(50), nullable=True),
    Column('country', String(50), nullable=False),
    Column('postalCode', String(15), nullable=False),
    Column('territory', String(10), nullable=False),
)

Employees = Table('employees', metadata,
    Column('employeeNumber', Integer, primary_key=True, nullable=False),
    Column('lastName', String(50), nullable=False),
    Column('firstname', String(50), nullable=False),
    Column('extension', String(10), nullable=False),
    Column('email', String(100), nullable=False),
    Column('officeCode', String(10), nullable=False),
    Column('reportsTo', Integer, nullable=True),
    Column('jobTitle', String(50), nullable=False),
)

ProductLines = Table("productlines", metadata,
    Column("productLine", String(50), primary_key=True, nullable=False),
    Column("textDescription", String(4000), nullable=True),
    Column("htmlDescription", MEDIUMTEXT, nullable=True),
    Column("image", MEDIUMBLOB, nullable=True)
)


metadata.create_all(engine)

#print('- - - Selection of PAYMENTS Table - - -')
#print("Column:", payments.c.keys())

#statement = select([payments.c.amount]).where(payments.c.paymentDate > datetime.datetime(2005, 6, 1))
#statement = payments.sum([payments.c.amount])
#result = connection.execute(statement).fetchall()
print('\n')

def repr(table: Table):
    for element in table:
        for field in element:
            print(f'{field}', end=', ')
        print()
    print()

print('- - - 1. Bureaux triés par pays, états, villes - - -')
query1 = session.query(Offices).order_by(Offices.c.country, Offices.c.state, Offices.c.city)
repr(query1)
print('\n')

print("- - - 2. Nombre d'employé - - -")
query2 = session.query(Employees).count()
print(query2)
print('\n')

print('- - - 3. Total des payements - - -')
query3 = session.query(func.sum(Payments.c.amount)).first()[0]
print(query3)
print('\n')

print('- - - 4. Liste des voitures - - -')
query4 = session.query(ProductLines).filter(ProductLines.c.productLine.like("%{}%".format('Cars')))
repr(query4)
print('\n')

print('- - - 5. Total des paiements le 28 octobre 2004 - - -')
query5 = session.query(Payments.c.amount).filter(Payments.c.paymentDate == "2004-10-28")
repr(query5)
print('\n')

print('- - - 6. Paiements >= 100.000$ - - -')
query6 = session.query(Payments).filter(Payments.c.amount >= 100000)
repr(query6)
print('\n')

print('- - - 7. Produits de chaque gamme - - -')
# à faire
# query7 = 
#repr(query7)
#print('\n')

#print('### All payments with date > 01 June 2005')
#print(result)

print('- - - Connection Close - - -')
connection.close()