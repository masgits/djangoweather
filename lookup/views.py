from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode= " + zipcode + "&distance=25&API_KEY=72DD6785-D8B9-424F-A768-581295BA6238")
		
		try:
			# Calling json from import json above to load content from the variable api_request above
			api = json.loads(api_request.content)

			# If the information from the above url cannot be accessed, an exception is called
		except Exception as e:
		    api = "Error..."	

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air Quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air Quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from the presence of particles in the air."
			category_color = "unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

			  
			
	    # The variable api above is the one transferred in the line below i.e {...: api} 
		return render(request, 'home.html', {
			'api': api, 
			'category_description' : category_description, 
			'category_color' : category_color
			})

	else:	
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11707&distance=25&API_KEY=72DD6785-D8B9-424F-A768-581295BA6238")
		
		try:
			# Calling json from import json above to load content from the variable api_request above
			api = json.loads(api_request.content)

			# If the information from the above url cannot be accessed, an exception is called
		except Exception as e:
		    api = "Error..."	

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air Quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air Quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from the presence of particles in the air."
			category_color = "unhealthyforsensitivegroups"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

			  
			
	    # The variable api above is the one transferred in the line below i.e {...: api} 
		return render(request, 'home.html', {
			'api': api, 
			'category_description' : category_description, 
			'category_color' : category_color
			})

def about(request):
	return render(request, 'about.html', {})
