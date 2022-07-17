# petstore
petstore api tests project

### Поддержка версий
Поддерживает `Python 3.7` и выше

### Установка зависимостей
python3 -m venv /path/to/directory/virtual_env_name

source /path/to/venv/bin/activate

pip3 install -r requirements.txt

### Запуск тестов
pytest -n=4 --alluredir=path_to_results\allure-results

### Генерация allure отчета
allure serve
