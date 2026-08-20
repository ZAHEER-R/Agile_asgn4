from DigitalWallet import DigitalWallet

def run_tests():
    print("--- RUNNING DIGITAL WALLET QA TESTS ---")
    w1 = DigitalWallet("W1", "1234", initial_balance=1000.0, daily_limit=500.0)
    w2 = DigitalWallet("W2", "5678", initial_balance=500.0)

    # 1. Normal Transaction
    res, msg = w1.withdraw(100, "1234")
    print(f"[Test 1 Normal] Success: {res} | Output: {msg}")

    # 2. Insufficient Balance
    res, msg = w1.withdraw(2000, "1234")
    print(f"[Test 2 Insufficient Balance] Success: {res} | Output: {msg}")

    # 3. Daily Limit
    res, msg = w1.withdraw(450, "1234") # total 550 > 500 limit
    print(f"[Test 3 Daily Limit] Success: {res} | Output: {msg}")

    # 4. Multiple Failed PINs
    w1.verify_pin("0000")
    w1.verify_pin("0000")
    res, msg = w1.verify_pin("0000")
    print(f"[Test 4 Failed PINs] Lock Triggered: {w1.is_locked} | Output: {msg}")

    # 5. Suspicious Transaction (Large Amount)
    w3 = DigitalWallet("W3", "1234", initial_balance=50000.0, daily_limit=100000.0)
    res, msg = w3.withdraw(15000, "1234")
    print(f"[Test 5 Suspicious Tx] Success: {res} | Output: {msg}")

    # 6. Negative Amount
    res, msg = w3.deposit(-50)
    print(f"[Test 6 Negative Amount] Success: {res} | Output: {msg}")

if __name__ == "__main__":
    run_tests()
