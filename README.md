#awsvm
Switch between AWS Credentials, similar to chefvm.

If you have multiple AWS accounts, you can use this to switch between profiles and set the default key.

#Installation:
Download files and place in a folder `~/.awsvm` or other desired location. Update your `.bash_profile` with a updated version of the PATH environment variable to contain the new location of your awsvm script:
`export PATH=$PATH:~/.awsvm`

#Usage:
```
awsvm                   - Lists the accounts in your aws credentials file
awsvm <account>         - Switch the 'default' account to the specified
awsvm -a                - Add a new profile
```

#Examples:
```
~/Programming/awsvm (master)> awsvm
You have the following AWS accounts:
    default             4SCJ0S2YBTYY845FVKNB
    biz1                H0ECYO8IQWQII87NO541
    personalacc         11E2L9J53EP9FB47E5M3
    serverfarm          CCI0TC8WDW290EBI51LI
    *account2           98FAGXLUMNU0131V0JTC


~/Programming/awsvm (master)> awsvm biz1
Using AWS config biz1


~/Programming/awsvm (master)> awsvm
You have the following AWS accounts:
    default             4SCJ0S2YBTYY845FVKNB
    *biz1               H0ECYO8IQWQII87NO541
    personalacc         11E2L9J53EP9FB47E5M3
    serverfarm          CCI0TC8WDW290EBI51LI
    account2            98FAGXLUMNU0131V0JTC
```
