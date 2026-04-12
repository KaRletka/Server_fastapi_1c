SECRET_KEY       = "change-me-in-production-use-random-string"

ONEC_PATH        = "/unf_dashboard/odata/standard.odata"  # путь к OData 1С

# Ref_Key видов цен из Catalog_ВидыЦен
PRICE_TYPE_RETAIL     = "7481362d-b5b8-11e4-8355-74d02b7dfd8c"  # Розничная
PRICE_TYPE_WHOLESALE  = "72e9e83e-fb07-11e4-8005-74d02b7dfd8c"  # Оптовая

# Названия колонок цен для HTML
PRICE_COLUMNS = {
    PRICE_TYPE_RETAIL:    "Розничная",
    PRICE_TYPE_WHOLESALE: "Оптовая",
}