import os
import pytds
import pg8000
import pymysql
import sqlalchemy
from google.cloud.sql.connector import connector


def init_mysql_engine() -> sqlalchemy.engine.Engine:
    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            os.environ["MYSQL_CONNECTION_NAME"],
            "pymysql",
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASS"],
            db=os.environ["MYSQL_DB"],
        )
        return conn

    engine = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return engine


def init_psql_engine() -> sqlalchemy.engine.Engine:
    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            os.environ["POSTGRES_CONNECTION_NAME"],
            "pg8000",
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASS"],
            db=os.environ["POSTGRES_DB"],
        )
        return conn

    engine = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    engine.dialect.description_encoding = None
    return engine


def init_sql_engine() -> sqlalchemy.engine.Engine:
    def getconn() -> pytds.Connection:
        conn = connector.connect(
            os.environ["SQLSERVER_CONNECTION_NAME"],
            "pytds",
            user=os.environ["SQLSERVER_USER"],
            password=os.environ["SQLSERVER_PASS"],
            db=os.environ["SQLSERVER_DB"],
        )
        return conn

    engine = sqlalchemy.create_engine(
        "mssql+pytds://localhost",
        creator=getconn,
    )
    engine.dialect.description_encoding = None
    return engine
