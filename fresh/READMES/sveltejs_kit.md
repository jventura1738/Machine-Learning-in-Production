# READ THIS FIRST!

SvelteKit is still in beta. Expect bugs! Read more [here](https://svelte.dev/blog/sveltekit-beta), and track progress towards 1.0 [here](https://github.com/sveltejs/kit/issues?q=is%3Aopen+is%3Aissue+milestone%3A1.0).

## Documentation

Please see [the documentation](https://kit.svelte.dev/docs) for information about getting started and developing with SvelteKit.

## Developing

This monorepo uses [pnpm](https://pnpm.js.org/en/). Install it...

```bash
npm i -g pnpm
```

...then install this repo's dependencies...

```bash
pnpm i
```

...then build SvelteKit and the other packages:

```bash
pnpm build
```

You should now be able to run the [examples](examples) by navigating to one of the directories and doing `pnpm dev`.

Run `pnpm dev` inside the `packages/kit` directory to continually rebuild `@sveltejs/kit` as you make changes to SvelteKit. Restarting the example/test apps will cause the newly built version to be used.

To use the git hooks in the repo, which will save you waiting for CI to tell you that you forgot to lint, run this:

```bash
git config core.hookspath .githooks
```

### Changelogs

For changes to be reflected in package changelogs, run `pnpx changeset` and follow the prompts. All changesets should be `patch` until SvelteKit 1.0

### Releases

The [Changesets GitHub action](https://github.com/changesets/action#with-publishing) will create and update a PR that applies changesets and publishes new versions of changed packages to npm.

> It uses `pnpm publish` rather than `pnpx changeset publish` so that we can use the `--filter` and (while in beta) `--tag` flags — though perhaps they work with `pnpx changeset publish`?

New packages will need to be published manually the first time if they are scoped to the `@sveltejs` organisation, by running this from the package directory:

```
npm publish --access=public
```

### Testing

Run `pnpm test` to run the tests from all subpackages. Browser tests live in subdirectories of `packages/kit/test` such as `packages/kit/test/apps/basics`.

You can run the tests for only a single package by first moving to that directory. E.g. `cd packages/kit`.

You must rebuild each time before running the tests if you've made code changes.

To run a single integration test, provide the `FILTER` env var with the test name. E.g. `FILTER="includes paths" pnpm test:integration`. You're also supposed to be a open up the file and change `test` to `test.only`, but this doesn't work as well. Help would be appreciated in fixing that.

You can run the test server with `cd packages/kit/test/apps/basics; pnpm run dev` to hit it with your browser.

You may need to install some dependencies first e.g. with `npx playwright install-deps` (which only works on Ubuntu).
