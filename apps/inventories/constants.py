class Constants:
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"
    ITEM_STATUS_CHOICES = [
        (IN_STOCK, "In Stock"),
        (OUT_OF_STOCK, "Out of Stock"),
        (DISCONTINUED, "Discontinued"),
    ]

    KG = "KGS"
    L = "LIT"
    GAL = "GAL"
    PCS = "PCS"
    MEASUREMENT_CHOICES = [
        (KG, "KGS"),
        (L, "LIT"),
        (GAL, "GAL"),
        (PCS, "PCS"),
    ]

    BOTTLE = "BOT"
    GALLON = "GAL"
    SACK = "SCK"
    TRAY = "TRY"
    OTHERS = "OTHERS"
    PACKAGING_CHOICES = [
        (BOTTLE, BOTTLE),
        (GALLON, GALLON),
        (SACK, SACK),
        (TRAY, TRAY),
        (OTHERS, OTHERS),
    ]
