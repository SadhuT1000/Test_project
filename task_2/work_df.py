from pyspark.sql import DataFrame
from pyspark.sql.functions import lit


def get_product_category_pairs(products_df, categories_df, data_f):
    """
    Возвращает  пары продукты и категория и продукты без категорий
    """

    with_categories = (
        data_f.join(products_df, "product_id")
        .join(categories_df, "category_id")
        .select("product_name", "category_name")
    )


    without_categories = (
        products_df.join(data_f, "product_id", "left_anti")
        .select("product_name", lit(None).alias("category_name"))
    )

    return with_categories.union(without_categories)