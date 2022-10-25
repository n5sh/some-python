import boto3, datetime


class s3Bucket:
    def __init__(self, bucketName: str) -> None:
        self.bucketName = bucketName

    def createBucket(self):
        try:
            client = boto3.client("s3")
            client.create_bucket(
                ACL="private",
                Bucket=self.bucketName,
                CreateBucketConf={"LocationConstraint": "us-west-1"},
            )
        except Exception as err:
            print(err)
        else:
            print("S3 bucket has been created!")

            
if __name__ == "__main__":
    date = datetime.datetime.now()
    current_time = "{}{}{}".format(date.month, date.day, date.year)
    bucketName = "someNameHere{}".format(current_time)
    s3Obj = s3Bucket(bucketName)
    s3Obj.createBucket()
