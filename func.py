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

def process(df: pandas.DataFrame) -> str:
    #df['lastname'] = df['lastname'].apply(lambda x: str(x).upper())
    return df.to_json(orient='records')

def handler(ctx, data: io.BytesIO = None):
    logger = logging.getLogger(__name__)
    logger.info('<< OCIDI-PASSTHROUGH BEGIN >>')

    try:
        body = data.getvalue() # bytes
        #logger.info(f'Request:\n{ body.decode("utf-8") }')

        request = json.loads(body) # json
        rows = base64.b64decode(request.get("data")).decode() # json str
        logger.info(f'Data:\n{ rows }')
        logger.info(f'Parameters: { request.get("parameters") }')

        df = pandas.read_json(rows, lines=True)
        result = process(df)

        logger.info(f'Response:\n{result}')

        return response.Response(
            ctx, 
            response_data=result, 
            headers={"Content-Type": "application/json"}
        )

    finally:
        logger.info('<< OCIDI-PASSTHROUGH END >>')

