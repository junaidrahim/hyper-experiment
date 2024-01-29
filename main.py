from tableauhyperapi import HyperProcess, Connection, Telemetry, CreateMode, Inserter

with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(hyper.endpoint, 'fivetran_platform_connector.hyper', CreateMode.NONE) as connection:
        my_data = connection.execute_list_query("""
            SELECT * FROM "Extract"."Extract"
        """)
        print(my_data)