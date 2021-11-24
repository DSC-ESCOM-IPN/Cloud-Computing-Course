from .utils.db import init_mysql_engine
from flask_restx import Namespace, Resource, fields

table_name = "profile"

try:
    engine = init_mysql_engine()
    connection = engine.connect()
except Exception as e:
    print(e)

api = Namespace('mysql_profile',
                description='profile related operations using MySQL')

profile = api.model('PROFILE', {
    "boleta":   fields.String(description='Person\'s boleta'),
    "LastName": fields.String(description='Person\'s last name'),
    "FirstName": fields.String(description='Person\'s first name'),
})


@api.route('/')
@api.response(404, 'profile not inserted')
@api.response(500, 'Server Error')
class Profiles(Resource):
    @api.doc('list_profiles')
    def get(self):
        rows = []
        data_rows = connection.execute("SELECT * FROM profile")
        for data_row in data_rows:
            rows.append({
                'boleta': data_row['boleta'],
                'LastName': data_row['LastName'],
                'FirstName': data_row['FirstName'],
            })
        return rows

    @api.doc('post_profiles')
    @api.expect(profile)
    def post(self):
        try:
            req = api.payload
            query = "INSERT INTO profile(boleta, LastName, FirstName) VALUES(%s, %s, %s)"
            data = (req["boleta"], req["LastName"], req["FirstName"])
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
            row = connection.execute(
                "SELECT * FROM profile WHERE boleta = '" + boleta + "'").fetchall()
            if row:
                return {
                    'boleta': row[0][0],
                    'LastName': row[0][1],
                    'FirstName': row[0][2],
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
            req = api.payload
            query = "UPDATE profile SET LastName = %s, FirstName = %s WHERE boleta = %s"
            data = (req["LastName"], req["FirstName"], boleta)
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
            query = "DELETE FROM profile WHERE boleta = '" + boleta + "'"
            connection.execute(query)
            return True

        except ValueError as ve:
            print('profile exception', ve)
            api.abort(404)
        except Exception as e:
            print('Server Error', e)
            api.abort(500)
