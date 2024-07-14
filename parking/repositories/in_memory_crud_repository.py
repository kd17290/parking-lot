from typing import Generic, TypeVar

T = TypeVar("T")


class InMemoryCRUDRepository(Generic[T]):
    _data: dict[int, T]
    counter: int

    def __init__(self):
        self._data = {}
        self.counter = 1

    def find_by_id(self, pk: int) -> T:
        return self._data.get(pk, None)

    def update(self, obj: T) -> None:
        self._data[obj.id] = obj
        return obj

    def delete(self, pk: int) -> None:
        return self._data.pop(pk, None)

    def create(self, obj: T) -> T:
        obj.id = self.counter
        self._data[obj.id] = obj
        self.counter += 1
        return obj

    def find(self, **kwargs) -> list[T]:
        result = []
        for obj in self._data.values():
            match = True
            for k, v in kwargs.items():
                if getattr(obj, k, None) != v:
                    match = False
            if match:
                result.append(obj)
        return result

    def find_one(self, **kwargs) -> T | None:
        result = self.find(**kwargs)
        if result:
            return result[0]
        return None
