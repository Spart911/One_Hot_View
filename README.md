# One_Hot_View
## Описание проекта
Этот проект создает и выводит DataFrame, содержащий столбцы "human" и "robot" на основе случайного перемешивания значений в исходном столбце "whoAmI", а далее приводит его к one hot виду.
## Как использовать
1. Убедитесь, что у вас установлен Python и библиотека pandas.
2. Откройте и запустите фаил main.py
## Особенности кода
- Создается DataFrame с именем "data", содержащим столбец "whoAmI" с перемешанными значениями "robot" и "human".
- Создаются два дополнительных столбца "human" и "robot", содержащие булевы значения в зависимости от того, является ли значение в столбце "whoAmI" соответствующим "human" или "robot".
- Исходный столбец "whoAmI" удаляется из DataFrame.
## Замечания
Данный код можно легко интегрировать в другие проекты, где необходимо создать DataFrame с определенными условиями.
## Автор
Столбовой Егор Васильевич
## Лицензия
Этот проект лицензирован согласно лицензии [MIT License].
