from framework.request_handler import YumSearchRequestHandler

class RegisterUser(YumSearchRequestHandler):
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        password = self.request.get('password')

        if name and email and password:
            # Success
            pass
        else:
            status = 400
            json_response = {}

            registration_data = {'Name': name, 'Password': password, 'Email': email}
            for field in registration_data:
                if not registration_data[field]:
                    json_response.update({
                        'title': 'The {} field is required'.format(field),
                        'message': 'Please fill in your {} in order to continue'.format(field)
                    })
                    break

            self.json_response(status_code=status, **json_response)