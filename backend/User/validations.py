from voluptuous import MultipleInvalid, Schema, Required

def validate_user_register(value):
    print("inside of validate_user_register")
    print(value)

    try:
        schema = Schema({
                Required('first_name'): str,
                Required('last_name'): str,
                Required('user_name'): str,
                Required('user_password'): str
            })

        schema(value)
        return {'response': 200, 'body': value}
    except MultipleInvalid as e:
        print(e)
        return {'response': 400, 'error': str(e)}

def validate_user_login(value):
    print("inside of validate_user_login")
    print(value)

    try:
        schema = Schema({
                Required('user_name'): str,
                Required('user_password'): str
            })

        schema(value)
        return {'response': 200, 'body': value}
    except MultipleInvalid as e:
        print(e)
        return {'response': 400, 'error': str(e)}

def validate_dashboard(value):
    print("inside of validate_dashboard")
    print(value)

    try:
        schema = Schema({
                Required('user_name'): str
        })

        schema(value)
        return {'response': 200, 'body': value}
    except MultipleInvalid as e:
        print(e)
        return {'response': 400, 'error': str(e)}

def validate_analytics(value):
    print("inside of validate_dashboard")
    print(value)

    try:
        schema = Schema({
                Required('user_name'): str
        })

        schema(value)
        return {'response': 200, 'body': value}
    except MultipleInvalid as e:
        print(e)
        return {'response': 400, 'error': str(e)}
