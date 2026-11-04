# Лабораторная работа 9

Автоматический запуск тестов калькулятора из лабораторной работы 6 через GitHub Actions.

## Локальная проверка

    python -m pip install -r requirements.txt
    python -m pytest -v test_calculator.py

Четыре тестовых метода проверяют 19 наборов данных с помощью unittest.subTest. Pytest запускает эти методы и показывает итог 4 passed.

## GitHub Actions

Workflow описан в .github/workflows/run-tests.yml.
При каждом push GitHub запускает Ubuntu, получает код, подготавливает Python 3.12, устанавливает pytest и выполняет тесты.

Результат находится на вкладке Actions. Откройте запуск Python tests, затем задание tests и шаг Run tests.

Для повторного запуска без изменения кода откройте Actions → Python tests → Run workflow.
