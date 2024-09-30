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
def get_airport_by_code(codes):

    sql = f"SELECT name, type from airport WHERE iso_country = '{codes}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for results in result:
            print(results)

codes = input("Enter area code of the country: ")
get_airport_by_code(codes)