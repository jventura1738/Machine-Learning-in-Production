[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<p>
  <a href="https://github.com/emadboctorx/yolov3-keras-tf2/">
  </a>

  <h3 align="center">Yolo (all versions) Real Time Object Detector in tensorflow 2.5</h3>
    .
    <a href="https://github.com/emadboctorx/yolov3-keras-tf2/issues">Report Bug</a>
    ·
    <a href="https://github.com/emadboctorx/yolov3-keras-tf2/issues">Request Feature</a>
  </p>
  
<!-- TODO -->
## **TODO**

* [ ] Transfer learning
* [x] YoloV4 configuration
* [x] YoloV4 training
* [ ] YoloV4 loss function adjustments.
* [ ] Live plot losses
* [x] Command line options
* [x] YoloV3 tiny
* [ ] Rasberry Pi support


<!-- TABLE OF CONTENTS -->
## **Table of Contents**

* [Getting Started](#getting-started)
  * [Installation](#installation)

* [Description](#description)

* [Updates](#updates)

* [Features](#features)
  * [(new) Command line options](#new-command-line-options)
    * [General](#general-options)
    * [Training](#training-options)
    * [Evaluation](#evaluation-options)
    * [Detection](#detection-options)
  * [DarkNet models loaded directly from .cfg files](#darknet-models-loaded-directly-from-cfg-files)
  * [YoloV4 support](#yolov4-support)
  * [tensorflow-2.5--keras-functional-api](#tensorflow-25--keras-functional-api)
  * [cpu-gpu support](#cpu--gpu-support)
  * [Random weights and DarkNet weights support](#random-weights-and-darknet-weights-support)
  * [csv-xml annotation parsers.](#csv-xml-annotation-parsers)
  * [Anchor generator.](#anchor-generation)
  * [matplotlib visualization of all stages.](#matplotlib-visualization-of-all-stages)
  * [tf.data input pipeline.](#tfdata-input-pipeline)
  * [imgaug augmentation pipeline(customizable).](#imgaug-augmentation-pipelinecustomizable)
  * [Logging](#logging)
  * [All-in-1 custom trainer.](#all-in-1-custom-trainer-class)
  * [Stop and resume training support.](#stop-and-resume-training)
  * [Fully vectorized mAP evaluation.](#fully-vectorized-map-evaluation)
  * [labelpix support.](#labelpix-support)
  * [Photo & video detection](#photo--video-detection)

* [Usage](#usage)
  * [Training](#training)
    * [Terminal command](#training-command-line-equivalent)
  * [Augmentation](#augmentation)
  * [Evaluation](#evaluation)
    * [Terminal command](#evaluation-command-line-equivalent)
  * [Detection](#detection)
    * [Terminal command (photos)](#detection-photo-command-line-equivalent)
    * [Terminal command (video)](#detection-video-command-line-equivalent)

* [Contributing](#contributing)
* [Issues](#issue-policy)
  * [What will be addressed](#relevant-issues)
  * [What will not be adressed](#irrelevant-issues)
    
* [License](#license)
* [Show your support](#show-your-support)
* [Contact](#contact)

![GitHub Logo](/samples/detections.png)

<!-- GETTING STARTED -->
## **Getting started**

### **Installation**

1. **Clone the repo**

```sh
git clone https://github.com/emadboctorx/yolo-tf2
```

2. **Install**

```sh
cd yolo-tf2
pip install .
```
3. **Verify installation**

```sh
yolotf2
```

**OUT:**

    Yolo-tf2 1.5
    
    Usage:
        yolotf2 <command> [options] [args]
    
    Available commands:
        train      Create new or use existing dataset and train a model
        evaluate   Evaluate a trained model
        detect     Detect a folder of images or a video

<!-- DESCRIPTION -->
## **Description**

yolo-tf2 was initially an implementation of [yolov3](https://pjreddie.com/darknet/yolo/) 
(you only look once)(training & inference) and support for all yolo versions was added in V1.1

Yolo's original repo is [here](https://github.com/AlexeyAB/darknet) (written in C/C++/Cu).
Yolo is a state-of-the-art, real-time object detection system that is extremely 
fast and accurate. There are many implementations that support tensorflow, only a few that 
support tensorflow v2 and as I did not find versions that suit my needs so, 
I decided to create this version which is very flexible and customizable. 
It requires python 3.8+, is not platform specific and is MIT licensed.

<!-- Updates -->

## **Updates**

### [1.5] - 2021-01-21
- Fix bug that creates out of image bounding boxes after augmentation.
- Fix bug with display commands
- Update dependencies to most recent versions.

### [1.4] - 2020-11-30
- Fix a bug that draws extra irrelevant boxes over photos for V4 configuration
- Fix a bug that causes shape incompatibility issues
- Remove extra required parameters `image_width`, `image_height` which are currently 
measured during runtime.
- Fix a bug that prevents output from saving due to path mishandling
- Unify all IO operations to go through `yolo_tf2.utils.common.get_abs_path()`
- All commands are currently supported from any working directory, so users shouldn't worry
about creating folders and matching names, which is handled automatically.
- Upgrade all dependencies to latest versions 

### [1.3] - 2020-10-20
- Add command line full support for training, evaluation and detection

### [1.2] - 2020-10-18
- Add setup.py, direct installation through python3 setup.py install
- Restructure package folders

### [1.1] - 2020-06-02
- Add yolov4 support

### [1.0] - 2020-05-29

- Models are loaded directly from DarkNet .cfg files
- YoloV4 is currently supported(inference only, no training)
- Mish activation function(YoloV4)

<!-- FEATURES -->

## **Features**

## **(new) Command line options**

### **General options**

| flags                | help                                                              | required   | default       |
|:---------------------|:------------------------------------------------------------------|:-----------|:--------------|
| --input-shape        | Input shape ex: (416, 416, 3)                                     | -          | (416, 416, 3) |
| --classes            | Path to classes .txt file                                         | True       | -             |
| --model-cfg          | Yolo DarkNet configuration .cfg file                              | True       | -             |
| --max-boxes          | Maximum boxes per image                                           | -          | 100           |
| --iou-threshold      | IOU(intersection over union threshold)                            | -          | 0.5           |
| --score-threshold    | Confidence score threshold                                        | -          | 0.5           |
| --workers            | Concurrent tasks(in areas where that is possible)                 | -          | 16            |
| --process-batch-size | Batch size of operations that needs batching (excluding training) | -          | 32            |

### **Training options**

| flags                 | help                                                         | required   | default   |
|:----------------------|:-------------------------------------------------------------|:-----------|:----------|
| --weights             | Path to trained weights .tf or .weights file                 | -          | -         |
| --epochs              | Number of training epochs                                    | -          | 100       |
| --batch-size          | Training batch size                                          | -          | 8         |
| --learning-rate       | Training learning rate                                       | -          | 0.001     |
| --dataset-name        | Name of the checkpoint                                       | True       | -         |
| --test-size           | test dataset relative size (a value between 0 and 1)         | -          | 0.1       |
| --evaluate            | If True, evaluation will be conducted after training         | -          | -         |
| --merge-evaluation    | If False, evaluate training and validation separately        | -          | -         |
| --shuffle-buffer      | Dataset shuffle buffer                                       | -          | 512       |
| --min-overlaps        | a float value between 0 and 1                                | -          | 0.5       |
| --display-stats       | If True, display evaluation statistics                       | -          | -         |
| --plot-stats          | If True, plot results                                        | -          | -         |
| --save-figs           | If True, save plots                                          | -          | -         |
| --clear-output        | If True, clear output folders                                | -          | -         |
| --n-eval              | Evaluate every n epochs                                      | -          | -         |
| --relative-labels     | Path to .csv file that contains                              | -          | -         |
| --voc-conf            | VOC configuration .json file                                 | -          | -         |
| --augmentation-preset | name of augmentation preset                                  | -          | -         |
| --image-folder        | Path to folder that contains images, defaults to data/photos | -          | -         |
| --xml-labels-folder   | Path to folder that contains XML labels                      | -          | -         |
| --train-tfrecord      | Path to training .tfrecord file                              | -          | -         |
| --valid-tfrecord      | Path to validation .tfrecord file                            | -          | -         |

### **Evaluation options**

| flags            | help                              | required   |
|:-----------------|:----------------------------------|:-----------|
| --predicted-data | csv file with predictions         | True       |
| --actual-data    | csv file with actual data         | True       |
| --train-tfrecord | Path to training .tfrecord file   | True       |
| --valid-tfrecord | Path to validation .tfrecord file | True       |

### **Detection options**

| flags         | help                                                     | required   | default   |
|:--------------|:---------------------------------------------------------|:-----------|:----------|
| --image       | Path to an image to predict and draw bounding boxes over | -          | -         |
| --image-dir   | A directory that contains images to predict              | -          | -         |
| --video       | A video to predict                                       | -          | -         |
| --codec       | Codec to use for predicting videos                       | -          | mp4v      |
| --display-vid | Display video during prediction                          | -          | -         |
| --weights     | Path to trained weights .tf or .weights file             | True       | -         |
| --output-dir  | Path to directory for saving results                     | -          | -         |

## **DarkNet models loaded directly from .cfg files**
This feature was introduced to replace the old hard-coded model.
Models are loaded directly from DarkNet .cfg files for convenience.

## **YoloV4 support**
As models currently load from .cfg files directly, all yolo versions including v4 are supported
the configuration file needs to be passed as argument, and the model is loaded.

### **tensorflow 2.5 & keras functional api**

This program leverages features that were introduced in tensorflow 2.x 
including: 

* **Eager execution:** an imperative programming environment that evaluates operations immediately,
 without building graphs check [here](https://www.tensorflow.org/guide/eager)
* **`tf.function`:** A JIT compilation decorator that speeds up some components of the program check [here](https://www.tensorflow.org/api_docs/python/tf/function)
* **`tf.data`:** API for input pipelines check [here](https://www.tensorflow.org/guide/data)

### **CPU & GPU support**

The program detects and uses available GPUs at runtime(training/detection)
if no GPUs available, the CPU will be used(slow).

### **Random weights and DarkNet weights support**

Both options are available, and NOTE in case of using DarkNet [yolov3 weights](https://pjreddie.com/media/files/yolov3.weights)
you must maintain the same number of [COCO classes](https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda) (80 classes)
as transfer learning to models with different classes will be supported in future versions.

### **csv-xml annotation parsers**

There are 2 currently supported formats that the program is able to read and translate to input.

* **XML VOC format which looks like the following example:**


```xml
<annotation>
	<folder>/path/to/image/folder</folder>
	<filename>image_filename.png</filename>
	<path>/path/to/image/folder/image_filename.png</path>
	<size>
		<width>1344</width>
		<height>756</height>
		<depth>3</depth>
	</size>
	<object>
		<name>Car</name>
		<bndbox>
			<xmin>873.0000007680001</xmin>
			<ymin>402.0000001920001</ymin>
			<xmax>1315.00000128</xmax>
			<ymax>697.0000000320001</ymax>
		</bndbox>
	</object>
	<object>
		<name>Car</name>
		<bndbox>
			<xmin>550.999999872</xmin>
			<ymin>404.999999838</ymin>
			<xmax>883.000000512</xmax>
			<ymax>711.000000018</ymax>
		</bndbox>
	</object>
	<object>
		<name>Car</name>
		<bndbox>
			<xmin>8.999999903999992</xmin>
			<ymin>374.999999976</ymin>
			<xmax>525.99999984</xmax>
			<ymax>736.000000344</ymax>
		</bndbox>
	</object>
	<object>
		<name>Traffic Lights</name>
		<bndbox>
			<xmin>857.999999808</xmin>
			<ymin>312.99999960599996</ymin>
			<xmax>903.9999991679999</xmax>
			<ymax>372.99999933</ymax>
		</bndbox>
	</object>
	<object>
		<name>Traffic Lights</name>
		<bndbox>
			<xmin>1220.99999952</xmin>
			<ymin>91.999999854</ymin>
			<xmax>1317.999999456</xmax>
			<ymax>249.99999985799997</ymax>
		</bndbox>
	</object>
	<object>
		<name>Traffic Lights</name>
		<bndbox>
			<xmin>701.999999232</xmin>
			<ymin>207.00000014399998</ymin>
			<xmax>753.999998976</xmax>
			<ymax>275.000000184</ymax>
		</bndbox>
	</object>
	<object>
		<name>Street Sign</name>
		<bndbox>
			<xmin>1220.99999952</xmin>
			<ymin>91.999999854</ymin>
			<xmax>1317.999999456</xmax>
			<ymax>249.99999985799997</ymax>
		</bndbox>
	</object>
	<object>
		<name>Traffic Lights</name>
		<bndbox>
			<xmin>701.999999232</xmin>
			<ymin>207.00000014399998</ymin>
			<xmax>753.999998976</xmax>
			<ymax>275.000000184</ymax>
		</bndbox>
	</object>
		<name>Street Sign</name>
		<bndbox>
			<xmin>798.99999984</xmin>
			<ymin>244.999999944</ymin>
			<xmax>881.00000016</xmax>
			<ymax>275.000000184</ymax>
		</bndbox>
</annotation>
```

* **CSV with relative labels that looks like the following example:**

image | object_name | object_index | bx | by | bw | bh | #
--- | --- | --- | --- |--- |--- |--- |--- 
img1.png | dog | 2 | 0.438616071 | 0.51521164 | 0.079613095	| 0.123015873
img1.png | car | 1 | 0.177827381 | 0.381613757 | 0.044642857 | 0.091269841
img2.png | Street Sign | 5 | 0.674107143 | 0.44047619 | 0.040178571 | 0.084656085

### **Anchor generation**

A [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithm finds the optimal sizes and generates 
anchors with process visualization.

### **matplotlib visualization of all stages**

**Including:**

* **k-means visualization:**

![GitHub Logo](/samples/anchors.png)

* **Generated anchors:**

![GitHub Logo](/samples/anchors_sample.png)

* **Precision and recall curves:**

![GitHub Logo](/samples/pr.png)

* **Evaluation bar charts:**

![GitHub Logo](/samples/map.png)

* **Actual vs. detections:**

![GitHub Logo](/samples/true_false.png)

* **Augmentation visualization:**

Augmentation visualization (before/after) as shown below:

![GitHub Logo](/samples/aug1.png)

* **Dataset pre/post augmentation view with bounding boxes:**

You can always visualize different stages of the program using my other repo 
[labelpix](https://github.com/emadboctorx/labelpix) which is tool for drawing 
bounding boxes, but can also be used to visualize bounding boxes over images using 
csv files in the format mentioned [here](#csv-xml-annotation-parsers).

### **`tf.data` input pipeline**

[TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord) a simple format for storing a sequence 
of binary records. Protocol buffers are a cross-platform, cross-language library for efficient serialization of 
structured data and are used as input pipeline to store and read data efficiently
the program takes as input images and their respective annotations and builds training and validation(optional)
TFRecords to be further used for all operations and TFRecords are also used in the evaluation(mid/post) training,
so it's valid to say you can delete images to free space after conversion to TFRecords.

### **`imgaug` augmentation pipeline(customizable)**

Special thanks to the amazing [imgaug](https://github.com/aleju/imgaug) creators,
an augmentation pipeline(optional) is available and NOTE that the augmentation is
conducted **before** the training not during the training due to technical complications
to integrate tensorflow and imgaug. If you have a small dataset, augmentation is an option
and it can be preconfigured before the training.

### **`logging`**

Different operations are recorded using `logging` module.

### **All-in-1 custom `Trainer` class**

For custom training, `Trainer` class accepts configurations for augmentation, 
new anchor generation, new dataset(TFRecord(s)) creation, mAP evaluation
mid-training and post training. So all you have to do is place images
in data > photos, provide the configuration that suits you and start the training
process, all operations are managed from the same place for convenience.
For detailed instructions.

### **Stop and resume training**

by default the trainer checkpoints to models > checkpoint_name.tf at the end
of each training epoch which enables the training to be resumed at any given 
point by loading the checkpoint which would be the most recent.

### **Fully vectorized mAP evaluation**

Evaluation is optional during the training every n epochs(not recommended for 
large datasets as it predicts every image in the dataset) and one evaluation 
at the end which is optional as well. Training and validation datasets
can be evaluated separately and calculate mAP(mean average precision) as well
as precision and recall curves for every class in the model.

![GitHub Logo](/samples/eval.png)

### **labelpix support**

You can check my other repo [labelpix](https://github.com/emadboctorx/labelpix) which is a
labeling tool for drawing bounding boxes over images if you need to make custom datasets
the tool can help and is supported by the detector. You can use csv files
in the format mentioned [here](#csv-xml-annotation-parsers) as labels and load
images if you need to preview any stage of the training/augmentation/evaluation/detection.

### **Photo & video detection**

Detections can be performed on photos or videos using Detector class.

## **Usage**

### **Training**

**Here are the most basic steps to train using a custom dataset:**

1- Create classes .txt file that contains classes delimited by \n


    dog
    cat
    car
    person
    boat
    fan
    laptop


2- Create a training instance and specify `input_shape`, `classes_file`,
and either specify `image_folder=/path/to/image/folder`
or it would default to `data > photos`
    
    from yolo_tf2.core.trainer import Trainer
    

    trainer = Trainer(
             input_shape=(416, 416, 3),
             model_configuration='yolo_tf2/config/yolo3.cfg',
             classes_file='/path/to/classes_file.txt',
             image_folder=/path/to/image/folder
    )

3- Create dataset configuration(dict) that contains the following keys:

- `dataset_name`: TFRecord prefix(required)

and one of the following:(required)

- `relative_labels`: path to csv file in the following [format](#csv-xml-annotation-parsers)

or

- `xml_labels_folder`: Path to folder containing xml labels (defaults to `data > xml_labels`) 
- `voc_conf`: path to .json file containing VOC parsing configuration (you may use the one
in `yolotf2 > config` or create a similar structure).

and

- `test_size`: percentage of the validation split ex: 0.1(required)
- `augmentation`: `True` (optional)

and if `augmentation` this implies the following:

- `sequences`: (required) A list of augmentation sequences. 
- `aug_workers`: (optional) defaults to 32 parallel augmentations.
- `aug_batch_size`: (optional) this is the augmentation batch size defaults to 64 images to load at once.

      dataset_conf = {
                    'relative_labels': '/path/to/labels.csv',
                    'dataset_name': 'dataset_name',
                    'test_size': 0.2,
                    'sequences': PRESET1,  # check Config > augmentation_options.py
                    'augmentation': True,
      }

4- Create new anchor generation configuration(dict) that contains the following keys(optional):

- `anchor_no`: number of anchors(should be 9)
and one of the following:
    -  `relative_labels`: same as dataset configuration above
    - `xml_labels_folder`: same as dataset configuration above
    
          anchors_conf = {
                          'anchor_no': 9,
                          'relative_labels':  '/path/to/labels.csv'
          }
    - `voc_conf`: should be included if `xml_labels_folder` is specified

5- Start the training

**Note** 

If you're going to use DarkNet yolov3 weights, make sure the classes file
contains 80 classes(COCO classes) or you'll get an error. Transfer learning 
to models with different number of classes will be supported in future versions
of the program.

    trainer.train(
             epochs=100, 
             batch_size=8, 
             learning_rate=1e-3, 
             dataset_name='dataset_name', 
             merge_evaluation=False,
             min_overlaps=0.5,
             new_dataset_conf=dataset_conf,  # check step 5
             new_anchors_conf=anchors_conf,  # check step 6
             #  weights='/path/to/weights'  # If you're using DarkNet weights or resuming training
             )

#### **Training command line equivalent**

    yolotf2 train --input-shape "(416, 416, 3)" --classes "path/to/classes.txt" --model-cfg "yolo_tf2/config/yolo3.cfg" --dataset-name "dataset_name" --relative-labels "path/to/labels.csv"  --epochs 100 --batch-size 8 --learning-rate 1e3 --merge-evaluation --min-overlaps 0.5 --test-size 0.2 --augmentation-preset PRESET1 --image-folder /path/to/image/folder

**Notes**  
- if you're training from outside the repo, specify --image-folder "your image folder"
- To train on an already existing dataset, specify --train-tfrecord and --valid-tfrecord 
- You can specify to parse from xml folder directly using --xml-labels-folder if
outside the repo, otherwise, you might place labels in `data > xml_labels`
- You can specify weights using --weights 
             

After the training completes:

1. The trained model is saved in models folder(which you can use to resume training later/predict photos or videos)
2. The resulting TFRecords and their corresponding csv data are saved in `data > tfrecords`
3. The resulting figures and evaluation results are saved in output folder.
And if you're training from outside the repo, the folders above will be created in
the working directory(if they do not exist)

### **Augmentation**

**Here are the most basic steps to augment images(no training, just augmentation):**

**Note:** Augmentation is supported through `yolotf2 train --augmentation-preset PRESET1`.

If you need to manually augment photos and take your time to examine/visualize the results,
here are the steps:

1- Copy images to data > photos or specify `image_folder=path_tom_image_folder`

2- Ensure you have a csv file containing the labels in the format 
mentioned [here](#csv-xml-annotation-parsers), if you have labels
in xml VOC format, you can easily convert them using utils > annotation_parsers.py` 
`parse_voc_folder()` (everything is explained in the docstrings)

3- Create augmentation instance:

    from yolo_tf2.config.augmentation_options import augmentations
    from yolo_tf2.core.augmentor import DataAugment
    
    
    aug = DataAugment(
          labels_file='/path/to/labels/csv/file',
          augmentation_map=augmentations)
    aug.create_sequences(sequences)  # check the docs
    aug.augment_photo_folder()

After augmentation you'll find augmented images in the data > photos folder
or the folder you specified(if you did specify one) 

And you should find 2 csv files in the output folder: 

1. `augmented_data_plus_original.csv` : you can use this with 
[labelpix](https://github.com/emadboctorx/labelpix) to visualize results with
bounding boxes

2. `adjusted_data_plus_original.csv`

and any of the 2 csv files above can be used in the new dataset configuration
in the training.

## **Evaluation**

Here are the most basic steps to evaluate a trained model:

1. Create an evaluation instance:
       
 
       from yolo_tf2.core.evaluator import Evaluator
       
       
       evaluator = Evaluator(
                   input_shape=(416, 416, 3),
                   model_configuration='yolo_tf2/config/yolo3.cfg',
                   train_tf_record='/path/to/train.tfrecord',
                   valid_tf_record='/path/to/valid.tfrecord',
                   classes_file='/path/to/classes.txt',
                   anchors=anchors,  # defaults to yolov3 anchors
                   score_threshold=0.1  # defaults to 0.5 but it's okay to be lower
                   )
                   
2. Read actual and prediction results(that resulted from the training)

       actual = pd.read_csv('data/tfrecords/full_data.csv')
       preds = pd.read_csv('output/full_dataset_predictions.csv')
       
3. Calculate mAP(mean average precision):

       evaluator.calculate_map(
                  prediction_data=preds, 
                  actual_data=actual, 
                  min_overlaps=0.5, 
                  display_stats=True)
                  
#### **Evaluation command line equivalent**

    yolotf2 evaluate --input-shape "(416, 416, 3)" --model-cfg "yolo_tf2/config/yolo3.cfg" --train-tfrecord "/path/to/train.tfrecord" --valid-tfrecord "/path/to/valid.tfrecord" --score-threshold 0.1 --predicted-data "output/full_dataset_predictions.csv" --actual-data "data/tfrecords/full_data.csv"

After evaluation, you'll find resulting plots and predictions in the output folder.

### **Detection**

Here are the most basic steps to perform detection:

1. Create a detection instance:

        from yolo_tf2.core.detector import Detector
        
        
        detector = Detector(
            input_shape=(416, 416, 3),
            model_configuration='/path/to/DarkNet/yolo_version.cfg,
            classes_file='/path/to/classes_file.txt',
            score_threshold=0.5,
            iou_threshold=0.5,
            max_boxes=100,
            anchors=anchors  # Optional if not specified, yolo default anchors are used
        )
2. Perform detections:

A) Photos:

    photos = ['photo/path1', 'photo/path2']
    detector.predict_photos(photos=photos,
                     trained_weights='/path/to/trained/weights')  # .tf or yolov3.weights(80 classes)

#### **Detection (photo) command line equivalent**

    yolotf2 detect --input-shape "(416, 416, 3)" --classes "path/to/classes.txt" --model-cfg "yolo_tf2/config/yolo3.cfg" --score-threshold 0.5 --iou-threshold 0.5 --image-dir "path/to/image/dir" --weights "path/to/weights"

or alternatively, if you want to perform detection on a single image specify --image instead of --image-dir

B) Video

    detector.detect_video(
        '/path/to/target/vid',
        '/path/to/trained/weights.tf',
    )

#### **Detection (video) command line equivalent**

    yolotf2 detect --input-shape "(416, 416, 3)" --classes "path/to/classes.txt" --model-cfg "yolo_tf2/config/yolo3.cfg" --score-threshold 0.5 --iou-threshold 0.5 --video "path/to/video" --weights "path/to/weights"


After predictions is complete you'll find photos/video
 in output > detections

## **Contributing**

Contributions are what make the open source community such an amazing place to  
learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## **Issue policy**
There are relevant cases in which the issues will be addressed and irrelevant ones that will be closed.

### Relevant issues
The following issues will be addressed.
- Bugs.
- Performance issues.
- Installation issues.
- Documentation issues.
- Feature requests.
- Dependency issues that can be solved.

### Irrelevant issues
The following issues will not be addressed and will be closed.
- Issues without context / clear and concise explanation.
- Issues without standalone code (minimum reproducible example), or a jupyter notebook link to reproduce errors.
- Issues that are improperly formatted.
- Issues that are dataset / label specific without a dataset sample link.
- Issues that are the result of doing something that is unsupported by the existing features.
- Issues that are not considered as improvement / useful.

## **License**

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## **Show your support**

Give a ⭐️ if this project helped you!

## **Contact**

Emad Boctor - emad_1989@hotmail.com

Project link: https://github.com/emadboctorx/yolov3-keras-tf2
                   


[contributors-shield]: https://img.shields.io/github/contributors/emadboctorx/yolov3-keras-tf2?style=flat-square
[contributors-url]: https://github.com/emadboctorx/yolov3-keras-tf2/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/emadboctorx/yolov3-keras-tf2?style=flat-square
[forks-url]: https://github.com/emadboctorx/yolov3-keras-tf2/network/members
[stars-shield]: https://img.shields.io/github/stars/emadboctorx/yolov3-keras-tf2?style=flat-square
[stars-url]: https://github.com/emadboctorx/yolov3-keras-tf2/stargazers
[issues-shield]: https://img.shields.io/github/issues/emadboctorx/yolov3-keras-tf2?style=flat-square
[issues-url]: https://github.com/emadboctorx/yolov3-keras-tf2/issues
[license-shield]: https://img.shields.io/github/license/emadboctorx/yolov3-keras-tf2
[license-url]: https://github.com/emadboctorx/yolov3-keras-tf2/blob/master/LICENSE
