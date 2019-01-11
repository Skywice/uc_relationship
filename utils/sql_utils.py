import pandas as pd
from sqlalchemy import create_engine
import pymysql

from . import utils


sql_config = utils.get_sql_config()
engine = None


def get_engine():
    global engine
    if engine is None:
        engine = create_engine(
            'mysql+mysqldb://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
                sql_config['user'],
                sql_config['password'],
                sql_config['host'],
                sql_config['port'],
                sql_config['db']
            ),
            pool_size=20,
            max_overflow=20
        )
    return engine


def save(df, table_name, dtype=None, index=False, if_exists='append'):
    df.to_sql(
        table_name,
        con=get_engine(),
        if_exists=if_exists,
        index=index,
        chunksize=1000,
        dtype=dtype
    )


def get_column_struct(table_name):
    return select('desc {}'.format(table_name))


def execute(sql, params=None):
    print(sql)
    pd.io.sql.execute(sql, get_engine(), params)


def get_column_names(table_name):
    table_struct = get_column_struct(table_name)
    table_struct = table_struct[table_struct['Field'] != 'id']
    column_list = table_struct['Field'].values.tolist()
    return column_list


def replace_save(df, table_name):
    table_struct = get_column_struct(table_name)
    table_struct = table_struct[table_struct['Field'] != 'id']
    column_list = table_struct['Field'].values.tolist()
    type_list = table_struct['Type'].values.tolist()
    df = df[column_list]
    column_list = ['`'+column+'`' for column in column_list]
    content_len = len(type_list)
    df_content = df.values.tolist()
    for content in df_content:
        query_content = []
        for i in range(content_len):
            if 'int' in type_list[i]:
                query_content.append(int(content[i]))
            elif 'char' in type_list[i] or 'text' in type_list[i]:
                query_content.append('"' + str(content[i]) + '"')
            elif 'float' in type_list[i] or 'double' in type_list[i]:
                query_content.append(float(content[i]))
        try:
            db_query = 'replace into {}({}) values ({})'.format(
                table_name,
                str(','.join([str(i) for i in column_list])),
                str(','.join([str(i) for i in query_content])))
            execute(db_query)
        except ValueError as e:
            with open('./fail_query.sql', 'w+', encoding='utf-8') as input:
                input.write(db_query + '\n')


def select(sql, params=None):
    return pd.read_sql_query(sql, get_engine(), params=params)


def get_table_names(database_name):
    return select("select table_name from information_schema.tables where table_schema='{}' and table_type='base table'".format(database_name))


def if_table_exists(table_name):
    table_names = get_table_names('paper')['table_name'].values.tolist()
    if table_name in table_names:
        return True
    else:
        return False