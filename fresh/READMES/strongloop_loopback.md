# LoopBack

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/strongloop/loopback?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Module LTS Adopted'](https://img.shields.io/badge/Module%20LTS-Adopted-brightgreen.svg?style=flat)](http://github.com/CloudNativeJS/ModuleLTS)
[![IBM Support](https://img.shields.io/badge/IBM%20Support-Frameworks-brightgreen.svg?style=flat)](http://ibm.biz/node-support)

**⚠️ LoopBack 3 has reached end of life. We are no longer accepting pull requests or providing 
support for community users. The only exception is fixes for critical bugs and security 
vulnerabilities provided as part of support for IBM API Connect customers.
We urge all LoopBack 3 users to migrate their applications to LoopBack 4 as soon as possible. 
Learn more about
<a href="https://loopback.io/doc/en/contrib/Long-term-support.html">LoopBack's long term support policy.</a>
will be provided or accepted. (See
[Module Long Term Support Policy](#module-long-term-support-policy) below.)**

We urge all LoopBack 3 users to migrate their applications to LoopBack 4 as
soon as possible. Refer to our
[Migration Guide](https://loopback.io/doc/en/lb4/migration-overview.html)
for more information on how to upgrade.

## Overview

LoopBack is a highly-extensible, open-source Node.js framework that enables you to:

  * Create dynamic end-to-end REST APIs with little or no coding.
  * Access data from Oracle, MySQL, PostgreSQL, MS SQL Server, MongoDB, SOAP and other REST APIs.
  * Incorporate model relationships and access controls for complex APIs.
  * Use built-in push, geolocation, and file services for mobile apps.
  * Easily create client apps using Android, iOS, and JavaScript SDKs.
  * Run your application on-premises or in the cloud.

LoopBack consists of:

  * A library of Node.js modules.
  * [Yeoman](http://yeoman.io/) generators for scaffolding applications.
  * Client SDKs for iOS, Android, and web clients.

LoopBack tools include:
  * Command-line tool `loopback-cli` to create applications, models, data sources, and so on.

For more details, see [https://loopback.io/](https://loopback.io/).


## Module Long Term Support Policy

LoopBack 3.x has reached End-of-Life.

This module adopts the [Module Long Term Support (LTS)](http://github.com/CloudNativeJS/ModuleLTS) policy, with the following End Of Life (EOL) dates:

| Version    | Status          | Published | EOL                  |
| ---------- | --------------- | --------- | -------------------- |
| LoopBack 4 | Current         | Oct 2018  | Apr 2023 _(minimum)_ |
| LoopBack 3 | End-of-Life     | Dec 2016  | Dec 2020             |
| LoopBack 2 | End-of-Life     | Jul 2014  | Apr 2019             |

Learn more about our LTS plan in [docs](https://loopback.io/doc/en/contrib/Long-term-support.html).

## LoopBack modules

The LoopBack framework is a set of Node.js modules that you can use independently or together.

![LoopBack modules](https://github.com/strongloop/loopback/raw/master/docs/assets/lb-modules.png "LoopBack modules")

### Core
* [loopback](https://github.com/strongloop/loopback)
* [loopback-datasource-juggler](https://github.com/strongloop/loopback-datasource-juggler)
* [strong-remoting](https://github.com/strongloop/strong-remoting)

### Connectors
* [loopback-connector-mongodb](https://github.com/strongloop/loopback-connector-mongodb)
* [loopback-connector-mysql](https://github.com/strongloop/loopback-connector-mysql)
* [loopback-connector-postgresql](https://github.com/strongloop/loopback-connector-postgresql)
* [loopback-connector-rest](https://github.com/strongloop/loopback-connector-rest)

### Enterprise Connectors
* [loopback-connector-oracle](https://github.com/strongloop/loopback-connector-oracle)
* [loopback-connector-mssql](https://github.com/strongloop/loopback-connector-mssql)
* [loopback-connector-soap](https://github.com/strongloop/loopback-connector-soap)
* [loopback-connector-atg](https://github.com/strongloop/loopback-connector-atg)

### Community Connectors

The LoopBack community has created and supports a number of additional connectors.  See [Community connectors](https://loopback.io/doc/en/lb2/Community-connectors.html) for details.

### Components
* [loopback-component-push](https://github.com/strongloop/loopback-component-push)
* [loopback-component-storage](https://github.com/strongloop/loopback-component-storage)
* [loopback-component-passport](https://github.com/strongloop/loopback-component-passport)

### Client SDKs
* [loopback-sdk-ios](https://github.com/strongloop/loopback-sdk-ios)
* [loopback-sdk-android](https://github.com/strongloop/loopback-sdk-android)
* [loopback-sdk-angular](https://github.com/strongloop/loopback-sdk-angular)
  * [loopback-sdk-angular-cli](https://github.com/strongloop/loopback-sdk-angular-cli)
  * [grunt-loopback-sdk-angular](https://github.com/strongloop/grunt-loopback-sdk-angular)

### Tools
* [loopback-explorer](https://github.com/strongloop/loopback-explorer)
* [loopback-workspace](https://github.com/strongloop/loopback-workspace)
* [generator-loopback](https://github.com/strongloop/generator-loopback)

### Examples

StrongLoop provides a number of example applications that illustrate various key LoopBack features. In some cases, they have accompanying step-by-step instructions (tutorials).

See [examples at loopback.io](https://loopback.io/examples/) for details.

## Resources

  * [Documentation](https://loopback.io/doc/).
  * [API documentation](https://apidocs.strongloop.com/loopback).
  * [LoopBack Announcements](https://groups.google.com/forum/#!forum/loopbackjs-announcements)
  * [LoopBack Google Group](https://groups.google.com/forum/#!forum/loopbackjs).
  * [GitHub issues](https://github.com/strongloop/loopback/issues).
  * [Gitter chat](https://gitter.im/strongloop/loopback).

## Contributing

Contributions to the LoopBack project are welcome! See [Contributing to LoopBack](https://loopback.io/doc/en/contrib/index.html) for more information.

## Reporting issues

One of the easiest ways to contribute to LoopBack is to report an issue. See [Reporting issues](https://loopback.io/doc/en/contrib/Reporting-issues.html) for more information.

[![Analytics](https://sl-beacon.appspot.com/UA-37775386-1/github/loopback/readme?pixel)](https://github.com/strongloop/loopback)
