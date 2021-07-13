<h1 align="center"><img src="https://raw.githubusercontent.com/ory/meta/master/static/banners/hydra.svg" alt="ORY Hydra - Open Source OAuth 2 and OpenID Connect server"></h1>

<h4 align="center">
    <a href="https://www.ory.sh/chat">Chat</a> |
    <a href="https://github.com/ory/hydra/discussions">Discussions</a> |
    <a href="http://eepurl.com/di390P">Newsletter</a><br/><br/>
    <a href="https://www.ory.sh/hydra/docs/index">Guide</a> |
    <a href="https://www.ory.sh/hydra/docs/reference/api">API Docs</a> |
    <a href="https://godoc.org/github.com/ory/hydra">Code Docs</a><br/><br/>
    <a href="https://opencollective.com/ory">Support this project!</a>
</h4>

---

<p align="left">
    <a href="https://circleci.com/gh/ory/hydra/tree/master"><img src="https://circleci.com/gh/ory/hydra/tree/master.svg?style=shield" alt="Build Status"></a>
    <a href="https://coveralls.io/github/ory/hydra?branch=master"> <img src="https://coveralls.io/repos/ory/hydra/badge.svg?branch=master&service=github" alt="Coverage Status"></a>
    <a href="https://goreportcard.com/report/github.com/ory/hydra"><img src="https://goreportcard.com/badge/github.com/ory/hydra" alt="Go Report Card"></a>
    <a href="https://pkg.go.dev/github.com/ory/hydra"><img src="https://pkg.go.dev/badge/www.github.com/ory/hydra" alt="PkgGoDev"></a>
    <a href="https://bestpractices.coreinfrastructure.org/projects/364"><img src="https://bestpractices.coreinfrastructure.org/projects/364/badge" alt="CII Best Practices"></a>
    <a href="#backers" alt="sponsors on Open Collective"><img src="https://opencollective.com/ory/backers/badge.svg" /></a> <a href="#sponsors" alt="Sponsors on Open Collective"><img src="https://opencollective.com/ory/sponsors/badge.svg" /></a>
    <a href="https://github.com/ory/hydra/blob/master/CODE_OF_CONDUCT.md" alt="Ory Code of Conduct"><img src="https://img.shields.io/badge/ory-code%20of%20conduct-green" /></a>
</p>

