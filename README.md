# YouTube Clickbait Detector

CLI-приложение для анализа метрик YouTube-видео и генерации отчётов по CSV-файлам.

## Пример запуска

```bash
python -m src.main --files data/stats1.csv data/stats2.csv --report clickbait
```

## Доступные отчёты

- `clickbait` — видео с высоким CTR и низким retention rate

## Тесты

```bash
pytest --cov=src
```