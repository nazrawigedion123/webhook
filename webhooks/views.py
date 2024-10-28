from django.shortcuts import render

# Create your views here.
import hmac
import hashlib
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from .models import Transaction
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def transaction_webhook(request):
    if request.method == "POST":
        # Step 1: Parse and verify the YAYA-SIGNATURE header
        signature_header = request.headers.get("YAYA-SIGNATURE")
        if not signature_header:
            return JsonResponse({"error": "Missing signature header"}, status=400)

        # Step 2: Load the request payload
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)

        # Step 3: Verify the signature
        secret_key = settings.YAYA_SECRET_KEY  # Store this key in environment variables
        signed_payload = ''.join(str(payload.get(key, '')) for key in payload)  # Concatenate values in order
        print('secret key', secret_key)
        calculated_signature = hmac.new(
            secret_key.encode(),
            signed_payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        print('calculated_signature',calculated_signature)
        print('signature_header',signature_header)

        # Check if calculated signature matches the received signature
        if not hmac.compare_digest(signature_header, calculated_signature):
            return JsonResponse({"error": "Invalid signature"}, status=400)

        # Step 4: Prevent replay attacks by validating the timestamp
        timestamp_tolerance = 300  # 5 minutes in seconds
        current_timestamp = int(timezone.now().timestamp())
        if abs(current_timestamp - payload.get("timestamp", 0)) > timestamp_tolerance:
            return JsonResponse({"error": "Request timestamp is too old"}, status=400)

        # Step 5: Save the transaction payload to the database
        Transaction.objects.create(
            transaction_id=payload["id"],
            amount=payload["amount"],
            currency=payload["currency"],
            created_at_time=payload["created_at_time"],
            timestamp=payload["timestamp"],
            cause=payload["cause"],
            full_name=payload["full_name"],
            account_name=payload["account_name"],
            invoice_url=payload["invoice_url"],
        )

        # Step 6: Respond quickly with a success message
        return JsonResponse({"status": "Transaction received successfully"}, status=200)

    # If the request is not POST
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
