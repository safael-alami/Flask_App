from flask_mysqldb import MySQL

mysql = MySQL()

def create_tables(app):
    with app.app_context():
        cursor = mysql.connection.cursor()

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL
            );
        """)
        

        mysql.connection.commit()
        cursor.close()