ORY Hydra is a hardened, **OpenID Certified OAuth 2.0 Server and OpenID Connect Provider** optimized for low-latency, high throughput,
and low resource consumption. ORY Hydra *is not* an identity provider (user sign up, user login, password reset flow),
but connects to your existing identity provider through a [login and consent app](https://www.ory.sh/docs/next/hydra/oauth2#authenticating-users-and-requesting-consent).
Implementing the login and consent app in a different language is easy, and exemplary consent apps
([Node](https://github.com/ory/hydra-login-consent-node)) and [SDKs](https://www.ory.sh/docs/next/hydra/sdk/) for all common languages are provided.

If you're looking to jump straight into it, go ahead:

- **[Run your own OAuth 2.0 Server - step by step guide](https://www.ory.sh/run-oauth2-server-open-source-api-security/)**: A in-depth look at setting up ORY Hydra and performing a variety of OAuth 2.0 Flows.
- [ORY Hydra 5 Minute Tutorial](https://www.ory.sh/docs/hydra/5min-tutorial): Set up and use ORY Hydra using Docker Compose in under 5 Minutes. Good for quickly hacking a Proof of Concept.
- [Install and Set Up ORY Hydra](https://www.ory.sh/docs/hydra/configure-deploy): An advanced look at installation options and interaction with ORY Hydra.
- [Integrating your Login and Consent UI with ORY Hydra](https://www.ory.sh/docs/hydra/oauth2): The go-to place if you wish to adopt ORY Hydra in your new or existing stack.

Besides mitigating various attack vectors, such as database compromisation and OAuth 2.0 weaknesses, ORY Hydra is also
able to securely manage JSON Web Keys.
[Click here](https://www.ory.sh/docs/next/hydra/security-architecture) to read more about security.

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [What is ORY Hydra?](#what-is-ory-hydra)
  - [Who's using it?](#whos-using-it)
  - [OAuth2 and OpenID Connect: Open Standards!](#oauth2-and-openid-connect-open-standards)
  - [OpenID Connect Certified](#openid-connect-certified)
- [Quickstart](#quickstart)
  - [5 minutes tutorial: Run your very own OAuth2 environment](#5-minutes-tutorial-run-your-very-own-oauth2-environment)
  - [Installation](#installation)
- [Ecosystem](#ecosystem)
  - [ORY Kratos: Identity and User Infrastructure and Management](#ory-kratos-identity-and-user-infrastructure-and-management)
  - [ORY Hydra: OAuth2 & OpenID Connect Server](#ory-hydra-oauth2--openid-connect-server)
  - [ORY Oathkeeper: Identity & Access Proxy](#ory-oathkeeper-identity--access-proxy)
  - [ORY Keto: Access Control Policies as a Server](#ory-keto-access-control-policies-as-a-server)
- [Security](#security)
  - [Disclosing vulnerabilities](#disclosing-vulnerabilities)
- [Benchmarks](#benchmarks)
- [Telemetry](#telemetry)
- [Documentation](#documentation)
  - [Guide](#guide)
  - [HTTP API documentation](#http-api-documentation)
  - [Upgrading and Changelog](#upgrading-and-changelog)
  - [Command line documentation](#command-line-documentation)
  - [Develop](#develop)
    - [Dependencies](#dependencies)
    - [Formatting Code](#formatting-code)
    - [Running Tests](#running-tests)
      - [Short Tests](#short-tests)
      - [Regular Tests](#regular-tests)
    - [E2E Tests](#e2e-tests)
    - [Build Docker](#build-docker)
    - [Run the Docker Compose quickstarts](#run-the-docker-compose-quickstarts)
- [Libraries and third-party projects](#libraries-and-third-party-projects)
- [Blog posts & articles](#blog-posts--articles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What is ORY Hydra?

ORY Hydra is a server implementation of the OAuth 2.0 authorization framework and the OpenID Connect Core 1.0. Existing OAuth2
implementations usually ship as libraries or SDKs such as [node-oauth2-server](https://github.com/oauthjs/node-oauth2-server)
or [fosite](https://github.com/ory/fosite/issues), or as fully featured identity solutions with user
management and user interfaces, such as [Keycloak](https://www.keycloak.org).

Implementing and using OAuth2 without understanding the whole specification is challenging and prone to errors, even when
SDKs are being used. The primary goal of ORY Hydra is to make OAuth 2.0 and OpenID Connect 1.0 better accessible.

ORY Hydra implements the flows described in OAuth2 and OpenID Connect 1.0 without forcing you to use a "Hydra User Management"
or some template engine or a predefined front-end. Instead it relies on HTTP redirection and cryptographic methods
to verify user consent allowing you to use ORY Hydra with any authentication endpoint, be it [authboss](https://github.com/go-authboss/authboss), [User Frosting](https://www.userfrosting.com/) or your proprietary Java authentication.

### Who's using it?

<!--BEGIN ADOPTERS-->

The Ory community stands on the shoulders of individuals, companies, and
maintainers. We thank everyone involved - from submitting bug reports and
feature requests, to contributing patches, to sponsoring our work. Our community
is 1000+ strong and growing rapidly. The Ory stack protects 16.000.000.000+ API
requests every month with over 250.000+ active service nodes. We would have
never been able to achieve this without each and everyone of you!

The following list represents companies that have accompanied us along the way
and that have made outstanding contributions to our ecosystem. _If you think
that your company deserves a spot here, reach out to
<a href="mailto:office-muc@ory.sh">office-muc@ory.sh</a> now_!

**Please consider giving back by becoming a sponsor of our open source work on
<a href="https://www.patreon.com/_ory">Patreon</a> or
<a href="https://opencollective.com/ory">Open Collective</a>.**

<table>
    <thead>
        <tr>
            <th>Type</th>
            <th>Name</th>
            <th>Logo</th>
            <th>Website</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sponsor</td>
            <td>Raspberry PI Foundation</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/raspi.svg" alt="Raspberry PI Foundation"></td>
            <td><a href="https://www.raspberrypi.org/">raspberrypi.org</a></td>
        </tr>
        <tr>
            <td>Contributor</td>
            <td>Kyma Project</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/kyma.svg" alt="Kyma Project"></td>
            <td><a href="https://kyma-project.io">kyma-project.io</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>ThoughtWorks</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/tw.svg" alt="ThoughtWorks"></td>
            <td><a href="https://www.thoughtworks.com/">thoughtworks.com</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>Tulip</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/tulip.svg" alt="Tulip Retail"></td>
            <td><a href="https://tulip.com/">tulip.com</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>Cashdeck / All My Funds</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/allmyfunds.svg" alt="All My Funds"></td>
            <td><a href="https://cashdeck.com.au/">cashdeck.com.au</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>3Rein</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/3R-horiz.svg" alt="3Rein"></td>
            <td><a href="https://3rein.com/">3rein.com</a></td>
        </tr>
        <tr>
            <td>Contributor</td>
            <td>Hootsuite</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/hootsuite.svg" alt="Hootsuite"></td>
            <td><a href="https://hootsuite.com/">hootsuite.com</a></td>
        </tr>
        <tr>
            <td>Adopter *</td>
            <td>Segment</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/segment.svg" alt="Segment"></td>
            <td><a href="https://segment.com/">segment.com</a></td>
        </tr>
        <tr>
            <td>Adopter *</td>
            <td>Arduino</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/arduino.svg" alt="Arduino"></td>
            <td><a href="https://www.arduino.cc/">arduino.cc</a></td>
        </tr>
        <tr>
            <td>Adopter *</td>
            <td>DataDetect</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/datadetect.svg" alt="Datadetect"></td>
            <td><a href="https://unifiedglobalarchiving.com/data-detect/">unifiedglobalarchiving.com/data-detect/</a></td>
        </tr>        
        <tr>
            <td>Adopter *</td>
            <td>Sainsbury's</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/sainsburys.svg" alt="Sainsbury's"></td>
            <td><a href="https://www.sainsburys.co.uk/">sainsburys.co.uk</a></td>
        </tr>
                <tr>
            <td>Adopter *</td>
            <td>Contraste</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/contraste.svg" alt="Contraste"></td>
            <td><a href="https://www.contraste.com/en">contraste.com</a></td>
        </tr>
        <tr>
            <td>Adopter *</td>
            <td>Reyah</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/reyah.svg" alt="Reyah"></td>
            <td><a href="https://reyah.eu/">reyah.eu</a></td>
        </tr>        
        <tr>
            <td>Adopter *</td>
            <td>Zero</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/commitzero.svg" alt="Project Zero by Commit"></td>
            <td><a href="https://getzero.dev/">getzero.dev</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>OrderMyGear</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/ordermygear.svg" alt="OrderMyGear"></td>
            <td><a href="https://www.ordermygear.com/">ordermygear.com</a></td>
        </tr>
        <tr>
            <td>Sponsor</td>
            <td>Spiri.bo</td>
            <td align="center"><img height="32px" src="https://raw.githubusercontent.com/ory/meta/master/static/adopters/spiribo.svg" alt="Spiri.bo"></td>
            <td><a href="https://spiri.bo/">spiri.bo</a></td>
        </tr>
    </tbody>
</table>

We also want to thank all individual contributors

<a href="https://opencollective.com/ory" target="_blank"><img src="https://opencollective.com/ory/contributors.svg?width=890&button=false" /></a>

as well as all of our backers

<a href="https://opencollective.com/ory#backers" target="_blank"><img src="https://opencollective.com/ory/backers.svg?width=890"></a>

and past & current supporters (in alphabetical order) on
[Patreon](https://www.patreon.com/_ory): Alexander Alimovs, Billy, Chancy
Kennedy, Drozzy, Edwin Trejos, Howard Edidin, Ken Adler Oz Haven, Stefan Hans,
TheCrealm.

<em>\* Uses one of Ory's major projects in production.</em>

<!--END ADOPTERS-->





















### OAuth2 and OpenID Connect: Open Standards!

ORY Hydra implements Open Standards set by the IETF:

* [The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
* [OAuth 2.0 Threat Model and Security Considerations](https://tools.ietf.org/html/rfc6819)
* [OAuth 2.0 Token Revocation](https://tools.ietf.org/html/rfc7009)
* [OAuth 2.0 Token Introspection](https://tools.ietf.org/html/rfc7662)
* [OAuth 2.0 for Native Apps](https://tools.ietf.org/html/draft-ietf-oauth-native-apps-10)
* [Proof Key for Code Exchange by OAuth Public Clients](https://tools.ietf.org/html/rfc7636)

and the OpenID Foundation:

* [OpenID Connect Core 1.0](http://openid.net/specs/openid-connect-core-1_0.html)
* [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)
* [OpenID Connect Dynamic Client Registration 1.0](https://openid.net/specs/openid-connect-registration-1_0.html)
* [OpenID Connect Front-Channel Logout 1.0](https://openid.net/specs/openid-connect-frontchannel-1_0.html)
* [OpenID Connect Back-Channel Logout 1.0](https://openid.net/specs/openid-connect-backchannel-1_0.html)

### OpenID Connect Certified

ORY Hydra is an OpenID Foundation [certified OpenID Provider (OP)](http://openid.net/certification/#OPs).

<p align="center">
    <img src="docs/static/img/docs/oidc-cert.png" alt="ORY Hydra is a certified OpenID Providier" width="256px">
</p>

The following OpenID profiles are certified:

* [Basic OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) (response types `code`)
* [Implicit OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth) (response types `id_token`, `id_token+token`)
* [Hybrid OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth) (response types `code+id_token`, `code+id_token+token`, `code+token`)
* [OpenID Provider Publishing Configuration Information](https://openid.net/specs/openid-connect-discovery-1_0.html)
* [Dynamic OpenID Provider](https://openid.net/specs/openid-connect-registration-1_0.html)

To obtain certification, we deployed the [reference user login and consent app](https://github.com/ory/hydra-login-consent-node)
(unmodified) and ORY Hydra v1.0.0.

## Quickstart

This section is a quickstart guide to working with ORY Hydra. In-depth docs are available as well:

* The documentation is available [here](https://www.ory.sh/docs/next/hydra).
* The REST API documentation is available [here](https://www.ory.sh/docs/next/hydra/sdk/api).

### 5 minutes tutorial: Run your very own OAuth2 environment

The **[tutorial](https://www.ory.sh/docs/next/hydra/5min-tutorial)** teaches you to set up ORY Hydra,
a Postgres instance and an exemplary identity provider written in React using docker-compose.
It will take you about 5 minutes to complete the **[tutorial](https://www.ory.sh/docs/next/hydra/5min-tutorial)**.

<img src="docs/static/img/docs/oauth2-flow.gif" alt="OAuth2 Flow">

<br clear="all">

### Installation

Head over to the [ORY Developer Documentation](https://www.ory.sh/docs/next/hydra/configure-deploy#installing-ory-hydra) to learn how to install ORY Hydra on Linux, macOS, Windows, and Docker and how to build ORY Hydra from source.

## Ecosystem

<!--BEGIN ECOSYSTEM-->

We build Ory on several guiding principles when it comes to our architecture
design:

- Minimal dependencies
- Runs everywhere
- Scales without effort
- Minimize room for human and network errors

Ory's architecture designed to run best on a Container Orchestration Systems
such as Kubernetes, CloudFoundry, OpenShift, and similar projects. Binaries are
small (5-15MB) and available for all popular processor types (ARM, AMD64, i386)
and operating systems (FreeBSD, Linux, macOS, Windows) without system
dependencies (Java, Node, Ruby, libxml, ...).

### Ory Kratos: Identity and User Infrastructure and Management

[Ory Kratos](https://github.com/ory/kratos) is an API-first Identity and User
Management system that is built according to
[cloud architecture best practices](https://www.ory.sh/docs/next/ecosystem/software-architecture-philosophy).
It implements core use cases that almost every software application needs to
deal with: Self-service Login and Registration, Multi-Factor Authentication
(MFA/2FA), Account Recovery and Verification, Profile and Account Management.

### Ory Hydra: OAuth2 & OpenID Connect Server

[Ory Hydra](https://github.com/ory/hydra) is an OpenID Certified™ OAuth2 and
OpenID Connect Provider which easily connects to any existing identity system by
writing a tiny "bridge" application. Gives absolute control over user interface
and user experience flows.

### Ory Oathkeeper: Identity & Access Proxy

[Ory Oathkeeper](https://github.com/ory/oathkeeper) is a BeyondCorp/Zero Trust
Identity & Access Proxy (IAP) with configurable authentication, authorization,
and request mutation rules for your web services: Authenticate JWT, Access
Tokens, API Keys, mTLS; Check if the contained subject is allowed to perform the
request; Encode resulting content into custom headers (`X-User-ID`), JSON Web
Tokens and more!

### Ory Keto: Access Control Policies as a Server

[Ory Keto](https://github.com/ory/keto) is a policy decision point. It uses a
set of access control policies, similar to AWS IAM Policies, in order to
determine whether a subject (user, application, service, car, ...) is authorized
to perform a certain action on a resource.

<!--END ECOSYSTEM-->





















## Security

*Why should I use ORY Hydra? It's not that hard to implement two OAuth2 endpoints and there are numerous SDKs out there!*

OAuth2 and OAuth2 related specifications are over 400 written pages. Implementing OAuth2 is easy, getting it right is hard.
ORY Hydra is trusted by companies all around the world, has a vibrant community and faces millions of requests in production
each day. Of course, we also compiled a security guide with more details on cryptography and security concepts.
Read [the security guide now](https://www.ory.sh/docs/next/hydra/security-architecture).

### Disclosing vulnerabilities

If you think you found a security vulnerability, please refrain from posting it publicly on the forums, the chat, or GitHub
and send us an email to [hi@ory.am](mailto:hi@ory.sh) instead.

## Benchmarks

Our continuous integration runs a collection of benchmarks against ORY Hydra. You can find the results [here](https://www.ory.sh/docs/next/performance/hydra).

## Telemetry

Our services collect summarized, anonymized data that can optionally be turned off. Click
[here](https://www.ory.sh/docs/next/ecosystem/sqa) to learn more.

## Documentation

### Guide

The Guide is available [here](https://www.ory.sh/docs/next/hydra).

### HTTP API documentation

The HTTP API is documented [here](https://www.ory.sh/docs/next/hydra/sdk/api).

### Upgrading and Changelog

New releases might introduce breaking changes. To help you identify and incorporate those changes, we document these
changes in [UPGRADE.md](./UPGRADE.md) and [CHANGELOG.md](./CHANGELOG.md).

### Command line documentation

Run `hydra -h` or `hydra help`.

### Develop

We encourage all contributions and encourage you to read our [contribution guidelines](./CONTRIBUTING.md).

#### Dependencies

You need Go 1.13+ with `GO111MODULE=on` and (for the test suites):

- Docker and Docker Compose
- Makefile
- NodeJS / npm

It is possible to develop ORY Hydra on Windows, but please be aware that all guides assume a Unix shell like bash or zsh.

#### Formatting Code

You can format all code using `make format`. Our CI checks if your code is properly formatted.

#### Running Tests

There are three types of tests you can run:

- Short tests (do not require a SQL database like PostgreSQL)
- Regular tests (do require PostgreSQL, MySQL, CockroachDB)
- End to end tests (do require databases and will use a test browser)

All of the above tests can be run using the makefile. See the commands below.

**Makefile commands**

```shell
# quick tests
make quicktest

# regular tests
make test
test-resetdb

# end-to-end tests
make e2e
```

##### Short Tests

It is recommended to use the make file to run your tests using `make quicktest`
, however, you can still use the `go test` command.

**Please note**:

All tests run against a sqlite in-memory database,
thus it is required to use the `-tags sqlite` build tag.

Short tests run fairly quickly. You can either test all of the code at once:

```shell script
go test -v -failfast -short -tags sqlite ./...
```

or test just a specific module:

```shell script
go test -v -failfast -short -tags sqlite ./client
```

or a specific test:

```shell script
go test -v -failfast -short -tags sqlite -run ^TestName$ ./...
```

##### Regular Tests

Regular tests require a database set up. Our test suite is able to work with docker directly (using [ory/dockertest](https://github.com/ory/dockertest))
but we encourage to use the Makefile instead. Using dockertest can bloat the number of Docker Images on your system
and are quite slow. Instead we recommend doing:

```shell script
make test
```

Please be aware that `make test` recreates the databases every time you run `make test`. This can be annoying if
you are trying to fix something very specific and need the database tests all the time. In that case we
suggest that you initialize the databases with:

```shell script
make resetdb
export TEST_DATABASE_MYSQL='mysql://root:secret@(127.0.0.1:3444)/mysql?parseTime=true&multiStatements=true'
export TEST_DATABASE_POSTGRESQL='postgres://postgres:secret@127.0.0.1:3445/postgres?sslmode=disable'
export TEST_DATABASE_COCKROACHDB='cockroach://root@127.0.0.1:3446/defaultdb?sslmode=disable'
```

Then you can run `go test` as often as you'd like:

```shell script
go test -p 1 ./...

# or in a module:
cd client; go test .
```

#### E2E Tests

The E2E tests use [Cypress](https://www.cypress.io) to run full browser tests. You can execute these tests with:

```
make e2e
```

The runner will not show the Browser window, as it runs in the CI Mode (background). That makes debugging these
type of tests very difficult, but thankfully you can run the e2e test in the browser which helps with debugging! Just run:

```shell script
./test/e2e/circle-ci.bash memory --watch

# Or for the JSON Web Token Access Token strategy:
# ./test/e2e/circle-ci.bash memory-jwt --watch
```

or if you would like to test one of the databases:

```shell script
make resetdb
export TEST_DATABASE_MYSQL='mysql://root:secret@(127.0.0.1:3444)/mysql?parseTime=true&multiStatements=true'
export TEST_DATABASE_POSTGRESQL='postgres://postgres:secret@127.0.0.1:3445/postgres?sslmode=disable'
export TEST_DATABASE_COCKROACHDB='cockroach://root@127.0.0.1:3446/defaultdb?sslmode=disable'

# You can test against each individual database:
./test/e2e/circle-ci.bash postgres --watch
./test/e2e/circle-ci.bash memory --watch
./test/e2e/circle-ci.bash mysql --watch
# ...
```

Once you run the script, a Cypress window will appear. Hit the button "Run all Specs"!

The code for these tests is located in [./cypress/integration](./cypress/integration) and
[./cypress/support](./cypress/support) and
[./cypress/helpers](./cypress/helpers). The website you're seeing is located in
[./test/e2e/oauth2-client](./test/e2e/oauth2-client).

##### OpenID Connect Conformity Tests

To run ORY Hydra against the OpenID Connect conformity suite, run

```shell script
$ test/conformity/start.sh --build
```

and then in a separate shell

```shell script
$ test/conformity/test.sh
```

Running these tests will take a significant amount of time which is why they are not part
of the CircleCI pipeline.

#### Build Docker

You can build a development Docker Image using:

```shell script
make docker
```

#### Run the Docker Compose quickstarts

If you wish to check your code changes against any of the docker-compose quickstart files, run:

```shell script
make docker
docker compose -f quickstart.yml up # ....
```

## Libraries and third-party projects

Official:
* [User Login & Consent Example](https://github.com/ory/hydra-login-consent-node)

Community:
* [Kubernetes helm chart](https://k8s.ory.sh/helm/hydra.html)
* [Werther - an Identity Provider over LDAP](https://github.com/i-core/werther)
* [Terraform Provider](https://registry.terraform.io/providers/hypnoglow/oryhydra/latest) and its [source code](https://github.com/hypnoglow/terraform-provider-oryhydra).

:warning: Outdated Community Projects:
The following projects are outdated and won't work anymore in most cases. Having said that they still might help you to better understand how to integrate HYDRA and solve specific cases.
* [ORY Hydra middleware for Gin](https://github.com/janekolszak/gin-hydra)
* [Consent App SDK for Go](https://github.com/janekolszak/idp)

## Blog posts & articles

* [Creating an oauth2 custom lamda authorizer for use with Amazons (AWS) API Gateway using Hydra](https://blogs.edwardwilde.com/2017/01/12/creating-an-oauth2-custom-lamda-authorizer-for-use-with-amazons-aws-api-gateway-using-hydra/)
* Warning, ORY Hydra has changed almost everything since writing this
article: [Hydra: Run your own Identity and Access Management service in <5 Minutes](https://blog.gopheracademy.com/advent-2015/hydra-auth/)
