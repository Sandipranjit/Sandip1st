import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="machapuchre",
    autocommit=True,
    collation = "utf8mb4_general_ci"
)

def get_airport_coordinates(identity):

    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{identity}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if cursor.rowcount > 0:
        return result

Ident_1 = input("Enter the ICAO code of the first airport: ").upper()
Ident_2 = input("Enter the ICAO code of the second airport: ").upper()
coordinate_1 = get_airport_coordinates(Ident_1)
coordinate_2 = get_airport_coordinates(Ident_2)

distance = geodesic(coordinate_1, coordinate_2).kilometers
print(f"The distance between {Ident_1} and {Ident_2} is {distance:.2f} kilometers.")






