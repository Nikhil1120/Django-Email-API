from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmailSerializer


def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "api/index.html", context)


@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        # Deserialize the request data
        serializer = EmailSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract data from the validated serializer
            address = serializer.validated_data['address']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            
            try:
                # Send the email
                send_mail(
                    subject,  # Subject
                    message,  # Message body
                    settings.EMAIL_HOST_USER,  # From email
                    [address],  # Recipient email (list of one recipient)
                )
                return Response({"status": "Email sent successfully"}, status=200)
            except Exception as e:
                return Response({"status": f"Error sending email: {str(e)}"}, status=500)
        else:
            return Response(serializer.errors, status=400)
