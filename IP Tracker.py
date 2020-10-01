# including requires librarires
import requests
import argparse
import json

# calling main method
if __name__ == "__main__":
	parser = argparse.ArgumentParser()					#argument parser to accept arguments when running script from a shell
	parser.add_argument("-i", "--ipaddress", help = "IP Address To Track")
	args = parser.parse_args()
	ip = args.ipaddress							#taking IP address
	data = {}
	if ip is None:
		print("Please provide IP ")
	else:
		url = "http://ip-api.com/json/"+ ip					#appending IP to domain
		try:
			response = requests.get(url)						#getting Response of the Query
			data = json.loads(response.content)					#Getting useful data from the response that we get
		except Exception as api_exception:
			print(f"Failed to get {ip} information")
			print(f"Detailed Error: {api_exception}")
			
		print("\t[+] IP \t", data.get("query"))					#
		print("\t[+] CITY \t", data.get("city"))				#
		print("\t[+] ISP \t", data.get("isp"))					#
		print("\t[+] LOC \t", data.get("country"))				#	
		print("\t[+] REG \t", data.get("regionName"))				#     printing required data about given IP Address
		print("\t[+] TIME \t", data.get("timezone"))				#
		print("\t[+] ZIP \t", data.get("zip"))					#
		print("\t[+] LAT \t", data.get("lat"))					#
		print("\t[+] LON \t", data.get("lon"))					#
