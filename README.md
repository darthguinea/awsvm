#awsvm
Switch between AWS Credentials, similar to chefvm.

If you have multiple AWS accounts, you can use this to 

#Installation
Download files and place in `~/.awsvm` or desired location, update your .bash_profile and add the path to the profile:
`PATH=$PATH:~/.awsvm`

#Usage:
```
awsvm                   - Lists the accounts in your aws credentials file
awsvm <account>         - Switch the 'default' account to the specified
```
