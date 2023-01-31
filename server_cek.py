import requests

def get_webiste_os(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
        response = requests.get(url, headers=headers)
        server = response.headers['Server']
        if "Windows" in server:
            return "Windows"
        elif "Linux" in server:
            return "Linux"
        elif "Unix" in server:
            return "Unix"
        elif "MacOS" in server:
            return "macOS"
        elif "nginx" in server:
            return "nginx"
        elif "Apache Tomcat" in server:
            return "Apache Tomcat"
        elif "IIS" in server:
            return "IIS Internet Information Services"
        elif "Lighttpd" in server:
            return "Lighttpd"
        elif "Caddy" in server:
            return "Caddy"
        elif "Litespeed" in server:
            return "Litespeed"
        elif "WildFly" in server:
            return "WildFly"
        elif "Node.js" in server:
            return "Node.js"
        elif "OpenLiteSpeed" in server:
            return "OpenLiteSpeed"
        else:
            return "Unknown"
    except:
        return None

#target = input("Enter URL : ")
# gunakan http/https
url = "https://liputan6.com"
os_type = get_website_os(url)
if os_type:
    print("Server OS Website " + url, "adalah:" + os_type)
else:
    print("Upss.. Tidak Bisa Menemukan nama server '" + url + "'.")
