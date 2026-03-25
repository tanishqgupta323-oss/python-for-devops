 you will get list of ARNS of iam users in your account, and then you will use split method to get the username from the ARN and print it out.
 ex- 
 arn="arn:aws:iam::123456789012:user/JohnDoe"
 username=arn.split("/")[-1]
 print(username)
