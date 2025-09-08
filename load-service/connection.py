import os
import psycopg2
import subprocess

def generate_auth_token(hostname, region):
    cmd = [
        "aws", "dsql", "generate-db-connect-admin-auth-token",
        "--hostname", hostname,
        "--region", region
    ]
    token = subprocess.check_output(cmd).decode().strip()
    return token

def get_connection():
    host = os.getenv("PGHOST")
    region = os.getenv("AWS_REGION", "us-west-3")
    user = os.getenv("PGUSER", "admin")
    db = os.getenv("PGDATABASE", "postgres")
    
    password = generate_auth_token(host, region)
    sslmode = "require"

    conn = psycopg2.connect(
        host=host,
        dbname=db,
        user=user,
        password=password,
        sslmode=sslmode
    )
    return conn
