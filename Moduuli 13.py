#Tehtävä 1

from flask import Flask, request

app = Flask(__name__)
@app.route("/alkuluku/<int:number>")

def toiminto(number):
    result = tester(number)
    response = {"Number": number, "isPrime": result}
    return response

def tester(number):
    prime = True
    while prime == True:
        for i in range(2, int(number)):
            if number % i == 0:
                prime = False
        else:
            break
    return prime

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)



#Tehtävä 2


from flask import Flask, request
import mysql.connector

app = Flask(__name__)
Connection = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'user1',
    password = '1234',
    autocommit = True
)


def GetAirportInfo(icao):
    Cursor = Connection.cursor()

    Cursor.execute(f"SELECT name, name FROM airport WHERE ident='{icao}'")
    airport = Cursor.fetchone()

    if airport:
        response = {"ICAO": icao, "Name": airport[0], "Municipality": airport[1]}
        return response


@app.route('/kenttä/<icao>')
def airport_info(icao):
    response = GetAirportInfo(icao)
    return response


if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.run(use_reloader=True, host='127.0.0.1', port=3000)