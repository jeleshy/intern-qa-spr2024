#### Тест-кейсы для блока со счетчиками
***Разметка: номер - тест-кейс, буллет-поинт - шаг, после | - что нужно проверить по каждому шагу***

1. Соответствие эко-счетчиков макету.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь не авторизован;
- Проверить соответствие счетчика с СО2 макету | Счетчик соответствует макету.
- Проверить соответствие счетчика с водой макету | Счетчик соответствует макету.
- Проверить соответствие с электричеством макету | Счетчик соответствует макету.
***Ожидаемый результат:** все счётчики соответствуют макетам.

2. Проверить тексты и единицы измерения в счетчиках по умолчанию. 
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь не авторизован;
- Проверить тексты и единицы счетчика с СО2 | единицы измерения: кг CO₂, текст: не попало в атмосферу.
- Проверить тексты и единицы счетчика с водой | единицы измерения: л воды, текст: было сохранено.
- Проверить тексты и единицы с электричеством | единицы измерения: кВт⋅ч энергии, текст: было сэкономлено.
***Ожидаемый результат:** текст и единицы измерения в счётчиках выставлены по умолчанию.

3. Просмотр блока **"Ваш экологический вклад"** незарегистрированным пользователем.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь не авторизован;
- Перейти к блоку **"Ваш экологический вклад"** | В блоке “Экологический вклад” 6 карточек эко-вклада в соответствии с макетом. 
- Проверить кнопку авторизации | Слева есть кликабельная кнопка "Авторизоваться".
- Проверить аватар пользователя | Картинки профиля пользователя нет, вместо нее - серый кружок. 
- Проверить эко-счетчики | Все счетчики равны 0, а тексты на карточках-счетчиках визуально серые. 
***Ожидаемый результат:** есть кнопка авторизации, не отображается картинка профиля, счётчики обнулены.

