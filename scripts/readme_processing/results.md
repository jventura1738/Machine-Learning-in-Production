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

# pytorchlightning/pytorch-lightning, 21 blocks.

```bash
pip install pytorch-lightning
```

```bash
  pip install pytorch-lightning['extra']
  ```

```bash
  conda install pytorch-lightning -c conda-forge
  ```

```bash
  pip install git+https://github.com/PytorchLightning/pytorch-lightning.git@release/1.3.x --upgrade
  ```

```bash
  pip install https://github.com/PyTorchLightning/pytorch-lightning/archive/master.zip
  ```

```bash
  pip install -iU https://test.pypi.org/simple/ pytorch-lightning
  ```

```python
import os
import torch
from torch import nn
import torch.nn.functional as F
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
import pytorch_lightning as pl
```

```python
class LitAutoEncoder(pl.LightningModule):

    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 3))
        self.decoder = nn.Sequential(nn.Linear(3, 128), nn.ReLU(), nn.Linear(128, 28 * 28))

    def forward(self, x):
        # in lightning, forward defines the prediction/inference actions
        embedding = self.encoder(x)
        return embedding

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop. It is independent of forward
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log('train_loss', loss)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
```

```python
dataset = MNIST(os.getcwd(), download=True, transform=transforms.ToTensor())
train, val = random_split(dataset, [55000, 5000])

autoencoder = LitAutoEncoder()
trainer = pl.Trainer()
trainer.fit(autoencoder, DataLoader(train), DataLoader(val))
```

```python
  # 8 GPUs
  # no code changes needed
  trainer = Trainer(max_epochs=1, gpus=8)

  # 256 GPUs
  trainer = Trainer(max_epochs=1, gpus=8, num_nodes=32)
  ```

```python
  # no code changes needed
  trainer = Trainer(tpu_cores=8)
   ```

```python
  # no code changes needed
  trainer = Trainer(precision=16)
   ```

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

```python
  es = EarlyStopping(monitor='val_loss')
  trainer = Trainer(callbacks=[es])
   ```

```python
  checkpointing = ModelCheckpoint(monitor='val_loss')
  trainer = Trainer(callbacks=[checkpointing])
   ```

```python
  # torchscript
  autoencoder = LitAutoEncoder()
  torch.jit.save(autoencoder.to_torchscript(), "model.pt")
   ```

```python
  # onnx
  with tempfile.NamedTemporaryFile(suffix='.onnx', delete=False) as tmpfile:
      autoencoder = LitAutoEncoder()
      input_sample = torch.randn((1, 64))
      autoencoder.to_onnx(tmpfile.name, input_sample, export_params=True)
      os.path.isfile(tmpfile.name)
   ```

```python
class LitAutoEncoder(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.automatic_optimization = False

    def training_step(self, batch, batch_idx):
        # access your optimizers with use_pl_optimizer=False. Default is True
        opt_a, opt_b = self.optimizers(use_pl_optimizer=True)

        loss_a = ...
        self.manual_backward(loss_a, opt_a)
        opt_a.step()
        opt_a.zero_grad()

        loss_b = ...
        self.manual_backward(loss_b, opt_b, retain_graph=True)
        self.manual_backward(loss_b, opt_b)
        opt_b.step()
        opt_b.zero_grad()
```

```
python my_model.py --learning_rate 1e-6 --layers 2 --gpus 4
```

```
grid train --grid_gpus 4 my_model.py --learning_rate 'uniform(1e-6, 1e-1, 20)' --layers '[2, 4, 8, 16]'
```

