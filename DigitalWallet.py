import datetime

class DigitalWallet:
    def __init__(self, account_id, pin, initial_balance=0.0, daily_limit=5000.0):
        self.account_id = account_id
        self.__pin = pin
        self.balance = initial_balance
        self.daily_limit = daily_limit
        self.daily_spent = 0.0
        self.transactions = []
        self.failed_pin_attempts = 0
        self.is_locked = False

    def verify_pin(self, pin):
        if self.is_locked:
            return False, "Account locked due to multiple failed PIN attempts."
        if pin == self.__pin:
            self.failed_pin_attempts = 0
            return True, "PIN verified."
        else:
            self.failed_pin_attempts += 1
            if self.failed_pin_attempts >= 3:
                self.is_locked = True
                return False, "FLAG: Account locked - Multiple failed PIN attempts."
            return False, f"Incorrect PIN. Attempt {self.failed_pin_attempts}/3."

    def _check_fraud_velocity(self):
        now = datetime.datetime.now()
        ten_mins_ago = now - datetime.timedelta(minutes=10)
        recent_txs = [t for t in self.transactions if t['timestamp'] > ten_mins_ago]
        return len(recent_txs) >= 5

    def deposit(self, amount):
        if amount <= 0:
            return False, "Invalid deposit amount."
        self.balance += amount
        tx = {"type": "Deposit", "amount": amount, "timestamp": datetime.datetime.now()}
        self.transactions.append(tx)
        return True, f"Deposited ${amount}. New Balance: ${self.balance}"

    def withdraw(self, amount, pin):
        is_valid, msg = self.verify_pin(pin)
        if not is_valid:
            return False, msg
        if amount <= 0:
            return False, "Invalid withdrawal amount."
        if amount > self.balance:
            return False, "Insufficient balance."
        if self.daily_spent + amount > self.daily_limit:
            return False, "Daily transaction limit exceeded."

        flags = []
        if self._check_fraud_velocity():
            flags.append("More than 5 transactions in 10 minutes")
        if amount > 10000:
            flags.append("Large transaction")
        if amount % 1000 != 0 and amount > 3000:
            flags.append("Unusual transaction amount")

        self.balance -= amount
        self.daily_spent += amount
        tx = {"type": "Withdrawal", "amount": amount, "timestamp": datetime.datetime.now()}
        self.transactions.append(tx)

        status = f"Withdrew ${amount}. Balance: ${self.balance}"
        if flags:
            status += f" | FLAG SUSPICIOUS: {', '.join(flags)}"
        return True, status

    def transfer(self, target_wallet, amount, pin):
        is_valid, msg = self.verify_pin(pin)
        if not is_valid:
            return False, msg
        if amount <= 0:
            return False, "Invalid transfer amount."
        if amount > self.balance:
            return False, "Insufficient balance."
        if self.daily_spent + amount > self.daily_limit:
            return False, "Daily limit exceeded."

        self.balance -= amount
        self.daily_spent += amount
        target_wallet.balance += amount

        now = datetime.datetime.now()
        self.transactions.append({"type": f"Transfer to {target_wallet.account_id}", "amount": amount, "timestamp": now})
        target_wallet.transactions.append({"type": f"Transfer from {self.account_id}", "amount": amount, "timestamp": now})
        return True, f"Transferred ${amount} to {target_wallet.account_id}."

if __name__ == "__main__":
    wallet = DigitalWallet("ACC1001", pin="1234", initial_balance=2000.0, daily_limit=3000.0)
    print(wallet.deposit(500))
    print(wallet.withdraw(200, "1234"))
