import os
import google_apis_oauth

from django.shortcuts import HttpResponseRedirect

REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'


SCOPES = ['https://www.googleapis.com/auth/calendar']

JSON_FILEPATH = os.path.join(os.getcwd(), 'client_id.json')

def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)