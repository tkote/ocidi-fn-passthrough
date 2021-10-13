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
    logger = logging.getLogger(__name__)

    try:
        body = data.getvalue() # bytes
        #logger.info(f'Request:\n{ body.decode("utf-8") }')

        request = json.loads(body) # json
        data = base64.b64decode(request.get("data")).decode() # json str
        logger.info(f'Data:\n{ data }')
        logger.info(f'Parameters: { request.get("parameters") }')

        df = pandas.read_json(data, lines=True)
        result = df.to_json(orient='records')

        logger.info(f'Response:\n{result}')

        return response.Response(
            ctx, 
            response_data=result, 
            headers={"Content-Type": "application/json"}
        )

    finally:
        logger.info('<< OCIDI-PASSTHROUGH END >>')

