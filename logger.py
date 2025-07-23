from datetime import datetime

LOG_FILE = "transactions.log"

def log_transaction(entry):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {entry}\n")
