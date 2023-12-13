# Deep Learning Project - LSTM Demand Forecasting

This is the repository for the Deep Learning semester project at MTSU (CSCI 7850).

## Getting Started

The project is setup as two (2) parts. The first is the `docs` folder which holds the the presentation and paper from this project. The second part is the source code that is under `src`. It holds all the source code used on this project.

### Documents - Paper & Presentation (`docs`)

All the paer details including **LaTex** source code can be found in this folder. In additon to the paper the in-class presentation is avalaible aswell both in `*.pptx` and `*.pdf` file formats.

### Source Code (`src`)
The source code folder (`src`) holds all the code used in this project. There are two (2) parts to this project to demo the deployment of it and how it best works.
1. `App_01_Train_LSTM_Model`: This Jupyter Notebook introduces to the download of the data set from AWS to the local system for processing.
2. `App_02_Test_LSTM_Model`: This Jupyter Notebook introduces the user to first fulling the saved parameter model from the previous step and shows how we can use it to load the model and make predictions into the future. 

## AWS S3 Objects

The data for this project can be retrieved by:

* <https://s3.amazonaws.com/mtsu.csci.7850.project/train.csv>
* <https://s3.amazonaws.com/mtsu.csci.7850.project/lstm-model-2023-12-13.pth>

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
