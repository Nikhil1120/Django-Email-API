# from django.core.mail import send_mail
# from .models import EmailLog
# from django.conf import settings


# def send_email_notification(subject, message, recipient_list):
#     """
#     Send email and log the sent email into the EmailLog model
#     """
#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         recipient_list,
#         fail_silently=False,
#     )
    
#     # Log the sent email
#     for recipient in recipient_list:
#         EmailLog.objects.create(
#             recipient=recipient,
#             subject=subject,
#             body=message
#         )
