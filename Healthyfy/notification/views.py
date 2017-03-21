from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django_cron import CronJobBase, Schedule
from announce import AnnounceClient
from django.contrib.auth.models import User
from notification.models import Notification
from django.utils import timezone
import json
announce_client = AnnounceClient()
# Create your views here.

def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/dashboard/')
		else:
			return HttpResponse("Login details are Invalid")
	else:
		return render(request, 'login.html', {})

@login_required
def home(request):
	print request.user.id
	return render(request, 'dashboard.html', {})



@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/')

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'My cron'    

    def send_notification(self, user_ids, notification_payload):
    	for id in user_ids:

    		announce_client.emit(id.pk,'notifications',data= notification_payload)

    def do(self):
    	#a = User.objects.raw('select * from auth_user')
    	current_time = timezone.now()
    	all_notice = Notification.objects.filter(timing__lte = current_time, is_visit = True)
    	
    	if all_notice.exists():
  
    		for notice in all_notice:
    			notification_payload = {}
    			try:
    				notification_payload['header'] = notice.header
    				notification_payload['content'] = notice.content
    				notification_payload['image_url'] = notice.image_url
    				print notice.image_url
    				user_ids = []
    				for user in User.objects.raw(notice.query):
    					user_ids.append(user)
    				print user_ids
    				self.send_notification(user_ids,notification_payload)

    				# notice.is_visit = False
    				# notice.save()
    			except:
    				print "Error"
    				pass
    	else:
    		print "No"
