from itertools import count


class Counter(type):

    def __init__(cls, name, bases, dict):
        cls.counter = count(1)
        return type.__init__(cls, name, bases, dict)

    def __call__(cls, *args, **kwargs):
        cls.count = next(cls.counter)
        return type.__call__(cls, *args, **kwargs)


class MultiTriggeredMethod(type):
    counter = []
    counter
    def countMethod(fun):
        def wrapper(*args):
            if fun.__name__ in MultiTriggeredMethod.counter:
                MultiTriggeredMethod.counter.remove(fun.__name__)
                fun(args)
            else:
                MultiTriggeredMethod.counter.append(fun.__name__)

        return wrapper

    def __new__(cls, name, bases, dic):

        [dic.update(
            {k: MultiTriggeredMethod.countMethod(v)}) for k, v in dic.items() if not k.startswith("__") and callable(v)]
        return type.__new__(cls, name, bases, dic)


class Spell(type):
    workerAttr = {}
    def __init__(self, name, bases, dic):
        if name=="Worker":
            Spell.workerAttr = dic.copy()
        return type.__init__(self, name, bases, dic)

    def __call__(cls,*args,**kwargs):
        if cls.__name__=="Person":
            setattr(cls,'_Worker__pay_per_hour',8)
            [setattr(cls,k,v) for k,v in Spell.workerAttr.items() if not "init" in k]
            return type.__call__(cls, *args, **kwargs)
        return type.__call__(cls, *args, **kwargs)

    

class Person(metaclass=Spell):
    def __init__(self, n, s, b):
        self.__name = n
        self.__surname = s
        self.__birthday = b

    name = property(lambda self: self.__name, lambda self, v: setattr(self, "_Person__name", v))
    surname = property(lambda self: self.__surname, lambda self, v: setattr(self, "_Person__surname", v))
    birthday = property(lambda self: self.__birthday, lambda self, v: setattr(self, "_Person__birthday", v))

    def __repr__(self):
        return "I'm %s %s and I'm %s years old" % (self.name, self.surname, self.birthday)

class Student(Person):
    def __init__(self, *args, lect):
        super().__init__(*args)
        self._lecture = lect

    lecture = property(lambda self: self.__lecture, lambda self, v: setattr(self, "_Student__lecture", v))
    grade_average = property(lambda self: sum(self.lecture.values()) / len(self.lecture))

    def __repr__(self):
        return super().__repr__() + ". My grade average is: %s" % self.grade_average


class Worker(Person):
    def __init__(self, *args, pph=8):
        super().__init__(*args)
        self.__pay_per_hour = pph

    pph = property(lambda self: self.__pay_per_hour, lambda self, v: setattr(self, "_Worker__pay_per_hour", v))

    day_salary = property(lambda self: self.__pay_per_hour * 8, lambda self, v: setattr(self, "_Worker__pay_per_hour", v / 8))
    
    week_salary = property(lambda self: self.day_salary * 5,
                           lambda self, v: setattr(self, "_Worker__pay_per_hour", v / (5 * 8)))
    
    month_salary = property(lambda self: self.week_salary * 4,
                            lambda self, v: setattr(self, "_Worker__pay_per_hour", v / (5 * 8 * 4)))
    
    year_salary = property(lambda self: self.month_salary * 12,
                           lambda self, v: setattr(self, "_Worker__pay_per_hour", v / (5 * 8 * 4 * 12)))


class Wizard(Person):
    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return super().__repr__() + "Month salary %s" % self.month_salary

    age = property(lambda self: self.birthday)


ilaria = Student("ilaria", "Picci", "25", lect={"mate": 22, "fisica": 30, "chimica": 30})
simo = Person("Simone","Cerioli","26")
w = Worker("Simone","Cerioli","26")


simo.name="andrea"
print(simo)