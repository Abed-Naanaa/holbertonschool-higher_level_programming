import requests
import csv


# URL: https://jsonplaceholder.typicode.com/posts



def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url)
    print("Status code: {}".format(resp.status_code))
    if resp.status_code != 200:
        print("Error")
        return
    respone_json = resp.json()

    for post in respone_json:
        print(post["title"])
        



def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url)
    print("Status code: {}".format(resp.status_code))
    if resp.status_code != 200:
        print("Error")
        return
    respone_json = resp.json()
    file = open("posts.csv", "w")
    writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
    for post in respone_json:
        new_post = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        writer.writerow(new_post)
