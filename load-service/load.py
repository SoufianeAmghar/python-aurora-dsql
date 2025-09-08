import time
from connection import get_connection

def run_query_load_test():
    conn = get_connection()
    
    print("Connected to the database.")
    cur = conn.cursor()
    
    start = time.perf_counter()

    # test query
    cur.execute("SELECT count(*) FROM information_schema.tables;")
    result = cur.fetchone()
    
    end = time.perf_counter()
    elapsed = end - start

    print(f"Query result: {result[0]}, elapsed time: {elapsed:.4f} seconds")
    cur.close()
    conn.close()

if __name__ == "__main__":
    run_query_load_test()
