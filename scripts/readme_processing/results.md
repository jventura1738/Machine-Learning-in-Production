# corentinj/real-time-voice-cloning, 0 blocks.

# gamestonkterminal/gamestonkterminal, 21 blocks.

```
conda install -c anaconda git
```

```
cd GamestonkTerminal/
```

```
conda env create -n gst --file build/conda/conda-3-8-env.yaml
```

```
conda activate gst
```

```
poetry install
```

```
pip install -r requirements.txt
```

```
python terminal.py
```

```
ENABLE_PREDICT = os.getenv("GTFF_ENABLE_PREDICT") or True
```

```
poetry install -E prediction
```

```
git pull
```

```
git stash
```

```
git stash pop
```

```
export GT_API_REDDIT_USERNAME=SexyYear
```

```
GT_API_REDDIT_USERNAME=SexyYear
```

```
load -t GME
```

```
view
```

```
load -t GME -s 2020-06-04
```

```
ta
```

```
sma
```

```
sma -h
```

```
sma -l 10
```

# getstream/winds, 21 blocks.

```
DATABASE_URI=mongodb://localhost/WINDS_DEV
CACHE_URI=redis://localhost:6379
JWT_SECRET=YOUR_JWT_SECRET

API_PORT=8080
REACT_APP_API_ENDPOINT=http://localhost:8080
STREAM_API_BASE_URL=https://windspersonalization.getstream.io/personalization/v1.0

STREAM_APP_ID=YOUR_STREAM_APP_ID
REACT_APP_STREAM_APP_ID=YOUR_STREAM_APP_ID
REACT_APP_STREAM_API_KEY=YOUR_STREAM_API_KEY
REACT_APP_STREAM_ANALYTICS=YOUR_STREAM_ANALYTICS_TOKEN
STREAM_API_KEY=YOUR_STREAM_API_KEY
STREAM_API_SECRET=YOUR_STREAM_API_SECRET

REACT_APP_ALGOLIA_APP_ID=YOUR_ALGOLIA_APP_ID
REACT_APP_ALGOLIA_SEARCH_KEY=YOUR_ALGOLIA_SEARCH_ONLY_API_KEY
ALGOLIA_WRITE_KEY=YOUR_ALGOLIA_ADMIN_API_KEY
```

```bash
git clone git@github.com:GetStream/Winds.git
```

```
brew install mongodb
```

```
brew services start mongodb
```

```
brew install redis
```

```
redis-server
```

```
brew services start redis
```

```
STREAM_APP_ID=YOUR_STREAM_APP_ID
STREAM_API_KEY=YOUR_STREAM_API_KEY
STREAM_API_SECRET=YOUR_STREAM_API_SECRET
```

```
REACT_APP_ALGOLIA_APP_ID=YOUR_ALGOLIA_APP_ID
REACT_APP_ALGOLIA_SEARCH_KEY=YOUR_ALGOLIA_SEARCH_ONLY_API_KEY
ALGOLIA_WRITE_KEY=YOUR_ALGOLIA_ADMIN_API_KEY
```

```
pm2 start process_dev.json
```

```
pm2 logs
```

```
cd app && yarn start
```

```
cd api && yarn run test
```

```
cd api && yarn run test_deep
```

```
./api/build.sh
```

```
pm2 start process_prod.json
```

```
winds rss https://techcrunch.com/feed/
```

```
winds podcast https://www.npr.org/rss/podcast.php\?id\=510289
```

```
winds og http://www.planetary.org/multimedia/planetary-radio/show/2018/0509-amy-mainzer-neowise.html
```

```
winds discover mashable.com
```

```
winds article https://alexiskold.net/2018/04/12/meet-12-startups-from-techstars-nyc-winter-2018-program/
```

# julialang/julia, 0 blocks.

# pytorchlightning/pytorch-lightning, 8 blocks.

```bash
pip install pytorch-lightning
```

