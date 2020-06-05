from voluptuous import MultipleInvalid, Schema, Required, All, Length


def validate_playlist(value):
    try:
        schema = Schema({
                Required('playlist_name'): All(str, Length(min=1))
            })

        schema(value)
        return {'response': 200, 'body': value}
    except MultipleInvalid as e:
        print(e)
        raise e
