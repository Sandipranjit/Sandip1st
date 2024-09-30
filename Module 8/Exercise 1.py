import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="machapuchre",
    autocommit=True,
    collation = "utf8mb4_general_ci"
)

def get_airport_by_ident(identity):

    sql = f"SELECT name, municipality FROM airport WHERE ident = '{identity}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if cursor.rowcount > 0:
        print(result)

identity = input("Enter a valid ICAO code of an airport: ").upper()
get_airport_by_ident(identity)


