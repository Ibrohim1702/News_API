from rest_framework.authentication import TokenAuthentication
import json
import requests

from sayt_api.models import ServerTokens



class BearerAuth(TokenAuthentication):
    keyword = 'Bearer'




def sms_sender(mobile, otp, lan="uz"):
    token = ServerTokens.objects.get(key="sms")
    txt = {
        "uz": f"sizning maxfiy codingiz {otp}, (uz). Bu codeni hech kimga bermang",
        "ru": f"kode {otp}, (ru)",
        "en": f"code {otp}, (en)"
    }

    url = "https://notify.eskiz.uz/api/message/sms/send"
    params = {
        "mobile_phone": mobile,
        "message": txt[lan],
        "from": 4546,
        "callback_url": "http://0000.uz/test.php"

    }
    headers = {
        "Authorization": f"Bearer {token.token}"
    }

    response = requests.post(url, data=params, headers=headers)
    return response.json()
