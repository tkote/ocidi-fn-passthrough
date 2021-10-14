
```
$ pytest -s functest.py 
================================= test session starts ==================================
platform linux -- Python 3.6.8, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /mnt/extra/work/fn/ocidi-passthrough
plugins: asyncio-0.12.0
collected 1 item                                                                       

functest.py None - func - INFO - << OCIDI-PASSTHROUGH BEGIN >>
None - func - INFO - Data:
{"firstname": "James", "lastname": "Brown", "secret_id_field": "0927e5a8-9097-4cad-a7fa-b6167184c744"}
{"firstname": "David", "lastname": "Paich", "secret_id_field": "58e25c06-6011-30b4-59e8-d1647eed49f1"}

None - func - INFO - Parameters: {'param1': 'param1value'}
None - func - INFO - Response:
[{"firstname":"James","lastname":"Brown","secret_id_field":"0927e5a8-9097-4cad-a7fa-b6167184c744"},{"firstname":"David","lastname":"Paich","secret_id_field":"58e25c06-6011-30b4-59e8-d1647eed49f1"}]
None - func - INFO - << OCIDI-PASSTHROUGH END >>
.

================================== 1 passed in 0.55s ===================================
```
