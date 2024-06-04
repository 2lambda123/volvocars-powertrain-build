"""Script generating and fetching notice report."""

import os
import re
import time
import requests
from ruamel.yaml import YAML
from requests.adapters import HTTPAdapter, Retry

def get_bearer_token(blackduck_url, api_token):
    """Get bearer token for Black Duck API.

    Args:
        blackduck_url (str): Black Duck URL.
        api_token (str): API token.

    Returns:
        str: Bearer token.

    """



    response = requests.post(
        f"{blackduck_url}/api/tokens/authenticate",
        headers={
            'Authorization': f'token {api_token}',
            'Accept': 'application/vnd.blackducksoftware.user-4+json'
        }
    )
    return response.json().get('bearerToken')

def create_notice_file(blackduck_url, bearer_token, version):
    """Create notice file for the given version.

    Args:
        blackduck_url (str): Black Duck URL.
        bearer_token (str): Bearer token.
        version (str): Version ID.

    Returns:
        str: Link header.

    """

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
    """Extract download URL from the link header.

    Args:
        link_header (str): Link header.

    Returns:
        str: Download URL.

    """


    urls = re.findall('<(.*?)>', link_header)
    rels = re.findall('rel="(.*?)"', link_header)
    link_dict = dict(zip(rels, urls))
    return link_dict.get('download')

def download_report(download_url, bearer_token, output_file):
    """Download the notice report.

    Args:
        download_url (str): Download URL.
        bearer_token (str): Bearer token.
        output_file (str): Output file.

    """

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
    with open(output_file, 'wb') as file:
        file.write(response.content)

def main():
    """Main function."""

    yaml = YAML(typ='safe', pure=True)
    report_version = os.getenv("REPORT_VERSION", "")
    version = yaml.load(report_version)
    blackduck_token = os.getenv("BLACKDUCK_TOKEN", "")
    api_token = yaml.load(blackduck_token)
    url = os.getenv("BLACKDUCK_URL", "")
    blackduck_url = yaml.load(url)

    bearer_token = get_bearer_token(blackduck_url, api_token)
    link_header = create_notice_file(blackduck_url, bearer_token, version)
    download_url = extract_download_url(link_header)

    time.sleep(60) # Wait for the report to be generated
    download_report(download_url, bearer_token, 'license-report.zip')

if __name__ == "__main__":
    main()
