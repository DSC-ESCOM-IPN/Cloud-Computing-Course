from flask_restx import Api
from .SQL_endpoints import api as nsSQL
from .MySQL_endpoints import api as nsMySQL
from .PostgreSQL_endpoints import api as nsPosgre

api = Api(
    title='Cloud SQL API example',
    version='1.0',
    description='this is a simple API exapmle working with cloud SQL',
    prefix='/api'
)

api.add_namespace(nsMySQL, path='/mysql')
api.add_namespace(nsPosgre, path='/psql')
api.add_namespace(nsSQL, path='/sql')