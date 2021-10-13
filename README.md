
```
$ pytest -s functest.py
================================== test session starts ===================================
platform linux -- Python 3.6.8, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /mnt/extra/work/fn/ocidi-passthrough
plugins: asyncio-0.12.0
collected 1 item                                                                         

functest.py None - func - INFO - << OCIDI-PASSTHROUGH BEGIN >>
None - func - INFO - Data:
{"firstname": "James", "lastname": "Brown"}
{"firstname": "David", "lastname": "Paich"}

None - func - INFO - Parameters: {'param1': 'param1value'}
None - func - INFO - Response:
[{"firstname":"James","lastname":"Brown"},{"firstname":"David","lastname":"Paich"}]
None - func - INFO - << OCIDI-PASSTHROUGH END >>
.

=================================== 1 passed in 0.54s ====================================
```