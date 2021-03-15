options = {'M': 'Male', 'F': 'Female'}


class Employee:
    def __init__(self, name, surname, salary, gender, phone_number, join_date,
                 leave_date, trial):
        self.name = name
        self.surname = surname
        self.salary = salary
        self._gender = None
        self.gender = gender
        self.phone_number = phone_number
        self.email = name + '.' + surname + '@company.com'
        self.join_date = join_date
        self.leave_date = leave_date
        self.trial = trial

    def __repr__(self):
        return f"{self.name} {self.surname} "

    def __str__(self):
        return f"{self.name} {self.surname} - {self.salary} - {self.gender} - {self.phone_number} - {self.email} - {self.join_date} - {self.leave_date} - {self.trial}"

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in options:
            raise ValueError('gender must be M or F')

        self._gender = value

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __add__(self, other):
        if isinstance(other, int):
            return self.salary + other
        return self.salary + other.salary

    def __len__(self, other):
        return len(self.surname + other.surname)


emp_1 = Employee('Davit', 'Tovmasyan', 15000, 'M', '077123456', '22.02.2018', '~', 'Trial Passed')
emp_2 = Employee('Tovmas', 'Davtyan', 45000, 'M', '~', '11.01.2020', '25.07.2020', 'Trial Not Passed')
print(emp_1.__dict__)
print(emp_2.__dict__)
