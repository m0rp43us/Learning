from minio import Minio
from minio.deleteobjects import DeleteObject
from minio.commonconfig import REPLACE, CopySource
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False,
)

#result = client.stat_object("asfim", "2014-01-03.xls")
#print(result)

#result = client.copy_object("asfim", "test/2014-01-03.xls", source=CopySource("asfim", "2014-01-03.xls"))

delete_object_list = map(
    lambda x: DeleteObject(x.object_name),
    client.list_objects("asfim", prefix="test",recursive=True)
)
errors = client.remove_objects("asfim", delete_object_list)
for delete_error in errors:
    # remove_objects returns a generator; iterate to reveal each error
    print(f"Failed to delete {delete_error.object_name}: {delete_error}")