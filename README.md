# Deep Learning Project - Demand Forecasting
This is the repository for the Deep Learning semester project at MTSU (CSCI 7850). I plan on focusing my research and student learning on demand fore- casting using Deep Learning recurrent neural networks (RNNs) in specific the Long Short Term Memory (`LSTM`) and Gate Recurrent Units (`GRU`) architectures. Both the LSTM and GRU models can capture complex temporal dependencies over longer ranges of time and patterns in historical sales data, making them a very good option for demand forecasting tasks.

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