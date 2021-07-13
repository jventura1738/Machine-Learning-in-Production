<img src="neon.png" alt="neon" width="100%" />

[![Cargo](http://meritbadge.herokuapp.com/neon)](https://crates.io/crates/neon)
[![npm](https://img.shields.io/npm/v/neon-cli.svg)](https://www.npmjs.com/package/neon-cli)
[![Linux Build Status](https://github.com/neon-bindings/neon/workflows/Test%20on%20Linux/badge.svg)](https://github.com/neon-bindings/neon/actions?query=workflow%3A%22Test+on+Linux%22)
[![macOS Build Status](https://github.com/neon-bindings/neon/workflows/Test%20on%20MacOS/badge.svg)](https://github.com/neon-bindings/neon/actions?query=workflow%3A%22Test+on+MacOS%22)
[![Windows Build Status](https://github.com/neon-bindings/neon/workflows/Test%20on%20Windows/badge.svg)](https://github.com/neon-bindings/neon/actions?query=workflow%3A%22Test+on+Windows%22)

Rust bindings for writing safe and fast native Node.js modules.

# Getting started

Once you have the [platform dependencies](https://neon-bindings.com/docs/getting-started#install-node-build-tools/) installed, getting started is as simple as:

```
$ npm init neon my-project
```

Then see the [Hello World guide](https://neon-bindings.com/docs/hello-world/) for writing your first Hello World in Neon!

_**Note:** This will create a new project with the `napi-backend` and some documentation may not be up to date._

# Docs

See our [Neon fundamentals docs](https://neon-bindings.com/docs/intro) and our [API docs](https://docs.rs/neon/latest/neon).

# N-API Migration Guide

We've ported Neon to a new backend based on [N-API](https://nodejs.org/api/n-api.html), which will be the basis for Neon 1.0.

**Read the new [migration guide](https://github.com/neon-bindings/neon/blob/main/MIGRATION_GUIDE.md)** to learn how to port your Neon projects to N-API!

# Platform Support

### Operating Systems

| Linux  | macOS | Windows |
| ------ | ----- | ------- |
| ✓      | ✓     | ✓       |

### Node.js

| Node 12 | Node 14 | Node 16 |
| ------- | ------- | ------- |
| ✓       | ✓       | ✓       |

Support for [LTS versions of Node](https://github.com/nodejs/LTS#release-schedule) and current are expected. If you're using a different version of Node and believe it should be supported, let us know.

### Rust

Neon supports Rust stable version 1.18 and higher. We test on the latest stable, beta, and nightly versions of Rust.

# A Taste...

```rust
fn make_an_array(mut cx: FunctionContext) -> JsResult<JsArray> {
    // Create some values:
    let n = cx.number(9000);
    let s = cx.string("hello");
    let b = cx.boolean(true);

    // Create a new array:
    let array: Handle<JsArray> = cx.empty_array();

    // Push the values into the array:
    array.set(&mut cx, 0, n)?;
    array.set(&mut cx, 1, s)?;
    array.set(&mut cx, 2, b)?;

    // Return the array:
    Ok(array)
}

register_module!(mut cx, {
    cx.export_function("makeAnArray", make_an_array)
})
```

For more examples, see our [examples repo](https://github.com/neon-bindings/examples).

# Get Involved

The Neon community is just getting started and there's tons of fun to be had. Come play! :)

The [Rust Bindings community Slack](https://rust-bindings.slack.com) is open to all; use [the Slackin app](https://rust-bindings-slackin.herokuapp.com) to receive an invitation.

# License

Licensed under either of

 * Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.
