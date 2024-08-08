#### Файлы с заданиями:
1. TASK1.pdf - первое задание, хорошо открывается для просмотра в гитхабе :) Формат в задании указан не был, поэтому оформила, как привычно - в таблице;
2. TESTCASES.md - часть задания 2 на составление тест-кейсов;
3. README.md - описание файлов и порядок работы с автотестами;
4. test1-1.png, test1-2.png, test1-3.png - скриншоты эко-счетчиков, т.к.  задании указано сохранить файлы в корневой папке;
5. python-файлы для тестов.

#### Файлы для тестов:

1. conftest.py, в котором определяется браузер и страница;
2. page_objects.py, в котором определяется класс страницы EcoImpact и содержатся методы, необходимые для ее тестирования;
3. test_eco_impact.py, в котором лежат авто-тесты для блока с эко-счетчиками страницы EcoImpact.

#### Для работы со скриптом нужно: 

1. Склонировать этот репозиторий себе на компьютер;  

`git clone git@github.com:jeleshy/test-task.git`  

*При возникновении ssh-ошибок (или Permission denied (publickey)), нужно добавить публичный ssh-ключ к Вашему gitHub аккаунту. Подробнее про [привязку](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) ssh-ключа и про его [генерацию](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)*

2. Установить [python](https://www.python.org/about/gettingstarted), [pytest](https://docs.pytest.org/en/8.2.x/getting-started.html) и [playwright](https://playwright.dev/python/docs/intro) или использовать команду `sh install_files/install_mcos_linux.sh` (mcOS/Linux) или `install_files/install_win.bat` (Windows);

3. В файле conftest.py можно выбрать браузер для тестирования - Chrome (chromium), Mozilla (mozilla) или Safari (webkit). Уберите значок `#` у нужного для тестирования. **Одновременно может использоваться только один браузер, остальные должны быть со значком #, например #browser = p.firefox.launch()`**. Браузер по умолчанию - Chrome;

4. Запустить **pytest** с помощью команды `pytest` (или `pytest -s test_eco_impact.py`, чтобы видеть принты в терминале - если менять номера эко-счетчиков на несуществующие, к примеру);

5. После этого в терминале появится сообщение о пройденных/непройденных тестах, а в папке **outro** - скриншоты эко-счетчиков.