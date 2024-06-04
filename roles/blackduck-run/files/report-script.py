import os
import requests
import re
import time
from ruamel.yaml import YAML
from requests.adapters import HTTPAdapter, Retry

def get_bearer_token(blackduck_url, api_token):
    response = requests.post(
        f"{blackduck_url}/api/tokens/authenticate",
        headers={
            'Authorization': f'token {api_token}',
            'Accept': 'application/vnd.blackducksoftware.user-4+json'
        }
    )
    return response.json().get('bearerToken')

def create_notice_file(blackduck_url, bearer_token, version):
    data = {
        "reportFormat": "TEXT",
        "versionId": version,
        "categories": ["COPYRIGHT_TEXT"],
    }
    response = requests.post(
        f"{blackduck_url}/api/versions/{version}/license-reports/",
        headers={
            'Authorization': f'Bearer {bearer_token}',
            "Accept": "application/vnd.blackducksoftware.report-4+json",
            "Content-Type": "application/vnd.blackducksoftware.report-4+json"
        },
        json=data
    )
    return response.headers.get('Link')

def extract_download_url(link_header):
    urls = re.findall('<(.*?)>', link_header)
    rels = re.findall('rel="(.*?)"', link_header)
    link_dict = dict(zip(rels, urls))
    return link_dict.get('download')

def download_report(download_url, bearer_token, output_file):
    session = requests.Session()
    retry = Retry(
        total=10,
        backoff_factor=10,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    response = session.get(
        download_url,
        headers={
            'Authorization': f'Bearer {bearer_token}',
            "Accept": "application/vnd.blackducksoftware.report-4+json"
        }
    )
    with open(output_file, 'wb') as f:
        f.write(response.content)

def main():
    yaml = YAML(typ='safe', pure=True)
    report_version = os.getenv("REPORT_VERSION", "")
    version = yaml.load(report_version)
    blackduck_token = os.getenv("BLACKDUCK_TOKEN", "")
    api_token = yaml.load(blackduck_token)
    blackduck_url = 'https://apus-blackduck.volvocars.biz'

    bearer_token = get_bearer_token(blackduck_url, api_token)
    link_header = create_notice_file(blackduck_url, bearer_token, version)
    download_url = extract_download_url(link_header)

    time.sleep(60) # Wait for the report to be generated
    download_report(download_url, bearer_token, 'license-report.zip')

if __name__ == "__main__":
    main()