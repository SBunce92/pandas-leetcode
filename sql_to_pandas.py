import pandas as pd

def sql_to_dfs(sql_string):
    return [pd.DataFrame(
        columns = sql_string['headers'][k],
        data = sql_string['rows'][k])
    for k in sql_string['headers'].keys()
    ]
