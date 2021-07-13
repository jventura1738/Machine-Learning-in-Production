= Kiali image:https://img.shields.io/twitter/url/http/shields.io.svg?style=social["Tweet about Kiali", link="https://twitter.com/intent/tweet?text=Learn%20what%20your%20Istio-Mesh%20is%20doing.%20Visit%20https://www.kiali.io/%20and%20@kiali_project"]
:toc: macro
:toc-title:

image:https://travis-ci.org/kiali/kiali.svg["Build Status", link="https://travis-ci.org/kiali/kiali"]
image:https://img.shields.io/badge/license-Apache2-blue.svg["Apache 2.0 license", link="LICENSE"]

== Introduction

Kiali provides answers to the questions: _What microservices are part of my Istio service mesh and how are they connected?_

image::https://raw.githubusercontent.com/kiali/kiali.io/master/static/images/documentation/features/graph-overview.png[Kiali Graph, width=880]

=== Table of contents

toc::[]

=== Description

A Microservice Architecture breaks up the monolith into many smaller pieces that are composed together. Patterns to secure the communication between services like fault tolerance (via timeout, retry, circuit breaking, etc.) have come up as well as distributed tracing to be able to see where calls are going.

A service mesh can now provide these services on a platform level and frees the application writers from those tasks. Routing decisions are done at the mesh level.

Kiali works with Istio to visualise the service mesh topology, and features like circuit breakers or request rates.

Kiali also includes an integration with Jaeger Tracing to augment the topology views with distributed transaction monitoring, and to also provide charts and stats about distributed traces.


=== Contributing

First, check the link:https://kiali.io/contribute[Contribute section in our web site], which provides a brief introduction on contributing, how to report issues and request features, and how to reach us.

If you would like to make code contributions, please also check the link:./CONTRIBUTING.md[Contribution Guide].

=== Getting Started

The target audience of this README are developers. If you are not a developer but want to learn more about Kiali, the link:https://www.kiali.io[Kiali documentation] should be more helpful. For instructions on installing Kiali, please read the link:https://www.kiali.io/documentation/latest/quick-start[Quick Start] page.

=== How and where Kiali is released?

Read the link:./RELEASING.adoc[RELEASING.adoc] file.

== Developer setup

[NOTE]
Please, complement the content of this readme document with the link:https://github.com/kiali/kiali-ui/blob/master/README.adoc[README.adoc document of the front-end repository]. Although this document has some instructions about building the front-end, they are not complete.

Make sure you have the following tools:

* The link:http://golang.org/doc/install[Go Programming Language]
** Currently, Kiali releases are built using Go 1.16. Although Kiali may build correctly using other versions of Go, it's suggested to use version 1.16.2 for development to ensure replicatable builds. Makefiles will require this minimum version of Go.
* link:http://git-scm.com/book/en/v2/Getting-Started-Installing-Git[git]
* link:https://docs.docker.com/installation/[Docker] or link:https://podman.io[Podman]
** If you are using `podman` declare the environment variable `DORP=podman`.
* link:https://nodejs.org[NodeJS] (with the NPM command)
* The _GNU make_ utility or any of it's alternatives

Once you have the required developer tools, you can get and build the code with the following script:

[source,shell]
----
# Checkout the source code
mkdir kiali_sources
cd kiali_sources
export KIALI_SOURCES=$(realpath .)

git clone https://github.com/kiali/kiali.git
git clone https://github.com/kiali/kiali-ui.git
git clone https://github.com/kiali/kiali-operator.git
git clone https://github.com/kiali/helm-charts.git

ln -s $KIALI_SOURCES/kiali-operator kiali/operator

# Build the back-end and run the tests
cd $KIALI_SOURCES/kiali
make build test

# Build the front-end and run the tests
cd $KIALI_SOURCES/kiali-ui
yarn && yarn build && yarn test
----

[NOTE]
The rest of this README assumes the directory tree created by the previous commands:

 -- kiali_sources
    |- kiali
    |- kiali-ui
    |- kiali-operator
    \- helm-charts

