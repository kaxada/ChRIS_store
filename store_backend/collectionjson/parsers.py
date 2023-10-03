from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

class CollectionJsonParser(JSONParser):
    media_type = 'application/vnd.collection+json'

    def validate_data(self, stream_data):
        template_valid_str = "Valid format: {template:{data:[{name: ,value: },...]}}"

        if not isinstance(stream_data, dict):
            detail = f"Template is not a dictionary. {template_valid_str}"
            raise ParseError(detail=detail)

        json_data = {}
        try:
            for x in stream_data['template']['data']:
                json_data[x['name']] = x['value']
        except KeyError as e:
            detail = f"{e} field required. "
            detail += template_valid_str
            raise ParseError(detail=detail)
        except TypeError as e:
            detail = f"Invalid data provided. {template_valid_str}"
            raise ParseError(detail=detail)
        return json_data 

    def parse(self, stream, media_type=None, parser_context=None):
        stream_data = super(CollectionJsonParser, self).parse(stream, media_type,
                                                          parser_context)
        return self.validate_data(stream_data)


