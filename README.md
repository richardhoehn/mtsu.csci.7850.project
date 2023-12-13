# Deep Learning Project - LSTM Demand Forecasting

This is the repository for the Deep Learning semester project at MTSU (CSCI 7850). This repository holds information regarding the term project that uses the Long-Short Term Memory (LSTM), a deep learning recurrent neural network architecture, to predict real-world sales demand. Predictions were based on the LSTM model which is frequently used to analyze and predict time-series (temporal) regression problems.

The results, presented in this project through various plots, demonstrate that the LSTM’s predictions closely match actual sales trends, indicating its effectiveness in learning demand patterns and forecasting future sales with a degree of accuracy. Since the predicted values follow the true values, one can infer that the model has good and reliable performance.

The paper concludes with the hypothesis that focusing on individual store data might enhance the model’s ability to predict store-specific demand, suggesting a direction for further research.

## Getting Started

The project is setup as two (2) parts. The first is the `docs` folder which holds the the presentation and paper from this project. The second part is the source code that is under `src`. It holds all the source code used on this project.

### Testing the Deployment

In order to test the deployment of this project you will need **Jupyter Notebooks** installed and running Python `3.1.x` on your local system. You can then follow the details in the `/src/..` folder by start at `App_01_Train_LSTM_Model.ipynb` and follow it's markdown comments inside the source file.

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
