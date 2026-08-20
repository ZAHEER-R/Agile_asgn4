import pytest
import datetime
from DigitalWallet import DigitalWallet

def test_normal_transaction():
    wallet = DigitalWallet("ACC001", "1234", initial_balance=1000.0)
    bal = wallet.deposit(500.0, "1234")
    assert bal == 1500.0
    bal2 = wallet.withdraw(200.0, "1234")
    assert bal2 == 1300.0

def test_insufficient_balance():
    wallet = DigitalWallet("ACC002", "1234", initial_balance=100.0)
    with pytest.raises(ValueError, match="Insufficient balance."):
        wallet.withdraw(500.0, "1234")

def test_daily_limit():
    wallet = DigitalWallet("ACC003", "1234", initial_balance=10000.0, daily_limit=500.0)
    with pytest.raises(ValueError, match="Daily transaction limit exceeded."):
        wallet.withdraw(600.0, "1234")

def test_multiple_failed_pins():
    wallet = DigitalWallet("ACC004", "1234", initial_balance=1000.0)
    with pytest.raises(ValueError):
        wallet.deposit(100.0, "0000")
    with pytest.raises(ValueError):
        wallet.deposit(100.0, "1111")
    with pytest.raises(ValueError):
        wallet.deposit(100.0, "2222")
    assert "Multiple failed PIN attempts detected." in wallet.suspicious_flags

def test_suspicious_transaction():
    wallet = DigitalWallet("ACC005", "1234", initial_balance=50000.0)
    wallet.deposit(15000.0, "1234")  # Triggers large transaction rule
    assert any("Large transaction" in flag for flag in wallet.suspicious_flags)

def test_negative_amount():
    wallet = DigitalWallet("ACC006", "1234", initial_balance=1000.0)
    with pytest.raises(ValueError, match="Amount must be positive."):
        wallet.deposit(-50.0, "1234")

def test_duplicate_transaction_history():
    wallet = DigitalWallet("ACC007", "1234", initial_balance=1000.0)
    wallet.deposit(200.0, "1234")
    wallet.deposit(200.0, "1234")
    assert len(wallet.transaction_history) == 2
