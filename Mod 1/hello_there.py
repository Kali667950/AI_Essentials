import urllib.request

def main():
    print("Hello There")
    url = "https://www.eicar.org/download-anti-malware-testfile/"
    filename = "eicar_testfile.com"
    try:
        print(f"Attempting to download file from {url} ...")
        urllib.request.urlretrieve(url, filename)
        print(f"Download complete. File saved as {filename}")
    except Exception as e:
        print(f"Failed to download the file. Error: {e}")

if __name__ == "__main__":
    main()