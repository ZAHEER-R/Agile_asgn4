import datetime

class DigitalWallet:
    def __init__(self, account_id, pin, initial_balance=0.0, daily_limit=5000.0):
        self.account_id = account_id
        self.pin = pin
        self.balance = initial_balance
        self.daily_limit = daily_limit
        self.transaction_history = []
        self.failed_pin_attempts = 0
        self.suspicious_flags = []

    def verify_pin(self, entered_pin):
        if entered_pin != self.pin:
            self.failed_pin_attempts += 1
            if self.failed_pin_attempts >= 3:
                self.suspicious_flags.append("Multiple failed PIN attempts detected.")
            return False
        self.failed_pin_attempts = 0  # Reset counter on success
        return True

    def deposit(self, amount, pin):
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        self.balance += amount
        self._log_transaction("DEPOSIT", amount)
        self._check_fraud("DEPOSIT", amount)
        return self.balance

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        
        # Verify daily limit
        today = datetime.date.today()
        today_total = sum(
            t['amount'] for t in self.transaction_history 
            if t['type'] == 'WITHDRAWAL' and t['date'] == today
        )
        if today_total + amount > self.daily_limit:
            raise ValueError("Daily transaction limit exceeded.")

        self.balance -= amount
        self._log_transaction("WITHDRAWAL", amount)
        self._check_fraud("WITHDRAWAL", amount)
        return self.balance

    def transfer(self, target_wallet, amount, pin):
        if not self.verify_pin(pin):
            raise ValueError("Invalid PIN.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        target_wallet.balance += amount
        self._log_transaction("TRANSFER", amount)
        self._check_fraud("TRANSFER", amount)
        return self.balance

    def get_balance(self):
        return self.balance

    def _log_transaction(self, tx_type, amount):
        self.transaction_history.append({
            'type': tx_type,
            'amount': amount,
            'timestamp': datetime.datetime.now(),
            'date': datetime.date.today()
        })

    def _check_fraud(self, tx_type, amount):
        now = datetime.datetime.now()
        
        # Rule 1: More than 5 transactions in 10 minutes (600 seconds)
        recent_txns = [
            t for t in self.transaction_history 
            if (now - t['timestamp']).total_seconds() <= 600
        ]
        if len(recent_txns) > 5:
            self.suspicious_flags.append("High frequency: >5 transactions in 10 minutes.")

        # Rule 2: Large transaction check (> 10,000)
        if amount > 10000.0:
            self.suspicious_flags.append(f"Large transaction detected: {amount}")

        # Rule 3: Unusual amount relative to current balance
        if amount > self.balance * 0.9 and amount > 4000:
            self.suspicious_flags.append("Unusual transaction amount relative to balance.")
