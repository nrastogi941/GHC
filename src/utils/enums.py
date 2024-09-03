from enum import Enum, unique


@unique
class BaseEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_(cls):
        return list(map(lambda c: c.name, cls))
    

class Providers(BaseEnum):
    SHOPIFY = "shopify"
    WOOCOMMERCE = "woocommerce"