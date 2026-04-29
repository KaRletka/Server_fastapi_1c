SECRET_KEY       = "change-me-in-production-use-random-string"

# IP внешнего AI-сервиса (1C AI Bridge). Заполнить вручную, например: "http://192.168.1.50:8000"
AI_SERVICE_URL   = "http://localhost:8888"

# Ref_Key видов цен из Catalog_ВидыЦен
PRICE_TYPE_RETAIL     = "7481362d-b5b8-11e4-8355-74d02b7dfd8c"  # Розничная
PRICE_TYPE_WHOLESALE  = "72e9e83e-fb07-11e4-8005-74d02b7dfd8c"  # Оптовая

# Названия колонок цен для HTML
PRICE_COLUMNS = {
    PRICE_TYPE_RETAIL:    "Розничная",
    PRICE_TYPE_WHOLESALE: "Оптовая",
}