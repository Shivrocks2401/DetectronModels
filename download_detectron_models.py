MODEL_CATALOG = {
    "HJDataset": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/6icw6at8m28a2ho/model_final.pth?dl=1",
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/893paxpy5suvlx9/model_final.pth?dl=1",
        "retinanet_R_50_FPN_3x": "https://www.dropbox.com/s/yxsloxu3djt456i/model_final.pth?dl=1",
    },
    "PubLayNet": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/dgy9c10wykk4lq4/model_final.pth?dl=1",
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/d9fc9tahfzyl6df/model_final.pth?dl=1",
        "mask_rcnn_X_101_32x8d_FPN_3x": "https://www.dropbox.com/s/57zjbwv6gh3srry/model_final.pth?dl=1",
    },
    "PrimaLayout": {
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/h7th27jfv19rxiy/model_final.pth?dl=1"
    },
    "NewspaperNavigator": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/6ewh6g8rqt2ev3a/model_final.pth?dl=1",
    },
    "TableBank": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/8v4uqmz1at9v72a/model_final.pth?dl=1",
        "faster_rcnn_R_101_FPN_3x": "https://www.dropbox.com/s/6vzfk8lk9xvyitg/model_final.pth?dl=1",
    },
    "MFD": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/7xel0i3iqpm2p8y/model_final.pth?dl=1",
    },
}

CONFIG_CATALOG = {
    "HJDataset": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/j4yseny2u0hn22r/config.yml?dl=1",
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/4jmr3xanmxmjcf8/config.yml?dl=1",
        "retinanet_R_50_FPN_3x": "https://www.dropbox.com/s/z8a8ywozuyc5c2x/config.yml?dl=1",
    },
    "PubLayNet": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/f3b12qc4hc0yh4m/config.yml?dl=1",
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/u9wbsfwz4y0ziki/config.yml?dl=1",
        "mask_rcnn_X_101_32x8d_FPN_3x": "https://www.dropbox.com/s/nau5ut6zgthunil/config.yaml?dl=1",
    },
    "PrimaLayout": {
        "mask_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/yc92x97k50abynt/config.yaml?dl=1"
    },
    "NewspaperNavigator": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/wnido8pk4oubyzr/config.yml?dl=1",
    },
    "TableBank": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/7cqle02do7ah7k4/config.yaml?dl=1",
        "faster_rcnn_R_101_FPN_3x": "https://www.dropbox.com/s/h63n6nv51kfl923/config.yaml?dl=1",
    },
    "MFD": {
        "faster_rcnn_R_50_FPN_3x": "https://www.dropbox.com/s/ld9izb95f19369w/config.yaml?dl=1",
    },
}


import os
import requests

# Function to download a file from a given URL
def download_file(url, dest_folder, filename):
    os.makedirs(dest_folder, exist_ok=True)
    file_path = os.path.join(dest_folder, filename)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Iterate over the catalogs and download files
def download_catalog(catalog, file_type):
    for dataset, models in catalog.items():
        for model_name, url in models.items():
            folder_path = os.path.join(dataset, model_name)
            filename = f"model_final.{file_type}" if file_type == "pth" else "config.yaml"
            download_file(url, folder_path, filename)

# Download models and configs
download_catalog(MODEL_CATALOG, "pth")
download_catalog(CONFIG_CATALOG, "yaml")
