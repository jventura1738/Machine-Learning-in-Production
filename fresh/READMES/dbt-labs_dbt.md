<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>
<p align="center">
  <a href="https://github.com/dbt-labs/dbt/actions/workflows/tests.yml?query=branch%3Adevelop">
    <img src="https://github.com/dbt-labs/dbt/actions/workflows/tests.yml/badge.svg" alt="GitHub Actions"/>
  </a>
  <a href="https://circleci.com/gh/dbt-labs/dbt/tree/develop">
    <img src="https://circleci.com/gh/dbt-labs/dbt/tree/develop.svg?style=svg"  alt="CircleCI" />
  </a>
  <a href="https://dev.azure.com/fishtown-analytics/dbt/_build?definitionId=1&_a=summary&repositoryFilter=1&branchFilter=789%2C789%2C789%2C789">
    <img src="https://dev.azure.com/fishtown-analytics/dbt/_apis/build/status/fishtown-analytics.dbt?branchName=develop" alt="Azure Pipelines" />
  </a>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

![dbt architecture](https://raw.githubusercontent.com/dbt-labs/dbt/6c6649f9129d5d108aa3b0526f634cd8f3a9d1ed/etc/dbt-arch.png)

## Understanding dbt

Analysts using dbt can transform their data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse.

These select statements, or "models", form a dbt project. Models frequently build on top of one another – dbt makes it easy to [manage relationships](https://docs.getdbt.com/docs/ref) between models, and [visualize these relationships](https://docs.getdbt.com/docs/documentation), as well as assure the quality of your transformations through [testing](https://docs.getdbt.com/docs/testing).

![dbt dag](https://raw.githubusercontent.com/dbt-labs/dbt/6c6649f9129d5d108aa3b0526f634cd8f3a9d1ed/etc/dbt-dag.png)

## Getting started

- [Install dbt](https://docs.getdbt.com/docs/installation)
- Read the [introduction](https://docs.getdbt.com/docs/introduction/) and [viewpoint](https://docs.getdbt.com/docs/about/viewpoint/)

## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://community.getdbt.com/), or open [an issue](https://github.com/dbt-labs/dbt/issues/new)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).
