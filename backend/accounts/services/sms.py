import requests

from django.conf import settings


def send_bulk_sms(message_text, mobiles):
    """
    ارسال پیامک گروهی با استفاده از SMS.ir
    """

    api_url = "https://api.sms.ir/v1/send/bulk"

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": settings.SMSAPIKEY,
    }

    payload = {
        "lineNumber": settings.SMSLINENUMBER,
        "messageText": message_text,
        "mobiles": mobiles,
    }

    response = requests.post(
        api_url,
        headers=headers,
        json=payload,
        timeout=10,
    )

    try:
        return response.json()
    except Exception:
        return {
            "status": 0,
            "message": "خطا در پردازش پاسخ سرور",
        }