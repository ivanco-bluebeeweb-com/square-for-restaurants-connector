# Square for Restaurants Connector — Discovery

**Vendor:** Square for Restaurants (https://squareup.com/us/en/point-of-sale/restaurants)  
**API Base URL:** `https://connect.squareup.com/v2`  
**Authentication:** OAuth 2.0 Bearer Token / Personal Access Token

## Архитектура API
- **Ключевые сущности:** заказы (/v2/orders), каталог блюд (/v2/catalog/object), платежи (/v2/payments), бронирования столов (/v2/bookings)
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /v2/locations`.
