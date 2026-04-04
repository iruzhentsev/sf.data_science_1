# Прогнозирование рейтинга отелей (Booking.com) – упрощённая версия

Проект выполнен в рамках курса Skillfactory.  
**Цель** – построить модель, предсказывающую оценку отеля (`reviewer_score`) на основе отзывов и метаданных.  
**Метрика качества** – MAPE (Mean Absolute Percentage Error).  
**Результат на валидации** – MAPE ≈ 13.06%.

## Данные

Используются данные из соревнования, содержащие отзывы об отелях (515 000 записей).   
Основные поля:

- `hotel_address` – адрес отеля
- `review_date` – дата отзыва
- `average_score` – средний балл отеля
- `hotel_name` – название отеля
- `reviewer_nationality` – страна рецензента
- `negative_review` / `positive_review` – тексты отзывов
- `review_total_negative_word_counts` / `review_total_positive_word_counts` – количество слов
- `reviewer_score` – **целевая переменная** (оценка от 2.5 до 10)
- `total_number_of_reviews`, `total_number_of_reviews_reviewer_has_given`
- `tags` – теги (тип поездки, количество ночей и др.)
- `days_since_review` – давность отзыва
- `additional_number_of_scoring` – число оценок без текста
- `lat`, `lng` – координаты отеля

## Этапы работы

### 1. Очистка и предобработка
- Заполнение пропусков в `lat`/`lng` средними значениями по отелю (или медианой).
- Преобразование `days_since_review` в числовой формат (извлечение числа дней).
- Извлечение из `review_date` года, месяца и дня недели.

### 2. Создание новых признаков (Feature Engineering)
- **Страна** – из адреса отеля (последнее слово).
- **Длина отзывов** – количество символов в `positive_review` и `negative_review`.
- **Из тегов** – количество ночей (`nights`) и тип поездки (`trip_type`: leisure / business / other).
- Все текстовые поля (`positive_review`, `negative_review`, `hotel_name`, `reviewer_nationality`) не используются напрямую, только производные признаки (длина, категории).

### 3. Преобразование признаков
- Категориальные признаки (`country`, `trip_type`) закодированы через `LabelEncoder`.
- Числовые признаки масштабированы с помощью `StandardScaler`.

### 4. Моделирование
- **Модель:** RandomForestRegressor
- **Параметры:**
  - `n_estimators = 100` (базовый)
  - `max_depth = 15`
  - `random_state = 42`
- Разделение данных: 80% – обучение, 20% – валидация.

### 5. Оценка качества
- **MAPE на валидации:** 0.1306 (13.06%)
- **MAE на валидации:** ~0.901

### 6. Визуализация
- Распределение целевой переменной
- Scatter‑plot «факт vs предсказание»
- Гистограмма остатков
- График важности признаков

## Результаты (топ‑5 важных признаков)

1. `neg_len` – длина негативного отзыва (41%)
2. `pos_len` – длина позитивного отзыва (24%)
3. `average_score` – средний балл отеля (12%)
4. `days_since_review_num` – давность отзыва (3.5%)
5. `review_total_negative_word_counts` – количество слов в негативном отзыве (2.3%)

## Файлы в репозитории

- `hotel_rating_prediction_RFR.ipynb` – Jupyter‑ноутбук с полным кодом.
- `submissions_RFR.csv` – файл для отправки на Kaggle.
- `requirements.txt` – список зависимостей.
- `README.md` – этот файл.

## Как запустить

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_username/booking-rating-simple.git
