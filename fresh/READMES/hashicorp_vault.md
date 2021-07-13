# Vault [![CircleCI](https://circleci.com/gh/hashicorp/vault.svg?style=svg)](https://circleci.com/gh/hashicorp/vault) [![vault enterprise](https://img.shields.io/badge/vault-enterprise-yellow.svg?colorB=7c8797&colorA=000000)](https://www.hashicorp.com/products/vault/?utm_source=github&utm_medium=banner&utm_campaign=github-vault-enterprise)

----

**Please note**: We take Vault's security and our users' trust very seriously. If you believe you have found a security issue in Vault, _please responsibly disclose_ by contacting us at [security@hashicorp.com](mailto:security@hashicorp.com).

----

-	Website: https://www.vaultproject.io
-	IRC: `#vault-tool` on Freenode
-	Announcement list: [Google Groups](https://groups.google.com/group/hashicorp-announce)
-	Discussion forum: [Discuss](https://discuss.hashicorp.com/c/vault)
- Documentation: [https://www.vaultproject.io/docs/](https://www.vaultproject.io/docs/)
- Tutorials: [HashiCorp's Learn Platform](https://learn.hashicorp.com/vault)
- Certification Exam: [Vault Associate](https://www.hashicorp.com/certification/#hashicorp-certified-vault-associate)

<img width="300" alt="Vault Logo" src="https://github.com/hashicorp/vault/blob/f22d202cde2018f9455dec755118a9b84586e082/Vault_PrimaryLogo_Black.png">

Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.

A modern system requires access to a multitude of secrets: database credentials, API keys for external services, credentials for service-oriented architecture communication, etc. Understanding who is accessing what secrets is already very difficult and platform-specific. Adding on key rolling, secure storage, and detailed audit logs is almost impossible without a custom solution. This is where Vault steps in.

The key features of Vault are:

* **Secure Secret Storage**: Arbitrary key/value secrets can be stored
  in Vault. Vault encrypts these secrets prior to writing them to persistent
  storage, so gaining access to the raw storage isn't enough to access
  your secrets. Vault can write to disk, [Consul](https://www.consul.io),
  and more.

* **Dynamic Secrets**: Vault can generate secrets on-demand for some
  systems, such as AWS or SQL databases. For example, when an application
  needs to access an S3 bucket, it asks Vault for credentials, and Vault
  will generate an AWS keypair with valid permissions on demand. After
  creating these dynamic secrets, Vault will also automatically revoke them
  after the lease is up.

* **Data Encryption**: Vault can encrypt and decrypt data without storing
  it. This allows security teams to define encryption parameters and
  developers to store encrypted data in a location such as SQL without
  having to design their own encryption methods.

* **Leasing and Renewal**: All secrets in Vault have a _lease_ associated
  with it. At the end of the lease, Vault will automatically revoke that
  secret. Clients are able to renew leases via built-in renew APIs.

* **Revocation**: Vault has built-in support for secret revocation. Vault
  can revoke not only single secrets, but a tree of secrets, for example
  all secrets read by a specific user, or all secrets of a particular type.
  Revocation assists in key rolling as well as locking down systems in the
  case of an intrusion.

Documentation, Getting Started, and Certification Exams
-------------------------------

Documentation is available on the [Vault website](https://www.vaultproject.io/docs/).

If you're new to Vault and want to get started with security automation, please
check out our [Getting Started guides](https://learn.hashicorp.com/collections/vault/getting-started)
on HashiCorp's learning platform. There are also [additional guides](https://learn.hashicorp.com/vault)
to continue your learning.

Show off your Vault knowledge by passing a certification exam. Visit the
[certification page](https://www.hashicorp.com/certification/#hashicorp-certified-vault-associate)
for information about exams and find [study materials](https://learn.hashicorp.com/collections/vault/certification)
on HashiCorp's learning platform.

Developing Vault
--------------------

If you wish to work on Vault itself or any of its built-in systems, you'll
first need [Go](https://www.golang.org) installed on your machine. Go version
1.16.5+ is *required*.

For local dev first make sure Go is properly installed, including setting up a
[GOPATH](https://golang.org/doc/code.html#GOPATH). Ensure that `$GOPATH/bin` is in
your path as some distributions bundle old version of build tools. Next, clone this
repository. Vault uses [Go Modules](https://github.com/golang/go/wiki/Modules),
so it is recommended that you clone the repository ***outside*** of the GOPATH.
You can then download any required build tools by bootstrapping your environment:

```sh
$ make bootstrap
...
```

To compile a development version of Vault, run `make` or `make dev`. This will
put the Vault binary in the `bin` and `$GOPATH/bin` folders:

```sh
$ make dev
...
$ bin/vault
...
```

To compile a development version of Vault with the UI, run `make static-dist dev-ui`. This will
put the Vault binary in the `bin` and `$GOPATH/bin` folders:

```sh
$ make static-dist dev-ui
...
$ bin/vault
...
```

To run tests, type `make test`. Note: this requires Docker to be installed. If
this exits with exit status 0, then everything is working!

```sh
$ make test
...
```

If you're developing a specific package, you can run tests for just that
package by specifying the `TEST` variable. For example below, only
`vault` package tests will be run.

```sh
$ make test TEST=./vault
...
```

### Acceptance Tests

Vault has comprehensive [acceptance tests](https://en.wikipedia.org/wiki/Acceptance_testing)
covering most of the features of the secret and auth methods.

If you're working on a feature of a secret or auth method and want to
verify it is functioning (and also hasn't broken anything else), we recommend
running the acceptance tests.

**Warning:** The acceptance tests create/destroy/modify *real resources*, which
may incur real costs in some cases. In the presence of a bug, it is technically
possible that broken backends could leave dangling data behind. Therefore,
please run the acceptance tests at your own risk. At the very least,
we recommend running them in their own private account for whatever backend
you're testing.

To run the acceptance tests, invoke `make testacc`:

```sh
$ make testacc TEST=./builtin/logical/consul
...
```

The `TEST` variable is required, and you should specify the folder where the
backend is. The `TESTARGS` variable is recommended to filter down to a specific
resource to test, since testing all of them at once can sometimes take a very
long time.

Acceptance tests typically require other environment variables to be set for
things such as access keys. The test itself should error early and tell
you what to set, so it is not documented here.

For more information on Vault Enterprise features, visit the [Vault Enterprise site](https://www.hashicorp.com/products/vault/?utm_source=github&utm_medium=referral&utm_campaign=github-vault-enterprise).
