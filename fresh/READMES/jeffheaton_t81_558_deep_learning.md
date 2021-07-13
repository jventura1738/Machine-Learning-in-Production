# T81 558:Applications of Deep Neural Networks
[Washington University in St. Louis](http://www.wustl.edu)

Instructor: [Jeff Heaton](https://sites.wustl.edu/jeffheaton/)

**The content of this course changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/jeffheaton).

* Section 1. Fall 2021, Monday, 2:30 PM, Online 
* Section 2. Fall 2021, Monday, 6:00 PM, Online

# Course Description

Deep learning is a group of exciting new technologies for neural networks. Through a combination of advanced training techniques and neural network architectural components, it is now possible to create neural networks that can handle tabular data, images, text, and audio as both input and output. Deep learning allows a neural network to learn hierarchies of information in a way that is like the function of the human brain. This course will introduce the student to classic neural network structures, Convolution Neural Networks (CNN), Long Short-Term Memory (LSTM), Gated Recurrent Neural Networks (GRU), General Adversarial Networks (GAN) and reinforcement learning. Application of these architectures to computer vision, time series, security, natural language processing (NLP), and data generation will be covered. High Performance Computing (HPC) aspects will demonstrate how deep learning can be leveraged both on graphical processing units (GPUs), as well as grids. Focus is primarily upon the application of deep learning to problems, with some introduction to mathematical foundations. Students will use the Python programming language to implement deep learning using Google TensorFlow and Keras. It is not necessary to know Python prior to this course; however, familiarity of at least one programming language is assumed. This course will be delivered in a hybrid format that includes both classroom and online instruction.

# Textbook

I am in the process of creating a textbook for this course.  You can find a draft [here](https://arxiv.org/abs/2009.05673). If you would like to cite the material from this course/book, please use the following bibtex citation:

```
@misc{heaton2020applications,
    title={Applications of Deep Neural Networks},
    author={Jeff Heaton},
    year={2020},
    eprint={2009.05673},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

# Objectives

1. Explain how neural networks (deep and otherwise) compare to other machine learning models.
2. Determine when a deep neural network would be a good choice for a particular problem.
3. Demonstrate your understanding of the material through a final project uploaded to GitHub.

# Syllabus
This syllabus presents the expected class schedule, due dates, and reading assignments.  [Download current syllabus.](https://data.heatonresearch.com/wustl/jheaton-t81-558-spring-2021-syllabus.pdf)

Module|Content
---|---
[Module 1](t81_558_class_01_1_overview.ipynb)<br>**Meet on 08/30/2021** | **Module 1: Python Preliminaries**<ul><li>Part 1.1: Course Overview<li>Part 1.2: Introduction to Python<li>Part 1.3: Python Lists, Dictionaries, Sets & JSON<li>Part 1.4: File Handling<li>Part 1.5: Functions, Lambdas, and Map/ReducePython Preliminaries<li>**We will meet on campus this week! (first meeting)** (first online meeting)</ul>
[Module 2](t81_558_class_02_1_python_pandas.ipynb)<br>Week of 09/13/2021 | **Module 2: Python for Machine Learning**<ul><li>	Part 2.1: Introduction to Pandas for Deep Learning<li>Part 2.2: Encoding Categorical Values in Pandas<li>Part 2.3: Grouping, Sorting, and Shuffling<li>Part 2.4: Using Apply and Map in Pandas<li>Part 2.5: Feature Engineering in Padas<li>[Module 1 Program](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class1.ipynb) due: 09/14/2021<li> Icebreaker due: 09/14/2021</ul>
[Module 3](t81_558_class_03_1_neural_net.ipynb)<br>Week of 09/20/2021 | **Module 3: TensorFlow and Keras for Neural Networks**<ul><li>Part 3.1: Deep Learning and Neural Network Introduction<li>Part 3.2: Introduction to Tensorflow & Keras<li>Part 3.3: Saving and Loading a Keras Neural Network<li>Part 3.4: Early Stopping in Keras to Prevent Overfitting<li>Part 3.5: Extracting Keras Weights and Manual Neural Network Calculation<li>[Module 2: Program](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class2.ipynb) due: 09/21/2021</ul>
[Module 4](t81_558_class_04_1_feature_encode.ipynb)<br>Week of 09/27/2021 |**Module 4: Training for Tabular Data**<ul><li>Part 4.1: Encoding a Feature Vector for Keras Deep Learning<li>Part 4.2: Keras Multiclass Classification for Deep Neural Networks with ROC and AUC<li>Part 4.3: Keras Regression for Deep Neural Networks with RMSE<li>Part 4.4: Backpropagation, Nesterov Momentum, and ADAM Training<li>Part 4.5: Neural Network RMSE and Log Loss Error Calculation from Scratch<li>[Module 3 Program](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class3.ipynb) due: 09/28/2021</ul>
[Module 5](t81_558_class_05_1_reg_ridge_lasso.ipynb)<br>**Meet on 10/14/2021** | **Module 5: Regularization and Dropout**<ul><li>Part 5.1: Introduction to Regularization: Ridge and Lasso<li>Part 5.2: Using K-Fold Cross Validation with Keras<li>Part 5.3: Using L1 and L2 Regularization with Keras to Decrease Overfitting<li>Part 5.4: Drop Out for Keras to Decrease Overfitting<li>Part 5.5: Bootstrapping and Benchmarking Hyperparameters<li>[Module 4 Program](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class4.ipynb) due: 10/15/2021<li>**We will meet on campus this week! (second meeting)**</ul>
[Module 6](t81_558_class_06_1_python_images.ipynb)<br>Week of 10/18/2021 | **Module 6: CNN for Vision**<ul>	Part 6.1: Image Processing in Python<li>Part 6.2: Keras Neural Networks for MINST and Fashion MINST<li>Part 6.3: Implementing a ResNet in Keras<li>Part 6.4: Computer Vision with OpenCV<li>Part 6.5: Recognizing Multiple Images with Darknet<li>[Module 5 Program](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class5.ipynb) due: 10/19/2021</ul>
[Module 7](t81_558_class_07_1_gan_intro.ipynb)<br>Week of 10/25/2021 | **Module 7: Generative Adversarial Networks (GANs)**<ul><li>Part 7.1: Introduction to GANS for Image and Data Generation<li>Part 7.2: Implementing a GAN in Keras<li>Part 7.3: Face Generation with StyleGAN and Python<li>Part 7.4: GANS for Semi-Supervised Learning in Keras<li>Part 7.5: An Overview of GAN Research<li>[Module 6 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class6.ipynb) due: 10/26/2021</ul>
[Module 8](t81_558_class_08_1_kaggle_intro.ipynb)<br>**Meet on 11/01/2021** | **Module 8: Kaggle**<ul><li>Part 8.1: Introduction to Kaggle<li>Part 8.2: Building Ensembles with Scikit-Learn and Keras<li>Part 8.3: How Should you Architect Your Keras Neural Network: Hyperparameters<li>Part 8.4: Bayesian Hyperparameter Optimization for Keras<li>Part 8.5: Current Semester's Kaggle<li>[Module 7 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class7.ipynb) due: 11/02/2021<li>**We will meet on campus this week! (third meeting)**</ul>
[Module 9](t81_558_class_09_1_keras_transfer.ipynb)<br>Week of 11/08/2021 | **Module 9: Transfer Learning**<ul><li>Part 9.1: Introduction to Keras Transfer Learning<li>Part 9.2: Popular Pretrained Neural Networks for Keras. <li>Part 9.3: Transfer Learning for Computer Vision and Keras<li>Part 9.4: Transfer Learning for Languages and Keras<li>Part 9.5: Transfer Learning for Keras Feature Engineering<li>[Module 8 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class8.ipynb) due: 11/09/2021</ul>
[Module 10](t81_558_class_10_1_timeseries.ipynb)<br>Week of 11/15/2021 | **Module 10: Time Series in Keras**<ul><li>Part 10.1: Time Series Data Encoding for Deep Learning, TensorFlow and Keras<li>Part 10.2: Programming LSTM with Keras and TensorFlow<li>Part 10.3: Text Generation with Keras and TensorFlow<li>Part 10.4: Image Captioning with Keras and TensorFlow<li>Part 10.5: Temporal CNN in Keras and TensorFlow<li>[Module 9 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class9.ipynb) due: 11/16/2021</ul>
[Module 11](t81_558_class_11_01_spacy.ipynb)<br>Week of 11/22/2021 | **Module 11: Natural Language Processing**<ul><li>Part 11.1: Getting Started with Spacy in Python<li>Part 11.2: Word2Vec and Text Classification<li>Part 11.3: Natural Language Processing with Spacy and Keras<li>Part 11.4: What are Embedding Layers in Keras<li>Part 11.5: Learning English from Scratch with Keras and TensorFlow<li>[Module 10 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class10.ipynb) due: 11/23/2021</ul>
[Module 12](t81_558_class_12_01_ai_gym.ipynb)<br>Week of 11/29/2021 | **Module 12: Reinforcement Learning**<ul><li>Kaggle Assignment due: 11/29/2021 (approx 4-6PM, due to Kaggle GMT timezone)<li>Part 12.1: Introduction to the OpenAI Gym<li>Part 12.2: Introduction to Q-Learning for Keras<li>Part 12.3: Keras Q-Learning in the OpenAI Gym<li>Part 12.4: Atari Games with Keras Neural Networks<li>Part 12.5: Application of Reinforcement Learning</ul>
[Module 13](t81_558_class_13_01_flask.ipynb)<br>**Meet Online on 12/06/2021** | **Module 13: Deployment and Monitoring**<ul><li>Part 13.1: Flask and Deep Learning Web Services <li>Part 13.2: Interrupting and Continuing Training<li>Part 13.3: Using a Keras Deep Neural Network with a Web Application<li>Part 13.4: When to Retrain Your Neural Network<li>Part 13.5: AI at the Edge: Using Keras on a Mobile Device<li>**We will meet on campus this week! (fourth meeting)**</ul>
[Module 14](t81_558_class_14_01_automl.ipynb)<br>Week of 12/13/2021 | **Module 14: Other Neural Network Techniques**<ul><li>Part 14.1: What is AutoML<li>Part 14.2: Using Denoising AutoEncoders in Keras<li>Part 14.3: Training an Intrusion Detection System with KDD99<li>Part 14.4: Anomaly Detection in Keras<li>Part 14.5: New Technology in Deep Learning<li>Final Project due 12/14/2021</ul>

# Datasets

* [Datasets can be downloaded here](https://data.heatonresearch.com/data/t81-558/index.html)

