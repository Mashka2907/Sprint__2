class EmployeeSalary:
    hourly_payment = 400    # Почасовая оплата

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    """метод рассчитывает часы, исходя из количества выходных """
    @classmethod
    def get_hours(cls, name, rest_days, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    """метод генерирует email"""
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            cls.email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    """метод меняет значение переменной hourly_payment"""
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    """метод расчёта заработной платы"""
    def salary(self):
        return self.hours * self.hourly_payment


employee = EmployeeSalary.get_hours("Иван", 2)
employee = EmployeeSalary.get_email(employee.name, hours=employee.hours, rest_days=employee.rest_days)
print(f"Зарплата {employee.name}: {employee.salary()}")