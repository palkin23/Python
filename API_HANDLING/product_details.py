
import requests

def fetch_product_details_fromapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_details = data["data"]["data"]

        category = product_details[6]["category"]
        images = product_details[8]["images"]

        return category, images
    else:
        raise Exception("Sorry, failed")


def main():
    try:
        category, images = fetch_product_details_fromapi()
        print(f"Category: {category}\nImages: {images}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()