=== Create a Kubernetes cluster and install a Service Mesh

Since Kiali is a management console for an Istio-based service mesh, you will need an Istio-like Service Mesh to try Kiali. Then, Istio Meshes are installed on Kubernetes clusters.

We provide a few unsupported scripts that can help to get started:

* If you have an OpenShift 4.x pull secret and also have an AWS account, you can use the link:hack/aws-openshift.sh[`aws-openshift.sh`] script to create an OpenShift cluster in AWS with the needed resources for the Service Mesh. The command you may want to try is `aws-openshift.sh -kuca true create`.
** Once you have a cluster, you can use the link:hack/istio/install-sm2.sh[`install-sm2.sh`] to install the OpenShift Service Mesh, which is an Istio-based Service Mesh. Alternatively, you can also use link:https://maistra.io/[Maistra].
* If you are familiar to minikube, you may try the link:hack/k8s-minikube.sh[`k8s-minikube.sh`] script. The command you may want to try is `k8s-minikube.sh start && k8s-minikube.sh istio` which will create a cluster and install Istio on it. This script accept flags to let you install the link:https://istio.io/latest/docs/examples/bookinfo/[Bookinfo sample application], install Kiali and also some other flags to set up an environment where you can try the OpenId authentication and also to ease the setup of a multi-cluster environment.
* Finally, the link:hack/istio/install-istio-via-istioctl.sh[`install-istio-via-istioctl.sh`] and the link:hack/istio/install-bookinfo-demo.sh[`install-bookinfo-demo.sh`] scripts can assist into installing Istio and the Bookinfo sample application in your cluster, respectively. You can try running these scripts without any arguments.

These scripts are written to rely on the minimum dependencies as possible and will try to download any required tools. You can try running them, and the scripts will abort and ask manually install any required tool.

You can also use link:https://kind.sigs.k8s.io/[kind], however we don't have a script to create a kind cluster.

Depending on the type of cluster you are using, you should define the `CLUSTER_TYPE` environment variable on your shell to `openshift` (this is the default if not set), `minikube` or `kind` value so that the Makefiles can assist in other operations. If you are not using any of these clusters, you should set the environment variable to `CLUSTER_TYPE=local`.

[NOTE]
If you are using `minikube` it's recommended that you enable the `registry` and `ingress` add-on. The `k8s-minikube.sh` script should do this for you.

[NOTE]
If you are using `docker` and using minikube's registry add-on or any custom non-secure registry, make sure the link:https://docs.docker.com/registry/insecure/[Docker daemon is properly configured to use your registry].

=== Building the Container Image and deploying to a cluster

Assuming that:

* you have successfully built the back-end and the front-end,
* you also have created a Kubernetes cluster with an Istio-based Service Mesh installed on it,
* and you are not using the `CLUSTER_TYPE=local` environment variable

the following commands should deploy a development build of Kiali to the cluster:

[source,shell]
----
cd $KIALI_SOURCES/kiali

# Build the Kiali-server and Kiali-operator container images and push them to the cluster
make cluster-push

# If you want to only build and push the Kiali-server container images:
# make cluster-push-kiali

# If you want to only build and push the Kiali-operator container images:
# make cluster-push-operator

# Deploy the operator to the cluster
make operator-create

# Create a KialCR to instruct the operator to deploy Kiali
make kiali-create
----

If you are using the `CLUSTER_TYPE=local` environment variable, you will need to declare some additional environment variables to set the container registry where container images should be pushed and use `make container-push*` targets instead of `cluster-push*` targets. For example, if your container registry is `localhost:5000`:

[source,shell]
----
export QUAY_NAME=localhost:5000/kiali/kiali
export CONTAINER_NAME=localhost:5000/kiali/kiali
export OPERATOR_QUAY_NAME=localhost:5000/kiali/kiali-operator
export OPERATOR_CONTAINER_NAME=localhost:5000/kiali/kiali-operator

cd $KIALI_SOURCES/kiali

# Build the Kiali-server and Kiali-operator container images and push them to the cluster
make container-build container-push

