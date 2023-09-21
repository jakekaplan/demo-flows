from prefect import flow

@flow(log_prints=True)
def oom_flow():
    x = []
    while True:
        x.append("a" * 1000000)

if __name__ == '__main__':
    oom_flow()
