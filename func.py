import io
import json
import logging
import base64
import pandas

from fdk import response


"""
Request:                          // JSON String
{
     data="",                     // inputMap -> JSON String -> UTF-8 Byte array -> base64 encoding
     parameters=""                // JSON String
}

Response:                         // JSON String
{

     "records"                    // dataframe -> JSON String

} 
"""

def handler(ctx, data: io.BytesIO = None):
    print('<< OCIDI-PASSTHROUGH BEGIN >>')

    try:
        #logger = logging.getLogger()
        bodystr = data.getvalue().decode('utf-8')
        print('[REQUEST]')
        print(bodystr)

        body = json.loads(data.getvalue()) # json

        input_data = base64.b64decode(body.get("data")).decode() # json str

        print(f'Data: {input_data}')

        df = pandas.read_json(input_data, lines=True)
        str=df.to_json(orient='records')
        print('[RESPONSE]')
        print(str)
        return response.Response(
            ctx, response_data=str, headers={"Content-Type": "application/json"}
        )

    except Exception as e:
        print(e)
        raise e

    finally:
        print('<< OCIDI-PASSTHROUGH END >>')

