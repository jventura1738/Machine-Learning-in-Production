## inlets is a Cloud Native Tunnel written in Go

<img src="docs/inlets-logo-sm.png" width="150px">

The open source version of inlets was a Cloud Native Tunnel written in Go. It was only ever designed to be a prototype and lessons were learned along the way resulting in a new version that is better suited for production use.

![Conceptual diagram](docs/inlets-tls.png)

inlets OSS has now been replaced by inlets PRO, a new version that does everything the original version did, but with secure defaults, and a better ecosystem.

inlets PRO ships binaries with support for Windows, MacOS and Linux. There is also an official public Docker image available. The code will run on Intel, AMD and ARM architectures.

inlets OSS remains available in a source-only format on GitHub and will not receive updates. Personal licenses for inlets PRO are available at a discounted rate for hobbyist users for 6 or 12 months.

### Going to production with inlets PRO

The following features / use-cases are covered by [inlets PRO](https://inlets.dev):

* Tunnel HTTPS / REST traffic, with automated Let's Encrypt support
* Tunnel L4 TCP traffic such as websockets, databases, reverse proxies, remote desktop, VNC and SSH
* Multiplex multiple HTTP sites over the same connection
* Connect multiple clients to the same server
* Automate server creation on the most popular developer clouds and hyperscalers
* Expose multiple ports from the same client - i.e. 80 and 443

There's also a broader ecosystem:

* Kubernetes helm charts, YAML and [Operator](https://github.com/inlets/inlets-operator)
* [Documentation](https://docs.inlets.dev/), [blog posts, tutorials and videos](https://inlets.dev/blog)
* Commercial services & support

Try it out for free: [inlets.dev](https://inlets.dev)

### How does it work?

In "A tale of two networks" Alex Ellis and Johan Siebens explore blog posts, use-cases and show demos of inlets PRO.

[A tale of two networks - demos and use-cases for inlets tunnels](https://www.youtube.com/watch?v=AFMA1xA4zts&feature=youtu.be)

[![https://img.youtube.com/vi/AFMA1xA4zts/hqdefault.jpg](https://img.youtube.com/vi/AFMA1xA4zts/maxresdefault.jpg)](https://youtu.be/AFMA1xA4zts)

### The inlets projects

inlets is a Cloud Native Tunnel and is [listed on the Cloud Native Landscape](https://landscape.cncf.io/category=service-proxy&format=card-mode&grouping=category&sort=stars) under *Service Proxies*.

* [inlets PRO](https://inlets.dev) - Secure HTTP(s) and TCP tunnels with automated TLS encryption. Replaces inlets OSS
* [inlets-operator](https://github.com/inlets/inlets-operator) - Public IPs for your private Kubernetes Services and CRD using inlets PRO
* [inletsctl](https://github.com/inlets/inletsctl) - The fastest way to create self-hosted exit-servers using inlets PRO
* [inlets](https://github.com/inlets/inlets) - Cloud Native Tunnel for HTTP only - **no** tutorials, automation, TLS, TCP or Kubernetes integration available. Replaced by inlets PRO

