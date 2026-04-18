import pandas as pd

def migrate_cyber_incidents(conn):
    data = pd.read_csv('DATA/cyber_incidents.csv')
    data.to_sql('cyber_incidents', conn)


def get_all_cyber_incidents(conn):
    sql = 'SELECT * FROM cyber_incidents'
    return pd.read_sql_query(sql, conn)