4. Просмотр блока **"Ваш экологический вклад"** авторизованным пользователем и проверка соответствия значений счетчиков цифровым.
- Предусловие: открыть страницу [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пройти авторизацию и переоткрыть страницу | В хедере есть информация о пользователе;
- Перейти к блоку **"Ваш экологический вклад"** | В блоке “Экологический вклад” 6 карточек эко-вклада в соответствии с макетом. 
- Проверить кнопку авторизации | Кнопка "Авторизоваться" отсуствует.
- Проверить аватар пользователя | Картинка в карточке “Эковклад” соответствует фото профиля пользователя.
- Проверить эко-счетчики | Данные по пользователю в счетчиках соответствуют значениям в БД. 
***Ожидаемый результат:** кнопка авторизации отсуствует, картинка пользователя и информация в счетчиках актуальна. **Значения в счетчиках - целые числа или числа с запятой соответствующей единицы измерения!** 

5. Соответствие всего блока **"Ваш экологический вклад"** макету.
- Сравнить блок  **"Ваш экологический вклад"** с макетом для неавторизованного пользователя | Страница соответсвует макету;
- Сравнить блок  **"Ваш экологический вклад"** с макетом для авторизованного пользователя | Страница соответсвует макету.
***Ожидаемый результат:** блок "Ваш экологический вклад" соответствует макету.

*Дальнейшие тесты привязаны к 1. ТЗ - каким образом округляются значения в счетчиках (floor/ceil), преобразуется ли ровно 1000л в 1м3, отображаются ли сотые или только десятые (буду считать, что только десятые), какие максимальные единицы - я буду брать млрд. 2. К тому, каким образом реализована обработка преобразования литров в м3, кг в тонны и дальнейшее добавление млн, млрд (и вообще, возможно ли это для одного пользователя! Беру максимумы по карточкам "Покупайте на Авито..."). Буду считать, что за л -> м3 и кг -> т отвечает один блок кода, а за тыс -> млн -> млрд отвечает один и тот же код - поэтому количество тест-кейсов можно сократить.* 

**Вообще, логика хорошо ложится на юнит-тесты, поэтому подобные вещи, мне кажется, нужно автоматизировать в первую очередь.**

6. Преобразование литров в кубометры.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчика воды;  

**В БД или при перехвате ответа от сервера:**  
*Граничные значения для перехода литры -> кубометры:*  
- Выставить значение счетчика воды 1000л | 1000л заменены на 1м3;
- Выставить значение счетчика воды 1000,1л | 1000,1л заменены на 1м3;
- Выставить значение счетчика воды 999,9л | 999,9л в карточке;  

*Граничные значения для отображения чисел после запятых - мне кажется, можно рандомизировать входящие числа (как и добавить числа после запятой при необходимости), а не использовать только 15ХХ:*  
- Выставить значение счетчика воды 1449л | 1449л заменены на 1,4м3;
- Выставить значение счетчика воды 1500л | 1500л заменены на 1,5м3;
- Выставить значение счетчика воды 1551л | 1551л заменены на 1,6м3;
***Ожидаемый результат:** литры в кубометры преобразуются правильно.

7. Преобразование килограммов в тонны.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчика воды;  

**В БД или при перехвате ответа от сервера:**  
*Граничные значения для перехода килограммы -> тонны:*
- Выставить значение счетчика CO2 1000кг | 1000кг заменены на "1 тонна";
- Выставить значение счетчика CO2 1001кг | 1001кг заменены на "1 тонна";
- Выставить значение счетчика CO2 999кг | 999кг в карточке;

*Дополнительные значения для "тонны", т.к. она склоняется:*  
- Выставить значение счетчика CO2 2000кг | 2000кг заменены на "2 тонны";
- Выставить значение счетчика CO2 5000кг | 5000кг заменены на "5 тонн";
- Выставить значение счетчика CO2 5000000кг | 5000000кг заменены на "5 тыс. тонн";
- Выставить значение счетчика CO2 1500кг | 1500кг заменены на "1,5 тонны";
- Выставить значение счетчика CO2 1500000кг | 1500000кг заменены на "1,5 тыс. тонн";
***Ожидаемый результат:** килограммы в тонны преобразуются правильно.

*Здесь, как мне кажется, можно проверять на случайных счетчиках для избежания тестирования одних и тех же данных. Преобразования берем относительно м3, тонны, кВт\*Ч + кажется, сочетания по числам и тысячным переходам можно тоже рандомизировать* 

8. Преобразование 1000 единиц в тысячи (относительно м3, тонны, кВт\*Ч).
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчиков;  
- Выставить значение случайного счетчика 1000м3/т/кВт\*Ч | 1000м3/т/кВт\*Ч заменены на 1 тыс. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 1001м3/т/кВт\*Ч | 1001м3/т/кВт\*Ч заменены на 1 тыс. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 999м3/т/кВт\*Ч | 999м3/т/кВт\*Ч в карточке;
- Выставить значение случайного счетчика 1500 м3/т/кВт\*Ч | 1500 м3/т/кВт\*Ч заменены на 1,5 тыс. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1449 м3/т/кВт\*Ч | 1449 м3/т/кВт\*Ч заменены на 1,4 тыс. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1551 м3/т/кВт\*Ч | 1551 м3/т/кВт\*Ч заменены на 1,6 тыс. м3/т/кВт\*Ч ; 
***Ожидаемый результат:** 1000 единиц в тысячи преобразуются правильно.

9. Преобразование 1000 тысяч в миллион.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчиков;  
- Выставить значение случайного счетчика 1000 тыс. м3/т/кВт\*Ч | 1000 тыс. м3/т/кВт\*Ч заменены на 1 млн. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 1001 тыс. м3/т/кВт\*Ч | 1001 тыс. м3/т/кВт\*Ч заменены на 1 млн. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 999 тыс. м3/т/кВт\*Ч | 999 тыс. м3/т/кВт\*Ч в карточке;
- Выставить значение случайного счетчика 1500 тыс. м3/т/кВт\*Ч | 1500 тыс. м3/т/кВт\*Ч заменены на 1,5 млн. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1449 тыс. м3/т/кВт\*Ч | 1449 тыс. м3/т/кВт\*Ч заменены на 1,4 млн. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1551 тыс. м3/т/кВт\*Ч | 1551 тыс. м3/т/кВт\*Ч заменены на 1,6 млн. м3/т/кВт\*Ч ; 
***Ожидаемый результат:** 1000 тысяч в миллион преобразуются правильно.

10. Преобразование 1000 миллионов в миллиард.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчиков;  
- Выставить значение случайного счетчика 1000 млн. м3/т/кВт\*Ч | 1000м3/т/кВт\*Ч заменены на 1 млрд. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 1001 млн. м3/т/кВт\*Ч | 1001м3/т/кВт\*Ч заменены на 1 млрд. м3/т/кВт\*Ч;
- Выставить значение случайного счетчика 999 млн. м3/т/кВт\*Ч | 999 млн. м3/т/кВт\*Ч в карточке;
- Выставить значение случайного счетчика 1500 млн. м3/т/кВт\*Ч | 1500 млн. м3/т/кВт\*Ч заменены на 1,5 млрд. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1449 млн. м3/т/кВт\*Ч | 1449 млн. м3/т/кВт\*Ч заменены на 1,4 млрд. м3/т/кВт\*Ч ;
- Выставить значение случайного счетчика 1551 млн. м3/т/кВт\*Ч | 1551 млн. м3/т/кВт\*Ч заменены на 1,6 млрд. м3/т/кВт\*Ч ;
***Ожидаемый результат:** 1000 миллионов в миллиард преобразуются правильно.

*Тут лишь мои предположения на тему ожидаемого поведения системы. Нужно смотреть, что указано в ТЗ.*

11. Негативные тесты для значений счетчиков.
- Предусловие: Открыта страница [эко-вклада](https://www.avito.ru/avito-care/eco-impact), пользователь залогинен | Для пользователя отображается значение счетчиков;  
- Выставить пустое значение случайного счетчика | В счетчике указывается заглушка/0.
- Выставить значение случайного счетчика с использованием отрицательного числа | Число берется по модулю/0.
- Выставить значение случайного счетчика с использованием кириллицы | В счетчике указывается заглушка/0.
- Выставить значение случайного счетчика с использованием латиницы (в т.ч. проверить значение "e", т.к. может восприниматься как число-основание натурального логарифма) | В счетчике указывается заглушка/0.
- Выставить значение случайного счетчика с использованием других ASCII-символов | В счетчике указывается заглушка/0.
- Выставить значение случайного счетчика с использованием более одной запятой/точки | В счетчике указывается значение до второго разделителя/заглушка/0.
- Выставить значение случайного счетчика с использованием дроби (и даты, не воспринимается ли как дробь) | В счетчике указывается значение дроби/заглушка/0.
- Изменить значение на файл | В счетчике указывается заглушка/0.
***Ожидаемый результат:** для негативных значений отображаются заглушки/0/правильная логика.