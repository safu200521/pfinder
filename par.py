import requests
import os
import re

def check_parameter(urls, value):
    for url in urls:
        try:
            response = requests.get(url)
            match = re.search(f'{value}', response.text)
            if match:
                print(f"\033[92m {url} - {value} Reflects \033[0m")
            else:
                print(f"\033[91m {url} - {value} Does not Reflect \033[0m")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    urls =[]
    print("Enter the url or url file path")
    url_or_file = input()
    if os.path.isfile(url_or_file):
        with open(url_or_file, 'r') as f:
            urls = f.readlines()
    else:
        urls.append(url_or_file)
    print("Enter the parameter value")
    value = input()
    check_parameter(urls, value)
