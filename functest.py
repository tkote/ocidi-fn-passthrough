import io
import json
import base64
from fdk import fixtures
import pytest
import func


@pytest.mark.asyncio
async def test_parse_request_without_data():
    rows = [
        {"firstname":"James","lastname":"Brown","secret_id_field":"0927e5a8-9097-4cad-a7fa-b6167184c744"},
        {"firstname":"David","lastname":"Paich","secret_id_field":"58e25c06-6011-30b4-59e8-d1647eed49f1"}
    ]
    parameters = {"param1" : "param1value"}
    data = []
    for row in rows:
        data.append(json.dumps(row) + '\n')
    request = {
        "data" : base64.b64encode(''.join(data).encode('utf-8')).decode('utf-8'),
        "parameters" : parameters
    }
    input_content = io.BytesIO(json.dumps(request).encode("utf-8"))
    call = await fixtures.setup_fn_call(func.handler, content=input_content)

    content, status, headers = await call

    assert 200 == status
    assert rows == json.loads(content)