# If you want to only build and push the Kiali-server container images:
# make container-build-kiali container-push-kiali-quay

# If you want to only build and push the Kiali-operator container images:
# make container-build-operator container-push-operator-quay

# Deploy the operator to the cluster
make operator-create

# Create a KialCR to instruct the operator to deploy Kiali
make kiali-create
----

=== Reloading Kiali image

If you already have Kiali installed and you want to recreate the kiali server pod, you can run the following command:

[source,shell]
----
cd $KIALI_SOURCES/kiali
make kiali-reload-image
----

This is to facilitate development. To quickly build a new Kiali container image and load it to the cluster, you can run:

[source,shell]
----
cd $KIALI_SOURCES/kiali-ui
yarn && yarn build

cd $KIALI_SOURCES/kiali
make clean build cluster-push-kiali kiali-reload-image
----

[NOTE]
There is no equivalent reload command for the operator. You would need to manually reload the operator via `kubectl` or `oc` commands.

=== Cluster clean-up

[source,shell]
----
cd $KIALI_SOURCES/kiali

# Delete the Kiali CR to let the operator remove Kiali.
make kiali-delete

# If the previous command never ends, the following command forces removal by bypassing the operator
# make kiali-purge

# Remove the operator
# NOTE: After this completes, the `kiali-create` and `kiali-delete` targets will be ineffective
# until you run the `operator-create` target to re-deploy the Kiali operator again.
make operator-delete
----

=== Code formatting and linting

If you are changing the back-end code of Kiali, before submitting a pull request make sure your changes are properly formatted and no new linting issues are introduced by running:

[source,shell]
----
# CD to the back-end source code
cd $KIALI_SOURCES/kiali

# Install linting tools
make lint-install

# Format the code and run linters
make format lint
----

=== Running Standalone

Rarely, you may want to run Kiali outside of any cluster environment, perhaps for debugging purposes. To do this, you
will want to use the link:./hack/run-kiali.sh[run-kiali.sh hack script] located in the
link:./hack[hack directory]. See the `--help` output for the options you can set.
The default configuration it uses is found in the link:./hack/run-kiali-config-template.yaml[config template file]
also located in the `hack` directory. Read the comments at the tops of both files for more details.

[source,shell]
----
cd $KIALI_SOURCES/kiali/hack
./run-kiali.sh
----

== Configuration

Many configuration settings can optionally be set within the Kiali Operator custom resource (CR) file. See link:https://github.com/kiali/kiali-operator/blob/master/deploy/kiali/kiali_cr.yaml[this example Kiali CR file] that has all the configuration settings documented.

== Embedding Kiali

If you want to embed Kiali in other applications, Kiali offers a simple feature called _Kiosk mode_. In this mode, Kiali won't show the main header, nor the main navigation bar.

To enable Kiosk mode, you only need to add a `kiosk=true` URL parameter. You will need to use the full path of the page you want to embed. For example, assuming that you access Kiali through HTTPS:

* To embed the _Overview_ page, use `https://_kiali_path_/overview?kiosk=true`.
* To embed the _Graph_ page, use `https://_kiali_path_/graph/namespaces?kiosk=true`.
* To embed the _Applications list_ page, use `https://_kiali_path_/applications?kiosk=true`.

If the page you want to embed uses other URL arguments, you can specify any of them to preset options. For example, if you want to embed the graph of the _bookinfo_ namespace, use the following URL: `http://_kiali_path_/graph/namespaces?namespaces=bookinfo&kiosk=true`.


== Configure External Services

=== Grafana

If you have Grafana installed in a custom way that is not easily auto-detectable by Kiali, you need to change in the Kiali CR the value of the grafana > url

[source,yaml]
----
apiVersion: kiali.io/v1alpha1
kind: Kiali
metadata:
  name: kiali
spec:
...
    external_services:
      grafana:
        url: http://grafana-istio-system.127.0.0.1.nip.io
...
----

== Additional Notes

=== Running the UI outside the cluster

