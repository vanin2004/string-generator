# String Generator

Сервис для генерации случайных строк

Расположение проекта:

- `app/` — точка входа и API
  - `app/main.py` — FastAPI приложение
  - `app/api/` — маршруты API
  - `app/domain/` — доменные сущности и исключения
  - `app/utils/` — утилиты

## Требования

- Python 3.10+ (проверьте `requirements.txt` для зависимостей)
- Docker (опционально, для запуска в контейнере)

## Установка (Windows PowerShell)

1. Клонируйте репозиторий или откройте папку проекта.
2. Создайте виртуальное окружение и активируйте его:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Установите зависимости:

```powershell
pip install -r requirements.txt
```

## Запуск локально

Проект использует FastAPI (см. `app/main.py`). Для запуска в режиме разработки используйте uvicorn:

```powershell
uvicorn app.main:app --reload --port 8000
```

После запуска API будет доступен по адресу:

- Документация OpenAPI (Swagger UI): http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Пример запроса

Пример с использованием curl (на Windows в PowerShell можете использовать Invoke-RestMethod):

```powershell
# пример POST-запроса, уточните детали в API (путь и тело)
curl -X POST "http://127.0.0.1:8000/api/random-string" -H "Content-Type: application/json" -d '{"length": 10, "use_lowercase": true}'
```

PowerShell (Invoke-RestMethod):

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/random-string" -ContentType "application/json" -Body (@{length=10; use_lowercase=$true} | ConvertTo-Json)
```

(Обратите внимание: путь `/random-string` служит примером — посмотрите реальные маршруты в `app/api`.)

## Запуск с Docker

Сборка образа и запуск через `docker-compose` (если присутствует `docker-compose.yaml`):

```powershell
# собрать и запустить контейнеры
docker-compose up --build -d

# остановить и удалить
docker-compose down
```

Или через Docker напрямую:

```powershell
# собрать образ
docker build -t string-generator:latest .

# запустить контейнер
docker run -p 8000:8000 string-generator:latest
```

## Тестирование и отладка

- Быстрая проверка: после запуска сервиса откройте `/docs` и отправьте тестовые запросы через Swagger UI.
- Локальная отладка: используйте `--reload` в uvicorn для автоперезагрузки при изменениях.

## Лицензия

Проект содержит файл `LICENSE` в корне репозитория — смотрите его для деталей.