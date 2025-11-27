class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    @classmethod
    def salary(cls, hours, hourly_payment):
        salary = hours * hourly_payment

        return salary


emp_1 = EmployeeSalary.get_hours("Alexandr", None, 4, "mail@gmail.com")
print(emp_1.__dict__)
emp_1_salary = emp_1.salary(emp_1.hours, emp_1.hourly_payment)
print(f'Сотрудник {emp_1.name} отработал(а) {emp_1.hours} часа(ов), по ставке {emp_1.hourly_payment}. '
      f'Общая зарплата составила {emp_1_salary}')

emp_2 = EmployeeSalary.get_email("Marina", 40, 2, None)
print(emp_2.__dict__)
EmployeeSalary.set_hourly_payment(550)
emp_2_salary = emp_2.salary(emp_2.hours, emp_2.hourly_payment)
emp_2.salary(emp_2.hours, emp_2.hourly_payment)

print(f'Сотрудник {emp_2.name} отработал(а) {emp_2.hours} часа(ов), по ставке {emp_2.hourly_payment}. '
      f'Общая зарплата составила {emp_2_salary}')