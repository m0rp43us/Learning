from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False,
)



print(client.stat_object("asfim", "2014-01-03.xls"))