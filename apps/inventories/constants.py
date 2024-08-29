class Constants:
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"
    ITEM_STATUS_CHOICES = [
        ("in_stock", "In Stock"),
        ("out_of_stock", "Out of Stock"),
        ("discontinued", "Discontinued"),
    ]

    KG = "kilograms"
    L = "liters"
    GAL = "gallons"

    MEASUREMENT_CHOICES = [
        (KG, "Kilograms"),
        (L, "Liters"),
        (GAL, "Gallons"),
    ]

    BOTTLE = "Bottle"
    GALLON = "Gallon"
    SACK = "Sack"
    TRAY = "Tray"
    OTHERS = "Others"
    PACKAGING_CHOICES = [
        (BOTTLE, BOTTLE),
        (GALLON, GALLON),
        (SACK, SACK),
        (TRAY, TRAY),
        (OTHERS, OTHERS),
    ]
