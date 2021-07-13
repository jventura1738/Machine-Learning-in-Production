# nconf

[![Version npm](https://img.shields.io/npm/v/nconf.svg?style=flat-square)](https://www.npmjs.com/package/nconf)[![npm Downloads](https://img.shields.io/npm/dm/nconf.svg?style=flat-square)](https://www.npmjs.com/package/nconf)[![Build Status](https://img.shields.io/travis/indexzero/nconf/master.svg?style=flat-square)](https://travis-ci.org/indexzero/nconf)[![Coverage](https://img.shields.io/coveralls/indexzero/nconf.svg?style=flat-square)](https://coveralls.io/github/indexzero/nconf)[![Dependencies](https://img.shields.io/david/indexzero/nconf.svg?style=flat-square)](https://david-dm.org/indexzero/nconf)

Hierarchical node.js configuration with files, environment variables, command-line arguments, and atomic object merging.

## Example
Using nconf is easy; it is designed to be a simple key-value store with support for both local and remote storage. Keys are namespaced and delimited by `:`. Let's dive right into sample usage:

``` js
  // sample.js
  var nconf = require('nconf');

  //
  // Setup nconf to use (in-order):
  //   1. Command-line arguments
  //   2. Environment variables
  //   3. A file located at 'path/to/config.json'
  //
  nconf.argv()
   .env()
   .file({ file: 'path/to/config.json' });

  //
  // Set a few variables on `nconf`.
  //
  nconf.set('database:host', '127.0.0.1');
  nconf.set('database:port', 5984);

  //
  // Get the entire database object from nconf. This will output
  // { host: '127.0.0.1', port: 5984 }
  //
  console.log('foo: ' + nconf.get('foo'));
  console.log('NODE_ENV: ' + nconf.get('NODE_ENV'));
  console.log('database: ' + nconf.get('database'));

  //
  // Save the configuration object to disk
  //
  nconf.save(function (err) {
    require('fs').readFile('path/to/your/config.json', function (err, data) {
      console.dir(JSON.parse(data.toString()))
    });
  });
```

If you run the below script:

``` bash
  $ NODE_ENV=production node sample.js --foo bar
```

The output will be:

```
  foo: bar
  NODE_ENV: production
  database: { host: '127.0.0.1', port: 5984 }
```

## Hierarchical configuration

Configuration management can get complicated very quickly for even trivial applications running in production. `nconf` addresses this problem by enabling you to setup a hierarchy for different sources of configuration with no defaults. **The order in which you attach these configuration sources determines their priority in the hierarchy.** Let's take a look at the options available to you

  1. **nconf.argv(options)** Loads `process.argv` using yargs. If `options` is supplied it is passed along to yargs.
  2. **nconf.env(options)** Loads `process.env` into the hierarchy.
  3. **nconf.file(options)** Loads the configuration data at options.file into the hierarchy.
  4. **nconf.defaults(options)** Loads the data in options.store into the hierarchy.
  5. **nconf.overrides(options)** Loads the data in options.store into the hierarchy.

A sane default for this could be:

``` js
  var nconf = require('nconf');

  //
  // 1. any overrides
  //
  nconf.overrides({
    'always': 'be this value'
  });

  //
  // 2. `process.env`
  // 3. `process.argv`
  //
  nconf.env().argv();

  //
  // 4. Values in `config.json`
  //
  nconf.file('/path/to/config.json');

  //
  // Or with a custom name
  // Note: A custom key must be supplied for hierarchy to work if multiple files are used.
  //
  nconf.file('custom', '/path/to/config.json');

  //
  // Or searching from a base directory.
  // Note: `name` is optional.
  //
  nconf.file(name, {
    file: 'config.json',
    dir: 'search/from/here',
    search: true
  });

  //
  // 5. Any default values
  //
  nconf.defaults({
    'if nothing else': 'use this value'
  });
```

## API Documentation

The top-level of `nconf` is an instance of the `nconf.Provider` abstracts this all for you into a simple API.

### nconf.add(name, options)
Adds a new store with the specified `name` and `options`. If `options.type` is not set, then `name` will be used instead:

``` js
  nconf.add('supplied', { type: 'literal', store: { 'some': 'config' } });
  nconf.add('user', { type: 'file', file: '/path/to/userconf.json' });
  nconf.add('global', { type: 'file', file: '/path/to/globalconf.json' });
```

### nconf.any(names, callback)
Given a set of key names, gets the value of the first key found to be truthy. The key names can be given as separate arguments
or as an array. If the last argument is a function, it will be called with the result; otherwise, the value is returned.

``` js
  //
  // Get one of 'NODEJS_PORT' and 'PORT' as a return value
  //
  var port = nconf.any('NODEJS_PORT', 'PORT');

  //
  // Get one of 'NODEJS_IP' and 'IPADDRESS' using a callback
  //
  nconf.any(['NODEJS_IP', 'IPADDRESS'], function(err, value) {
    console.log('Connect to IP address ' + value);
  });
```

### nconf.use(name, options)
Similar to `nconf.add`, except that it can replace an existing store if new options are provided

``` js
  //
  // Load a file store onto nconf with the specified settings
  //
  nconf.use('file', { file: '/path/to/some/config-file.json' });

  //
  // Replace the file store with new settings
  //
  nconf.use('file', { file: 'path/to/a-new/config-file.json' });
```

### nconf.remove(name)
Removes the store with the specified `name.` The configuration stored at that level will no longer be used for lookup(s).

``` js
  nconf.remove('file');
```

### nconf.required(keys)
Declares a set of string keys to be mandatory, and throw an error if any are missing.

``` js
  nconf.defaults({
    keya: 'a',
  });

  nconf.required(['keya', 'keyb']);
  // Error: Missing required keys: keyb
```
You can also chain `.required()` calls when needed. for example when a configuration depends on another configuration store

```js
config
  .argv()
  .env()
  .required([ 'STAGE']) //here you should have STAGE otherwise throw an error
  .file( 'stage', path.resolve( 'configs', 'stages', config.get( 'STAGE' ) + '.json' ) )
  .required([ 'OAUTH:redirectURL']) // here you should have OAUTH:redirectURL, otherwise throw an error
  .file( 'oauth', path.resolve( 'configs', 'oauth', config.get( 'OAUTH:MODE' ) + '.json' ) )
  .file( 'app', path.resolve( 'configs', 'app.json' ) )
  .required([ 'LOGS_MODE']) // here you should haveLOGS_MODE, otherwise throw an error
  .add( 'logs', {
    type: 'literal',
    store: require( path.resolve( 'configs', 'logs', config.get( 'LOGS_MODE' ) + '.js') )
  } )
  .defaults( defaults );
```

## Storage Engines

### Memory
A simple in-memory storage engine that stores a nested JSON representation of the configuration. To use this engine, just call `.use()` with the appropriate arguments. All calls to `.get()`, `.set()`, `.clear()`, `.reset()` methods are synchronous since we are only dealing with an in-memory object.

All built-in storage engines inherit from the Memory store.

Basic usage:

``` js
  nconf.use('memory');
```

#### Options

The options defined below apply to all storage engines that inherit from Memory.

##### `accessSeparator: string` (default: `':'`)
Defines the separator used to get or set data using the `get()` and `set()` methods. Even if this is changed, the default "colon" separator will be available unless explicitly disabled (see `disableDefaultAccessSeparator`).

##### `inputSeparator: string` (default: `'__'`)
This option is used by the `argv` and `env` storage engines when loading values. Since most systems only allow dashes, underscores, and alphanumeric characters in environment variables and command line arguments, the `inputSeparator` provides a mechanism for loading hierarchical values from these sources.

##### `disableDefaultAccessSeparator: {true|false}` (default: `false`)
Disables the default access separator of `':'`, which is always available otherwise. This is mainly used to preserve legacy behavior. It can also be used to set keys that contain the default separator (e.g. `{ 'some:long:key' : 'some value' }`).

### Argv
Responsible for loading the values parsed from `process.argv` by `yargs` into the configuration hierarchy. See the [yargs option docs](https://github.com/bcoe/yargs#optionskey-opt) for more on the option format.

#### Options

##### `parseValues: {true|false}` (default: `false`)
Attempt to parse well-known values (e.g. 'false', 'true', 'null', 'undefined', '3', '5.1' and JSON values)
into their proper types. If a value cannot be parsed, it will remain a string.

##### `transform: function(obj)`
Pass each key/value pair to the specified function for transformation.

The input `obj` contains two properties passed in the following format:
``` js
{
  key: '<string>',
  value: '<string>'
}
```

The transformation function may alter both the key and the value.

The function may return either an object in the same format as the input or a value that evaluates to false.
If the return value is falsey, the entry will be dropped from the store, otherwise it will replace the original key/value.

*Note: If the return value doesn't adhere to the above rules, an exception will be thrown.*

#### Examples

``` js
  //
  // Can optionally also be an object literal to pass to `yargs`.
  //
  nconf.argv({
    "x": {
      alias: 'example',
      describe: 'Example description for usage generation',
      demand: true,
      default: 'some-value',
      parseValues: true,
      transform: function(obj) {
        if (obj.key === 'foo') {
          obj.value = 'baz';
        }
        return obj;
      }
    }
  });
```

It's also possible to pass a configured yargs instance

``` js
  nconf.argv(require('yargs')
    .version('1.2.3')
    .usage('My usage definition')
    .strict()
    .options({
      "x": {
        alias: 'example',
        describe: 'Example description for usage generation',
        demand: true,
        default: 'some-value'
      }
    }));
```

### Env
Responsible for loading the values parsed from `process.env` into the configuration hierarchy.
By default, the env variables values are loaded into the configuration as strings.

#### Options

##### `lowerCase: {true|false}` (default: `false`)
Convert all input keys to lower case. Values are not modified.

If this option is enabled, all calls to `nconf.get()` must pass in a lowercase string (e.g. `nconf.get('port')`)

##### `parseValues: {true|false}` (default: `false`)
Attempt to parse well-known values (e.g. 'false', 'true', 'null', 'undefined', '3', '5.1' and JSON values)
into their proper types. If a value cannot be parsed, it will remain a string.

##### `transform: function(obj)`
Pass each key/value pair to the specified function for transformation.

The input `obj` contains two properties passed in the following format:
``` js
{
  key: '<string>',
  value: '<string>'
}
```

The transformation function may alter both the key and the value.

The function may return either an object in the asme format as the input or a value that evaluates to false.
If the return value is falsey, the entry will be dropped from the store, otherwise it will replace the original key/value.

*Note: If the return value doesn't adhere to the above rules, an exception will be thrown.*

#### `readOnly: {true|false}` (default: `true`)
Allow values in the env store to be updated in the future. The default is to not allow items in the env store to be updated.

#### Examples

``` js
  //
  // Can optionally also be an Array of values to limit process.env to.
  //
  nconf.env(['only', 'load', 'these', 'values', 'from', 'process.env']);

  //
  // Can also specify an input separator for nested keys
  //
  nconf.env('__');
  // Get the value of the env variable 'database__host'
  var dbHost = nconf.get('database:host');

  //
  // Can also lowerCase keys.
  // Especially handy when dealing with environment variables which are usually
  // uppercased while argv are lowercased.
  //

  // Given an environment variable PORT=3001
  nconf.env();
  var port = nconf.get('port') // undefined

  nconf.env({ lowerCase: true });
  var port = nconf.get('port') // 3001

  //
  // Or use all options
  //
  nconf.env({
    inputSeparator: '__',
    match: /^whatever_matches_this_will_be_whitelisted/
    whitelist: ['database__host', 'only', 'load', 'these', 'values', 'if', 'whatever_doesnt_match_but_is_whitelisted_gets_loaded_too'],
    lowerCase: true,
    parseValues: true,
    transform: function(obj) {
      if (obj.key === 'foo') {
        obj.value = 'baz';
      }
      return obj;
    }
  });
  var dbHost = nconf.get('database:host');
```

### Literal
Loads a given object literal into the configuration hierarchy. Both `nconf.defaults()` and `nconf.overrides()` use the Literal store.

``` js
  nconf.defaults({
    'some': 'default value'
  });
```

### File
Based on the Memory store, but provides additional methods `.save()` and `.load()` which allow you to read your configuration to and from file. As with the Memory store, all method calls are synchronous with the exception of `.save()` and `.load()` which take callback functions.

It is important to note that setting keys in the File engine will not be persisted to disk until a call to `.save()` is made. Note a custom key must be supplied as the first parameter for hierarchy to work if multiple files are used.

``` js
  nconf.file('path/to/your/config.json');
  // add multiple files, hierarchically. notice the unique key for each file
  nconf.file('user', 'path/to/your/user.json');
  nconf.file('global', 'path/to/your/global.json');
```

The file store is also extensible for multiple file formats, defaulting to `JSON`. To use a custom format, simply pass a format object to the `.use()` method. This object must have `.parse()` and `.stringify()` methods just like the native `JSON` object.

If the file does not exist at the provided path, the store will simply be empty.

#### Encrypting file contents

As of `nconf@0.8.0` it is now possible to encrypt and decrypt file contents using the `secure` option:

``` js
nconf.file('secure-file', {
  file: 'path/to/secure-file.json',
  secure: {
    secret: 'super-secretzzz-keyzz',
    alg: 'aes-256-ctr'
  }
})
```

This will encrypt each key using [`crypto.createCipheriv`](https://nodejs.org/api/crypto.html#crypto_crypto_createcipheriv_algorithm_key_iv_options), defaulting to `aes-256-ctr`. The encrypted file contents will look like this:

``` js
{
  "config-key-name": {
    "alg": "aes-256-ctr", // cipher used
    "value": "af07fbcf",   // encrypted contents
    "iv": "49e7803a2a5ef98c7a51a8902b76dd10" // initialization vector
  },
  "another-config-key": {
    "alg": "aes-256-ctr",   // cipher used
    "value": "e310f6d94f13", // encrypted contents
    "iv": "b654e01aed262f37d0acf200be193985" // initialization vector
  },
}
```

### Redis
There is a separate Redis-based store available through [nconf-redis][0]. To install and use this store simply:

``` bash
  $ npm install nconf
  $ npm install nconf-redis
```

Once installing both `nconf` and `nconf-redis`, you must require both modules to use the Redis store:

``` js
  var nconf = require('nconf');

  //
  // Requiring `nconf-redis` will extend the `nconf`
  // module.
  //
  require('nconf-redis');

  nconf.use('redis', { host: 'localhost', port: 6379, ttl: 60 * 60 * 1000 });
```

## Installation
``` bash
  npm install nconf --save
```

## Run Tests
Tests are written in vows and give complete coverage of all APIs and storage engines.

``` bash
  $ npm test
```

#### Author: [Charlie Robbins](http://nodejitsu.com)
#### License: MIT

[0]: http://github.com/indexzero/nconf-redis
