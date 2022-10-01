import logging
from typing import Any

from asgiref.sync import sync_to_async
from django.db.models.query import QuerySet

from easy.domain.orm import CrudModel

logger = logging.getLogger(__name__)


class CrudService(CrudModel):
    def __init__(self, model=None):
        super().__init__(model)
        self.model = model

    async def get_obj(self, id: int):
        return await sync_to_async(self._crud_get_obj)(id)

    async def get_objs(self, maximum: int = None, **filters: Any) -> QuerySet:
        return await sync_to_async(self._crud_get_objs_all)(maximum, **filters)

    async def patch_obj(self, id: int, payload: Any):
        return await sync_to_async(self._crud_update_obj)(id, payload)

    async def del_obj(self, id: int):
        return await sync_to_async(self._crud_del_obj)(id)

    async def add_obj(self, **payload: Any):
        return await sync_to_async(self._crud_add_obj)(**payload)

    async def filter_objs(self, **payload: Any):
        return await sync_to_async(self._crud_filter)(**payload)

    async def filter_exclude_objs(self, **payload: Any):
        return await sync_to_async(self._crud_filter_exclude)(**payload)

    async def bulk_create_objs(self):
        ...

    async def recover_obj(self):
        ...