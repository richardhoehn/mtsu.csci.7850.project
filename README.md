# Deep Learning Project - Demand Forecasting
This is the repository fro the Deep LEarning Semester project at MTSU (CSCI 7850). 

## AWS S3 Objects
The data for this project can be retrieved by:
* https://s3.amazonaws.com/mtsu.csci.7850.project/train.csv
* https://s3.amazonaws.com/mtsu.csci.7850.project/test.csv

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

## Links
* https://machinelearningmastery.com/multi-label-classification-with-deep-learning/
* https://machinelearningmastery.com/update-neural-network-models-with-more-data/