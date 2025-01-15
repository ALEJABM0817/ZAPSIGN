import psycopg2
from psycopg2 import sql


DB_CONFIG = {
    'dbname': 'my_database',  
    'user': 'admin',          
    'password': 'admin',      
    'host': 'localhost',      
    'port': 5432             
}


def update_api_token(company_name, api_token):
    try:
        
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        
        update_query = sql.SQL("""
            UPDATE company
            SET api_token = %s
            WHERE name = %s;
        """)
       
        cursor.execute(update_query, (api_token, company_name))
        connection.commit()

       
        if cursor.rowcount > 0:
            print(f"API token actualizado correctamente para '{company_name}'.")
        else:
            print(f"No se encontró ninguna compañía con el nombre '{company_name}'.")

    except psycopg2.Error as e:
        print(f"Error al actualizar el API token: {e}")
    finally:
        
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
   
    company_name = "My Company"  
    api_token = "b8b79543-cd3e-4b44-922c-1e2ed094771d9c245189-252c-4ba0-b8dd-e0db4a61bd96" 
    
    update_api_token(company_name, api_token)
