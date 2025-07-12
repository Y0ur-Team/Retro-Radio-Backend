import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import UserSession , Channel, ChannelMember, UserSession
from core.utils import generate_callsign


# auth api just for account creation's
@csrf_exempt
def anonymous_auth(request):
    if request.method == "POST":
        session_id = request.headers.get("RETRO-TOKEN")
        if session_id:
            try:
                session = UserSession.objects.get(session_id=session_id)
                return JsonResponse({"callsign": session.callsign, "session_id": str(session.session_id)})
            except UserSession.DoesNotExist:
                pass  

        for _ in range(5):
            callsign = generate_callsign()
            if not UserSession.objects.filter(callsign=callsign).exists():
                break
        else:
            return JsonResponse({"error": "Call sign collision, try again"}, status=500)

        session = UserSession.objects.create(callsign=callsign)

        return JsonResponse({
            "callsign": session.callsign,
            "session_id": str(session.session_id)
        })

    return JsonResponse({"error": "Invalid method"}, status=405)

# joining end point for user with session id 
@csrf_exempt
def join_channel(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            frequency = body.get("frequency")

            if not frequency:
                return JsonResponse({"error": "Missing frequency"}, status=400)

            session_id = request.headers.get("RETRO-TOKEN")
            if not session_id:
                return JsonResponse({"error": "Missing RETRO-TOKEN header"}, status=401)

            try:
                user = UserSession.objects.get(session_id=session_id)
            except UserSession.DoesNotExist:
                return JsonResponse({"error": "Invalid session"}, status=403)

            channel, _ = Channel.objects.get_or_create(frequency=frequency)

            ChannelMember.objects.get_or_create(channel=channel, user=user)

            return JsonResponse({
                "message": f"Joined {frequency} MHz",
                "callsign": user.callsign,
                "frequency": channel.frequency
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)

