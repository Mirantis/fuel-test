========
Введение
========
Fuel-test -- набор библиотек и скриптов для проверки качества работы библиотеки puppet-модулей Fuel (https://fuel.mirantis.com/).

Основная задача -- это проверить соответствие спецификации и работоспособность Fuel на поддерживаемых окружениях:

- single
- simple
- minimal
- compact
- full

Fuel-test используется для следующих видов тестирования:

- проверка синтаксиса -- Syntax and Style Check
- модульные тесты -- Unit testing (rspec)
- интеграционные тесты для модулей puppet -- Integration testing
- системное тестирование -- System testing
- tempest


Также библиотека включают проверку каждого модуля  Fuel по отдельности, что упрощает полное развёртывание и тестирование всей системы.
Регулярное автоматическое тестирование работы всей системы лежит в основе технологии Непрерывной интеграции. При обычном каскадном или 
итеративном процессе разработки стадия интеграции обычно является последней и часто приводит к появлению непредсказуемых проблем, которые 
могут сильно задержать выпуск следующей версии. Переход к непрерывной интеграции позволяет снизить эти риски и способствует раннему 
обнаружению ошибок, противочечий и других сложностей.

Непрерывная интеграция вместе с разработкой через тестирование входит в состав приёмов Гибкой (Agile) методики разработки программного обеспечения.
