import pymysql	
	
connection = pymysql.connect(host = "ego.kie.ue.poznan.pl", port = 8080, user="inz_opr", passwd="inz_opr", database="inzynieria_oprogramowania")
cursor = connection.cursor()

cursor.execute("select * from polaczenia;")
suma=0


for i in cursor:
	suma+=i[3]


if __name__ == "__main__":
    pass


print(suma)