```bash
  pip install pytorch-lightning['extra']
  ```

  #### Conda

  ```bash
  conda install pytorch-lightning -c conda-forge
  ```

  #### Install stable 1.3.x

  the actual status of 1.3 [stable] is following:

  ![CI base testing](https://github.com/PyTorchLightning/pytorch-lightning/workflows/CI%20base%20testing/badge.svg?branch=release%2F1.3.x&event=push)
  ![CI complete testing](https://github.com/PyTorchLightning/pytorch-lightning/workflows/CI%20complete%20testing/badge.svg?branch=release%2F1.3.x&event=push)
  ![PyTorch & Conda](https://github.com/PyTorchLightning/pytorch-lightning/workflows/PyTorch%20&%20Conda/badge.svg?branch=release%2F1.3.x&event=push)
  ![TPU tests](https://github.com/PyTorchLightning/pytorch-lightning/workflows/TPU%20tests/badge.svg?branch=release%2F1.3.x&event=push)
  ![Docs check](https://github.com/PyTorchLightning/pytorch-lightning/workflows/Docs%20check/badge.svg?branch=release%2F1.3.x&event=push)

  Install future release from the source
  ```bash
  pip install git+https://github.com/PytorchLightning/pytorch-lightning.git@release/1.3.x --upgrade
  ```

  #### Install bleeding-edge - future 1.4

  Install nightly from the source (no guarantees)
  ```bash
  pip install https://github.com/PyTorchLightning/pytorch-lightning/archive/master.zip
  ```

  or from testing PyPI
  ```bash
  pip install -iU https://test.pypi.org/simple/ pytorch-lightning
  ```
</details>
<!-- end skipping PyPI description -->

### Step 1: Add these imports

```

```

### Step 2: Define a LightningModule (nn.Module subclass)
A LightningModule defines a full *system* (ie: a GAN, autoencoder, BERT or a simple Image Classifier).

```

```

**Note: Training_step defines the training loop. Forward defines how the LightningModule behaves during inference/prediction.**

### Step 3: Train!

```

```

## Advanced features
Lightning has over [40+ advanced features](https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html#trainer-flags) designed for professional AI research at scale.

Here are some examples:

<div align="center">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/features_2.jpg" max-height="600px">
</div>

<details>
  <summary>Highlighted feature code snippets</summary>

  ```python
  # 8 GPUs
  # no code changes needed
  trainer = Trainer(max_epochs=1, gpus=8)

  # 256 GPUs
  trainer = Trainer(max_epochs=1, gpus=8, num_nodes=32)
  ```

  <summary>Train on TPUs without code changes</summary>

  ```python
  # no code changes needed
  trainer = Trainer(tpu_cores=8)
   ```

  <summary>16-bit precision</summary>

  ```python
  # no code changes needed
  trainer = Trainer(precision=16)
   ```

  <summary>Experiment managers</summary>

  ```python
  from pytorch_lightning import loggers

  # tensorboard
  trainer = Trainer(logger=TensorBoardLogger('logs/'))

  # weights and biases
  trainer = Trainer(logger=loggers.WandbLogger())

  # comet
  trainer = Trainer(logger=loggers.CometLogger())

  # mlflow
  trainer = Trainer(logger=loggers.MLFlowLogger())

  # neptune
  trainer = Trainer(logger=loggers.NeptuneLogger())

  # ... and dozens more
   ```

  <summary>EarlyStopping</summary>

  ```python
  es = EarlyStopping(monitor='val_loss')
  trainer = Trainer(callbacks=[es])
   ```

  <summary>Checkpointing</summary>

  ```python
  checkpointing = ModelCheckpoint(monitor='val_loss')
  trainer = Trainer(callbacks=[checkpointing])
   ```

  <summary>Export to torchscript (JIT) (production use)</summary>

  ```python
  # torchscript
  autoencoder = LitAutoEncoder()
  torch.jit.save(autoencoder.to_torchscript(), "model.pt")
   ```

  <summary>Export to ONNX (production use)</summary>

  ```python
  # onnx
  with tempfile.NamedTemporaryFile(suffix='.onnx', delete=False) as tmpfile:
      autoencoder = LitAutoEncoder()
      input_sample = torch.randn((1, 64))
      autoencoder.to_onnx(tmpfile.name, input_sample, export_params=True)
      os.path.isfile(tmpfile.name)
   ```
</details>

### Pro-level control of training loops (advanced users)
For complex/professional level work, you have optional full control of the training loop and optimizers.

```

```
---

## Advantages over unstructured PyTorch

* Models become hardware agnostic
* Code is clear to read because engineering code is abstracted away
* Easier to reproduce
* Make fewer mistakes because lightning handles the tricky engineering
* Keeps all the flexibility (LightningModules are still PyTorch modules), but removes a ton of boilerplate
* Lightning has dozens of integrations with popular machine learning tools.
* [Tested rigorously with every new PR](https://github.com/PyTorchLightning/pytorch-lightning/tree/master/tests). We test every combination of PyTorch and Python supported versions, every OS, multi GPUs and even TPUs.
* Minimal running speed overhead (about 300 ms per epoch compared with pure PyTorch).

---

## Examples

###### Hello world
- [MNIST hello world](https://pytorch-lightning.readthedocs.io/en/latest/notebooks/lightning_examples/mnist-hello-world.html)

###### Contrastive Learning
- [BYOL](https://lightning-bolts.readthedocs.io/en/latest/self_supervised_models.html#byol)
- [CPC v2](https://lightning-bolts.readthedocs.io/en/latest/self_supervised_models.html#cpc-v2)
- [Moco v2](https://lightning-bolts.readthedocs.io/en/latest/self_supervised_models.html#moco-v2)
- [SIMCLR](https://lightning-bolts.readthedocs.io/en/latest/self_supervised_models.html#simclr)

###### NLP
- [GPT-2](https://lightning-bolts.readthedocs.io/en/latest/convolutional.html#gpt-2)
- [BERT](https://pytorch-lightning.readthedocs.io/en/latest/notebooks/lightning_examples/text-transformers.html)


###### Reinforcement Learning
- [DQN](https://lightning-bolts.readthedocs.io/en/latest/reinforce_learn.html#dqn-models)
- [Dueling-DQN](https://lightning-bolts.readthedocs.io/en/latest/reinforce_learn.html#dueling-dqn)
- [Reinforce](https://lightning-bolts.readthedocs.io/en/latest/reinforce_learn.html#reinforce)

###### Vision
- [GAN](https://pytorch-lightning.readthedocs.io/en/latest/notebooks/lightning_examples/basic-gan.html)

###### Classic ML
- [Logistic Regression](https://lightning-bolts.readthedocs.io/en/latest/classic_ml.html#logistic-regression)
- [Linear Regression](https://lightning-bolts.readthedocs.io/en/latest/classic_ml.html#linear-regression)

---

## Community

The lightning community is maintained by
- [10+ core contributors](https://pytorch-lightning.readthedocs.io/en/latest/governance.html) who are all a mix of professional engineers, Research Scientists, and Ph.D. students from top AI labs.
- 480+ active community contributors.

Want to help us build Lightning and reduce boilerplate for thousands of researchers? [Learn how to make your first contribution here](https://devblog.pytorchlightning.ai/quick-contribution-guide-86d977171b3a)

Lightning is also part of the [PyTorch ecosystem](https://pytorch.org/ecosystem/) which requires projects to have solid testing, documentation and support.

### Asking for help
If you have any questions please:
1. [Read the docs](https://pytorch-lightning.rtfd.io/en/latest).
2. [Search through existing Discussions](https://github.com/PyTorchLightning/pytorch-lightning/discussions), or [add a new question](https://github.com/PyTorchLightning/pytorch-lightning/discussions/new)
3. [Join our slack](https://join.slack.com/t/pytorch-lightning/shared_invite/zt-pw5v393p-qRaDgEk24~EjiZNBpSQFgQ).
### Funding
[We're venture funded](https://techcrunch.com/2020/10/08/grid-ai-raises-18-6m-series-a-to-help-ai-researchers-and-engineers-bring-their-models-to-production/) to make sure we can provide around the clock support, hire a full-time staff, attend conferences, and move faster through implementing features you request.

---

## Grid AI
Grid AI is our platform for training models at scale on the cloud!

**Sign up for our FREE community Tier [here](https://www.grid.ai/pricing/)**

To use grid, take your regular command:

```

```

And change it to use the grid train command:

```

```

The above command will launch (20 * 4) experiments each running on 4 GPUs (320 GPUs!) - by making ZERO changes to
your code.

---

## Licence

Please observe the Apache 2.0 license that is listed in this repository.
In addition, the Lightning framework is Patent Pending.

## BibTeX
If you want to cite the framework feel free to use this (but only if you loved it 😊) or [zenodo](https://zenodo.org/record/3828935#.YC45Lc9Khqs):

```

# rare-technologies/gensim, 2 blocks.

```bash
    pip install --upgrade gensim
```

```bash
    python setup.py install
```

# aleju/imgaug, 18 blocks.

```bash
conda config --add channels conda-forge
conda install imgaug
```

```bash
pip install imgaug
```

```bash
pip install git+https://github.com/aleju/imgaug.git
```

```python
import numpy as np
import imgaug.augmenters as iaa

def load_batch(batch_idx):
    # dummy function, implement this
    # Return a numpy array of shape (N, height, width, #channels)
    # or a list of (height, width, #channels) arrays (may have different image
    # sizes).
    # Images should be in RGB for colorspace augmentations.
    # (cv2.imread() returns BGR!)
    # Images should usually be in uint8 with values from 0-255.
    return np.zeros((128, 32, 32, 3), dtype=np.uint8) + (batch_idx % 255)

def train_on_images(images):
    # dummy function, implement this
    pass

# Pipeline:
# (1) Crop images from each side by 1-16px, do not resize the results
#     images back to the input size. Keep them at the cropped size.
# (2) Horizontally flip 50% of the images.
# (3) Blur images using a gaussian kernel with sigma between 0.0 and 3.0.
seq = iaa.Sequential([
    iaa.Crop(px=(1, 16), keep_size=False),
    iaa.Fliplr(0.5),
    iaa.GaussianBlur(sigma=(0, 3.0))
])

for batch_idx in range(100):
    images = load_batch(batch_idx)
    images_aug = seq(images=images)  # done by the library
    train_on_images(images_aug)
```

```python
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

# random example images
images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

# Sometimes(0.5, ...) applies the given augmenter in 50% of all cases,
# e.g. Sometimes(0.5, GaussianBlur(0.3)) would blur roughly every second image.
sometimes = lambda aug: iaa.Sometimes(0.5, aug)

# Define our sequence of augmentation steps that will be applied to every image
# All augmenters with per_channel=0.5 will sample one value _per image_
# in 50% of all cases. In all other cases they will sample new values
# _per channel_.

seq = iaa.Sequential(
    [
        # apply the following augmenters to most images
        iaa.Fliplr(0.5), # horizontally flip 50% of all images
        iaa.Flipud(0.2), # vertically flip 20% of all images
        # crop images by -5% to 10% of their height/width
        sometimes(iaa.CropAndPad(
            percent=(-0.05, 0.1),
            pad_mode=ia.ALL,
            pad_cval=(0, 255)
        )),
        sometimes(iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}, # scale images to 80-120% of their size, individually per axis
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, # translate by -20 to +20 percent (per axis)
            rotate=(-45, 45), # rotate by -45 to +45 degrees
            shear=(-16, 16), # shear by -16 to +16 degrees
            order=[0, 1], # use nearest neighbour or bilinear interpolation (fast)
            cval=(0, 255), # if mode is constant, use a cval between 0 and 255
            mode=ia.ALL # use any of scikit-image's warping modes (see 2nd image from the top for examples)
        )),
        # execute 0 to 5 of the following (less important) augmenters per image
        # don't execute all of them, as that would often be way too strong
        iaa.SomeOf((0, 5),
            [
                sometimes(iaa.Superpixels(p_replace=(0, 1.0), n_segments=(20, 200))), # convert images into their superpixel representation
                iaa.OneOf([
                    iaa.GaussianBlur((0, 3.0)), # blur images with a sigma between 0 and 3.0
                    iaa.AverageBlur(k=(2, 7)), # blur image using local means with kernel sizes between 2 and 7
                    iaa.MedianBlur(k=(3, 11)), # blur image using local medians with kernel sizes between 2 and 7
                ]),
                iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), # sharpen images
                iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)), # emboss images
                # search either for all edges or for directed edges,
                # blend the result with the original image using a blobby mask
                iaa.SimplexNoiseAlpha(iaa.OneOf([
                    iaa.EdgeDetect(alpha=(0.5, 1.0)),
                    iaa.DirectedEdgeDetect(alpha=(0.5, 1.0), direction=(0.0, 1.0)),
                ])),
                iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5), # add gaussian noise to images
                iaa.OneOf([
                    iaa.Dropout((0.01, 0.1), per_channel=0.5), # randomly remove up to 10% of the pixels
                    iaa.CoarseDropout((0.03, 0.15), size_percent=(0.02, 0.05), per_channel=0.2),
                ]),
                iaa.Invert(0.05, per_channel=True), # invert color channels
                iaa.Add((-10, 10), per_channel=0.5), # change brightness of images (by -10 to 10 of original value)
                iaa.AddToHueAndSaturation((-20, 20)), # change hue and saturation
                # either change the brightness of the whole image (sometimes
                # per channel) or change the brightness of subareas
                iaa.OneOf([
                    iaa.Multiply((0.5, 1.5), per_channel=0.5),
                    iaa.FrequencyNoiseAlpha(
                        exponent=(-4, 0),
                        first=iaa.Multiply((0.5, 1.5), per_channel=True),
                        second=iaa.LinearContrast((0.5, 2.0))
                    )
                ]),
                iaa.LinearContrast((0.5, 2.0), per_channel=0.5), # improve or worsen the contrast
                iaa.Grayscale(alpha=(0.0, 1.0)),
                sometimes(iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25)), # move pixels locally around (with random strengths)
                sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.05))), # sometimes move parts of the image around
                sometimes(iaa.PerspectiveTransform(scale=(0.01, 0.1)))
            ],
            random_order=True
        )
    ],
    random_order=True
)
images_aug = seq(images=images)
```

```python
import numpy as np
import imgaug.augmenters as iaa

images = np.zeros((2, 128, 128, 3), dtype=np.uint8)  # two example images
images[:, 64, 64, :] = 255
points = [
    [(10.5, 20.5)],  # points on first image
    [(50.5, 50.5), (60.5, 60.5), (70.5, 70.5)]  # points on second image
]

seq = iaa.Sequential([
    iaa.AdditiveGaussianNoise(scale=0.05*255),
    iaa.Affine(translate_px={"x": (1, 5)})
])

# augment keypoints and images
images_aug, points_aug = seq(images=images, keypoints=points)

print("Image 1 center", np.argmax(images_aug[0, 64, 64:64+6, 0]))
print("Image 2 center", np.argmax(images_aug[1, 64, 64:64+6, 0]))
print("Points 1", points_aug[0])
print("Points 2", points_aug[1])
```

```python
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

images = np.zeros((2, 128, 128, 3), dtype=np.uint8)  # two example images
images[:, 64, 64, :] = 255
bbs = [
    [ia.BoundingBox(x1=10.5, y1=15.5, x2=30.5, y2=50.5)],
    [ia.BoundingBox(x1=10.5, y1=20.5, x2=50.5, y2=50.5),
     ia.BoundingBox(x1=40.5, y1=75.5, x2=70.5, y2=100.5)]
]

seq = iaa.Sequential([
    iaa.AdditiveGaussianNoise(scale=0.05*255),
    iaa.Affine(translate_px={"x": (1, 5)})
])

images_aug, bbs_aug = seq(images=images, bounding_boxes=bbs)
```

```python
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

images = np.zeros((2, 128, 128, 3), dtype=np.uint8)  # two example images
images[:, 64, 64, :] = 255
polygons = [
    [ia.Polygon([(10.5, 10.5), (50.5, 10.5), (50.5, 50.5)])],
    [ia.Polygon([(0.0, 64.5), (64.5, 0.0), (128.0, 128.0), (64.5, 128.0)])]
]

seq = iaa.Sequential([
    iaa.AdditiveGaussianNoise(scale=0.05*255),
    iaa.Affine(translate_px={"x": (1, 5)})
])

images_aug, polygons_aug = seq(images=images, polygons=polygons)
```

```python
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

images = np.zeros((2, 128, 128, 3), dtype=np.uint8)  # two example images
images[:, 64, 64, :] = 255
ls = [
    [ia.LineString([(10.5, 10.5), (50.5, 10.5), (50.5, 50.5)])],
    [ia.LineString([(0.0, 64.5), (64.5, 0.0), (128.0, 128.0), (64.5, 128.0),
                    (128.0, 0.0)])]
]

seq = iaa.Sequential([
    iaa.AdditiveGaussianNoise(scale=0.05*255),
    iaa.Affine(translate_px={"x": (1, 5)})
])

images_aug, ls_aug = seq(images=images, line_strings=ls)
```

```python
import numpy as np
import imgaug.augmenters as iaa

# Standard scenario: You have N RGB-images and additionally 21 heatmaps per
# image. You want to augment each image and its heatmaps identically.
images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)
heatmaps = np.random.random(size=(16, 64, 64, 1)).astype(np.float32)

seq = iaa.Sequential([
    iaa.GaussianBlur((0, 3.0)),
    iaa.Affine(translate_px={"x": (-40, 40)}),
    iaa.Crop(px=(0, 10))
])

images_aug, heatmaps_aug = seq(images=images, heatmaps=heatmaps)
```

```python
import numpy as np
import imgaug.augmenters as iaa

# Standard scenario: You have N=16 RGB-images and additionally one segmentation
# map per image. You want to augment each image and its heatmaps identically.
images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)
segmaps = np.random.randint(0, 10, size=(16, 64, 64, 1), dtype=np.int32)

seq = iaa.Sequential([
    iaa.GaussianBlur((0, 3.0)),
    iaa.Affine(translate_px={"x": (-40, 40)}),
    iaa.Crop(px=(0, 10))
])

images_aug, segmaps_aug = seq(images=images, segmentation_maps=segmaps)
```

```python
import numpy as np
import imgaug.augmenters as iaa

images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)
seq = iaa.Sequential([iaa.Fliplr(0.5), iaa.GaussianBlur((0, 3.0))])

# Show an image with 8*8 augmented versions of image 0 and 8*8 augmented
# versions of image 1. Identical augmentations will be applied to
# image 0 and 1.
seq.show_grid([images[0], images[1]], cols=8, rows=8)
```

```python
import numpy as np
import imgaug as ia

image = np.zeros((64, 64, 3), dtype=np.uint8)

# points
kps = [ia.Keypoint(x=10.5, y=20.5), ia.Keypoint(x=60.5, y=60.5)]
kpsoi = ia.KeypointsOnImage(kps, shape=image.shape)
image_with_kps = kpsoi.draw_on_image(image, size=7, color=(0, 0, 255))
ia.imshow(image_with_kps)

# bbs
bbsoi = ia.BoundingBoxesOnImage([
    ia.BoundingBox(x1=10.5, y1=20.5, x2=50.5, y2=30.5)
], shape=image.shape)
image_with_bbs = bbsoi.draw_on_image(image)
image_with_bbs = ia.BoundingBox(
    x1=50.5, y1=10.5, x2=100.5, y2=16.5
).draw_on_image(image_with_bbs, color=(255, 0, 0), size=3)
ia.imshow(image_with_bbs)

# polygons
psoi = ia.PolygonsOnImage([
    ia.Polygon([(10.5, 20.5), (50.5, 30.5), (10.5, 50.5)])
], shape=image.shape)
image_with_polys = psoi.draw_on_image(
    image, alpha_points=0, alpha_face=0.5, color_lines=(255, 0, 0))
ia.imshow(image_with_polys)

# heatmaps
hms = ia.HeatmapsOnImage(np.random.random(size=(32, 32, 1)).astype(np.float32),
                         shape=image.shape)
image_with_hms = hms.draw_on_image(image)
ia.imshow(image_with_hms)
```

```python
from imgaug import augmenters as iaa
import numpy as np

images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

# always horizontally flip each input image
images_aug = iaa.Fliplr(1.0)(images=images)

# vertically flip each input image with 90% probability
images_aug = iaa.Flipud(0.9)(images=images)

# blur 50% of all images using a gaussian kernel with a sigma of 3.0
images_aug = iaa.Sometimes(0.5, iaa.GaussianBlur(3.0))(images=images)
```

```python
import skimage.data
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.batches import UnnormalizedBatch

# Number of batches and batch size for this example
nb_batches = 10
batch_size = 32

# Example augmentation sequence to run in the background
augseq = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.CoarseDropout(p=0.1, size_percent=0.1)
])

# For simplicity, we use the same image here many times
astronaut = skimage.data.astronaut()
astronaut = ia.imresize_single_image(astronaut, (64, 64))

# Make batches out of the example image (here: 10 batches, each 32 times
# the example image)
batches = []
for _ in range(nb_batches):
    batches.append(UnnormalizedBatch(images=[astronaut] * batch_size))

# Show the augmented images.
# Note that augment_batches() returns a generator.
for images_aug in augseq.augment_batches(batches, background=True):
    ia.imshow(ia.draw_grid(images_aug.images_aug, cols=8))
```

```python
import numpy as np
from imgaug import augmenters as iaa
from imgaug import parameters as iap

images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

# Blur by a value sigma which is sampled from a uniform distribution
# of range 10.1 <= x < 13.0.
# The convenience shortcut for this is: GaussianBlur((10.1, 13.0))
blurer = iaa.GaussianBlur(10 + iap.Uniform(0.1, 3.0))
images_aug = blurer(images=images)

# Blur by a value sigma which is sampled from a gaussian distribution
# N(1.0, 0.1), i.e. sample a value that is usually around 1.0.
# Clip the resulting value so that it never gets below 0.1 or above 3.0.
blurer = iaa.GaussianBlur(iap.Clip(iap.Normal(1.0, 0.1), 0.1, 3.0))
images_aug = blurer(images=images)
```

```python
import numpy as np
import imgaug.augmenters as iaa

# fake RGB images
images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

# add a random value from the range (-30, 30) to the first two channels of
# input images (e.g. to the R and G channels)
aug = iaa.WithChannels(
  channels=[0, 1],
  children=iaa.Add((-30, 30))
)

images_aug = aug(images=images)
```

```latex
@misc{imgaug,
  author = {Jung, Alexander B.
            and Wada, Kentaro
            and Crall, Jon
            and Tanaka, Satoshi
            and Graving, Jake
            and Reinders, Christoph
            and Yadav, Sarthak
            and Banerjee, Joy
            and Vecsei, Gábor
            and Kraft, Adam
            and Rui, Zheng
            and Borovec, Jirka
            and Vallentin, Christian
            and Zhydenko, Semen
            and Pfeiffer, Kilian
            and Cook, Ben
            and Fernández, Ismael
            and De Rainville, François-Michel
            and Weng, Chi-Hung
            and Ayala-Acevedo, Abner
            and Meudec, Raphael
            and Laporte, Matias
            and others},
  title = {{imgaug}},
  howpublished = {\url{https://github.com/aleju/imgaug}},
  year = {2020},
  note = {Online; accessed 01-Feb-2020}
}
```

# alex000kim/nsfw_data_scraper, 1 blocks.

```bash
$ docker build . -t docker_nsfw_data_scraper
Sending build context to Docker daemon  426.3MB
Step 1/3 : FROM ubuntu:18.04
 ---> 775349758637
Step 2/3 : RUN apt update  && apt upgrade -y  && apt install wget rsync imagemagick default-jre -y
 ---> Using cache
 ---> b2129908e7e2
Step 3/3 : ENTRYPOINT ["/bin/bash"]
 ---> Using cache
 ---> d32c5ae5235b
Successfully built d32c5ae5235b
Successfully tagged docker_nsfw_data_scraper:latest
$ # Next command might run for several hours. It is recommended to leave it overnight
$ docker run -v $(pwd):/root/nsfw_data_scraper docker_nsfw_data_scraper scripts/runall.sh
Getting images for class: neutral
...
...
$ ls data
test  train
$ ls data/train/
drawings  hentai  neutral  porn  sexy
$ ls data/test/
drawings  hentai  neutral  porn  sexy
```

# amark/gun, 0 blocks.

# bloc97/anime4k, 0 blocks.

# cmusatyalab/openface, 1 blocks.

```
@techreport{amos2016openface,
  title={OpenFace: A general-purpose face recognition
    library with mobile applications},
  author={Amos, Brandon and Bartosz Ludwiczuk and Satyanarayanan, Mahadev},
  year={2016},
  institution={CMU-CS-16-118, CMU School of Computer Science},
}

B. Amos, B. Ludwiczuk, M. Satyanarayanan,
"Openface: A general-purpose face recognition library with mobile applications,"
CMU-CS-16-118, CMU School of Computer Science, Tech. Rep., 2016.
```

# codota/tabnine, 0 blocks.

# d2l-ai/d2l-zh, 1 blocks.

```
@article{zhang2021dive,
    title={Dive into Deep Learning},
    author={Zhang, Aston and Lipton, Zachary C. and Li, Mu and Smola, Alexander J.},
    journal={arXiv preprint arXiv:2106.11342},
    year={2021}
}
```

# deepfakes/faceswap, 0 blocks.

# donnemartin/data-science-ipython-notebooks, 0 blocks.

# eriklindernoren/ml-from-scratch, 0 blocks.

# explosion/spacy, 10 blocks.

```bash
pip install -U pip setuptools wheel
pip install spacy
```

```bash
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install spacy
```

```bash
conda install -c conda-forge spacy
```

```bash
pip install -U spacy
python -m spacy validate
```

```bash
# Download best-matching version of specific model for your spaCy installation
python -m spacy download en_core_web_sm

# pip install .tar.gz archive or .whl from path or URL
pip install /Users/you/en_core_web_sm-3.0.0.tar.gz
pip install /Users/you/en_core_web_sm-3.0.0-py3-none-any.whl
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
```

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
```

```python
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")
```

```bash
git clone https://github.com/explosion/spaCy
cd spaCy

python -m venv .env
source .env/bin/activate

# make sure you are using the latest pip
python -m pip install -U pip setuptools wheel

pip install -r requirements.txt
pip install --no-build-isolation --editable .
```

```bash
pip install --no-build-isolation --editable .[lookups,cuda102]
```

```bash
pip install -r requirements.txt
python -m pytest --pyargs spacy
```

# floodsung/deep-learning-papers-reading-roadmap, 0 blocks.

# google/trax, 11 blocks.

```python
import os
import numpy as np

!pip install -q -U trax
import trax
```

```python
# Create a Transformer model.
# Pre-trained model config in gs://trax-ml/models/translation/ende_wmt32k.gin
model = trax.models.Transformer(
    input_vocab_size=33300,
    d_model=512, d_ff=2048,
    n_heads=8, n_encoder_layers=6, n_decoder_layers=6,
    max_len=2048, mode='predict')

# Initialize using pre-trained weights.
model.init_from_file('gs://trax-ml/models/translation/ende_wmt32k.pkl.gz',
                     weights_only=True)

# Tokenize a sentence.
sentence = 'It is nice to learn new things today!'
tokenized = list(trax.data.tokenize(iter([sentence]),  # Operates on streams.
                                    vocab_dir='gs://trax-ml/vocabs/',
                                    vocab_file='ende_32k.subword'))[0]

# Decode from the Transformer.
tokenized = tokenized[None, :]  # Add batch dimension.
tokenized_translation = trax.supervised.decoding.autoregressive_sample(
    model, tokenized, temperature=0.0)  # Higher temperature: more diverse results.

# De-tokenize,
tokenized_translation = tokenized_translation[0][:-1]  # Remove batch and EOS.
translation = trax.data.detokenize(tokenized_translation,
                                   vocab_dir='gs://trax-ml/vocabs/',
                                   vocab_file='ende_32k.subword')
print(translation)
```

```python
from trax.fastmath import numpy as fastnp
trax.fastmath.use_backend('jax')  # Can be 'jax' or 'tensorflow-numpy'.

matrix  = fastnp.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'matrix = \n{matrix}')
vector = fastnp.ones(3)
print(f'vector = {vector}')
product = fastnp.dot(vector, matrix)
print(f'product = {product}')
tanh = fastnp.tanh(product)
print(f'tanh(product) = {tanh}')
```

```python
def f(x):
  return 2.0 * x * x

grad_f = trax.fastmath.grad(f)

print(f'grad(2x^2) at 1 = {grad_f(1.0)}')
```

```python
class Embedding(base.Layer):
  """Trainable layer that maps discrete tokens/IDs to vectors."""

  def __init__(self,
               vocab_size,
               d_feature,
               kernel_initializer=init.RandomNormalInitializer(1.0)):
    """Returns an embedding layer with given vocabulary size and vector size.

    Args:
      vocab_size: Size of the input vocabulary. The layer will assign a unique
          vector to each ID in `range(vocab_size)`.
      d_feature: Dimensionality/depth of the output vectors.
      kernel_initializer: Function that creates (random) initial vectors for
          the embedding.
    """
    super().__init__(name=f'Embedding_{vocab_size}_{d_feature}')
    self._d_feature = d_feature  # feature dimensionality
    self._vocab_size = vocab_size
    self._kernel_initializer = kernel_initializer

  def forward(self, x):
    """Returns embedding vectors corresponding to input token IDs.

    Args:
      x: Tensor of token IDs.

    Returns:
      Tensor of embedding vectors.
    """
    return jnp.take(self.weights, x, axis=0, mode='clip')

  def init_weights_and_state(self, input_signature):
    """Returns tensor of newly initialized embedding vectors."""
    del input_signature
    shape_w = (self._vocab_size, self._d_feature)
    w = self._kernel_initializer(shape_w, self.rng)
    self.weights = w
```

```python
from trax import layers as tl

# Create an input tensor x.
x = np.arange(15)
print(f'x = {x}')

# Create the embedding layer.
embedding = tl.Embedding(vocab_size=20, d_feature=32)
embedding.init(trax.shapes.signature(x))

# Run the layer -- y = embedding(x).
y = embedding(x)
print(f'shape of y = {y.shape}')
```

```python
model = tl.Serial(
    tl.Embedding(vocab_size=8192, d_feature=256),
    tl.Mean(axis=1),  # Average on axis 1 (length of sentence).
    tl.Dense(2),      # Classify 2 classes.
    tl.LogSoftmax()   # Produce log-probabilities.
)

# You can print model structure.
print(model)
```

```python
train_stream = trax.data.TFDS('imdb_reviews', keys=('text', 'label'), train=True)()
eval_stream = trax.data.TFDS('imdb_reviews', keys=('text', 'label'), train=False)()
print(next(train_stream))  # See one example.
```

```python
data_pipeline = trax.data.Serial(
    trax.data.Tokenize(vocab_file='en_8k.subword', keys=[0]),
    trax.data.Shuffle(),
    trax.data.FilterByLength(max_length=2048, length_keys=[0]),
    trax.data.BucketByLength(boundaries=[  32, 128, 512, 2048],
                             batch_sizes=[256,  64,  16,    4, 1],
                             length_keys=[0]),
    trax.data.AddLossWeights()
  )
train_batches_stream = data_pipeline(train_stream)
eval_batches_stream = data_pipeline(eval_stream)
example_batch = next(train_batches_stream)
print(f'shapes = {[x.shape for x in example_batch]}')  # Check the shapes.
```

```python
from trax.supervised import training

# Training task.
train_task = training.TrainTask(
    labeled_data=train_batches_stream,
    loss_layer=tl.WeightedCategoryCrossEntropy(),
    optimizer=trax.optimizers.Adam(0.01),
    n_steps_per_checkpoint=500,
)

# Evaluaton task.
eval_task = training.EvalTask(
    labeled_data=eval_batches_stream,
    metrics=[tl.WeightedCategoryCrossEntropy(), tl.WeightedCategoryAccuracy()],
    n_eval_batches=20  # For less variance in eval numbers.
)

# Training loop saves checkpoints to output_dir.
output_dir = os.path.expanduser('~/output_dir/')
!rm -rf {output_dir}
training_loop = training.Loop(model,
                              train_task,
                              eval_tasks=[eval_task],
                              output_dir=output_dir)

# Run 2000 steps (batches).
training_loop.run(2000)
```

```python
example_input = next(eval_batches_stream)[0][0]
example_input_str = trax.data.detokenize(example_input, vocab_file='en_8k.subword')
print(f'example input_str: {example_input_str}')
sentiment_log_probs = model(example_input[None, :])  # Add batch dimension.
print(f'Model returned sentiment probabilities: {np.exp(sentiment_log_probs)}')
```

# hanxiao/bert-as-service, 52 blocks.

```bash
pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
```

```bash
bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4 
```

```bash
docker build -t bert-as-service -f ./docker/Dockerfile .
NUM_WORKER=1
PATH_MODEL=/PATH_TO/_YOUR_MODEL/
docker run --runtime nvidia -dit -p 5555:5555 -p 5556:5556 -v $PATH_MODEL:/model -t bert-as-service $NUM_WORKER
```

```python
from bert_serving.client import BertClient
bc = BertClient()
bc.encode(['First do it', 'then do it right', 'then do it better'])
```

```python
bc.encode(['First do it ||| then do it right'])
```

```python
# on another CPU machine
from bert_serving.client import BertClient
bc = BertClient(ip='xx.xx.xx.xx')  # ip address of the GPU machine
bc.encode(['First do it', 'then do it right', 'then do it better'])
```

```bash
bert-serving-start --help
bert-serving-terminate --help
bert-serving-benchmark --help
```

```python
prefix_q = '##### **Q:** '
with open('README.md') as fp:
    questions = [v.replace(prefix_q, '').strip() for v in fp if v.strip() and v.startswith(prefix_q)]
    print('%d questions loaded, avg. len of %d' % (len(questions), np.mean([len(d.split()) for d in questions])))
```

```bash
bert-serving-start -num_worker=1 -model_dir=/data/cips/data/lab/data/model/uncased_L-12_H-768_A-12
```

```python
bc = BertClient(port=4000, port_out=4001)
doc_vecs = bc.encode(questions)
```

```python
while True:
    query = input('your question: ')
    query_vec = bc.encode([query])[0]
    # compute normalized dot product as score
    score = np.sum(query_vec * doc_vecs, axis=1) / np.linalg.norm(doc_vecs, axis=1)
    topk_idx = np.argsort(score)[::-1][:topk]
    for idx in topk_idx:
        print('> %s\t%s' % (score[idx], questions[idx]))
```

```bash
checkpoint                                        128
eval                                              4.0K
eval_results.txt                                  86
eval.tf_record                                    219K
events.out.tfevents.1545202214.TENCENT64.site     6.1M
events.out.tfevents.1545203242.TENCENT64.site     14M
graph.pbtxt                                       9.0M
model.ckpt-0.data-00000-of-00001                  1.3G
model.ckpt-0.index                                23K
model.ckpt-0.meta                                 3.9M
model.ckpt-343.data-00000-of-00001                1.3G
model.ckpt-343.index                              23K
model.ckpt-343.meta                               3.9M
train.tf_record                                   2.0M
```

```bash
bert-serving-start -model_dir=/pretrained/uncased_L-12_H-768_A-12 -tuned_model_dir=/tmp/mrpc_output/ -ckpt_name=model.ckpt-343
```

```text
I:GRAPHOPT:[gra:opt: 50]:checkpoint (override by fine-tuned model): /tmp/mrpc_output/model.ckpt-343
```

```bash
bert-serving-start -pooling_strategy NONE -model_dir /tmp/english_L-12_H-768_A-12/
```

```python
# max_seq_len = 25
# pooling_strategy = NONE

bc = BertClient()
vec = bc.encode(['hey you', 'whats up?'])

vec  # [2, 25, 768]
vec[0]  # [1, 25, 768], sentence embeddings for `hey you`
vec[0][0]  # [1, 1, 768], word embedding for `[CLS]`
vec[0][1]  # [1, 1, 768], word embedding for `hey`
vec[0][2]  # [1, 1, 768], word embedding for `you`
vec[0][3]  # [1, 1, 768], word embedding for `[SEP]`
vec[0][4]  # [1, 1, 768], word embedding for padding symbol
vec[0][25]  # error, out of index!
```

```python
texts = ['hello world!', 'good day']

# a naive whitespace tokenizer
texts2 = [s.split() for s in texts]

vecs = bc.encode(texts2, is_tokenized=True)
```

```python
bc.encode(['hello world!', 'thisis it'], show_tokens=True)
```

```text
(array([[[ 0.        , -0.        ,  0.        , ...,  0.        , -0.        , -0.        ],
        [ 1.1100919 , -0.20474958,  0.9895898 , ...,  0.3873255  , -1.4093989 , -0.47620595],
        ..., -0.        , -0.        ]],

       [[ 0.        , -0.        ,  0.        , ...,  0.        , 0.        ,  0.        ],
        [ 0.6293478 , -0.4088499 ,  0.6022662 , ...,  0.41740108, 1.214456  ,  1.2532915 ],
        ..., 0.        ,  0.        ]]], dtype=float32),
         
          [['[CLS]', 'hello', 'world', '!', '[SEP]'], ['[CLS]', 'this', '##is', 'it', '[SEP]']])
```

```python
bc.encode([['hello', 'world!'], ['thisis', 'it']], show_tokens=True, is_tokenized=True)
```

```text
(array([[[ 0.        , -0.        ,  0.        , ...,  0.       ,  -0.        ,  0.        ],
        [ 1.1111546 , -0.56572634,  0.37183186, ...,  0.02397121,  -0.5445367 ,  1.1009651 ],
        ..., -0.        ,  0.        ]],

       [[ 0.        ,  0.        ,  0.        , ...,  0.        ,  -0.        ,  0.        ],
        [ 0.39262453,  0.3782491 ,  0.27096173, ...,  0.7122045 ,  -0.9874849 ,  0.9318679 ],
        ..., -0.        ,  0.        ]]], dtype=float32),
         
         [['[CLS]', 'hello', '[UNK]', '[SEP]'], ['[CLS]', '[UNK]', 'it', '[SEP]']])
```

```python
batch_size = 256
num_parallel_calls = 4
num_clients = num_parallel_calls * 2  # should be at least greater than `num_parallel_calls`

# start a pool of clients
bc_clients = [BertClient(show_server_config=False) for _ in range(num_clients)]


def get_encodes(x):
    # x is `batch_size` of lines, each of which is a json object
    samples = [json.loads(l) for l in x]
    text = [s['raw_text'] for s in samples]  # List[List[str]]
    labels = [s['label'] for s in samples]  # List[str]
    # get a client from available clients
    bc_client = bc_clients.pop()
    features = bc_client.encode(text)
    # after use, put it back
    bc_clients.append(bc_client)
    return features, labels


ds = (tf.data.TextLineDataset(train_fp).batch(batch_size)
        .map(lambda x: tf.py_func(get_encodes, [x], [tf.float32, tf.string]),  num_parallel_calls=num_parallel_calls)
        .map(lambda x, y: {'feature': x, 'label': y})
        .make_one_shot_iterator().get_next())
```

```python
estimator = DNNClassifier(
    hidden_units=[512],
    feature_columns=[tf.feature_column.numeric_column('feature', shape=(768,))],
    n_classes=len(laws),
    config=run_config,
    label_vocabulary=laws_str,
    dropout=0.1)

input_fn = lambda fp: (tf.data.TextLineDataset(fp)
                       .apply(tf.contrib.data.shuffle_and_repeat(buffer_size=10000))
                       .batch(batch_size)
                       .map(lambda x: tf.py_func(get_encodes, [x], [tf.float32, tf.string]), num_parallel_calls=num_parallel_calls)
                       .map(lambda x, y: ({'feature': x}, y))
                       .prefetch(20))

train_spec = TrainSpec(input_fn=lambda: input_fn(train_fp))
eval_spec = EvalSpec(input_fn=lambda: input_fn(eval_fp), throttle_secs=0)
train_and_evaluate(estimator, train_spec, eval_spec)
```

```python
bc = BertClient()
list_vec = bc.encode(lst_str)
list_label = [0 for _ in lst_str]  # a dummy list of all-zero labels

# write to tfrecord
with tf.python_io.TFRecordWriter('tmp.tfrecord') as writer:
    def create_float_feature(values):
        return tf.train.Feature(float_list=tf.train.FloatList(value=values))

    def create_int_feature(values):
        return tf.train.Feature(int64_list=tf.train.Int64List(value=list(values)))

    for (vec, label) in zip(list_vec, list_label):
        features = {'features': create_float_feature(vec), 'labels': create_int_feature([label])}
        tf_example = tf.train.Example(features=tf.train.Features(feature=features))
        writer.write(tf_example.SerializeToString())
```

```python
def _decode_record(record):
    """Decodes a record to a TensorFlow example."""
    return tf.parse_single_example(record, {
        'features': tf.FixedLenFeature([768], tf.float32),
        'labels': tf.FixedLenFeature([], tf.int64),
    })

ds = (tf.data.TFRecordDataset('tmp.tfrecord').repeat().shuffle(buffer_size=100).apply(
    tf.contrib.data.map_and_batch(lambda record: _decode_record(record), batch_size=64))
      .make_one_shot_iterator().get_next())
```

```python
def create_float_feature(values):
    return tf.train.Feature(float_list=tf.train.FloatList(value=values.reshape(-1)))
```

```python
name_to_features = {
    "feature": tf.FixedLenFeature([max_seq_length * num_hidden], tf.float32),
    "label_ids": tf.FixedLenFeature([], tf.int64),
}
    
def _decode_record(record, name_to_features):
    """Decodes a record to a TensorFlow example."""
    example = tf.parse_single_example(record, name_to_features)
    example['feature'] = tf.reshape(example['feature'], [max_seq_length, -1])
    return example
```

```python
# an endless data stream, generating data in an extremely fast speed
def text_gen():
    while True:
        yield lst_str  # yield a batch of text lines

bc = BertClient()

# get encoded vectors
for j in bc.encode_async(text_gen(), max_num_batch=10):
    print('received %d x %d' % (j.shape[0], j.shape[1]))
```

```python
# clone a client by reusing the identity 
def client_clone(id, idx):
    bc = BertClient(identity=id)
    for j in bc.listen():
        print('clone-client-%d: received %d x %d' % (idx, j.shape[0], j.shape[1]))

bc = BertClient()
# start two cloned clients sharing the same identity as bc
for j in range(2):
    threading.Thread(target=client_clone, args=(bc.identity, j)).start()

for _ in range(3):
    bc.encode(lst_str)
```

```python
bc = BertClient(ip='server_ip')

json.dumps(bc.server_status, ensure_ascii=False)
```

```bash
bert-serving-start -http_port 8081 -model_dir ...
```

```bash
pip install -U bert-serving-server[http]
```

```bash
bert-serving-start -model_dir=/YOUR_MODEL -http_port 8125
```

```json
{
    "id": 123,
    "texts": ["hello world", "good day!"],
    "is_tokenized": false
}
```

```bash
curl -X POST http://xx.xx.xx.xx:8125/encode \
  -H 'content-type: application/json' \
  -d '{"id": 123,"texts": ["hello world"], "is_tokenized": false}'
```

```json
{
    "id": 123,
    "results": [[768 float-list], [768 float-list]],
    "status": 200
}
```

```python
from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
args = get_args_parser().parse_args(['-model_dir', 'YOUR_MODEL_PATH_HERE',
                                     '-port', '5555',
                                     '-port_out', '5556',
                                     '-max_seq_len', 'NONE',
                                     '-mask_cls_sep',
                                     '-cpu'])
server = BertServer(args)
server.start()
```

```python
BertServer.shutdown(port=5555)
```

```bash
bert-serving-terminate -port 5555
```

```bash
bert-serving-start -pooling_layer -4 -3 -2 -1 -model_dir /tmp/english_L-12_H-768_A-12/
```

```python
bc.encode(['hey you', 'whats up?', '你好么？', '我 还 可以'])
```

```
tokens: [CLS] hey you [SEP]
input_ids: 101 13153 8357 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
input_mask: 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

tokens: [CLS] what ##s up ? [SEP]
input_ids: 101 9100 8118 8644 136 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
input_mask: 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

tokens: [CLS] 你 好 么 ？ [SEP]
input_ids: 101 872 1962 720 8043 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
input_mask: 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

tokens: [CLS] 我 还 可 以 [SEP]
input_ids: 101 2769 6820 1377 809 102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
input_mask: 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

```python
input = "unaffable"
tokenizer_output = ["un", "##aff", "##able"]
```

```python
# BAD example
bc = BertClient()

# in Proc1/Thread1 scope:
bc.encode(lst_str)

# in Proc2/Thread2 scope:
bc.encode(lst_str)
```

```python
# in Proc1/Thread1 scope:
bc1 = BertClient()
bc1.encode(lst_str)

# in Proc2/Thread2 scope:
bc2 = BertClient()
bc2.encode(lst_str)
```

```
if cosine(A, B) > 0.9, then A and B are similar
```

```
if cosine(A, B) > cosine(A, C), then A is more similar to B than C.
```

```bash
bert-serving-start -device_map 0 1 4 -num_worker 4 -model_dir ...
```

```bash
bert-serving-benchmark --help
```

```python
# prepare your sent in advance
bc = BertClient()
my_sentences = [s for s in my_corpus.iter()]
# doing encoding in one-shot
vec = bc.encode(my_sentences)
```

```python
bc = BertClient()
vec = []
for s in my_corpus.iter():
    vec.append(bc.encode(s))
```

```latex
@misc{xiao2018bertservice,
  title={bert-as-service},
  author={Xiao, Han},
  howpublished={\url{https://github.com/hanxiao/bert-as-service}},
  year={2018}
}
```

# hindupuravinash/the-gan-zoo, 0 blocks.

# interpretml/interpret, 5 blocks.

```sh
pip install interpret
```

```python
from interpret.glassbox import ExplainableBoostingClassifier

ebm = ExplainableBoostingClassifier()
ebm.fit(X_train, y_train)

# or substitute with LogisticRegression, DecisionTreeClassifier, RuleListClassifier, ...
# EBM supports pandas dataframes, numpy arrays, and handles "string" data natively.
```

```python
from interpret import show

ebm_global = ebm.explain_global()
show(ebm_global)
```

```python
ebm_local = ebm.explain_local(X_test, y_test)
show(ebm_local)
```

```python
show([logistic_regression_global, decision_tree_global])
```

# iterative/dvc, 0 blocks.

# jackzhenguo/python-small-examples, 95 blocks.

```python
import smtplib
from email import (header)
from email.mime import (text, application, multipart)
import time

def sender_mail():
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    sender, password = '113097485@qq.com', "**************"
    smt_p.login(sender, password)
    receiver_addresses, count_num = [
        'guozhennianhua@163.com', 'xiaoxiazi99@163.com'], 1
    for email_address in receiver_addresses:
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = "zhenguo"
            msg['To'] = email_address
            msg['subject'] = header.Header('这是邮件主题通知', 'utf-8')
            msg.attach(text.MIMEText(
                '这是一封测试邮件，请勿回复本邮件~', 'plain', 'utf-8'))
            smt_p.sendmail(sender, email_address, msg.as_string())
            time.sleep(10)
            print('第%d次发送给%s' % (count_num, email_address))
            count_num = count_num + 1
        except Exception as e:
            print('第%d次给%s发送邮件异常' % (count_num, email_address))
            continue
    smt_p.quit()

sender_mail()
```

```python
def binarySearch(arr, left, right, x):
    while left <= right:

        mid = int(left + (right - left) / 2); # 找到中间位置。求中点写成(left+right)/2更容易溢出，所以不建议这样写

        # 检查x是否出现在位置mid
        if arr[mid] == x:
            print('found %d 在索引位置%d 处' %(x,mid))
            return mid

            # 假如x更大，则不可能出现在左半部分
        elif arr[mid] < x:
            left = mid + 1 #搜索区间变为[mid+1,right]
            print('区间缩小为[%d,%d]' %(mid+1,right))

        # 同理，假如x更小，则不可能出现在右半部分
        elif x<arr[mid]:
            right = mid - 1 #搜索区间变为[left,mid-1]
            print('区间缩小为[%d,%d]' %(left,mid-1))

    # 假如搜索到这里，表明x未出现在[left,right]中
    return -1
```

```python
In [8]: binarySearch([4,5,6,7,10,20,100],0,6,5)
区间缩小为[0,2]
found 5 at 1
Out[8]: 1

In [9]: binarySearch([4,5,6,7,10,20,100],0,6,4)
区间缩小为[0,2]
区间缩小为[0,0]
found 4 at 0
Out[9]: 0

In [10]: binarySearch([4,5,6,7,10,20,100],0,6,20)
区间缩小为[4,6]
found 20 at 5
Out[10]: 5

In [11]: binarySearch([4,5,6,7,10,20,100],0,6,100)
区间缩小为[4,6]
区间缩小为[6,6]
found 100 at 6
Out[11]: 6
```

```python
import requests
from lxml import etree
import pandas as pd
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml#input'
with requests.get(url) as res:
    content = res.content
    html = etree.HTML(content)
```

```python
location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
```

```python
['香河', '涿州', '唐山', '沧州', '天津', '廊坊', '太原', '石家庄', '涿鹿', '张家口', '保定', '三河', '北京孔庙', '北京国子监', '中国地质博物馆', '月坛公
园', '明城墙遗址公园', '北京市规划展览馆', '什刹海', '南锣鼓巷', '天坛公园', '北海公园', '景山公园', '北京海洋馆']

['11/-5°C', '14/-5°C', '12/-6°C', '12/-5°C', '11/-1°C', '11/-5°C', '8/-7°C', '13/-2°C', '8/-6°C', '5/-9°C', '14/-6°C', '11/-4°C', '13/-3°C'
, '13/-3°C', '12/-3°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-2°C', '12/-2°C', '12/-3°C']
```

```python
df = pd.DataFrame({'location':location, 'temperature':temperature})
print('温度列')
print(df['temperature'])
```

```python
df['high'] = df['temperature'].apply(lambda x: int(re.match('(-?[0-9]*?)/-?[0-9]*?°C', x).group(1) ) )
df['low'] = df['temperature'].apply(lambda x: int(re.match('-?[0-9]*?/(-?[0-9]*?)°C', x).group(1) ) )
print(df)
```

```python
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 010-12345
# 010
# 12345
```

```kepython
Name: temperature, dtype: object
    location temperature  high  low
0         香河     11/-5°C    11   -5
1         涿州     14/-5°C    14   -5
2         唐山     12/-6°C    12   -6
3         沧州     12/-5°C    12   -5
4         天津     11/-1°C    11   -1
5         廊坊     11/-5°C    11   -5
6         太原      8/-7°C     8   -7
7        石家庄     13/-2°C    13   -2
8         涿鹿      8/-6°C     8   -6
9        张家口      5/-9°C     5   -9
10        保定     14/-6°C    14   -6
11        三河     11/-4°C    11   -4
12      北京孔庙     13/-3°C    13   -3
13     北京国子监     13/-3°C    13   -3
14   中国地质博物馆     12/-3°C    12   -3
15      月坛公园     12/-3°C    12   -3
16   明城墙遗址公园     13/-3°C    13   -3
17  北京市规划展览馆     12/-2°C    12   -2
18       什刹海     12/-3°C    12   -3
19      南锣鼓巷     13/-3°C    13   -3
20      天坛公园     12/-2°C    12   -2
21      北海公园     12/-2°C    12   -2
22      景山公园     12/-2°C    12   -2
23     北京海洋馆     12/-3°C    12   -3
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Bar,Grid,Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType
```

```python
Out[89]:
        a  val
0  apple1  1.0
1  apple2  2.0
2  apple3  3.0
3  apple4  4.0
4  apple5  5.0
```

```python
a  apple1  apple2  apple3  apple4  apple5
0     1.0     2.0     3.0     4.0     5.0
```

```python
In [113]: pd.DataFrame(index=[0],columns=df.a,data=dict(zip(df.a,df.val)))
Out[113]:
a  apple1  apple2  apple3  apple4  apple5
0     1.0     2.0     3.0     4.0     5.0
```

```python
In [116]: dict(zip(df.a,df.val))
Out[116]: {'apple1': 1.0, 'apple2': 2.0, 'apple3': 3.0, 'apple4': 4.0, 'apple5': 5.0}
```

```python
import pandas as pd

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::', engine='python', header=None, names = ['Movie ID', 'Movie Title', 'Genre'])
```

```python
   Movie ID                                        Movie Title  \
0         8      Edison Kinetoscopic Record of a Sneeze (1894)   
1        10                La sortie des usines Lumi猫re (1895)   
2        12                      The Arrival of a Train (1896)   
3        25  The Oxford and Cambridge University Boat Race ...   
4        91                         Le manoir du diable (1896)   
5       131                           Une nuit terrible (1896)   
6       417                      Le voyage dans la lune (1902)   
7       439                     The Great Train Robbery (1903)   
8       443        Hiawatha, the Messiah of the Ojibway (1903)   
9       628                    The Adventures of Dollie (1908)  
                                          Genre  
0                             Documentary|Short  
1                             Documentary|Short  
2                             Documentary|Short  
3                                           NaN  
4                                  Short|Horror  
5                           Short|Comedy|Horror  
6  Short|Action|Adventure|Comedy|Fantasy|Sci-Fi  
7                    Short|Action|Crime|Western  
8                                           NaN  
9                                  Action|Short  
```

```python
users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Twitter ID'])
print(users.head())
```

```python
   User ID  Twitter ID
0        1   397291295
1        2    40501255
2        3   417333257
3        4   138805259
4        5  2452094989
5        6   391774225
6        7    47317010
7        8    84541461
8        9  2445803544
9       10   995885060
```

```python
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])
print(ratings.head())
```

```python
   User ID  Movie ID  Rating  Rating Timestamp
0        1    111161      10        1373234211
1        1    117060       7        1373415231
2        1    120755       6        1373424360
3        1    317919       6        1373495763
4        1    454876      10        1373621125
5        1    790724       8        1374641320
6        1    882977       8        1372898763
7        1   1229238       9        1373506523
8        1   1288558       5        1373154354
9        1   1300854       8        1377165712
```

```python
import pandas as pd

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::', engine='python', header=None, names = ['Movie ID', 'Movie Title', 'Genre'])
users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Twitter ID'])
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python', header=None, names = ['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])
```

```python
mask = movies.Genre.str.contains('comedy',case=False,na=False)
```

```python
0    False
1    False
2    False
3    False
4    False
5     True
6     True
7    False
8    False
9    False
Name: Genre, dtype: bool

```

```python
comedy = movies[mask]
comdey_ids = comedy['Movie ID']

```

```python
5      131
6      417
15    2354
18    3863
19    4099
20    4100
21    4101
22    4210
23    4395
25    4518
Name: Movie ID, dtype: int64

```

```python
5      131
6      417
15    2354
18    3863
19    4099
20    4100
21    4101
22    4210
23    4395
25    4518
Name: Movie ID, dtype: int64

```

```python
   User ID  Movie ID  Rating  Rating Timestamp
0        1    111161      10        1373234211
1        1    117060       7        1373415231
2        1    120755       6        1373424360
3        1    317919       6        1373495763
4        1    454876      10        1373621125
5        1    790724       8        1374641320
6        1    882977       8        1372898763
7        1   1229238       9        1373506523
8        1   1288558       5        1373154354
9        1   1300854       8        1377165712

```

```python
combine = ratings.join(comedy, on='Movie ID', rsuffix='2')

```

```python
combine = ratings.join(comedy.set_index('Movie ID'), on='Movie ID')
print(combine.head(10))

```

```python
   User ID  Movie ID  Rating  Rating Timestamp Movie Title Genre
0        1    111161      10        1373234211         NaN   NaN
1        1    117060       7        1373415231         NaN   NaN
2        1    120755       6        1373424360         NaN   NaN
3        1    317919       6        1373495763         NaN   NaN
4        1    454876      10        1373621125         NaN   NaN
5        1    790724       8        1374641320         NaN   NaN
6        1    882977       8        1372898763         NaN   NaN
7        1   1229238       9        1373506523         NaN   NaN
8        1   1288558       5        1373154354         NaN   NaN
9        1   1300854       8        1377165712         NaN   NaN

```

```python
mask = pd.notnull(combine['Genre'])

```

```python
result = combine[mask]
print(result.head())

```

```python
    User ID  Movie ID  Rating  Rating Timestamp             Movie Title  \
12        1   1588173       9        1372821281      Warm Bodies (2013)   
13        1   1711425       3        1372604878        21 & Over (2013)   
14        1   2024432       8        1372703553   Identity Thief (2013)   
17        1   2101441       1        1372633473  Spring Breakers (2012)   
28        2   1431045       7        1457733508         Deadpool (2016)   

                             Genre  
12           Comedy|Horror|Romance  
13                          Comedy  
14    Adventure|Comedy|Crime|Drama  
17              Comedy|Crime|Drama  
28  Action|Adventure|Comedy|Sci-Fi  


```

```python
    User ID  Movie ID  Rating  Rating Timestamp             Movie Title  \
12        1   1588173       9        1372821281      Warm Bodies (2013)   
13        1   1711425       3        1372604878        21 & Over (2013)   
14        1   2024432       8        1372703553   Identity Thief (2013)   
17        1   2101441       1        1372633473  Spring Breakers (2012)   
28        2   1431045       7        1457733508         Deadpool (2016)   

                             Genre  
12           Comedy|Horror|Romance  
13                          Comedy  
14    Adventure|Comedy|Crime|Drama  
17              Comedy|Crime|Drama  
28  Action|Adventure|Comedy|Sci-Fi  
```

```python
score_as_movie = result.groupby('Movie ID').mean()
```

```python
               User ID  Rating  Rating Timestamp
Movie ID                                        
131       34861.000000     7.0      1.540639e+09
417       34121.409091     8.5      1.458680e+09
2354       6264.000000     8.0      1.456343e+09
3863      43803.000000    10.0      1.430439e+09
4099      25084.500000     7.0      1.450323e+09
```

```python
score_as_movie.sort_values(by='Rating', ascending = False,inplace=True)
score_as_movie
```

```python
	User ID	Rating	Rating Timestamp
Movie ID			
7134690	30110.0	10.0	1.524974e+09
416889	1319.0	10.0	1.543320e+09
57840	23589.0	10.0	1.396802e+09
5693562	50266.0	10.0	1.511024e+09
5074	43803.0	10.0	1.428352e+09
```

```python
watchs = result.groupby('Movie ID').agg(['count'])
watchs2 = watchs['Rating']['count']
```

```python
print(watchs2.head(20))
```

```python
Movie ID
131      1
417     22
2354     1
3863     1
4099     2
4100     1
4101     1
4210     1
4395     1
4518     1
4546     2
4936     2
5074     1
5571     1
6177     1
6414     3
6684     1
6689     1
7145     1
7162     2
Name: count, dtype: int64
```

```python
watchs2.describe()
```

```python
count    10740.000000
mean        20.192086
std         86.251411
min          1.000000
25%          1.000000
50%          2.000000
75%          7.000000
max       1843.000000
Name: count, dtype: float64
```

```python
fig = plt.figure(figsize=(12,8))
histn = plt.hist(watchs2[watchs2 <=19],19,histtype='step')
plt.scatter([i+1 for i in range(len(histn[0]))],histn[0])
```

```python
array([4383., 1507.,  787.,  541.,  356.,  279.,  209.,  163.,  158.,
        118.,  114.,   90.,  104.,   81.,   80.,   73.,   62.,   65.,
         52.])
```

```python
sum(histn[0]) # 9222
```

```python
n3 = result.groupby('Movie ID').agg(['count','mean','std'])
n3r = n3[n3['Rating']['count']>=20]['Rating']
```

```python
	count	mean	std
Movie ID			
417	22	8.500000	1.263027
12349	68	8.485294	1.227698
15324	20	8.350000	1.039990
15864	51	8.431373	1.374844
17925	44	8.636364	1.259216
```

```python
nmin = (1.96**2*n3r['std']**2) / ( (n3r['mean']*0.025)**2 )
```

```python
Movie ID
417         135.712480
12349       128.671290
15324        95.349276
15864       163.434005
17925       130.668350
```

```python
n3s = n3r[ n3r['count'] >= nmin ]
```

```python

count	mean	std
Movie ID			
53604	129	8.635659	1.230714
57012	207	8.449275	1.537899
70735	224	8.839286	1.190799
75686	209	8.095694	1.358885
88763	296	8.945946	1.026984
...	...	...	...
6320628	860	7.966279	1.469924
6412452	276	7.510870	1.389529
6662050	22	10.000000	0.000000
6966692	907	8.673649	1.286455
7131622	1102	7.851180	1.751500
173 rows × 3 columns
```

```python
n3s_sort = n3s.sort_values(by='mean',ascending=False)
```

```python
	count	mean	std
Movie ID			
6662050	22	10.000000	0.000000
4921860	48	10.000000	0.000000
5262972	28	10.000000	0.000000
5512872	353	9.985836	0.266123
3863552	199	9.010050	1.163372
...	...	...	...
1291150	647	6.327666	1.785968
2557490	546	6.307692	1.858434
1478839	120	6.200000	0.728761
2177771	485	6.150515	1.523922
1951261	1091	6.083410	1.736127
173 rows × 3 columns
```

```python
ms = movies.drop_duplicates(subset=['Movie ID'])
ms = ms.set_index('Movie ID')
n3s_final = n3s_drops.join(ms,on='Movie ID')
```

```python
Movie Title
Five Minutes (2017)
MSG 2 the Messenger (2015)
Avengers: Age of Ultron Parody (2015)
Be Somebody (2016)
Bajrangi Bhaijaan (2015)
Back to the Future (1985)
La vita 鐚?bella (1997)
The Intouchables (2011)
The Sting (1973)
Coco (2017)
Toy Story 3 (2010)
3 Idiots (2009)
Green Book (2018)
Dead Poets Society (1989)
The Apartment (1960)
P.K. (2014)
The Truman Show (1998)
Am鑼卨ie (2001)
Inside Out (2015)
Toy Story 4 (2019)
Toy Story (1995)
Finding Nemo (2003)
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)
Home Alone (1990)
Zootopia (2016)
Up (2009)
Monsters, Inc. (2001)
La La Land (2016)
Relatos salvajes (2014)
En man som heter Ove (2015)
Snatch (2000)
Lock, Stock and Two Smoking Barrels (1998)
How to Train Your Dragon 2 (2014)
As Good as It Gets (1997)
Guardians of the Galaxy (2014)
The Grand Budapest Hotel (2014)
Fantastic Mr. Fox (2009)
Silver Linings Playbook (2012)
Sing Street (2016)
Deadpool (2016)
Annie Hall (1977)
Pride (2014)
In Bruges (2008)
Big Hero 6 (2014)
Groundhog Day (1993)
The Breakfast Club (1985)
Little Miss Sunshine (2006)
Deadpool 2 (2018)
The Terminal (2004)
```

```python
x = n3s_final['Movie Title'][:10].tolist()[::-1]
y = n3s_final['count'][:10].tolist()[::-1]
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('评论数',y,category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="喜剧电影被评论次数"),
                    toolbox_opts=opts.ToolboxOpts(),)
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)
grid.render_notebook()
```

```python
x = n3s_final['Movie Title'][:10].tolist()[::-1]
y = n3s_final['mean'][:10].round(3).tolist()[::-1]
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('平均得分',y,category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="喜剧电影平均得分"),
                    xaxis_opts=opts.AxisOpts(min_=8.0,name='平均得分'),
                    toolbox_opts=opts.ToolboxOpts(),)
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)
grid.render_notebook()
```

```python
In [8]: s = pd.Series(list('ABCA'))
In [9]: pd.get_dummies(s)
Out[9]:
   A  B  C
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
```

```python
In [5]: s = pd.Series(list('abaccd'))
In [6]: pd.get_dummies(s)
Out[6]:
   a  b  c  d
0  1  0  0  0
1  0  1  0  0
2  1  0  0  0
3  0  0  1  0
4  0  0  1  0
5  0  0  0  1
```

```python
d:\source\test\settingwithcopy.py:9: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy 
```

```python
tmp = df[df.a<4]
tmp['c'] = 200
```

```python
import pandas as  pd

df = pd.DataFrame({'a':[1,3,5],'b':[4,2,7]},index=['a','b','c'])
df.loc[df.a<4,'c'] = 100
print(df)
print('it\'s ok')

tmp = df[df.a<4]
tmp['c'] = 200
print('-----tmp------')
print(tmp)
print('-----df-------')
print(df)
```

```python
   a  b      c
a  1  4  100.0
b  3  2  100.0
c  5  7    NaN
it's ok
d:\source\test\settingwithcopy.py:9: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy     
  tmp['c'] = 200
-----tmp------
   a  b    c
a  1  4  200
b  3  2  200
-----df-------
   a  b      c
a  1  4  100.0
b  3  2  100.0
c  5  7    NaN
```

```python
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
wid = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[1])
```

```python
array([3.5, 3. , 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3. ,
       3. , 4. , 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6, 3.3, 3.4, 3. ,
       3.4, 3.5, 3.4, 3.2, 3.1, 3.4, 4.1, 4.2, 3.1, 3.2, 3.5, 3.1, 3. ,
       3.4, 3.5, 2.3, 3.2, 3.5, 3.8, 3. , 3.8, 3.2, 3.7, 3.3, 3.2, 3.2,
       3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 2. , 3. , 2.2, 2.9, 2.9,
       3.1, 3. , 2.7, 2.2, 2.5, 3.2, 2.8, 2.5, 2.8, 2.9, 3. , 2.8, 3. ,
       2.9, 2.6, 2.4, 2.4, 2.7, 2.7, 3. , 3.4, 3.1, 2.3, 3. , 2.5, 2.6,
       3. , 2.6, 2.3, 2.7, 3. , 2.9, 2.9, 2.5, 2.8, 3.3, 2.7, 3. , 2.9,
       3. , 3. , 2.5, 2.9, 2.5, 3.6, 3.2, 2.7, 3. , 2.5, 2.8, 3.2, 3. ,
       3.8, 2.6, 2.2, 3.2, 2.8, 2.8, 2.7, 3.3, 3.2, 2.8, 3. , 2.8, 3. ,
       2.8, 3.8, 2.8, 2.8, 2.6, 3. , 3.4, 3.1, 3. , 3.1, 3.1, 3.1, 2.7,
       3.2, 3.3, 3. , 2.5, 3. , 3.4, 3. ])
      
```

```python
smax = np.max(wid)
smin = np.min(wid)

In [51]: smax,smin
Out[51]: (4.4, 2.0)
```

```python
s = (wid - smin) / (smax - smin)
```

```python
np.set_printoptions(precision=3)  
```

```markdown
array([0.625, 0.417, 0.5  , 0.458, 0.667, 0.792, 0.583, 0.583, 0.375,
       0.458, 0.708, 0.583, 0.417, 0.417, 0.833, 1.   , 0.792, 0.625,
       0.75 , 0.75 , 0.583, 0.708, 0.667, 0.542, 0.583, 0.417, 0.583,
       0.625, 0.583, 0.5  , 0.458, 0.583, 0.875, 0.917, 0.458, 0.5  ,
       0.625, 0.458, 0.417, 0.583, 0.625, 0.125, 0.5  , 0.625, 0.75 ,
       0.417, 0.75 , 0.5  , 0.708, 0.542, 0.5  , 0.5  , 0.458, 0.125,
       0.333, 0.333, 0.542, 0.167, 0.375, 0.292, 0.   , 0.417, 0.083,
       0.375, 0.375, 0.458, 0.417, 0.292, 0.083, 0.208, 0.5  , 0.333,
       0.208, 0.333, 0.375, 0.417, 0.333, 0.417, 0.375, 0.25 , 0.167,
       0.167, 0.292, 0.292, 0.417, 0.583, 0.458, 0.125, 0.417, 0.208,
       0.25 , 0.417, 0.25 , 0.125, 0.292, 0.417, 0.375, 0.375, 0.208,
       0.333, 0.542, 0.292, 0.417, 0.375, 0.417, 0.417, 0.208, 0.375,
       0.208, 0.667, 0.5  , 0.292, 0.417, 0.208, 0.333, 0.5  , 0.417,
       0.75 , 0.25 , 0.083, 0.5  , 0.333, 0.333, 0.292, 0.542, 0.5  ,
       0.333, 0.417, 0.333, 0.417, 0.333, 0.75 , 0.333, 0.333, 0.25 ,
       0.417, 0.583, 0.458, 0.417, 0.458, 0.458, 0.458, 0.292, 0.5  ,
       0.542, 0.417, 0.208, 0.417, 0.583, 0.417])
```

```python
import seaborn as sns
sns.distplot(s,kde=False,rug=True)
```

```python
sns.distplot(s,hist=True,kde=True,rug=True)
```

```python
from scipy import stats
sns.distplot(s, kde=False, fit = stats.gamma)
```

```python
from scipy import stats
sns.distplot(s, kde=False, fit = stats.dgamma)
```

```python
import pandas as pd
import numpy as np

df = pd.read_csv("big_data.csv", 
skiprows = 
lambda x: x>0 and np.random.rand() > 0.01)

print("The shape of the df is {}. 
It has been reduced 100 times!".format(df.shape))
```

```python
from flask import Flask

App = Flask(__name__)
```

```python
@App.route('/')
def index():
    return "hello world"
```

```python
if __name__ == "__main__":
    App.run(debug=True)
```

```python
* Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 663-788-611
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

```python
 27.0.0.1 - - [03/Feb/2020 21:26:50] "GET / HTTP/1.1" 200 -
 ```

 以上就是flask的hello world 版

#### 2 Flask之数据入库操作

数据持久化就是将数据写入到数据库存储的过程。

本例子使用`sqlite3`数据库。

1)导入`sqlite3`，未安装前使用命令`pip install sqlite3`

创建一个`py`文件：`sqlite3_started.py`，并写下第一行代码：
```

```
2)手动创建一个数据库实例`db`, 命名`test.db`

3)创建与数据库实例`test.db`的连接:
```

```

4)拿到连接`conn`的cursor
```

```

5)创建第一张表`books`

共有四个字段：`id`,`sort`,`name`,`price`，类型分别为：`int`,`int`,`text`,`real`. 其中`id`为`primary key`. 主键的取值必须是唯一的(`unique`)，否则会报错。


```

```
第一次执行上面语句，表`books`创建完成。当再次执行时，就会报`重复建表`的错误。需要优化脚本，检查表是否存在`IF NOT EXISTS books`，不存在再创建：
```

```

6)插入一行记录

共为4个字段赋值

```

```

7)一次插入多行记录

先创建一个list:`books`，使用`executemany`一次插入多行。
```

```

8)提交

提交后才会真正生效，写入到数据库

```

```

9)关闭期初建立的连接conn

务必记住手动关闭，否则会出现内存泄漏
```

```

10)查看结果
例子君使用`vs code`，在扩展库中选择：`SQLite`安装。

