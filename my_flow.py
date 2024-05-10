from prefect import flow


@flow()
def hello_flow(
    user=None,
    debug=None,
    limit=None,
    ref_date=None,
    force_calc=None,
    dbt_commands = []
):
    print (f"{type(user)} and {user}")
    print (f"{type(debug)} and {debug}")
    print (f"{type(limit)} and {limit}")
    print (f"{type(ref_date)} and {ref_date}")
    print (f"{type(force_calc)} and {force_calc}")
    print (f"{type(dbt_commands)} and {dbt_commands}")

    print("Hello, Prefect!")

if __name__ == "__main__":
    hello_flow(user="user", debug="debug", limit=12345, ref_date="12345", force_calc="\"12345\"", dbt_commands=["dbt deps", "dbt run --profile-dir ."])