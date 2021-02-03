from sqlalchemy import *
import subprocess
import logging
import datetime

import conn

engine = conn.engine
connection = engine.connect()

metadata = MetaData()

print('- - - MySQL Docker Container Python connection ok - - - \n')

print('- - - docker ps info - - -')
bashCommand = "docker ps"
output = subprocess.check_output(bashCommand, shell=True)
print(output)

print('- - - Tables into database - - -')
print(engine.table_names())

print('- - - Selection of PAYMENTS Table - - -')
payments = Table('payments', metadata,
    Column('customerNumber', Integer, primary_key=True, nullable=False),
    Column('checkNumber', String(50), primary_key=True, nullable=False),
    Column('paymentDate', Date, nullable=False),
    Column('amount', Float(10,2), nullable=False)
)

offices = Table('offices', metadata,
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

employees = Table('employees', metadata,
    Column('employeeNumber', Integer, primary_key=True, nullable=False),
    Column('lastName', String(50), nullable=False),
    Column('firstname', String(50), nullable=False),
    Column('extension', String(10), nullable=False),
    Column('email', String(100), nullable=False),
    Column('officeCode', String(10), nullable=False),
    Column('reportTo', Integer, nullable=True),
    Column('jobTitle', String(50), nullable=False),
)

metadata.create_all(engine)
print("Column:", payments.c.keys())

#statement = select([payments.c.amount]).where(payments.c.paymentDate > datetime.datetime(2005, 6, 1))
statement = payments.sum([payments.c.amount])
result = connection.execute(statement).fetchall()

print('### All payments with date > 01 June 2005')
print(result)

print('- - - Connection Close - - -')
connection.close()