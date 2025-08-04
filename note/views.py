from django.shortcuts import redirect
from django.views.generic import TemplateView

from note.send_notice import send_email, send_sms, send_telegram_message
from note.utils import cleaned_id_telegram, cleaned_phone_number, cleaned_text


class ShowMainPage(TemplateView):
    template_name = "note/index.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data_phone = request.POST.get('data_phone')
            data_email = request.POST.get('data_email')
            data_telegram = request.POST.get('data_telegram')
            data_text = request.POST.get('data_text')

            data_text = cleaned_text(str(data_text))
            data_phone = cleaned_phone_number(data_phone)
            data_telegram = cleaned_id_telegram(data_telegram)
            # print(data_phone)
            # print(data_email)
            # print(data_telegram)
            # print(data_text)
            if data_email:
                send_email(data_email, data_text)
            if data_telegram:
                send_telegram_message(data_telegram, data_text)
            if data_phone:
                send_sms(data_phone, str(data_text))
            return redirect('note:succes')
        return super().get(request, *args, **kwargs)

class ShowSucces(TemplateView):
    template_name = 'note/succes.html'