![image-20200208211721377](./img/image-20200208211721377.png)

新建一个`sq`文件：`a.sql`，内容如下：

```

```
右键`run query`，得到表`books`插入的4行记录可视化图：

![image-20200208211806853](./img/image-20200208211806853.png)

以上十步就是sqlite3写入数据库的主要步骤，作为Flask系列的第二篇，为后面的前端讲解打下基础。

#### 3 Flask各层调用关系

这篇介绍Flask和B/S模式，即浏览器/服务器模式，是接下来快速理解Flask代码的关键理论篇：**理解Views、models和渲染模板层的调用关系**。

1) 发出请求

当我们在浏览器地址栏中输入某个地址，按回车后，完成第一步。

2) 视图层 views接收1)步发出的请求，Flask中使用解释器的方式处理这个求情，实例代码如下，它通常涉及到调用models层和模板文件层

```

```

3) models层会负责创建数据模型，执行CRUD操作

4) 模板文件层处理html模板

5) 组合后返回html

6) models层和html模板组合后返回给views层

7）最后views层响应并渲染到浏览器页面，我们就能看到请求的页面。

完整过程图如下所示：

![image-20200211152007983](./img/web1.png)

读者朋友们，如果你和例子君一样都是初学Flask编程，需要好好理解上面的过程。理解这些对于接下来的编程会有一定的理论指导，方向性指导价值。

