# DrowsinessDetectionApp: Drowsiness detection using Ultralytics YOLOv5
A YOLOv5 based custom trained model and a GUI application for real-time drowsiness detection

This app is designed to help prevent accidents by alerting drivers when they become drowsy. By using a real-time detection system with an alarm, drivers can be more alert and responsive, potentially averting dangerous situations.

## Model Details

- **Labels**: Custom trained on `awake` and `drowsy` labels.
- **Dataset**: 20 images collected for each label.
- **Labeling**: Images were labeled using [LabelImg]([https://github.com/HumanSignal/labelImg]) from GitHub.
- **Training**: Model was trained for 420 epochs (roughly 90 minutes).

### Benefits of YOLOv5

- **Efficiency**: The "You Only Look Once" properties allow the model to stride through each box once to estimate the presence of an object.
- **Stability**: The model automatically stores the best and last weights separately for user convenience.
- **Activation Function**: Uses SiLU activation function, which is optimal for object detection.
- **Dataset**: Labels were added to the predefined COCO dataset for training with noise to avoid underfitting.

## Application Features

- **GUI**: Created a Tkinter and CustomTkinter based GUI app.
- **Real-Time Detection**: Uses OpenCV for real-time detection.
- **Count Function**: Displays the number of times a person gets drowsy.
- **Alert System**: Plays a sound whenever drowsiness above 89% is detected to alert the person to awaken and focus.

## Future Plans

- Improve the interface.
- Create an Android app integrated with this trained model.

## Running the App

1. **Download Weights**: Download the weights from the GitHub repository.
2. **Replace Path**: Replace the source path in `App.py` with the path to the downloaded weights.
3. **Run the App**: python App.py

## Training the model with your own data:

1. **Clone the repository**: Clone this repo by running: git clone https://github.com/aaranayaadi/DrowsinessDetectionApp
2. **Open Notebook**: Open the DrowsinessDetector.ipynb file in your code editor with a Python environment set up.
3. **Run Import Cell**: Import necessary modules. (Note: if you aren't able to import the modules, kindly install using "pip install" command in the terminal)
4. **Load Model**: Run the cells in "2. Loading Model".
5. **Collect Images**: Collect 20-30 images each for awake and drowsiness using the OpenCV cell.
6. **Label the images**: 
   -Clone labelImg and install PyQT5
   -open terminal and navigate to cd labelImg
   -run labelImg: "python labelImg.py"
   -Choose the folder where your images are stored and import them. Label each image manually with the labels of awake and drowsy.
7. **Create Dataset**: Create a dataset.yaml file within the YOLOv5 folder and copy the contents from the dataset.yaml on GitHub.
8. **Train Model**:
   -Run the training cell to train the model. Ideal number of epochs is around 500.
   -Training duration depends on your hardware and can take from a few minutes to several hours.
9. **Load Model**: Load the model using the following cell. Replace the path with the path to your model's weights.
10. **Test Model**: Finally, test the model.

## Running the model with your weights:

1. Replace the path to the weights in App.py with your path.
2. open terminal and run: "python App.py"

## License: This project is licensed under the MIT license.
