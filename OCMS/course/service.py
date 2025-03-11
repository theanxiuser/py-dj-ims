from django.core.mail import send_mail
from ocms.settings import EMAIL_HOST_USER


def send_result_mail(data):
    try:
        send_mail(
            subject="MCQ Result",
            message=f"Hi {data['student'].first_name},\n\nYou have scored {data['marks']} marks in the course {data['course'].title}.",
            from_email=EMAIL_HOST_USER,
            recipient_list=[data['student'].email],
            fail_silently=False
        )
        return True
    except Exception as e:
        print("detail", e)
        return False