### Python 问答

#### Python 如何生成二维码？





## qrcode

今天先来解答如何生成二维码。Python的`qrcode`包支持生成二维码。

用法也很简单：

```

```

生成的二维码如下：

![](https://imgkr2.cn-bj.ufileos.com/f0b08c53-0107-483b-bbe5-072bebc58e8d.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=rVtaeBWhzLPPq%252BFCVtiOv6rS0tI%253D&Expires=1603544615)


大家微信扫描后，会出现我的二维码。

另外，还可以设置二维码的颜色等样式：

```

```

生成一个orange的二维码：

![](https://imgkr2.cn-bj.ufileos.com/cbd26fd8-27cf-4630-935f-6896822ce483.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=uy1r24x%252Fp5QpI5Wy10Ebdaz%252BpLM%253D&Expires=1603544681)

更多样式，大家可以自己去玩耍。

## Python小项目：句子KWIC显示

上下文关键字（KWIC, Key Word In Context）是最常见的多行协调显示格式。

此小项目描述：输入一系列句子，给定一个给定单词，每个句子中至少会出现一次给定单词。目标输出，给定单词按照KWIC显示，KWIC显示的基本要求：待查询单词居中，前面`pre`序列右对齐，后面`post`序列左对齐，待查询单词前和后长度相等，若输入句子无法满足要求，用空格填充。

输入参数：输入句子sentences, 待查询单词selword, 滑动窗口长度`window_len`

举例，输入如下六个句子，给定单词`secure`，输出如下字符串：

```

```

请补充实现下面函数：

```

# jadore801120/attention-is-all-you-need-pytorch, 6 blocks.

```bash
# conda install -c conda-forge spacy 
python -m spacy download en
python -m spacy download de
```

```bash
python preprocess.py -lang_src de -lang_trg en -share_vocab -save_data m30k_deen_shr.pkl
```

```bash
python train.py -data_pkl m30k_deen_shr.pkl -log m30k_deen_shr -embs_share_weight -proj_share_weight -label_smoothing -output_dir output -b 256 -warmup 128000 -epoch 400
```

```bash
python translate.py -data_pkl m30k_deen_shr.pkl -model trained.chkpt -output prediction.txt
```

```bash
python preprocess.py -raw_dir /tmp/raw_deen -data_dir ./bpe_deen -save_data bpe_vocab.pkl -codes codes.txt -prefix deen
```

```bash
python train.py -data_pkl ./bpe_deen/bpe_vocab.pkl -train_path ./bpe_deen/deen-train -val_path ./bpe_deen/deen-val -log deen_bpe -embs_share_weight -proj_share_weight -label_smoothing -output_dir output -b 256 -warmup 128000 -epoch 400
```

# junyanz/pytorch-cyclegan-and-pix2pix, 14 blocks.

```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
cd pytorch-CycleGAN-and-pix2pix
```

```bash
bash ./datasets/download_cyclegan_dataset.sh maps
```

```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan
```

```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan
```

```bash
bash ./datasets/download_pix2pix_dataset.sh facades
```

```bash
#!./scripts/train_pix2pix.sh
python train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction BtoA
```

```bash
#!./scripts/test_pix2pix.sh
python test.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction BtoA
```

```bash
bash ./scripts/download_cyclegan_model.sh horse2zebra
```

```bash
bash ./datasets/download_cyclegan_dataset.sh horse2zebra
```

```bash
python test.py --dataroot datasets/horse2zebra/testA --name horse2zebra_pretrained --model test --no_dropout
```

```bash
bash ./scripts/download_pix2pix_model.sh facades_label2photo
```

```bash
bash ./datasets/download_pix2pix_dataset.sh facades
```

```bash
python test.py --dataroot ./datasets/facades/ --direction BtoA --model pix2pix --name facades_label2photo_pretrained
```

```
@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}


@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}
```

# keras-team/keras, 8 blocks.

```python
from tensorflow.keras.models import Sequential

