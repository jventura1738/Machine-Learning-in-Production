Node.js Addon Examples
=========================================

**A repository of [Node.js Addons](https://nodejs.org/api/addons.html#addons_c_addons) examples.**

Implementations of examples are named either after Node.js versions (`node_0.10`,
`node_0.12`, etc), or Node.js addon implementation APIs:

- [`nan`](https://github.com/nodejs/nan): C++-based abstraction between Node and direct V8 APIs.
- [`Node-API`](https://nodejs.org/api/n-api.html): C-based API guaranteeing [ABI stability](https://nodejs.org/en/docs/guides/abi-stability/) across different node versions as well as JavaScript engines. (Node-API was previously known as N-API.)
- [`node-addon-api`](https://github.com/nodejs/node-addon-api): header-only C++ wrapper classes which simplify the use of the C-based Node-API.

Implementations against unsupported versions of Node.js are provided for
completeness and historical context. They are not maintained.

The examples are primarily maintained for Node-API and node-addon-api and as outlined in
the Node.js [documentation](https://nodejs.org/dist/latest/docs/api/addons.html), 
unless there is a need for direct access to functionality which
is not exposed by Node-API, use Node-API. 

The [Node-API Resource](http://nodejs.github.io/node-addon-examples/) offers an 
excellent orientation and tips for developers just getting started with Node-API 
and `node-addon-api`.

## Usage

The directory structure is as follows:

```
<name of example>
  |
  +--- <implementation 1>
  |      |
  |      +--- files...
  +--- <implementation 2>
  .      |
  .      +--- files...
  .
```


In each example's implementation subdirectory, run

```text
$ npm install
$ node ./
```

to see the example in action.

