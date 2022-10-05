import logging

from ninja_extra import ControllerBase

from easy.controller.meta import CrudAPI, CrudApiMetaclass

logger = logging.getLogger(__name__)


class CrudAPIController(ControllerBase, CrudAPI, metaclass=CrudApiMetaclass):
    """
    Base APIController for auto creating CRUD APIs

    GET /?pk={id}       - Retrieve a single Object
    PUT /               - Create a single Object
    PATCH /?pk={id}     - Update fields for an Object
    DELETE /?pk={id}    - Delete a single Object
    GET /get_all        - Retrieve multiple Object, paginated
    GET /filter/?filters={filters_dict}
                        - Filter Objects with django-orm filter dict, paginated
    GET /filter_exclude/?filters={filters_dict}
                        - Filter exclude Objects with Django-ORM filter dict, paginated

    """

    ...
