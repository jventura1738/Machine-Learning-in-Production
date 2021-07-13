<div align="center">
<img src="https://raw.githubusercontent.com/google/jax/main/images/jax_logo_250px.png" alt="logo"></img>
</div>

# JAX: Autograd and XLA

![Continuous integration](https://github.com/google/jax/workflows/Continuous%20integration/badge.svg)
![PyPI version](https://img.shields.io/pypi/v/jax)

[**Quickstart**](#quickstart-colab-in-the-cloud)
| [**Transformations**](#transformations)
| [**Install guide**](#installation)
| [**Neural net libraries**](#neural-network-libraries)
| [**Change logs**](https://jax.readthedocs.io/en/latest/changelog.html)
| [**Reference docs**](https://jax.readthedocs.io/en/latest/)
| [**Code search**](https://cs.opensource.google/jax/jax)


**News:** [JAX tops largest-scale MLPerf Training 0.7 benchmarks!](https://cloud.google.com/blog/products/ai-machine-learning/google-breaks-ai-performance-records-in-mlperf-with-worlds-fastest-training-supercomputer)

## What is JAX?

JAX is [Autograd](https://github.com/hips/autograd) and [XLA](https://www.tensorflow.org/xla),
brought together for high-performance machine learning research.

With its updated version of [Autograd](https://github.com/hips/autograd),
JAX can automatically differentiate native
Python and NumPy functions. It can differentiate through loops, branches,
recursion, and closures, and it can take derivatives of derivatives of
derivatives. It supports reverse-mode differentiation (a.k.a. backpropagation)
via [`grad`](#automatic-differentiation-with-grad) as well as forward-mode differentiation,
and the two can be composed arbitrarily to any order.

What’s new is that JAX uses [XLA](https://www.tensorflow.org/xla)
to compile and run your NumPy programs on GPUs and TPUs. Compilation happens
under the hood by default, with library calls getting just-in-time compiled and
executed. But JAX also lets you just-in-time compile your own Python functions
into XLA-optimized kernels using a one-function API,
[`jit`](#compilation-with-jit). Compilation and automatic differentiation can be
composed arbitrarily, so you can express sophisticated algorithms and get
maximal performance without leaving Python. You can even program multiple GPUs
or TPU cores at once using [`pmap`](#spmd-programming-with-pmap), and
differentiate through the whole thing.

Dig a little deeper, and you'll see that JAX is really an extensible system for
[composable function transformations](#transformations). Both
[`grad`](#automatic-differentiation-with-grad) and [`jit`](#compilation-with-jit)
are instances of such transformations. Others are
[`vmap`](#auto-vectorization-with-vmap) for automatic vectorization and
[`pmap`](#spmd-programming-with-pmap) for single-program multiple-data (SPMD)
parallel programming of multiple accelerators, with more to come.

This is a research project, not an official Google product. Expect bugs and
[sharp edges](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html).
Please help by trying it out, [reporting
bugs](https://github.com/google/jax/issues), and letting us know what you
think!

```python
import jax.numpy as jnp
from jax import grad, jit, vmap

def predict(params, inputs):
  for W, b in params:
    outputs = jnp.dot(inputs, W) + b
    inputs = jnp.tanh(outputs)
  return outputs

def logprob_fun(params, inputs, targets):
  preds = predict(params, inputs)
  return jnp.sum((preds - targets)**2)

grad_fun = jit(grad(logprob_fun))  # compiled gradient evaluation function
perex_grads = jit(vmap(grad_fun, in_axes=(None, 0, 0)))  # fast per-example grads
```

### Contents
* [Quickstart: Colab in the Cloud](#quickstart-colab-in-the-cloud)
* [Transformations](#transformations)
* [Current gotchas](#current-gotchas)
* [Installation](#installation)
* [Neural net libraries](#neural-network-libraries)
* [Citing JAX](#citing-jax)
* [Reference documentation](#reference-documentation)

## Quickstart: Colab in the Cloud
Jump right in using a notebook in your browser, connected to a Google Cloud GPU.
Here are some starter notebooks:
- [The basics: NumPy on accelerators, `grad` for differentiation, `jit` for compilation, and `vmap` for vectorization](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html)
- [Training a Simple Neural Network, with TensorFlow Dataset Data Loading](https://colab.research.google.com/github/google/jax/blob/main/docs/notebooks/neural_network_with_tfds_data.ipynb)

**JAX now runs on Cloud TPUs.** To try out the preview, see the [Cloud TPU
Colabs](https://github.com/google/jax/tree/main/cloud_tpu_colabs).

For a deeper dive into JAX:
- [The Autodiff Cookbook, Part 1: easy and powerful automatic differentiation in JAX](https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html)
- [Common gotchas and sharp edges](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html)
- See the [full list of
notebooks](https://github.com/google/jax/tree/main/docs/notebooks).

You can also take a look at [the mini-libraries in
`jax.experimental`](https://github.com/google/jax/tree/main/jax/experimental/README.md),
like [`stax` for building neural
networks](https://github.com/google/jax/tree/main/jax/experimental/README.md#neural-net-building-with-stax)
and [`optimizers` for first-order stochastic
optimization](https://github.com/google/jax/tree/main/jax/experimental/README.md#first-order-optimization),
or the [examples](https://github.com/google/jax/tree/main/examples).

## Transformations

At its core, JAX is an extensible system for transforming numerical functions.
Here are four of primary interest: `grad`, `jit`, `vmap`, and `pmap`.

### Automatic differentiation with `grad`

JAX has roughly the same API as [Autograd](https://github.com/hips/autograd).
The most popular function is
[`grad`](https://jax.readthedocs.io/en/latest/jax.html#jax.grad)
for reverse-mode gradients:

```python
from jax import grad
import jax.numpy as jnp

def tanh(x):  # Define a function
  y = jnp.exp(-2.0 * x)
  return (1.0 - y) / (1.0 + y)

grad_tanh = grad(tanh)  # Obtain its gradient function
print(grad_tanh(1.0))   # Evaluate it at x = 1.0
# prints 0.4199743
```

You can differentiate to any order with `grad`.

```python
print(grad(grad(grad(tanh)))(1.0))
# prints 0.62162673
```

For more advanced autodiff, you can use
[`jax.vjp`](https://jax.readthedocs.io/en/latest/jax.html#jax.vjp) for
reverse-mode vector-Jacobian products and
[`jax.jvp`](https://jax.readthedocs.io/en/latest/jax.html#jax.jvp) for
forward-mode Jacobian-vector products. The two can be composed arbitrarily with
one another, and with other JAX transformations. Here's one way to compose those
to make a function that efficiently computes [full Hessian
matrices](https://jax.readthedocs.io/en/latest/jax.html#jax.hessian):

```python
from jax import jit, jacfwd, jacrev

def hessian(fun):
  return jit(jacfwd(jacrev(fun)))
```

As with [Autograd](https://github.com/hips/autograd), you're free to use
differentiation with Python control structures:

```python
def abs_val(x):
  if x > 0:
    return x
  else:
    return -x

abs_val_grad = grad(abs_val)
print(abs_val_grad(1.0))   # prints 1.0
print(abs_val_grad(-1.0))  # prints -1.0 (abs_val is re-evaluated)
```

See the [reference docs on automatic
differentiation](https://jax.readthedocs.io/en/latest/jax.html#automatic-differentiation)
and the [JAX Autodiff
Cookbook](https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html)
for more.

### Compilation with `jit`

You can use XLA to compile your functions end-to-end with
[`jit`](https://jax.readthedocs.io/en/latest/jax.html#just-in-time-compilation-jit),
used either as an `@jit` decorator or as a higher-order function.

```python
import jax.numpy as jnp
from jax import jit

def slow_f(x):
  # Element-wise ops see a large benefit from fusion
  return x * x + x * 2.0

x = jnp.ones((5000, 5000))
fast_f = jit(slow_f)
%timeit -n10 -r3 fast_f(x)  # ~ 4.5 ms / loop on Titan X
%timeit -n10 -r3 slow_f(x)  # ~ 14.5 ms / loop (also on GPU via JAX)
```

You can mix `jit` and `grad` and any other JAX transformation however you like.

Using `jit` puts constraints on the kind of Python control flow
the function can use; see
the [Gotchas
Notebook](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#python-control-flow-+-JIT)
for more.

### Auto-vectorization with `vmap`

[`vmap`](https://jax.readthedocs.io/en/latest/jax.html#vectorization-vmap) is
the vectorizing map.
It has the familiar semantics of mapping a function along array axes, but
instead of keeping the loop on the outside, it pushes the loop down into a
function’s primitive operations for better performance.

Using `vmap` can save you from having to carry around batch dimensions in your
code. For example, consider this simple *unbatched* neural network prediction
function:

```python
def predict(params, input_vec):
  assert input_vec.ndim == 1
  activations = input_vec
  for W, b in params:
    outputs = jnp.dot(W, activations) + b  # `activations` on the right-hand side!
    activations = jnp.tanh(outputs)
  return outputs
```

We often instead write `jnp.dot(activations, W)` to allow for a batch dimension on the
left side of `activations`, but we’ve written this particular prediction function to
apply only to single input vectors. If we wanted to apply this function to a
batch of inputs at once, semantically we could just write

```python
from functools import partial
predictions = jnp.stack(list(map(partial(predict, params), input_batch)))
```

But pushing one example through the network at a time would be slow! It’s better
to vectorize the computation, so that at every layer we’re doing matrix-matrix
multiplication rather than matrix-vector multiplication.

The `vmap` function does that transformation for us. That is, if we write

```python
from jax import vmap
predictions = vmap(partial(predict, params))(input_batch)
# or, alternatively
predictions = vmap(predict, in_axes=(None, 0))(params, input_batch)
```

then the `vmap` function will push the outer loop inside the function, and our
machine will end up executing matrix-matrix multiplications exactly as if we’d
done the batching by hand.

It’s easy enough to manually batch a simple neural network without `vmap`, but
in other cases manual vectorization can be impractical or impossible. Take the
problem of efficiently computing per-example gradients: that is, for a fixed set
of parameters, we want to compute the gradient of our loss function evaluated
separately at each example in a batch. With `vmap`, it’s easy:

```python
per_example_gradients = vmap(partial(grad(loss), params))(inputs, targets)
```

Of course, `vmap` can be arbitrarily composed with `jit`, `grad`, and any other
JAX transformation! We use `vmap` with both forward- and reverse-mode automatic
differentiation for fast Jacobian and Hessian matrix calculations in
`jax.jacfwd`, `jax.jacrev`, and `jax.hessian`.

### SPMD programming with `pmap`

For parallel programming of multiple accelerators, like multiple GPUs, use
[`pmap`](https://jax.readthedocs.io/en/latest/jax.html#parallelization-pmap).
With `pmap` you write single-program multiple-data (SPMD) programs, including
fast parallel collective communication operations. Applying `pmap` will mean
that the function you write is compiled by XLA (similarly to `jit`), then
replicated and executed in parallel across devices.

Here's an example on an 8-GPU machine:

```python
from jax import random, pmap
import jax.numpy as jnp

# Create 8 random 5000 x 6000 matrices, one per GPU
keys = random.split(random.PRNGKey(0), 8)
mats = pmap(lambda key: random.normal(key, (5000, 6000)))(keys)

# Run a local matmul on each device in parallel (no data transfer)
result = pmap(lambda x: jnp.dot(x, x.T))(mats)  # result.shape is (8, 5000, 5000)

# Compute the mean on each device in parallel and print the result
print(pmap(jnp.mean)(result))
# prints [1.1566595 1.1805978 ... 1.2321935 1.2015157]
```

In addition to expressing pure maps, you can use fast [collective communication
operations](https://jax.readthedocs.io/en/latest/jax.lax.html#parallel-operators)
between devices:

```python
from functools import partial
from jax import lax

@partial(pmap, axis_name='i')
def normalize(x):
  return x / lax.psum(x, 'i')

print(normalize(jnp.arange(4.)))
# prints [0.         0.16666667 0.33333334 0.5       ]
```

You can even [nest `pmap` functions](https://colab.research.google.com/github/google/jax/blob/main/cloud_tpu_colabs/Pmap_Cookbook.ipynb#scrollTo=MdRscR5MONuN) for more
sophisticated communication patterns.

It all composes, so you're free to differentiate through parallel computations:

```python
from jax import grad

@pmap
def f(x):
  y = jnp.sin(x)
  @pmap
  def g(z):
    return jnp.cos(z) * jnp.tan(y.sum()) * jnp.tanh(x).sum()
  return grad(lambda w: jnp.sum(g(w)))(x)

print(f(x))
# [[ 0.        , -0.7170853 ],
#  [-3.1085174 , -0.4824318 ],
#  [10.366636  , 13.135289  ],
#  [ 0.22163185, -0.52112055]]

print(grad(lambda x: jnp.sum(f(x)))(x))
# [[ -3.2369726,  -1.6356447],
#  [  4.7572474,  11.606951 ],
#  [-98.524414 ,  42.76499  ],
#  [ -1.6007166,  -1.2568436]]
```

When reverse-mode differentiating a `pmap` function (e.g. with `grad`), the
backward pass of the computation is parallelized just like the forward pass.

See the [SPMD
Cookbook](https://colab.research.google.com/github/google/jax/blob/main/cloud_tpu_colabs/Pmap_Cookbook.ipynb)
and the [SPMD MNIST classifier from scratch
example](https://github.com/google/jax/blob/main/examples/spmd_mnist_classifier_fromscratch.py)
for more.

## Current gotchas

For a more thorough survey of current gotchas, with examples and explanations,
we highly recommend reading the [Gotchas
Notebook](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html).
Some standouts:

1. JAX transformations only work on [pure functions](https://en.wikipedia.org/wiki/Pure_function), which don't have side-effects and respect [referential transparency](https://en.wikipedia.org/wiki/Referential_transparency) (i.e. object identity testing with `is` isn't preserved). If you use a JAX transformation on an impure Python function, you might see an error like `Exception: Can't lift Traced...`  or `Exception: Different traces at same level`.
1. [In-place mutating updates of
   arrays](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#%F0%9F%94%AA-In-Place-Updates), like `x[i] += y`, aren't supported, but [there are functional alternatives](https://jax.readthedocs.io/en/latest/jax.ops.html). Under a `jit`, those functional alternatives will reuse buffers in-place automatically.
1. [Random numbers are
   different](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#%F0%9F%94%AA-Random-Numbers), but for [good reasons](https://github.com/google/jax/blob/main/design_notes/prng.md).
1. If you're looking for [convolution
   operators](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#%F0%9F%94%AA-Convolutions),
   they're in the `jax.lax` package.
1. JAX enforces single-precision (32-bit, e.g. `float32`) values by default, and
   [to enable
   double-precision](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#Double-(64bit)-precision)
   (64-bit, e.g. `float64`) one needs to set the `jax_enable_x64` variable at
   startup (or set the environment variable `JAX_ENABLE_X64=True`).
1. Some of NumPy's dtype promotion semantics involving a mix of Python scalars
   and NumPy types aren't preserved, namely `np.add(1, np.array([2],
   np.float32)).dtype` is `float64` rather than `float32`.
1. Some transformations, like `jit`, [constrain how you can use Python control
   flow](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html#%F0%9F%94%AA-Control-Flow).
   You'll always get loud errors if something goes wrong. You might have to use
   [`jit`'s `static_argnums`
   parameter](https://jax.readthedocs.io/en/latest/jax.html#just-in-time-compilation-jit),
   [structured control flow
   primitives](https://jax.readthedocs.io/en/latest/jax.lax.html#control-flow-operators)
   like
   [`lax.scan`](https://jax.readthedocs.io/en/latest/_autosummary/jax.lax.scan.html#jax.lax.scan),
   or just use `jit` on smaller subfunctions.

## Installation

JAX is written in pure Python, but it depends on XLA, which needs to be
installed as the `jaxlib` package. Use the following instructions to install a
binary package with `pip`, or to build JAX from source.

We support installing or building `jaxlib` on Linux (Ubuntu 16.04 or later) and
macOS (10.12 or later) platforms. Windows users can use JAX on CPU and GPU via
the
[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about).
There is some initial native Windows support, but since it is still somewhat
immature, there are no binary releases and it must be
[built from source](https://jax.readthedocs.io/en/latest/developer.html#additional-notes-for-building-jaxlib-from-source-on-windows).

### pip installation: CPU

To install a CPU-only version of JAX, which might be useful for doing local
development on a laptop, you can run

```bash
pip install --upgrade pip
pip install --upgrade "jax[cpu]"
```

On Linux, it is often necessary to first update `pip` to a version that supports
`manylinux2010` wheels.

### pip installation: GPU (CUDA)

If you want to install JAX with both CPU and NVidia GPU support, you must first
install [CUDA](https://developer.nvidia.com/cuda-downloads) and
[CuDNN](https://developer.nvidia.com/CUDNN),
if they have not already been installed. Unlike some other popular deep
learning systems, JAX does not bundle CUDA or CuDNN as part of the `pip`
package. The CUDA 10 JAX wheels require CuDNN 7, whereas the CUDA 11 wheels of
JAX require CuDNN 8. Other combinations of CUDA and CuDNN are possible but
require building from source.

Next, run

```bash
pip install --upgrade pip
pip install --upgrade "jax[cuda111]" -f https://storage.googleapis.com/jax-releases/jax_releases.html
```

The jaxlib version must correspond to the version of the existing CUDA
installation you want to use:
* For CUDA 11.1, 11.2, or 11.3, use `cuda111`. The same wheel should work for
  CUDA 11.x releases from 11.1 onwards.
* For CUDA 11.0, use `cuda110`.
* For CUDA 10.2, use `cuda102`.
* For CUDA 10.1, use `cuda101`.
* Older CUDA versions are not supported.

You can find your CUDA version with the command:

```bash
nvcc --version
```

Some GPU functionality expects the CUDA installation to be at
`/usr/local/cuda-X.X`, where X.X should be replaced with the CUDA version number
(e.g. `cuda-10.2`). If CUDA is installed elsewhere on your system, you can either
create a symlink:

```bash
sudo ln -s /path/to/cuda /usr/local/cuda-X.X
```

Please let us know on [the issue tracker](https://github.com/google/jax/issues)
if you run into any errors or problems with the prebuilt wheels.

### pip installation: Google Cloud TPU
JAX also provides pre-built wheels for
[Google Cloud TPU](https://cloud.google.com/tpu/docs/users-guide-tpu-vm).
To install JAX along with appropriate versions of `jaxlib` and `libtpu`, you can run
the following in your cloud TPU VM:
```bash
pip install --upgrade pip
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

### Building JAX from source
See [Building JAX from
source](https://jax.readthedocs.io/en/latest/developer.html#building-from-source).

## Neural network libraries

Multiple Google research groups develop and share libraries for training neural
networks in JAX. If you want a fully featured library for neural network
training with examples and how-to guides, try
[Flax](https://github.com/google/flax). Another option is
[Trax](https://github.com/google/trax), a combinator-based framework focused on
ease-of-use and end-to-end single-command examples, especially for sequence
models and reinforcement learning. Finally,
[Objax](https://github.com/google/objax) is a minimalist object-oriented
framework with a PyTorch-like interface.

DeepMind has open-sourced an
[ecosystem of libraries around JAX](https://deepmind.com/blog/article/using-jax-to-accelerate-our-research) including [Haiku](https://github.com/deepmind/dm-haiku) for neural
network modules, [Optax](https://github.com/deepmind/optax) for gradient
processing and optimization, [RLax](https://github.com/deepmind/rlax) for RL
algorithms, and [chex](https://github.com/deepmind/chex) for reliable code and
testing. (Watch the NeurIPS 2020 JAX Ecosystem at DeepMind talk [here](https://www.youtube.com/watch?v=iDxJxIyzSiM))

## Citing JAX

To cite this repository:

```
@software{jax2018github,
  author = {James Bradbury and Roy Frostig and Peter Hawkins and Matthew James Johnson and Chris Leary and Dougal Maclaurin and George Necula and Adam Paszke and Jake Vander{P}las and Skye Wanderman-{M}ilne and Qiao Zhang},
  title = {{JAX}: composable transformations of {P}ython+{N}um{P}y programs},
  url = {http://github.com/google/jax},
  version = {0.2.5},
  year = {2018},
}
```

In the above bibtex entry, names are in alphabetical order, the version number
is intended to be that from [jax/version.py](../main/jax/version.py), and
the year corresponds to the project's open-source release.

A nascent version of JAX, supporting only automatic differentiation and
compilation to XLA, was described in a [paper that appeared at SysML
2018](https://mlsys.org/Conferences/2019/doc/2018/146.pdf). We're currently working on
covering JAX's ideas and capabilities in a more comprehensive and up-to-date
paper.

## Reference documentation

For details about the JAX API, see the
[reference documentation](https://jax.readthedocs.io/).

For getting started as a JAX developer, see the
[developer documentation](https://jax.readthedocs.io/en/latest/developer.html).
