from urllib import request

url_name = 'https://pubs.vmware.com/vfabric52/topic/com.vmware.vfabric.tc-server.2.8/getting-started/tutwebapp-index-html-file.html'


def download_regular_file(url):
    response = request.urlopen(url)
    fr = response.read()
    fr_str = str(fr)
    fw = open('website.html', 'w')
    lines = str(fr_str).split('\\n')
    for line in lines:
        fw.write(line + "\n")

    fw.close()
    return fw


file = download_regular_file(url_name)
print(file)