```bibtex
@article{falcon2019pytorch,
  title={PyTorch Lightning},
  author={Falcon, WA, et al.},
  journal={GitHub. Note: https://github.com/PyTorchLightning/pytorch-lightning},
  volume={3},
  year={2019}
}
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

# jackzhenguo/python-small-examples, 0 blocks.

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

# onnx/onnx, 10 blocks.

```
pip install numpy protobuf==3.11.3
pip install onnx
```

```
conda install -c conda-forge numpy protobuf==3.11.3 libprotobuf=3.11.3
conda install -c conda-forge onnx
```

```
git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive
# prefer lite proto
set CMAKE_ARGS=-DONNX_USE_LITE_PROTO=ON
pip install -e .
```

```
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v3.11.3
cd cmake
cmake -G "Visual Studio 16 2019" -A x64 -DCMAKE_INSTALL_PREFIX=<protobug_install_dir> -Dprotobuf_MSVC_STATIC_RUNTIME=ON -Dprotobuf_BUILD_SHARED_LIBS=OFF -Dprotobuf_BUILD_TESTS=OFF -Dprotobuf_BUILD_EXAMPLES=OFF .
msbuild protobuf.sln /m /p:Configuration=Release
msbuild INSTALL.vcxproj /p:Configuration=Release
```

```
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v3.11.3
git submodule update --init --recursive
mkdir build_source && cd build_source
cmake ../cmake -Dprotobuf_BUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SYSCONFDIR=/etc -DCMAKE_POSITION_INDEPENDENT_CODE=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
make install
```

```
export NUM_CORES=`sysctl -n hw.ncpu`
brew update
brew install autoconf && brew install automake
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.11.3/protobuf-cpp-3.11.3.tar.gz
tar -xvf protobuf-cpp-3.11.3.tar.gz
cd protobuf-3.11.3
mkdir build_source && cd build_source
cmake ../cmake -Dprotobuf_BUILD_SHARED_LIBS=OFF -DCMAKE_POSITION_INDEPENDENT_CODE=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release
make -j${NUM_CORES}
make install
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

# zihangdai/xlnet, 11 blocks.

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

```shell
  wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
  tar zxvf aclImdb_v1.tar.gz
  ```

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

```shell
mkdir -p ${SQUAD_DIR} && cd ${SQUAD_DIR}
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
```

```python
import xlnet

# some code omitted here...
# initialize FLAGS
# initialize instances of tf.Tensor, including input_ids, seg_ids, and input_mask

# XLNetConfig contains hyperparameters that are specific to a model checkpoint.
xlnet_config = xlnet.XLNetConfig(json_path=FLAGS.model_config_path)

# RunConfig contains hyperparameters that could be different between pretraining and finetuning.
run_config = xlnet.create_run_config(is_training=True, is_finetune=True, FLAGS=FLAGS)

# Construct an XLNet model
xlnet_model = xlnet.XLNetModel(
    xlnet_config=xlnet_config,
    run_config=run_config,
    input_ids=input_ids,
    seg_ids=seg_ids,
    input_mask=input_mask)

# Get a summary of the sequence using the last hidden state
summary = xlnet_model.get_pooled_out(summary_type="last")

# Get a sequence output
seq_out = xlnet_model.get_sequence_output()

# build your applications based on `summary` or `seq_out`
```

```python
import sentencepiece as spm
from prepro_utils import preprocess_text, encode_ids

# some code omitted here...
# initialize FLAGS

text = "An input text string."

sp_model = spm.SentencePieceProcessor()
sp_model.Load(FLAGS.spiece_model_file)
text = preprocess_text(text, lower=FLAGS.uncased)
ids = encode_ids(sp_model, text)
```

```shell
python data_utils.py \
	--bsz_per_host=32 \
	--num_core_per_host=16 \
	--seq_len=512 \
	--reuse_len=256 \
	--input_glob=*.txt \
	--save_dir=${SAVE_DIR} \
	--num_passes=20 \
	--bi_data=True \
	--sp_path=spiece.model \
	--mask_alpha=6 \
	--mask_beta=1 \
	--num_predict=85
```

```bash
spm_train \
	--input=$INPUT \
	--model_prefix=sp10m.cased.v3 \
	--vocab_size=32000 \
	--character_coverage=0.99995 \
	--model_type=unigram \
	--control_symbols=<cls>,<sep>,<pad>,<mask>,<eod> \
	--user_defined_symbols=<eop>,.,(,),",-,–,£,€ \
	--shuffle_input_sentence \
	--input_sentence_size=10000000
```

```
This is the first sentence.
This is the second sentence and also the end of the paragraph.<eop>
Another paragraph.

Another document starts here.
```

```shell
python train.py
  --record_info_dir=$DATA/tfrecords \
  --train_batch_size=2048 \
  --seq_len=512 \
  --reuse_len=256 \
  --mem_len=384 \
  --perm_size=256 \
  --n_layer=24 \
  --d_model=1024 \
  --d_embed=1024 \
  --n_head=16 \
  --d_head=64 \
  --d_inner=4096 \
  --untie_r=True \
  --mask_alpha=6 \
  --mask_beta=1 \
  --num_predict=85
```

