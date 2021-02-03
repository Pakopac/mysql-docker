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
metadata.create_all(engine)
print("Column:", payments.c.keys())

statement = select([payments.c.amount]).where(payments.c.paymentDate > datetime.datetime(2005, 6, 1))
result = connection.execute(statement).fetchall()
print('### All payments with date > 01 June 2005')
print(result)

print('- - - Connection Close - - -')
connection.close()