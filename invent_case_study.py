import mysql.connector
from config import config

def get_sales_history():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "SELECT * FROM inventory_sales"
    cursor.execute(query)
    print("Sales History:")
    for line in cursor:
        print(line)
    cnx.close()

get_sales_history()

def add_new_sales(val):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "INSERT INTO inventory_sales VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,val)
    cnx.commit()
    cnx.close()
    print(cursor.rowcount, "record inserted.")

new_val=(3,2,'2021-12-23',5,34)
add_new_sales(new_val)

def delete_sales(val):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "DELETE FROM inventory_sales WHERE ProductId= %s and StoreId = %s"
    cursor.execute(query,val)
    cnx.commit()
    cnx.close()
    print(cursor.rowcount, "record deleted.")

delete_val=(3,2)
delete_sales(delete_val)

def update_sales_hist():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query ="UPDATE inventory_sales SET Stock=20 WHERE ProductId=1 and StoreId=2;"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    print(cursor.rowcount, "record updated.")


update_sales_hist()

def get_profit():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "SELECT products.ProductName, sum((products.SalesPrice-products.Cost)*inventory_sales.SalesQuantity) from products inner join inventory_sales ON products.id = inventory_sales.ProductId GROUP BY products.ProductName;"
    cursor.execute(query)
    print("Here are the profits for all of the stores:")
    for line in cursor:
        print(line)
    cnx.close()


get_profit()

def get_best_seller_product():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "SELECT ProductName,SalesQuantity FROM products INNER JOIN inventory_sales ON products.Id=inventory_sales.ProductId ORDER BY SalesQuantity DESC LIMIT 1"
    cursor.execute(query)
    print("Here is the best seller product and its sales quantity:")
    for line in cursor:
        print(line)
    cnx.close()

get_best_seller_product()






