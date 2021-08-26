from google.auth.transport import requests
from google.oauth2 import id_token


# フロントからのリクエストを受け取り、headersのauthorizationからid_token（idToken）を受け取る。
# 受け取ったトークンを解析して、トークンが有効であるかを調べる。
def validate_token(function):
    def validate(root, info, **kwargs):
      id = kwargs.get('id')
      # Bearer token... の形式でトークンを受け取る。
      token = info.context.headers['authorization']
      print(token)
      try:
          # Specify the CLIENT_ID of the app that accesses the backend:
          idinfo = id_token.verify_oauth2_token(token, requests.Request())
          print(idinfo)
          # Or, if multiple clients access the backend server:
          # idinfo = id_token.verify_oauth2_token(token, requests.Request())
          # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
          #     raise ValueError('Could not verify audience.')

          # If auth request is from a G Suite domain:
          # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
          #     raise ValueError('Wrong hosted domain.')

          # ID token is valid. Get the user's Google Account ID from the decoded token.
          userid = idinfo['sub']
      except ValueError:
          # Invalid token
          pass
    return validate
