# Deep Learning Project - LSTM Demand Forecasting
This is the repository for the Deep Learning semester project at MTSU (CSCI 7850). 

## Getting Started


## AWS S3 Objects
The data for this project can be retrieved by:
* https://s3.amazonaws.com/mtsu.csci.7850.project/train.csv
* https://s3.amazonaws.com/mtsu.csci.7850.project/lstm-model-2023-12-13.pth

The bucket policy is for `s3:GetObject` objects only. As the following bucket policy setup:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mtsu.csci.7850.project/*"
        }
    ]
}
```