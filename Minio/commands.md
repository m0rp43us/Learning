# MC commands

### download mc binary : 
```console
curl https://dl.min.io/client/mc/release/linux-amd64/mc \ --create-dirs \ -o $HOME minio-binaries/mc
```

### address proper rights : 
```console
chmod +x $HOME/minio-binaries/mc export PATH="$PATH:$HOME/minio-binaries/"
```
### create alias : 
```console
mc alias set myminio http://your-minio-server-ip:9000 your_root_user your_root_password
```
### test connection : 
```console
mc admin info myminio
```
### create user : 
```console
mc admin user add <ALIAS> <USERNAME> <PASSWORD>
```
### create bucket : 
```console
mc mb <ALIAS>/<BUCKET-NAME>
```
### add policy file (to add specific policy) : 
```json
	{		
		"Version": "2012-10-17",
		"Statement": [
		{
			"Effect": "Allow",
			"Action": "s3:*",
			"Resource": [
				"arn:aws:s3:::<BUCKET-NAME>/*",
				"arn:aws:s3:::<BUCKET-NAME>"
			]
		}
		]
	}
```
### create the policy in minio : 
```console
mc admin policy create <ALIAS> <POLICY-NAME> policy.json
```
### attach policy : 
```console
mc admin policy attach <ALIAS> <POLICY-NAME> --user <USERNAME>
```