model = Sequential()
```

```python
from tensorflow.keras.layers import Dense

model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
```

```python
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

```python
model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.SGD(
                  learning_rate=0.01, momentum=0.9, nesterov=True))
```

```python
# x_train and y_train are Numpy arrays.
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

```python
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
```

```python
classes = model.predict(x_test, batch_size=128)
```

```python
import tensorflow as tf

# Prepare an optimizer.
optimizer = tf.keras.optimizers.Adam()
# Prepare a loss function.
loss_fn = tf.keras.losses.kl_divergence

# Iterate over the batches of a dataset.
for inputs, targets in dataset:
    # Open a GradientTape.
    with tf.GradientTape() as tape:
        # Forward pass.
        predictions = model(inputs)
        # Compute the loss value for this batch.
        loss_value = loss_fn(targets, predictions)

    # Get gradients of loss wrt the weights.
    gradients = tape.gradient(loss_value, model.trainable_weights)
    # Update the weights of the model.
    optimizer.apply_gradients(zip(gradients, model.trainable_weights))
```

# lengstrom/fast-style-transfer, 3 blocks.

```
conda create -n tf-gpu tensorflow-gpu=2.1.0
conda activate tf-gpu
conda install jupyterlab
jupyter lab
```

```
!pip install moviepy==1.0.2
```

```
  @misc{engstrom2016faststyletransfer,
    author = {Logan Engstrom},
    title = {Fast Style Transfer},
    year = {2016},
    howpublished = {\url{https://github.com/lengstrom/fast-style-transfer/}},
    note = {commit xxxxxxx}
  }
```

# leon-ai/leon, 3 blocks.

```sh
# Clone the repository (stable branch)
git clone -b master https://github.com/leon-ai/leon.git leon
# OR download the latest release at: https://github.com/leon-ai/leon/releases/latest

# Go to the project root
cd leon

# Install
npm install
```

```sh
# Check the setup went well
npm run check

# Build
npm run build

# Run
npm start

# Go to http://localhost:1337
# Hooray! Leon is running
```

```sh
# Build
npm run docker:build

# Run
npm run docker:run

# Go to http://localhost:1337
# Hooray! Leon is running
```

# lmcinnes/umap, 0 blocks.

# lutzroeder/netron, 0 blocks.

# mxgmn/wavefunctioncollapse, 1 blocks.

```
dotnet run WaveFunctionCollapse.csproj
```

# naptha/tesseract.js, 6 blocks.

```javascript
import Tesseract from 'tesseract.js';

Tesseract.recognize(
  'https://tesseract.projectnaptha.com/img/eng_bw.png',
  'eng',
  { logger: m => console.log(m) }
).then(({ data: { text } }) => {
  console.log(text);
})
```

```javascript
import { createWorker } from 'tesseract.js';

const worker = createWorker({
  logger: m => console.log(m)
});

(async () => {
  await worker.load();
  await worker.loadLanguage('eng');
  await worker.initialize('eng');
  const { data: { text } } = await worker.recognize('https://tesseract.projectnaptha.com/img/eng_bw.png');
  console.log(text);
  await worker.terminate();
})();
```

```html
<!-- v2 -->
<script src='https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js'></script>

<!-- v1 -->
<script src='https://unpkg.com/tesseract.js@1.0.19/src/index.js'></script>
```

```shell
# For v2
npm install tesseract.js
yarn add tesseract.js

# For v1
npm install tesseract.js@1
yarn add tesseract.js@1
```

```shell
# First we clone the repository
git clone https://github.com/naptha/tesseract.js.git
cd tesseract.js

# Then we install the dependencies
npm install

# And finally we start the development server
npm start
```

```shell
npm run build
```

# nltk/nltk, 0 blocks.

# onnx/onnx, 12 blocks.

```
conda install -c conda-forge onnx
```

```
# Use conda-forge protobuf, as default doesn't come with protoc
conda install -c conda-forge protobuf numpy
```

```
pip install onnx
```

```
git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive
python setup.py install
```

```
sudo apt-get install protobuf-compiler libprotoc-dev
pip install onnx
```

```
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v3.11.3
cd cmake
# Explicitly set -Dprotobuf_MSVC_STATIC_RUNTIME=OFF to make sure protobuf does not statically link to runtime library
cmake -G -A -Dprotobuf_MSVC_STATIC_RUNTIME=OFF -Dprotobuf_BUILD_TESTS=OFF -Dprotobuf_BUILD_EXAMPLES=OFF -DCMAKE_INSTALL_PREFIX=<protobuf_install_dir>
# For example:
# cmake -G "Visual Studio 16 2019" -A x64 -Dprotobuf_MSVC_STATIC_RUNTIME=OFF -Dprotobuf_BUILD_TESTS=OFF -Dprotobuf_BUILD_EXAMPLES=OFF -DCMAKE_INSTALL_PREFIX=..\install
msbuild protobuf.sln /m /p:Configuration=Release
msbuild INSTALL.vcxproj /p:Configuration=Release
```

```
# Get ONNX
git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive

# Set environment variables to find protobuf and turn off static linking of ONNX to runtime library.
# Even better option is to add it to user\system PATH so this step can be performed only once.
# For more details check https://docs.microsoft.com/en-us/cpp/build/reference/md-mt-ld-use-run-time-library?view=vs-2017
set PATH=<protobuf_install_dir>\bin;<protobuf_install_dir>\include;<protobuf_install_dir>\libs;%PATH%
set USE_MSVC_STATIC_RUNTIME=0

# use the static installed protobuf
set CMAKE_ARGS=-DONNX_USE_PROTOBUF_SHARED_LIBS=OFF -DProtobuf_USE_STATIC_LIBS=ON

# Optional: Set environment variable `ONNX_ML=1` for onnx-ml

# Build ONNX
python setup.py install
```

```
# Use conda-forge protobuf
conda install -c conda-forge numpy libprotobuf=3.11.3 protobuf

# Get ONNX
git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive

# Set environment variable for ONNX to use protobuf shared lib
set USE_MSVC_STATIC_RUNTIME=0
set CMAKE_ARGS=-DONNX_USE_PROTOBUF_SHARED_LIBS=ON -DProtobuf_USE_STATIC_LIBS=OFF -DONNX_USE_LITE_PROTO=ON

# Build ONNX
# Optional: Set environment variable `ONNX_ML=1` for onnx-ml

python setup.py install
```

```
pip install cython protobuf numpy
sudo apt-get install libprotobuf-dev protobuf-compiler
pip install onnx
```

```
python -c "import onnx"
```

```
pip install pytest nbval
```

```
pytest
```

# phillipi/pix2pix, 17 blocks.

```bash
luarocks install nngraph
luarocks install https://raw.githubusercontent.com/szym/display/master/display-scm-0.rockspec
```

```bash
git clone git@github.com:phillipi/pix2pix.git
cd pix2pix
```

```bash
bash ./datasets/download_dataset.sh facades
```

```bash
DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA th train.lua
```

```bash
DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA gpu=0 cudnn=0 batchSize=10 save_epoch_freq=5 th train.lua
```

```bash
th -ldisplay.start 8000 0.0.0.0
```

```bash
DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA phase=val th test.lua
```

```bash
DATA_ROOT=/path/to/data/ name=expt_name which_direction=AtoB th train.lua
```

```bash
DATA_ROOT=/path/to/data/ name=expt_name which_direction=AtoB phase=val th test.lua
```

```bash
bash ./datasets/download_dataset.sh dataset_name
```

```bash
bash ./models/download_model.sh model_name
```

```bash
python scripts/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data
```

```bash
bash ./scripts/eval_cityscapes/download_fcn8s.sh
```

```bash
export PYTHONPATH=${PYTHONPATH}:./scripts/eval_cityscapes/
```

```bash
python ./scripts/eval_cityscapes/evaluate.py --cityscapes_dir /path/to/original/cityscapes/dataset/ --result_dir /path/to/your/predictions/ --output_dir /path/to/output/directory/
```

```bash
th -ldisplay.start 8000 0.0.0.0
```

```
@article{pix2pix2017,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  journal={CVPR},
  year={2017}
}
```

# photoprism/photoprism, 0 blocks.

# pytorch/pytorch, 15 blocks.

```bash
conda install astunparse numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
```

```bash
# CUDA only: Add LAPACK support for the GPU if needed
conda install -c pytorch magma-cuda110  # or the magma-cuda* that matches your CUDA version from https://anaconda.org/pytorch/repo
```

```bash
# Add these packages if torch.distributed is needed
conda install pkg-config libuv
```

```bash
# Add these packages if torch.distributed is needed.
# Distributed package support on Windows is a prototype feature and is subject to changes.
conda install -c conda-forge libuv=1.39
```

```bash
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive
```

```bash
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py install
```

```bash
python tools/amd_build/build_amd.py
```

```plaintext
build/temp.linux-x86_64-3.7/torch/csrc/stub.o: file not recognized: file format not recognized
collect2: error: ld returned 1 exit status
error: command 'g++' failed with exit status 1
```

```bash
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py install
```

```cmd
cmd

:: [Optional] If you want to build with the VS 2017 generator for old CUDA and PyTorch, please change the value in the next line to `Visual Studio 15 2017`.
:: Note: This value is useless if Ninja is detected. However, you can force that by using `set USE_NINJA=OFF`.
set CMAKE_GENERATOR=Visual Studio 16 2019

:: Read the content in the previous section carefully before you proceed.
:: [Optional] If you want to override the underlying toolset used by Ninja and Visual Studio with CUDA, please run the following script block.
:: "Visual Studio 2019 Developer Command Prompt" will be run automatically.
:: Make sure you have CMake >= 3.12 before you do this when you use the Visual Studio generator.
set CMAKE_GENERATOR_TOOLSET_VERSION=14.27
set DISTUTILS_USE_SDK=1
for /f "usebackq tokens=*" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -version [15^,16^) -products * -latest -property installationPath`) do call "%i\VC\Auxiliary\Build\vcvarsall.bat" x64 -vcvars_ver=%CMAKE_GENERATOR_TOOLSET_VERSION%

:: [Optional] If you want to override the CUDA host compiler
set CUDAHOSTCXX=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.27.29110\bin\HostX64\x64\cl.exe

python setup.py install

```

```bash
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py build --cmake-only
ccmake build  # or cmake-gui build
```

```bash
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py build --cmake-only
ccmake build  # or cmake-gui build
```

```bash
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```

```bash
make -f docker.Makefile
# images are tagged as docker.io/${your_docker_username}/pytorch
```

```bash
cd docs/
pip install -r requirements.txt
```

# pytorch/vision, 0 blocks.

# scikit-learn/scikit-learn, 0 blocks.

# sebastianruder/nlp-progress, 0 blocks.

# sfyc23/everydaywechat, 13 blocks.

```
机器人渠道（1: 图灵机器人，2: 一个AI ,3 : 青云客，4 腾讯智能闲聊，5:天行机器人，6：海知智能，7：思知机器人)
bot_channel: 7
```

```
is_auto_reply_all：False
# 指定自动回复的好友名单。
auto_reply_white_list:
  - '好友1'
  - '好友2'
```

```
is_auto_reply_all：True
auto_reply_black_list:
    - '好友1'
    - '好友2'
```

```
turing_conf:
  apiKey: '你所获取apikey'
```

```
txapi_conf:
  app_key: '个人中心中的key'
  reply_name: '宝宝' # 回复的人的名字(可空)（也可在个人中心->机器人管理 修改）
  bot_name: '老公' # 机器人的名字（可空）
```

```
qqnlpchat_conf:
    app_id: '你申请的api_id'
    app_key: '你申请的app_key'
```

```
yigeai_conf:
  client_token: '客户访问令牌'
```

```
ownthink_conf:
    app_key: '你申请的api_id'
```

```
alarm_info:
  is_alarm: True
```

```
alarm_timed:
  - "9:00"
  - "12:30"
  - "22:00"
wechat_name:
  - '文件传输助手'
  - '诗风'
group_name:
  - 'EverydayWechat 交流群'
is_tomorrow: False
city_name: '桂林'
dictum_channel : 3
start_date: '2017-10-10'
start_date_msg: '爱你的第{}天'
calendar: True
horescope: "处女座"
sweet_words: '你脚下的蚂蚁'

```

```
2019-06-29 星期六 农历五月廿七 
【宜】嫁娶,祭祀,沐浴,扫舍,修饰垣墙 
【忌】行丧,安葬 
桂林天气预报 
【今日天气】阵雨
【今日温度】低温 26.0℃,高温 33.0℃ 
【今日风速】南风<3级
【出行提示】阵雨来袭，出门记得带伞 
【桂林PM2.5】142 轻度污染
处女座今日运势 
【幸运颜色】2
【幸运数字】薄荷绿
【综合运势】今天的你有机会重逢旧同学、旧朋友，对方会为你带来一些小惊喜，可能是某个不错的商机，也可能是某个消息。工作/学习上，今天的你目标性很强，能把当初奋斗的初心捡回来，重新出发。感情方面，有伴者今天要提防烂桃花的挑拨离间，多给对方一些信任。
你知道五氧化二磷被氧化前是什么样子嘛，什么样子？五二磷。 
宝贝这是我们在一起的第628天 
你脚下的蚂蚁
```

```
pip3 install -r requirements.txt
# 或者是使用 pip
# pip install -r requirements.txt
```

```
python run.py
```

# streamlit/streamlit, 3 blocks.

```bash
pip install streamlit
streamlit hello
```

```python
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
```

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)
```

# tensorflow/serving, 1 blocks.

```bash
# Download the TensorFlow Serving Docker image and repo
docker pull tensorflow/serving

git clone https://github.com/tensorflow/serving
# Location of demo models
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"

# Start TensorFlow Serving container and open the REST API port
docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &

# Query the model using the predict API
curl -d '{"instances": [1.0, 2.0, 5.0]}' \
    -X POST http://localhost:8501/v1/models/half_plus_two:predict

# Returns => { "predictions": [2.5, 3.0, 4.5] }
```

# ultralytics/yolov3, 7 blocks.

```bash
$ git clone https://github.com/ultralytics/yolov3  # master branch (default)
```

```bash
$ git clone https://github.com/ultralytics/yolov3 -b archive  # archive branch
```

```bash
$ pip install -r requirements.txt
```

```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

```bash
$ python detect.py --source data/images --weights yolov3.pt --conf 0.25
```

```python
import torch

# Model
model = torch.hub.load('ultralytics/yolov3', 'yolov3')  # or 'yolov3_spp', 'yolov3_tiny'

# Image
img = 'https://ultralytics.com/images/zidane.jpg'

# Inference
results = model(img)
results.print()  # or .show(), .save()
```

```bash
$ python train.py --data coco.yaml --cfg yolov3.yaml      --weights '' --batch-size 24
                                         yolov3-spp.yaml                            24
                                         yolov3-tiny.yaml                           64
```

# ultralytics/yolov5, 4 blocks.

```bash
$ git clone https://github.com/ultralytics/yolov5
$ cd yolov5
$ pip install -r requirements.txt
```

```python
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, PIL, OpenCV, numpy, multiple

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
```

```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

```bash
$ python train.py --data coco.yaml --cfg yolov5s.yaml --weights '' --batch-size 64
                                         yolov5m                                40
                                         yolov5l                                24
                                         yolov5x                                16
```

# zalandoresearch/fashion-mnist, 5 blocks.

```bash
git clone git@github.com:zalandoresearch/fashion-mnist.git
```

```python
import mnist_reader
X_train, y_train = mnist_reader.load_mnist('data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist('data/fashion', kind='t10k')
```

```python
from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets('data/fashion')

data.train.next_batch(BATCH_SIZE)
```

```python
data = input_data.read_data_sets('data/fashion', source_url='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/')
```

```latex
@online{xiao2017/online,
  author       = {Han Xiao and Kashif Rasul and Roland Vollgraf},
  title        = {Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning Algorithms},
  date         = {2017-08-28},
  year         = {2017},
  eprintclass  = {cs.LG},
  eprinttype   = {arXiv},
  eprint       = {cs.LG/1708.07747},
}
```

# zihangdai/xlnet, 7 blocks.

```shell
  CUDA_VISIBLE_DEVICES=0,1,2,3 python run_classifier.py \
    --do_train=True \
    --do_eval=False \
    --task_name=sts-b \
    --data_dir=${GLUE_DIR}/STS-B \
    --output_dir=proc_data/sts-b \
    --model_dir=exp/sts-b \
    --uncased=False \
    --spiece_model_file=${LARGE_DIR}/spiece.model \
    --model_config_path=${LARGE_DIR}/xlnet_config.json \
    --init_checkpoint=${LARGE_DIR}/xlnet_model.ckpt \
    --max_seq_length=128 \
    --train_batch_size=8 \
    --num_hosts=1 \
    --num_core_per_host=4 \
    --learning_rate=5e-5 \
    --train_steps=1200 \
    --warmup_steps=120 \
    --save_steps=600 \
    --is_regression=True
  ```

- Evaluate the finetuning results with a single GPU by

  ```shell
  CUDA_VISIBLE_DEVICES=0 python run_classifier.py \
    --do_train=False \
    --do_eval=True \
    --task_name=sts-b \
    --data_dir=${GLUE_DIR}/STS-B \
    --output_dir=proc_data/sts-b \
    --model_dir=exp/sts-b \
    --uncased=False \
    --spiece_model_file=${LARGE_DIR}/spiece.model \
    --model_config_path=${LARGE_DIR}/xlnet_config.json \
    --max_seq_length=128 \
    --eval_batch_size=8 \
    --num_hosts=1 \
    --num_core_per_host=1 \
    --eval_all_ckpt=True \
    --is_regression=True

  # Expected performance: "eval_pearsonr 0.916+ "
  ```

**Notes**:

- In the context of GPU training, `num_core_per_host` denotes the number of GPUs to use.
- In the multi-GPU setting, `train_batch_size` refers to the <u>per-GPU batch size</u>.
- `eval_all_ckpt` allows one to evaluate all saved checkpoints (save frequency is controlled by `save_steps`) after training finishes and choose the best model based on dev performance.
- `data_dir` and `output_dir` refer to the directories of the "raw data" and "preprocessed tfrecords" respectively, while `model_dir` is the working directory for saving checkpoints and tensorflow events. **`model_dir` should be set as a separate folder to `init_checkpoint`.**
- To try out <u>XLNet-base</u>, one can simply set `--train_batch_size=32` and `--num_core_per_host=1`, along with according changes in `init_checkpoint` and `model_config_path`.
- For GPUs with smaller RAM, please proportionally decrease the `train_batch_size` and increase `num_core_per_host` to use the same training setting.
- **Important**: we separate the training and evaluation into "two phases", as using multi GPUs to perform evaluation is tricky (one has to correctly separate the data across GPUs). To ensure correctness, we only support single-GPU evaluation for now.


#### (2) IMDB: movie review sentiment classification (with TPU V3-8)

- Download and unpack the IMDB dataset by running

  ```shell
  wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
  tar zxvf aclImdb_v1.tar.gz
  ```

- Launch a Google cloud TPU V3-8 instance (see the [Google Cloud TPU tutorial](https://cloud.google.com/tpu/docs/tutorials/mnist) for how to set up Cloud TPUs).

- Set up your Google storage bucket path `$GS_ROOT` and move the IMDB dataset and pretrained checkpoint into your Google storage.

- Perform TPU finetuning with XLNet-Large by running

  ```shell
  python run_classifier.py \
    --use_tpu=True \
    --tpu=${TPU_NAME} \
    --do_train=True \
    --do_eval=True \
    --eval_all_ckpt=True \
    --task_name=imdb \
    --data_dir=${IMDB_DIR} \
    --output_dir=${GS_ROOT}/proc_data/imdb \
    --model_dir=${GS_ROOT}/exp/imdb \
    --uncased=False \
    --spiece_model_file=${LARGE_DIR}/spiece.model \
    --model_config_path=${GS_ROOT}/${LARGE_DIR}/model_config.json \
    --init_checkpoint=${GS_ROOT}/${LARGE_DIR}/xlnet_model.ckpt \
    --max_seq_length=512 \
    --train_batch_size=32 \
    --eval_batch_size=8 \
    --num_hosts=1 \
    --num_core_per_host=8 \
    --learning_rate=2e-5 \
    --train_steps=4000 \
    --warmup_steps=500 \
    --save_steps=500 \
    --iterations=500

  # Expected performance: "eval_accuracy 0.962+ "
  ```

**Notes**:

- To obtain the SOTA on the IMDB dataset, using sequence length 512 is **necessary**. Therefore, we show how this can be done with a TPU V3-8.
- Alternatively, one can use a sequence length smaller than 512, a smaller batch size, or switch to XLNet-base to train on GPUs. But performance drop is expected.
- Notice that the `data_dir` and `spiece_model_file` both use a local path rather than a Google Storage path. The reason is that data preprocessing is actually performed locally. Hence, using local paths leads to a faster preprocessing speed.

### SQuAD2.0

The code for the SQuAD dataset is included in `run_squad.py`.

To run the code:

(1) Download the SQuAD2.0 dataset into `$SQUAD_DIR` by:

```

```

(2) Perform data preprocessing using the script `scripts/prepro_squad.sh`.

- This will take quite some time in order to accurately map character positions (raw data) to sentence piece positions (used for training).

- For faster parallel preprocessing, please refer to the flags `--num_proc` and `--proc_id` in `run_squad.py`.

(3) Perform training and evaluation.

For the best performance, XLNet-Large uses <u>sequence length 512</u> and <u>batch size 48</u> for training.

- As a result, reproducing the best result with GPUs is quite difficult.

- For training with one TPU v3-8, one can simply run the script `scripts/tpu_squad_large.sh` after both the TPU and Google storage have been setup.
- `run_squad.py` will automatically perform threshold searching on the dev set of squad and output the score. With `scripts/tpu_squad_large.sh`, the expected F1 score should be around 88.6 (median of our multiple runs).

Alternatively, one can use XLNet-Base with GPUs (e.g. three V100). One set of reasonable hyper-parameters can be found in the script `scripts/gpu_squad_base.sh`.


### RACE reading comprehension

The code for the reading comprehension task [RACE](https://www.cs.cmu.edu/~glai1/data/race/) is included in `run_race.py`.

- Notably, the average length of the passages in RACE is over 300 tokens (not peices), which is <u>significantly longer</u> than other popular reading comprehension datasets such as SQuAD.
- Also, many questions can be very difficult and requires complex reasoning for machines to solve (see [one example here](misc/race_example.md)).


To run the code:

(1) Download the RACE dataset from the [official website](https://www.cs.cmu.edu/~glai1/data/race/) and unpack the raw data to `$RACE_DIR`.

(2) Perform training and evaluation:

- The SOTA performance (accuracy 81.75) of RACE is produced using XLNet-Large with sequence length 512 and batch size 32, which requires a large TPU v3-32 in the pod setting. Please refer to the script `script/tpu_race_large_bsz32.sh` for this setting.
- Using XLNet-Large with sequence length 512 and batch size 8 on a TPU v3-8 can give you an accuracy of around 80.3 (see `script/tpu_race_large_bsz8.sh`).

### Using Google Colab

[An example](notebooks/colab_imdb_gpu.ipynb) of using Google Colab with GPUs has been provided. Note that since the hardware is constrained in the example, the results are worse than the best we can get. It mainly serves as an example and should be modified accordingly to maximize performance.


## Custom Usage of XLNet

### XLNet Abstraction

For finetuning, it is likely that you will be able to modify existing files such as `run_classifier.py`, `run_squad.py` and `run_race.py` for your task at hand. However, we also provide an abstraction of XLNet to enable more flexible usage. Below is an example:

```

```

### Tokenization

Below is an example of doing tokenization in XLNet:
```

```
where `FLAGS.spiece_model_file` is the SentencePiece model file in the same zip as the pretrained model, `FLAGS.uncased` is a bool indicating whether to do uncasing.


## Pretraining with XLNet

Refer to `train.py` for pretraining on TPUs and `train_gpu.py` for pretraining on GPUs. First we need to preprocess the text data into tfrecords.

```

```

where `input_glob` defines all input text files, `save_dir` is the output directory for tfrecords, and `sp_path` is a [Sentence Piece](https://github.com/google/sentencepiece) model. Here is our script to train the Sentence Piece model

```

```

Special symbols are used, including `control_symbols` and `user_defined_symbols`. We use `<eop>` and `<eod>` to denote End of Paragraph and End of Document respectively.

The input text files to `data_utils.py` must use the following format:
* Each line is a sentence.
* An empty line means End of Document.
* (Optional) If one also wants to model paragraph structures, `<eop>` can be inserted at the end of certain lines (without any space) to indicate that the corresponding sentence ends a paragraph.

For example, the text input file could be:
```

```

After preprocessing, we are ready to pretrain an XLNet. Below are the hyperparameters used for pretraining XLNet-Large:

```

