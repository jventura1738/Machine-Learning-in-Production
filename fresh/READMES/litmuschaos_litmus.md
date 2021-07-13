<img alt="LitmusChaos" src="https://landscape.cncf.io/logos/litmus.svg" width="200" align="left">

# Litmus
### Cloud-Native Chaos Engineering

[![Slack Channel](https://img.shields.io/badge/Slack-Join-purple)](https://slack.litmuschaos.io)
![GitHub Workflow](https://github.com/litmuschaos/litmus/actions/workflows/push.yml/badge.svg?branch=master)
[![Docker Pulls](https://img.shields.io/docker/pulls/litmuschaos/chaos-operator.svg)](https://hub.docker.com/r/litmuschaos/chaos-operator)
[![GitHub stars](https://img.shields.io/github/stars/litmuschaos/litmus?style=social)](https://github.com/litmuschaos/litmus/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/litmuschaos/litmus)](https://github.com/litmuschaos/litmus/issues)
[![Twitter Follow](https://img.shields.io/twitter/follow/litmuschaos?style=social)](https://twitter.com/LitmusChaos)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3202/badge)](https://bestpractices.coreinfrastructure.org/projects/3202)
[![BCH compliance](https://bettercodehub.com/edge/badge/litmuschaos/litmus?branch=master)](https://bettercodehub.com/)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Flitmuschaos%2Flitmus.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Flitmuschaos%2Flitmus?ref=badge_shield)
[![YouTube Channel](https://img.shields.io/badge/YouTube-Subscribe-red)](https://www.youtube.com/channel/UCa57PMqmz_j0wnteRa9nCaw)
<br><br><br><br>

#### *Read this in [other languages](translations/TRANSLATIONS.md).*

[🇰🇷](translations/README-ko.md) [🇨🇳](translations/README-chn.md) [🇧🇷](translations/README-pt-br.md) [🇮🇳](translations/README-hi.md)


## Overview

Litmus is a toolset to do cloud-native chaos engineering. Litmus provides tools to orchestrate chaos on Kubernetes to help SREs find weaknesses in their deployments. SREs use Litmus to run chaos experiments initially in the staging environment and eventually in production to find bugs, vulnerabilities. Fixing the weaknesses leads to increased resilience of the system.

Litmus takes a cloud-native approach to create, manage and monitor chaos. Chaos is orchestrated using the following Kubernetes Custom Resource Definitions (**CRDs**):

- **ChaosEngine**: A resource to link a Kubernetes application or Kubernetes node to a ChaosExperiment. ChaosEngine is watched by Litmus' Chaos-Operator which then invokes Chaos-Experiments
- **ChaosExperiment**: A resource to group the configuration parameters of a chaos experiment. ChaosExperiment CRs are created by the operator when experiments are invoked by ChaosEngine.
- **ChaosResult**: A resource to hold the results of a chaos-experiment. The Chaos-exporter reads the results and exports the metrics into a configured Prometheus server.

Chaos experiments are hosted on <a href="https://hub.litmuschaos.io" target="_blank">hub.litmuschaos.io</a>. It is a central hub where the application developers or vendors share their chaos experiments so that their users can use them to increase the resilience of the applications in production.

![Litmus workflow](/images/litmus-arch_1.png)

## Use cases

- **For Developers**: To run chaos experiments during application development as an extension of unit testing or integration testing.
- **For CI pipeline builders**: To run chaos as a pipeline stage to find bugs when the application is subjected to fail paths in a pipeline.
- **For SREs**: To plan and schedule chaos experiments into the application and/or surrounding infrastructure. This practice identifies the weaknesses in the system and increases resilience.

## Getting Started with Litmus

[![IMAGE ALT TEXT](images/maxresdefault.jpg)](https://youtu.be/W5hmNbaYPfM)

Check out the <a href="https://docs.litmuschaos.io/docs/next/getstarted.html" target="_blank">Litmus Docs</a> to get started.

## Contributing to Chaos Hub

Check out the <a href="https://github.com/litmuschaos/community-charts/blob/master/CONTRIBUTING.md" target="_blank">Contributing Guidelines for the Chaos Hub</a>

## Things to Consider

Some of the considerations that need to be made with Litmus (as a chaos framework), are broadly listed here. Many of these are already being worked on
as mentioned in the [ROADMAP](./ROADMAP.md). For details or limitations around specific experiments, refer to the respective [experiments docs](https://docs.litmuschaos.io/docs/pod-delete/).

- Litmus chaos operator and the chaos experiments run as kubernetes resources in the cluster. In case of airgapped environments, the chaos custom resources
  and images need to be hosted on premise.
- When attempting to execute platform specific chaos experiments (like those on AWS, GCP cloud) the access details are passed via kubernetes secrets. Support
  for other modes of secret management with Litmus is yet to be tested/implemented.
- Some chaos experiments make use of the docker api from within the experiment pods, and thereby require the docker socket to be mounted. User discretion is
  advised when allowing developers/devops admins/SREs access for running these experiments.
- In (rare) cases where chaos experiments make use of privileged containers, the recommended security policies will be documented.


## Community

Community Resources:

Feel free to reach out if you have any queries,concerns, or feature requests

- Follow LitmusChaos on Twitter [@LitmusChaos](https://twitter.com/LitmusChaos).

- Subscribe to the [LitmusChaos YouTube channel](https://www.youtube.com/channel/UCa57PMqmz_j0wnteRa9nCaw) for regular updates & meeting recordings. 

- To join our [Slack Community](https://slack.litmuschaos.io/) and meet our community members, put forward your questions & opinions, join the #litmus channel on the [Kubernetes Slack](https://slack.k8s.io/). 
### Community Meetings
The Litmus community meets on the third wednesday of every month at 10:00PM IST/6:30 PM CEST/9:30 AM PST.

- [Sync Up Meeting Link](https://zoom.us/j/91358162694)
- [Sync Up Agenda & Meeting Notes](https://hackmd.io/a4Zu_sH4TZGeih-xCimi3Q)
- [Release Tracker](https://github.com/litmuschaos/litmus/milestones)

### Blogs

- CNCF: [Introduction to LitmusChaos](https://www.cncf.io/blog/2020/08/28/introduction-to-litmuschaos/)
- Hackernoon: [Manage and Monitor Chaos via Litmus Custom Resources](https://hackernoon.com/solid-tips-on-how-to-manage-and-monitor-chaos-via-litmus-custom-resources-5g1s33m9)
- [Observability Considerations in Chaos: The Metrics Story](https://dev.to/ksatchit/observability-considerations-in-chaos-the-metrics-story-6cb)

Community Blogs:

- Daniyal Rayn: [Do I need Chaos Engineering on my environment? Trust me you need it!](https://maveric-systems.com/blog/do-i-need-chaos-engineering-on-my-environment-trust-me-you-need-it/)
- LiveWyer: [LitmusChaos Showcase: Chaos Experiments in a Helm Chart Test Suite](https://livewyer.io/blog/2021/03/22/litmuschaos-showcase-chaos-experiments-in-a-helm-chart-test-suite/)
- Jessica Cherry: [Test Kubernetes cluster failures and experiments in your terminal](https://opensource.com/article/21/6/kubernetes-litmus-chaos)
- Yang Chuansheng(KubeSphere): [KubeSphere 部署 Litmus 至 Kubernetes 开启混沌实验](https://kubesphere.io/zh/blogs/litmus-kubesphere/)
- Saiyam Pathak(Civo): [Chaos Experiments on Kubernetes using Litmus to ensure your cluster is production ready](https://www.civo.com/learn/chaos-engineering-kubernetes-litmus)
- Andreas Krivas(Container Solutions):[Comparing Chaos Engineering Tools for Kubernetes Workloads](https://blog.container-solutions.com/comparing-chaos-engineering-tools)
- Akram Riahi(WeScale):[Chaos Engineering : Litmus sous tous les angles](https://blog.wescale.fr/2021/03/11/chaos-engineering-litmus-sous-tous-les-angles/)
- Prashanto Priyanshu(LensKart):[Lenskart’s approach to Chaos Engineering-Part 2](https://blog.lenskart.com/lenskarts-approach-to-chaos-engineering-part-2-6290e4f3a74e)
- DevsDay.ru(Russian):[LitmusChaos at Kubecon EU '21](https://devsday.ru/blog/details/40746)
- Ryan Pei(Armory): [LitmusChaos in your Spinnaker Pipeline](https://www.armory.io/blog/litmuschaos-in-your-spinnaker-pipeline/)
- David Gildeh(Zebrium): [Using Autonomous Monitoring with Litmus Chaos Engine on Kubernetes](https://www.zebrium.com/blog/using-autonomous-monitoring-with-litmus-chaos-engine-on-kubernetes)


## Adopters

Check out the <a href="https://github.com/litmuschaos/litmus/blob/master/ADOPTERS.md" target="_blank">Adopters of LitmusChaos</a>

(_Send a PR to the above page if you are using Litmus in your chaos engineering practice_)

## License

Litmus is licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE) for the full license text. Some of the projects used by the Litmus project may be governed by a different license, please refer to its specific license.

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Flitmuschaos%2Flitmus.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Flitmuschaos%2Flitmus?ref=badge_large)

Litmus Chaos is part of the CNCF Projects.

[![CNCF](https://github.com/cncf/artwork/blob/master/other/cncf/horizontal/color/cncf-color.png)](https://landscape.cncf.io/selected=litmus)

## Important Links

<a href="https://docs.litmuschaos.io">
  Litmus Docs <img src="https://avatars0.githubusercontent.com/u/49853472?s=200&v=4" alt="Litmus Docs" height="15">
</a>
<br>
<a href="https://landscape.cncf.io/selected=litmus">
  CNCF Landscape <img src="https://landscape.cncf.io/images/left-logo.svg" alt="Litmus on CNCF Landscape" height="15">
</a>
