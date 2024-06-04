import requests
import re
import time
from ruamel.yaml import YAML
import os


blackduck_token = os.getenv("BLACKDUCK_TOKEN", "")
report_version = os.getenv("REPORT_VERSION", "")
yaml = YAML(typ='safe', pure=True)
api_token = yaml.load(blackduck_token)
version = yaml.load(report_version)
blackduck_url = 'https://apus-blackduck.volvocars.biz'
bearer_token_respons = requests.post(blackduck_url + "/api/tokens/authenticate", headers={'Authorization': 'token ' + api_token, 'Accept': 'application/vnd.blackducksoftware.user-4+json'})
bearer_token = bearer_token_respons.json().get('bearerToken')
data={
  "reportFormat" : "TEXT",
  "versionId" : version,
  "categories" : [ "COPYRIGHT_TEXT" ],
}
create_notice_file_result = requests.post(blackduck_url + f"/api/versions/{version}/license-reports/", headers={'Authorization': 'Bearer ' + bearer_token, "Accept": "application/vnd.blackducksoftware.report-4+json" ,"Content-Type": "application/vnd.blackducksoftware.report-4+json"}, json=data)
link_header = create_notice_file_result.headers.get('Link')
urls = re.findall('<(.*?)>', link_header)
rels = re.findall('rel="(.*?)"', link_header)
link_dict = dict(zip(rels, urls))
download_url = link_dict.get('download')
time.sleep(60)
for attempts in range(10):
    try:
        zip_respons = requests.get(download_url, headers={'Authorization': 'Bearer ' + bearer_token, "Accept": "application/vnd.blackducksoftware.report-4+json"})
        break
    except requests.exceptions.RequestException:
        time.sleep(10)
with open('license-report.zip', 'wb') as f:
    f.write(zip_respons.content)
