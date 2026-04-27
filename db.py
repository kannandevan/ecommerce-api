import sqlite3
import uuid

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user'
        )
        """  
    )
    
    conn.commit()
    conn.close()
    
    
def create_user(username,password,role):
    try:
        with sqlite3.connect(DB_NAME, timeout=5) as conn:
            cursor = conn.cursor()
            user_id = str(uuid.uuid4())
            
            cursor.execute("""
                           INSERT INTO users (id,username,password,role)
                           VALUES(?,?,?,?)
                           """,(user_id,username,password,role))
            return({"user_id":user_id,"username":username,"role":role})
        
    except sqlite3.IntegrityError:
        return None

    except Exception as e:
        print("DB ERROR:", e)
        return None
    
    
def get_user_by_username(username):
    try:
        with sqlite3.connect(DB_NAME,timeout=5) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT * from users where username=?
                           """,(username,))
            row = cursor.fetchone()
            
            if not row:
                return None
            return {
                "id":row[0],
                "username":row[1],
                "password":row[2]
            }
            
    except sqlite3.IntegrityError:
        return None
    
    except Exception as e:
        print("DB ERROR:", e)
        return None