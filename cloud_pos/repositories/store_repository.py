class StoreRepository:
    stores = []

    @classmethod
    def save_store(cls, store):
        cls.stores.append(store)

    @classmethod
    def get_store_by_id(cls, store_id):
        for store in cls.stores:
            if store.store_id == store_id:
                return store
        return None
