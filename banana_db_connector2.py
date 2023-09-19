import psycopg2

def connect_to_db():
    try:
        # Set up the connection string
        cnx = psycopg2.connect(
            user="postgres",
            password="BananaApp1",
            host="banana-app-postgres-db.postgres.database.azure.com",
            port=5432,
            database="postgres"
        )

        # Create a new cursor
        cur = cnx.cursor()

        command = """
        CREATE TABLE donations (
            id SERIAL PRIMARY KEY,
            food_name VARCHAR(255),
            donor_id INTEGER,
            created_at TIMESTAMP(6) NOT NULL,
            updated_at TIMESTAMP(6) NOT NULL,
            category VARCHAR(255),
            total_amount VARCHAR(255),
            pickup_instructions VARCHAR(255),
            status VARCHAR(255)
        );
        """

        cur.execute(command)

        # Commit the transaction
        cnx.commit()

        print("Tables created successfully!")

        # Close the cursor and the connection
        cur.close()
        cnx.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    connect_to_db()
