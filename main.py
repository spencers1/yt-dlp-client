import os
import logging
import boto3
from botocore.exceptions import ClientError

from yt_dlp import YoutubeDL

def download_video(video):
    print("video:" + video);
    URL = [video]
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URL)

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    dl_url = os.environ.get('DL_URL')
    file_name = os.environ.get('FILE_NAME')
    s3_bucket = os.environ.get('S3_BUCKET_NAME')
    s3_object = os.environ.get('S3_OBJECT_NAME')

    download_video(dl_url)

    upload_file(file_name, s3_bucket, s3_object)
