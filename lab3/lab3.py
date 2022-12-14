# Лабораторная работа 3

# 1. Черновую архитектуру проекта и **задачи** проекта — что будем обрабатывать и что хотим из этого всего получить
# 2. Отчитаться за блок документом с целью, задачами, архитектурой, функциональными требованиями, входными и выходными воздействиями
# 3. Продолжить изучение ООП в Питоне — взять свои коллекции из первых 2-х лаб. работ и переработать их в иерархию классов
# 4. Изучить и быть готовыми объяснить на примерах разницу между `__str__` и `__repr__` для пользовательского класса, можно прямо написать вывод иерархии классов через эти методы
# 5. Проработать имитацию функции `__call__`
# 
# 1. Архитектура приложения: MVC
#     Задачи проекта: На входе в веб интерфейсе будут: товар с товарной биржи, даты и показатели для анализа. Далее необходимые данные забираются из кэша/бд/апи, анализируются и на выход идет данные о торгах за день, объем торгов, среднее значение, максимум, минимум, изменение цены, стандартое отклонение и т.д. и т.п.</br>
#     project</br>
#     │   server.py</br>
#     │</br>
#     ├───controllers</br>
#     ├───models</br>
#     │       db.py</br>
#     └───views</br>
# 2. Цель: разработать прототип для магистерской работы, научиться собирать и анализировать данные.</br>
#     Задачи: найти и изучть апи для получения данных, разработать программу в виде веб-приложения.</br>
#     Функциональные требования: наличие интерфейса, возможность выбора товара, даты и анализируемых данных</br>
#     Входные воздействия: данные с интерфейса, исторические данные торгов</br>
#     Выходные воздействия: диаграммы, объем торгов, среднее значение, максимум, минимум, изменение цены, стандартое отклонение и т.д. и т.п.</br>
# 3. Иерархия классов для первых 2-х лаб</br>
#     databaseClass</br>
#     ├─── documentsDbs</br>
#     │       mongoClass</br>
#     ├─── SqlDbs</br>
#     │       mariaDbClass</br>
#     │       postgresqlClass</br>
#     │       sqliteClass</br>
#     └─── graphDbs</br>
# 4. `__str__` и `__repr__` определяют метод вывода информации об объекте. Repl выводит информацию "для разработчиков", которая может присваиваться через eval(), т.е. в формате объекта. А str выводит строковое читаемое значение

class testClass():

    def __repr__(self) -> str:
        return "__repl__"
    
    def __str__(self) -> str:
        return "__str__"

test = testClass()
print(test)

# 5.
class testClass2():

    def __call__(self):
        print("Имитация функции")

testClass2()()
