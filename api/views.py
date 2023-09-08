from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

github_file_url = "https://github.com/dfamiliarstranger/Zuri-Hng/blob/main/manage.py"  # Replace with your GitHub URL
github_repo_url = "https://github.com/dfamiliarstranger/Zuri-Hng"  

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if not slack_name or not track:
        return JsonResponse({"error": "slack_name and track parameters are required"}, status=400)

    current_day = timezone.now().strftime("%A")
    utc_time = timezone.now().strftime("%Y-%m-%dT%H:%M:%SZ")



    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": "200"
    }

    return JsonResponse(response_data)
