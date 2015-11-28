from django.http import HttpResponse, HttpResponseRedirect

#Standard Import related to Python
import json, requests
from asyncio import get_event_loop, coroutine
from aiohttp.client import ClientSession


# Main View which returns api respose
def bill_info(request, consumer_num):
	# getting the loop event
    loop = get_event_loop()
    # calling the ep function until we recive a response from server
    r_bill_info = loop.run_until_complete(bill_info_ep(consumer_id))
    
    # display the response to public whatever it is
    return HttpResponse(json.dumps(r_bill_info))




# Get bill information for User
@coroutine
def bill_info_ep(consumer_id, msisdn="03342921358"):

    # get the the Credtionals for EasyPaisa # Setting must exist in DB with PK of 1
    # settings = SiteSettings.objects.get(pk=1)

    # Defining Constants Private
    PHONE = "923418553996"
    USERNAME = "zaintariqs"
    PASSWORD = "P@Ybill123!@#"

    with ClientSession() as client:
        msisdn = "03026622855"

        print("Getting the Bill info for ", consumer_num)
        print("Number to be Notified after Bill payment: ", msisdn)
        
        # Create a Browser session
        url = 'https://online.easypaisa.com.pk/j_spring_security_check'
        response = yield from client.get(url)
        yield from response.text()
        jscookiesid = client.cookies['JSESSIONID'].value
        headers = {'Cookie': 'JSESSIONID=' + jscookiesid}
        login_data = dict(
            j_usermsisdn=PHONE, j_username=USERNAME, j_password=PASSWORD)

        response = yield from client.post(
            url, data=login_data, headers=headers)
        yield from response.text()

        cooked_url = (
            "https://online.easypaisa.com.pk/inquiremanualbill.htm?" +
            "consumerNo=" + str(consumer_num) +
            "&utilityType=Telephone&companyName=PTCL0003" +
            "&msisdn=" + msisdn)
        response = yield from client.get(cooked_url)
        page = yield from response.text()
        
        print("Response from EasyPaisa is", page)
        
    return json.loads(page)