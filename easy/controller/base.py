import logging
from abc import ABC
from typing import Union

from ninja_extra import ControllerBase

from easy.controller.meta import AdminApiMetaclass, CrudAPI, CrudApiMetaclass
from easy.services import BaseService

logger = logging.getLogger(__name__)


class BaseAdminAPIController(ControllerBase, CrudAPI, ABC, metaclass=AdminApiMetaclass):
    """For AdminAPI"""

    def __init__(self, service: Union["BaseService", None] = None):
        super().__init__(service=service)  # pragma: no cover


class CrudAPIController(ControllerBase, CrudAPI, ABC, metaclass=CrudApiMetaclass):
    """For Client facing APIs"""

    def __init__(self, service: Union["BaseService", None] = None):
        super().__init__(service=service)  # pragma: no cover
