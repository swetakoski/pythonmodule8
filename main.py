# import mysql.connector
# from geopy import distance
# connection = mysql.connector.connect(
#     host='2001:999:480:9874:af8f:6672:817f:b13e',
#     port=3306,
#     database='flight_game',
#     user='root',
#     password='Medowlarks04250.',
#     autocommit=True
#     )

#8.1
# my_db = connection.cursor()
# icao = input("Icao: ")
# sql= "SELECT name, municipality FROM airport WHERE ident = %s "
# icao =(icao, ) #tuple
# my_db.execute(sql, icao)
# result = my_db.fetchall()
# for r in result:
#     print(r)

#8.2
# my_db = connection.cursor()
# area_code = input("Area Code: ")
# sql = "SELECT type, count(*) FROM airport, country Where airport.iso_country = country.iso_country AND country.iso_country = %s group by airport.type"
# area_code = (area_code, )
# my_db.execute(sql, area_code)
# result = my_db.fetchall()
# for r in result:
#     print(r)

#8.3
# my_db = connection.cursor()
# icao1 = input("Icao 1: ")
# icao2 = input("Icao 2: ")
# sql = "SELECT latitude_deg, longitude_deg from airport WHERE ident = %s"
# icao1 = (icao1, )
# icao2 = (icao2, )
# my_db.execute(sql, icao1)
# icao1_coordinate = my_db.fetchall()
# my_db.execute(sql, icao2)
# icao2_coordinate = my_db.fetchall()
# print(icao2_coordinate, icao1_coordinate)
# print(f"The distance between these two airport is {distance.distance(icao1_coordinate, icao2_coordinate).km:.2f} km")
