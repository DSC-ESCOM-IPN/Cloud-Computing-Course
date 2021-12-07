from .utils.db import getconn
from flask_restx import Namespace, Resource, fields

table_name = "profile"

api = Namespace('psql_profile',
                description='profile related operations using PostgreSQL')

profile = api.model('PSQL_PROFILE', {
    "boleta":   fields.String(description='Person\'s boleta'),
    "lastname": fields.String(description='Person\'s last name'),
    "firstname": fields.String(description='Person\'s first name'),
})


@api.route('/')
@api.response(404, 'profile not inserted')
@api.response(500, 'Server Error')
class Profiles(Resource):
    @api.doc('list_profiles')
    def get(self):
        connection = getconn()
        rows = []
        data_rows = connection.execute("SELECT * FROM profile")
        for data_row in data_rows:
            rows.append({
                'boleta': data_row['boleta'],
                'lastname': data_row['lastname'],
                'firstname': data_row['firstname'],
            })
        return rows

    @api.doc('post_profiles')
    @api.expect(profile)
    def post(self):
        try:
            connection = getconn()
            req = api.payload
            query = "INSERT INTO profile(boleta, lastname, firstname) VALUES(%s, %s, %s)"
            data = (req["boleta"], req["lastname"], req["firstname"])
            connection.execute(query, data)
            return True
        except ValueError as ve:
            print('profile exception', ve)
            api.abort(404)
        except Exception as e:
            print('Server Error', e)
            api.abort(500)


@api.route('/<boleta>')
@api.param('boleta', 'The profile identifier')
@api.response(404, 'profile not found')
@api.response(500, 'Server Error')
class profile(Resource):
    @api.doc('get_profile')
    def get(self, boleta):
        try:
            connection = getconn()
            row = connection.execute(
                "SELECT * FROM profile WHERE boleta = '" + boleta + "'").fetchall()
            if row:
                return {
                    'boleta': row[0][0],
                    'lastname': row[0][1],
                    'firstname': row[0][2],
                }
            raise ValueError('not rows returned')
        except ValueError as ve:
            print('profile exception', ve)
            api.abort(404)
        except Exception as e:
            print('Server Error', e)
            api.abort(500)

    @api.doc('put_profile')
    @api.expect(profile)
    def put(self, boleta):
        try:
            connection = getconn()
            req = api.payload
            query = "UPDATE profile SET lastname = %s, firstname = %s WHERE boleta = %s"
            data = (req["lastname"], req["firstname"], boleta)
            connection.execute(query, data)
            return True

        except ValueError as ve:
            print('profile exception', ve)
            api.abort(404)
        except Exception as e:
            print('Server Error', e)
            api.abort(500)

    @api.doc('delete_profile')
    def delete(self, boleta):
        try:
            connection = getconn()
            query = "DELETE FROM profile WHERE boleta = '" + boleta + "'"
            connection.execute(query)
            return True

        except ValueError as ve:
            print('profile exception', ve)
            api.abort(404)
        except Exception as e:
            print('Server Error', e)
            api.abort(500)