When developing the http://github.com/kiali/kiali-ui[Kiali UI] you will find it useful to run it outside of the cluster to make it easier to update the UI code and see the changes without having to re-deploy. The preferred approach for this is to use the _proxy_ feature of React. The process is described https://github.com/kiali/kiali-ui#developing[here].

=== Disabling SSL

In the provided OpenShift templates, SSL is turned on by default. If you want to turn it off, you should:

* Remove the "tls: termination: reencrypt" option from the Kiali route

* Remove the "identity" block, with certificate paths, from the Kiali Config Map.

* Optionally you can also remove the annotation "service.beta.openshift.io/serving-cert-secret-name" in the Kiali Service, and the related `kiali-cabundle` volume that is declared and mounted in Kiali Deployment (but if you don't, they will just be ignored).

== Exposing Kiali to External Clients Using Istio Gateway

The operator will create a Route or Ingress by default (see the Kiali CR setting "deployment.ingress_enabled"). If you want to expose Kiali via Istio itself, you can create Gateway, Virtual Service, and Destination Rule resources similar to below:

[source,yaml]
----
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: kiali-gateway
  namespace: istio-system
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http-kiali
      protocol: HTTP
    # https://istio.io/latest/docs/reference/config/networking/gateway/#ServerTLSSettings
    tls:
      httpsRedirect: false
    hosts: [<your-host>]
  - port:
      number: 443
      name: https-kiali
      protocol: HTTPS
    tls: {}
    hosts: [<your-host>]
...
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: kiali-virtualservice
  namespace: istio-system
spec:
  gateways:
  - kiali-gateway
  hosts: [<your-host>]
  http:
  - route:
    - destination:
        host: kiali.istio-system.svc.cluster.local
        port:
          number: 20001
      weight: 100
...
---
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: kiali-destinationrule
  namespace: istio-system
spec:
  host: kiali
  trafficPolicy:
    tls:
      mode: DISABLE
...
----

== Experimental

=== Observing a Remote Cluster

[NOTE]
The "Central IstioD" setup is currently named "Primary-remote" multi-cluster setup.

[WARNING]
When this support was incorporated into Kiali, the "Central IstioD" setup of Istio was in an early development phase. These instructions are probably now broken.

There are certain use cases where Kiali needs to be deployed in one cluster (Control Plane) and observe a different cluster (Data Plane). link:https://user-images.githubusercontent.com/6889074/87819080-ad099980-c839-11ea-834b-56eec038ce4d.png[Diagram].

Follow these steps:

1: You should have the link:https://github.com/istio/istio/wiki/Central-Istiod-single-cluster-steps[remote central istiod with a single cluster] setup running

2: Create the link:https://github.com/istio/istio/blob/master/samples/addons/kiali.yaml[Kiali ClusterRole, ClusterRoleBinding, and ServiceAccount] in the Data Plane cluster

3: Create a remote secret in the Control Plane, using the Data Plane ServiceAccount you just created. This allows the Control Plane to read from and modify the Data Plane
[source,shell]
----
istioctl x create-remote-secret --service-account kiali-service-account --context=$DataPlane --name kiali | kubectl apply -n istio-system --context=$ControlPlane -f -
----

4: You will now run Kiali in the Control Plane. You need to add the remote secret to the Kiali Deployment by specifying a Volume and VolumeMount. When Kiali sees */kiali-remote-secret/kiali* it will use the remote cluster's API server instead of the local API server
[source,yaml]
----
spec:
  template:
    spec:
      containers:
      - volumeMounts:
        - mountPath: /kiali-remote-secret
          name: kiali-remote-secret
      volumes:
      - name: kiali-remote-secret
        secret:
          defaultMode: 420
          optional: true
          secretName: istio-remote-secret-kiali
----

5: Kiali now needs the Istio metrics from the sidecars. You need to run Prometheus in the Control Plane and have it scrape the metrics from an link:https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig:[envoyMetricsService]. These metrics are *required*:

  - istio_requests_total
  - istio_request_duration_milliseconds
  - istio_response_bytes
  - istio_request_bytes

6: Kiali in the Control Plane should now be fully functional with the Data Plane
