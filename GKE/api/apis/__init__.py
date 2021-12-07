from flask_restx import Api
from .endpoints import api as nsPosgres

api = Api(
    title='Cloud SQL API example in GKE',
    version='1.0',
    description='this is a simple API exapmle working with cloud SQL and deployed in GKE',
    prefix='/api'
)

api.add_namespace(nsPosgres, path='/psql')