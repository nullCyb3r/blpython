import requests

def check_vulnerabilities(service, version):
    base_url = "https://nvd.nist.gov/vuln"
    params = {
        "keyword":f"{service} {version}",
        "resultsPerPage" : 5
    }
    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["totalResults"] > 0:
            print(f"Potential Vulnerabilities for {service} {version} : ")
            for result in data["result"]["CVE_Items"]:
                cve_id = result["cve"]["CVE_data_meta"]["ID"]
                description = result["cve"]["description"]["description_data"][0]["value"]
                print(f" {cve_id} : {description[:100]}")
            else:
                print(f"No known vulnerabilities found for {service} {version}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking vulnerabilities : {e}")
check_vulnerabilities("Apache","2.4.29")