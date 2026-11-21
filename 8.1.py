# Лабораторная работа № 8. Вариант 8: «Банковские счета»
# Иерархия: базовый абстрактный класс Account и 3 наследника (Savings, Credit, Salary)
from abc import ABC, abstractmethod

class Account(ABC):
    """Абстрактный базовый класс банковского счёта."""
    def __init__(self, account_id: str, owner: str, balance: float) -> None:
        self.account_id: str = account_id
        self.owner: str = owner
        self.balance: float = balance

    @abstractmethod
    def account_type(self) -> str: pass

    @abstractmethod
    def calculate_month_end(self) -> float: pass

    def print_statement(self) -> None:
        """Полиморфный вывод выписки (принцип подстановки Лисков)."""
        final_bal: float = self.calculate_month_end()
        diff: float = final_bal - self.balance
        print(f"[{self.account_type()}] №{self.account_id} ({self.owner})")
        print(f"Баланс: {self.balance:.2f} руб. | Изменение: {diff:+.2f} руб. | Итого: {final_bal:.2f} руб.\n")

class Savings(Account):
    """Накопительный счёт: начисление процентов на остаток."""
    def __init__(self, account_id: str, owner: str, balance: float, rate: float = 0.08) -> None:
        super().__init__(account_id, owner, balance)
        self.rate: float = rate

    def account_type(self) -> str: return "Накопительный счёт"
    def calculate_month_end(self) -> float: return self.balance * (1 + self.rate / 12)

class Credit(Account):
    """Кредитный счёт: списание ежемесячного обслуживания."""
    def __init__(self, account_id: str, owner: str, balance: float, fee: float = 450.0) -> None:
        super().__init__(account_id, owner, balance)
        self.fee: float = fee

    def account_type(self) -> str: return "Кредитный счёт"
    def calculate_month_end(self) -> float: return self.balance - self.fee

class Salary(Account):
    """Зарплатный счёт: начисление фиксированного бонуса за активность."""
    def __init__(self, account_id: str, owner: str, balance: float, bonus: float = 500.0) -> None:
        super().__init__(account_id, owner, balance)
        self.bonus: float = bonus

    def account_type(self) -> str: return "Зарплатный счёт"
    def calculate_month_end(self) -> float: return self.balance + self.bonus

if __name__ == "__main__":
    accounts: list[Account] = [
        Savings("40817-01", "Иванов А.А.", 120000.0, 0.12),
        Credit("45502-02", "Петров В.С.", 50000.0, 450.0),
        Salary("40817-03", "Сидорова М.И.", 35000.0, 500.0),
    ]
    for acc in accounts:
        acc.print_statement()
