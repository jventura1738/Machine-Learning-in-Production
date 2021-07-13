## Golem

Official Rust implementation of Golem. Golem is a network of nodes that implement the Golem Network protocol. We provide the default implementation of such a node in the form of the Golem daemon, Yagna.

<h5 align="center">
  <a href='https://golem.network/'><img
      width='500px'
      alt=''
      src="https://user-images.githubusercontent.com/35585644/111472751-939f5100-872a-11eb-8c26-926117080e35.png" /></a>
  <br/>A flexible, open-source platform for democratised access to digital resources.
</a>
</h5>

</p>
<p align="center">
    <a href="https://github.com/golemfactory/yagna/workflows/CI/badge.svg" alt="CI">
        <img src="https://github.com/golemfactory/yagna/workflows/CI/badge.svg" /></a>
    <a href="https://github.com/golemfactory/yagna/watchers" alt="Watch on GitHub">
        <img src="https://img.shields.io/github/watchers/golemfactory/yagna.svg?style=social" /></a>
    <a href="https://github.com/golemfactory/yagna/stargazers" alt="Star on GitHub">
        <img src="https://img.shields.io/github/stars/golemfactory/yagna.svg?style=social" /></a>
    <a href="https://discord.gg/y29dtcM" alt="Discord">
        <img src="https://img.shields.io/discord/684703559954333727?logo=discord" /></a>
    <a href="https://twitter.com/golemproject" alt="Twitter">
        <img src="https://img.shields.io/twitter/follow/golemproject?style=social" /></a>
    <a href="https://reddit.com/GolemProject" alt="Reddit">
        <img src="https://img.shields.io/reddit/subreddit-subscribers/GolemProject?style=social" /></a>
</p>

Golem Network has officially gone on Ethereum Mainnet with the [Beta I release](https://blog.golemproject.net/mainnet-release-beta-i/) in March 2021.

Golem democratizes society’s access to computing power by creating a decentralized platform where anyone can build a variety of applications, request computational resources and/or offer their idle systems in exchange for cryptocurrency tokens (GLM). The actors in this decentralized network can assume one of the three non-exclusive roles:

* **Requestor**
Has a need to use IT resources such as computation hardware. Those resources are purchased in the decentralized market. The actual usage of the resources is backed by Golem's decentralized infrastructure.

* **Provider**
Has IT resources available that can be shared with other actors in the network. Those resources are sold in the decentralized market.

* **Developer**
Builds applications to run for requestors on the network. Golem's potential goes much beyond a singular application. See [Awesome Golem](https://github.com/golemfactory/awesome-golem/blob/main/README.md#%EF%B8%8F-apps) for just a taste of the various types of applications that can be built and run on Golem!

## Documentation
For a more in-depth look at how Golem works, head over to our [documentation.](https://handbook.golem.network/)

## Project Layout

* [agent/provider](agent/provider) - provider agent implementation based on core services.
* [core](core) - core services for the open computation marketplace.
* [exe-unit](exe-unit) -  ExeUnit Supervisor - a common part of all [runtimes](#runtimes) for yagna.
* [test-utils](test-utils) - some helpers for testing purposes
* [utils](utils) - trash bin for all other stuff ;)
* [docs](docs) - project documentation including analysis and specifications.

## Public API
The public API rust binding with data model is in the 
[ya-client](https://github.com/golemfactory/ya-client) repo.

## High Level APIs
The public high-level API for Python is in 
[yapapi](https://github.com/golemfactory/yapapi) repo and the JS/TS port is contained in the [yaJSapi](https://github.com/golemfactory/yajsapi) repo.

## Runtimes
We call our runtime **ExeUnit**. As for now we support
 * [Light VM](https://github.com/golemfactory/ya-runtime-vm) - [QEMU](https://www.qemu.org/)\-based ExeUnit.
 * and WASM in two flavours:
   * [wasmtime](https://github.com/golemfactory/ya-runtime-wasi) - [Wasmtime](https://github.com/bytecodealliance/wasmtime)\-based ExeUnit.
   * [emscripten](https://github.com/golemfactory/ya-runtime-emscripten) - [SpiderMonkey](https://github.com/servo/rust-mozjs)\-based ExeUnit.

Other ExeUnit types are to come (see below).

## Golem Beta Release(s)
Important milestones for Golem development were [Beta I](https://github.com/golemfactory/yagna/releases/tag/v0.6.1) and most recent [Beta II](https://github.com/golemfactory/yagna/releases/tag/v0.7.0). With those releases we have delivered:
* MVP (minimum viable product), though not feature rich yet, it is usable for early adopters
* Clean and easy experience for new and existing users.
* Support for GLM payments (both L1 & L2 on Ethreum Mainnet)
* **Production-ready** and **easy to maintain** code base.
* **Modular architecture** with all the building blocks beeing replaceable.
* Small binaries (under 30Mb).
* [Documentation and SDK](https://handbook.golem.network/) for Golem app developers.

## List of implemented and planned functionality 

1. Distributed computations
    * [x] **Batching**
    * [x] Services _(PoC stage)_
1. Computational environment (aka ExeUnit)
   * [x] **Wasm computation**
   * [x] Light vm-s
   * [ ] Docker on Linux _(optional)_
   * [x] SGX on Graphene _(PoC stage)_
1. Payment platform
    * [x] **Payments with GLM**
    * [x] [**ERC20 token**](https://blog.golemproject.net/gnt-to-glm-migration/)
    * [x] **Layer 1 & [Layer 2](https://blog.golemproject.net/new-golem-alpha-iii-reveal/) transactions**
    * [ ] Payment matching _(optional)_ (Ability for the invoice issuer to match the payment with Debit Note(s)/Invoice(s)).
1. Transaction system
    * [x] **Pay as you go(lem)** ([see more](https://blog.golemproject.net/pay-as-you-use-golem-a-brief-but-effective-primer/))
    * [x] **Pay per task**
    * [ ] Pay for dev _(optional)_
1. Network
    * [ ] **P2P** (Hybrid P2P; in progress) 
    * [ ] **Ability to work behind NAT** (Relays; in progress)
1. Verification
    * [ ] **Verification by redundancy** ([see also](https://blog.golemproject.net/gwasm-verification/))
    * [x] **No verification**
    * [ ] Verification by humans _(optional)_

## Road ahead

We are actively working on improving Yagna and extending its functionality, check upcoming releases and other news on [our blog](https://blog.golem.network/).

