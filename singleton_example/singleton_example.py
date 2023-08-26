from employee_singleton.employee_singleton import singleton

@singleton
class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

    # Это создаст первый объект класса Employee
emp = Employee("Андрей", 2000)
emp.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)
