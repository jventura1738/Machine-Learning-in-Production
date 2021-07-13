# Hound

[![Build Status](https://travis-ci.org/hound-search/hound.svg?branch=master)](https://travis-ci.org/hound-search/hound)
[![.github/workflows/go.yaml](https://github.com/hound-search/hound/workflows/.github/workflows/go.yaml/badge.svg)](https://github.com/hound-search/hound/actions)

> ## :warning: Hound's default branch name has changed! :warning:
> **We renamed our default branch from `master` to `main` on February 24, 2021**. We used [Github's branch renaming feature](https://github.com/github/renaming/#renaming-existing-branches), which means that any open pull requests should be automatically re-targeted, and web requests pointing to code on the `master` branch should redirect as expected. This change should mostly be invisible, but you will need to update any code that explicitly relies on the existence of Hound's `master` branch.

Hound is an extremely fast source code search engine. The core is based on this article (and code) from Russ Cox:
[Regular Expression Matching with a Trigram Index](http://swtch.com/~rsc/regexp/regexp4.html). Hound itself is a static
[React](http://facebook.github.io/react/) frontend that talks to a [Go](http://golang.org/) backend. The backend keeps an up-to-date index for each repository and answers searches through a minimal API. Here it is in action:

![Hound Screen Capture](imgs/screen_capture.gif)

## Quick Start Guide

### Using Go Tools


0. [Install Go](https://golang.org/doc/install) if you don't have it already. Hound requires version 1.4 or later. 
You might also want to define a [`GOPATH`](https://github.com/golang/go/wiki/GOPATH) environment variable) 
(it defaults to $HOME/go if you don't explicitly have one set). If everything is installed properly, `go version` should 
print out the installed version of go. 

1. Use the Go tools to install Hound. The binaries `houndd` (server) and `hound` (cli) will be installed in your $GOPATH/bin directory. Your $GOPATH should be in your $PATH (`echo $PATH` to check).


```
go get github.com/hound-search/hound/cmds/...
```

2. Create a config.json file and use it to list your repositories. Check out our [example-config.json](config-example.json) 
to see how to set up various types of repositories. For example, we can configure Hound to search its own source code using 
the config found in [default-config.json](default-config.json):

```json
{
  "dbpath" : "db",
  "repos" : {
    "Hound" : { "url" : "https://github.com/etsy/hound.git" }
  }
}
```


A complete list of available config options can be found [here](docs/config-options.md).  
3. Run the Hound server with `houndd` in the same directory as your `config.json`. You should see output similar to:
```
2015/03/13 09:07:42 Searcher started for statsd
2015/03/13 09:07:42 Searcher started for Hound
2015/03/13 09:07:42 All indexes built!
2015/03/13 09:07:42 running server at http://localhost:6080
```

4. By default, hound hosts a web ui at http://localhost:6080 . Open it in your browser, and start searching.

### Using Docker (1.4+)

0. [Install the docker](https://docs.docker.com/get-docker/) if you don't have it. We need at least `Docker >= 1.14`.

1. Create a config.json file and use it to list your repositories. Check out our [example-config.json](config-example.json) 
to see how to set up various types of repositories. For example, we can configure Hound to search its own source code using 
the config found in [default-config.json](default-config.json). 

2. Run 
```
docker run -d -p 6080:6080 --name hound -v $(pwd):/data etsy/hound
```

You should be able to navigate to [http://localhost:6080/](http://localhost:6080/) as usual. 

## Running in Production

There are no special flags to run Hound in production. You can use the `--addr=:6880` flag to control the port to which the server binds. 
Currently, Hound does not support TLS as most users simply run Hound behind either Apache or nginx. However, we are open to contributions to add TLS support.

## Why Another Code Search Tool?

We've used many similar tools in the past, and most of them are either too slow, too hard to configure, or require too much software to be installed.
Which brings us to...

## Requirements
* Go 1.13+

Yup, that's it. You can proxy requests to the Go service through Apache/nginx/etc., but that's not required.


## Support

Currently Hound is only tested on MacOS and CentOS, but it should work on any *nix system. Hound on Windows is not supported but we've heard it compiles and runs just fine (although it helps to to exclude your data folder from Windows Search Indexer).

Hound supports the following version control systems: 

* Git - This is the default
* Mercurial - use `"vcs" : "hg"` in the config
* SVN - use `"vcs" : "svn"` in the config
* Bazaar - use `"vcs" : "bzr"` in the config

See [config-example.json](config-example.json) for examples of how to use each VCS.

## Private Repositories

There are a couple of ways to get Hound to index private repositories:

* Use the `file://` protocol. This allows you to index a local clone of a repository. The downside here is that the polling to keep the repo up to date will
not work. (This also doesn't work on local folders that are not of a supported repository type.) If you're using Docker, you must mount a volume to your repository (e.g., `-v $(pwd)/src:/src`) and use the relative path to the repo in your configuration.
* Use SSH style URLs in the config: `"url" : "git@github.com:foo/bar.git"`. As long as you have your 
[SSH keys](https://help.github.com/articles/generating-ssh-keys/) set up on the box where Hound is running this will work.

## Keeping Repos Updated

By default Hound polls the URL in the config for updates every 30 seconds. You can override this value by setting the `ms-between-poll` key on a per repo basis in the config. If you are indexing a large number of repositories, you may also be interested in tweaking the `max-concurrent-indexers` property. You can see how these work in the [example config](config-example.json). 

## Editor Integration

Currently the following editors have plugins that support Hound:

* [Sublime Text](https://github.com/bgreenlee/SublimeHound)
* [Vim](https://github.com/urthbound/hound.vim)
* [Emacs](https://github.com/ryoung786/hound.el)
* [Visual Studio Code](https://github.com/sjzext/vscode-hound)

## Hacking on Hound

### Editing & Building

#### Requirements:
 * make
 * Node.js ([Installation Instructions](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager))

Hound includes a `Makefile` to aid in building locally, but it depends on the source being added to a proper Go workspace so that
Go tools work accordingly. See [Setting GOPATH](https://github.com/golang/go/wiki/SettingGOPATH) for further details about setting
up your Go workspace. With a `GOPATH` set, the following commands will build hound locally.

```
git clone https://github.com/hound-search/hound.git ${GOPATH}/src/github.com/hound-search/hound
cd ${GOPATH}/src/github.com/hound-search/hound
make
```

If this is your only Go project, you can set your GOPATH just for Hound:
```
git clone https://github.com/hound-search/hound.git src/github.com/hound-search/hound
GOPATH=$(pwd) make -C src/github.com/hound-search/hound
```

### Testing

There are an increasing number of tests in each of the packages in Hound. Please make sure these pass before uploading your Pull Request. You can run the tests with the following command.
To run the entire test suite, use:

```
make test
```

If you want to just run the JavaScript test suite, use:
```
npm test
```

Any Go files that end in `_test.go` are assumed to be test files.  Similarly, any JavaScript files that ends in `.test.js` are automatically run by Jest, our test runner. Tests should live next to the files that they cover. 
[Check out Jest's docs](https://jestjs.io/docs/en/getting-started) for more details on writing Jest tests, 
and [check out Go's testing docs](https://golang.org/pkg/testing/) for more details on testing Go code.

You need to install `Node.js >= 12` and install `jest` by `npm install jest` to run the JS tests.

### Working on the web UI

Hound includes a web UI that is composed of several files (html, css, javascript, etc.). To make sure hound works seamlessly with the standard Go tools, these resources are all bundled inside of the `houndd` binary. Note that changes to the UI will result in local changes to the `ui/bindata.go` file. You must include these changes in your Pull Request.

To bundle UI changes in `ui/bindata.go` use:

```
make ui
```

To make development easier, there is a flag that will read the files from the file system (allowing the much-loved edit/refresh cycle).

First you should ensure you have all the dependencies installed that you need by running:

```
make dev
```

Then run the hound server with the --dev option:

```
bin/houndd --dev
```

## Get in Touch

Created at [Etsy](https://www.etsy.com) by:

* [Kelly Norton](https://github.com/kellegous)
* [Jonathan Klein](https://github.com/jklein)

Hound is maintained by:

* [David Schott](https://github.com/dschott68)
* [Jacob Rose](https://github.com/jacobrose)
* [Nick Sawyer](https://github.com/nickmoorman)
* [Salem Hilal](https://github.com/salemhilal)
