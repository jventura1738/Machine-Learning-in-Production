include::shared-doc/attributes.adoc[]

:toc:
:toclevels: 4
:numbered:

ifndef::ProductRelease,EAPCDRelease[]
= WildFly Quickstarts

[toc]

[abstract]
The quickstarts demonstrate Jakarta EE 8 and a few additional technologies from the WildFly stack. They provide small, specific, working examples that can be used as a reference for your own project.

[[introduction]]
== Introduction

These quickstarts run on the WildFly application server. The quickstarts are configured to use the correct Maven dependencies and ensure that you test and compile the quickstarts against the correct runtime environment.

Each quickstart folder contains a `README.adoc` file that describes the quickstart features and provides instructions about how to build and run it. Instructions are provided to build the more readable `README.html` files.

Make sure you read this entire document before you attempt to work with the quickstarts.

[[system_requirements]]
== System Requirements

The applications these projects produce are designed to be run on WildFly 16 or later.

All you need to build these projects is Java 8.0 (Java SDK 1.8) or later and Maven 3.3.1 or later.

[[use_of_product_home_and_jboss_home_variables]]
== Use of WILDFLY_HOME and QUICKSTART_HOME Variables

The quickstart `README` files use the _replaceable_ value `__WILDFLY_HOME__` to denote the path to the WildFly server. When you encounter this value in a `README` file, make sure you replace it with the actual path to your WildFly server.

When you see the replaceable variable __QUICKSTART_HOME__, replace it with the path to the root directory of all of the quickstarts.

[[prerequisites]]
== Prerequisites

Before you begin, you must perform the following tasks.

. xref:build_wildfly_server[Build the WildFly Server (Optional)]: This step is only required if you plan to run the latest https://github.com/wildfly/wildfly[development version of the WildFly server]. It is not required if you are running a https://github.com/wildfly/wildfly/tags[tagged] or https://github.com/wildfly/wildfly/releases[released] version of the WildFly server.

. xref:build_wildfly_boms[Build and Install the WildFly BOMs (Optional)]: This step is only required if you are building a development version of the WildFly server and see dependency issues when you build the quickstarts. It is not required if you are running a https://github.com/wildfly/quickstart/tags[tagged] or  https://github.com/wildfly/boms/releases[released] version of the WildFly server.

. xref:install_the_quickstart_parent_artifact_in_maven[Install the Quickstart Parent Artifact in Maven (Optional)]: This step is only required if you are running the latest https://github.com/wildfly/quickstart[development version of the quickstarts]. It is not required if you are running a https://github.com/wildfly/quickstart/tags[tagged] or https://github.com/wildfly/quickstart/releases[released] version of the quickstarts.

. xref:build_quickstart_readme_files[Build the Quickstart README.html Files (Required)]: The quickstart `README` files are written in AsciiDoc to provide modular, reusable content; however, this makes them difficult to read. For this reason, you must also build the quickstart `README.html` files from the AsciiDoc source.

[[build_wildfly_server]]
=== Build the WildFly Server (Optional)

If you have downloaded a https://github.com/wildfly/wildfly/tags[tagged] or https://github.com/wildfly/wildfly/releases[released] version of the WildFly server, you can ignore this step. You can simply extract the WildFly server from the compressed file and https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/START_JBOSS_EAP.adoc#start-the-red-hat-jboss-enterprise-application-platform-server[start the server] from that directory.

If you plan to run the https://github.com/wildfly/wildfly[development version of the WildFly server], you must first download and build the WildFly server from source.

. If you have not yet done so, you must clone https://github.com/wildfly/wildfly[Wildfly server] repository and navigate to it. You might also want to change the remote name from `origin` to `upstream` to be consistent with your other repositories.
+
[source,options="nowrap"]
----
$ git clone git@github.com:wildfly/wildfly.git
$ cd wildfly
$ git remote rename origin upstream
----
. Verify that your local `master` branch contains the latest updates.
+
[source,options="nowrap"]
----
$ git fetch upstream
$ git checkout master
$ git reset --hard upstream/master
----

. Build the WildFly server using the following command.
+
[source,options="nowrap"]
----
$ mvn clean install -DskipTests -Denforcer.skip=true -Dcheckstyle.skip=true
----

. The WildFly server folder and ZIP files, which are named `wildfly-__VERSION__-SNAPSHOT` and `wildfly-__VERSION__-SNAPSHOT.ZIP` respectively,  are located in the `build/target/` directory. You can copy that folder or unzip the file to another location or https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/START_JBOSS_EAP.adoc#start-the-red-hat-jboss-enterprise-application-platform-server[start the server] from that directory.


[[build_wildfly_boms]]
=== Build and Install the WildFly BOMs (Optional)

If you have downloaded and are running a https://github.com/wildfly/quickstart/tags[tagged] or https://github.com/wildfly/quickstart/releases[released] version of the quickstarts, you can ignore this step because the required BOMs are already installed in Maven.

If you are using the latest https://github.com/wildfly/quickstart[development version] of the quickstarts and you are able to successfully build and deploy the quickstarts, you can also ignore this step because the required BOMS are already installed in Maven.

However, if you  are using the latest https://github.com/wildfly/quickstart[development version] of the quickstarts and you see build errors indicating missing dependencies, you must first xref:build_wildfly_server[build the latest WildFly server] and then build and install the WildFly BOMs. This installs the latest Maven artifacts that are required by the SNAPSHOT version of the WildFly quickstarts that are still under development.

. If you have not yet done so, clone https://github.com/wildfly/boms[Wildfly BOMs] repository and navigate to it. You might also want to rename the directory to `wildfly-boms` to make it clear which BOMs it contains and also change the remote name from `origin` to `upstream` to be consistent with your other repositories.
+
[source,options="nowrap"]
----
$ git clone git@github.com:wildfly/boms.git
$ mv boms wildfly-boms
$ cd wildfly
$ git remote rename origin upstream
----
. Verify that your local `master` branch contains the latest updates.
+
[source,options="nowrap"]
----
$ git fetch upstream
$ git checkout master
$ git reset --hard upstream/master
----

. Build the WildFly BOMs using the following command.
+
[source,options="nowrap"]
----
$ mvn clean install
----
+
NOTE: If you run into build errors, check with the WildFly team to see if the repositories are temporarily out of sync.

. At this point, you can verify that all of the quickstarts build using the following command.
+
[source,options="nowrap"]
----
$ mvn clean install '-Pdefault,!complex-dependencies'
----

[[install_the_quickstart_parent_artifact_in_maven]]
=== Install the Quickstart Parent Artifact in Maven (Optional)

The root `POM.xml` file defines dependencies that are required by some of the quickstarts.

If you have downloaded and are running a https://github.com/wildfly/quickstart/tags[tagged] or https://github.com/wildfly/quickstart/releases[released] version of the quickstarts, you can ignore this step because the `quickstart-parent` artifact is already installed in Maven.

If you are running the latest https://github.com/wildfly/quickstart[development version] of the quickstarts, you must install the `quickstart-parent` artifact so its dependencies are available to the quickstarts that need it. To install it, navigate to your __QUICKSTART_HOME__ directory  directory and run the following command.

[source,subs="+quotes,attributes+",options="nowrap"]
----
$ cd __QUICKSTART_HOME__
$ mvn clean install -N
----

[[build_quickstart_readme_files]]
=== Build the Quickstart README.html Files (Required)

The quickstart `README` files are written in AsciiDoc, not only because the language is much more powerful than Markdown, but also also because it is possible to extract common instructions into separate files to be reused across the quickstarts. While this makes them more flexible and easier to maintain, unfortunately, included files do not render in a readable format in GitHub or in most text editors.

The Maven plugin that is used to build and deploy the quickstarts can also generate fully rendered `README.html` instructions from the `README.adoc` files.

To build all of the quickstart `README.html` files, including the root `README.html` file that contains the table with links to all available quickstarts, navigate to the root folder of the quickstarts and run the following command.

[source,options="nowrap"]
----
$ mvn clean package -Pdocs
----

[TIP]
====
To build the `README.html` file for a specific quickstart, navigate to the quickstart directory and run the above command.
====

If you see errors about missing dependencies, check the xref:prerequisites[prerequisites] section to determine whether you need to xref:build_wildfly_boms[build the WildFly BOMs] that corresponds to the version of the quickstarts that you are using.

[[suggested_approach_to_the_quickstarts]]
== Suggested Approach to the Quickstarts

We recommend that you approach the quickstarts as follows:

* Regardless of your level of expertise, we suggest you start with the `helloworld` quickstart. It is the simplest example and is an easy way to prove the server is configured and running correctly.
* If you are a beginner or new to JBoss, start with the quickstarts labeled `Beginner`, then try those marked as `Intermediate`. When you are comfortable with those, move on to the `Advanced` quickstarts.
* Some quickstarts are based upon other quickstarts but have expanded capabilities and functionality. If a prerequisite quickstart is listed, make sure you deploy and test it before looking at the expanded version.


[[run_the_quickstarts]]
== Run the Quickstarts Using the Maven Command Line

The root folder of each individual quickstart contains a `README.html` file with detailed instructions on how to build and run the example. In most cases you do the following:

* https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/START_JBOSS_EAP.adoc#start_the_jboss_eap_server[Start the WildFly server].
* Optionally, you can xref:build_the_quickstart_archive[build the quickstart archive] to test for compile errors.
* xref:build_and_deploy_the_quickstart[Build and deploy the quickstart].
* xref:undeploy_the_quickstart[Undeploy the quickstart] when you are finished testing.

IMPORTANT: See the `README` file in each individual quickstart folder for specific details and information on how to run and access the example.

[[build_the_quickstart_archive]]
==== Build the Quickstart Archive

You can follow these steps to build the application to test for compile errors or to view the contents of the archive. See the specific quickstart `README` file for complete details.

. Open a terminal and navigate to the root directory of the quickstart you want to build.
. Use the following command if you only want to build the archive, but not deploy it.
+
[source,options="nowrap"]
----
$ mvn clean install
----

[[build_and_deploy_the_quickstart]]
==== Build and Deploy the Quickstart

This section describes the basic steps to build and deploy an application. See the specific instructions in each quickstart `README` file for any variations to this process.

. Make sure you start the WildFly server as described in the quickstart `README` file.
. Open a terminal and navigate to the root directory of the quickstart you want to run.
. Use the following command to build and deploy the archive.
+
[source,options="nowrap"]
----
$ mvn clean install wildfly:deploy
----

[[undeploy_the_quickstart]]
==== Undeploy the Quickstart

Use the following command to undeploy the quickstart.

[source,options="nowrap"]
----
$ mvn wildfly:undeploy
----

[[run_the_quickstarts_in_jboss_developer_studio_or_eclipse]]
== Run the Quickstarts in Red Hat Developer Studio or Eclipse

You can also start the server and deploy the quickstarts or run the Arquillian tests from Eclipse using JBoss tools. For general information about how to import a quickstart, add a WildFly server, and build and deploy a quickstart, see https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/USE_JBDS.adoc#use_red_hat_jboss_developer_studio_or_eclipse_to_run_the_quickstarts[Use Red Hat Developer Studio or Eclipse to Run the Quickstarts].

[[optional_components]]
== Configure Optional Components

The following components are needed for only a small subset of the quickstarts. Do not install or configure them unless the quickstart requires it.

* xref:create_quickstart_users[Create Quickstart Users]
* xref:configure_postgresql[Configure the PostgreSQL Database]
* xref:configure_byteman[Configure Byteman]

[[create_quickstart_users]]
=== Create Quickstart Users

Some of the quickstarts, particularly those that run in a secured mode and demonstrate security, require that you create quickstart users with different roles for authorization purposes. See https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CREATE_USERS.adoc#create_users_required_by_the_quickstarts[Create Users Required by the Quickstarts] for detailed instructions to create users required by the quickstarts.

[[configure_postgresql]]
=== Configure the PostgreSQL Database

Some of the quickstarts that demonstrate transactions require that you install and configure the PostgreSQL database. See https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CONFIGURE_POSTGRESQL_JBOSS_EAP.adoc#configure_the_postgresql_database_for_use_with_the_quickstarts[Configure the PostgreSQL Database for Use with the Quickstarts] for instructions.

[[configure_byteman]]
=== Configure Byteman

A few of the quickstarts use _Byteman_ to demonstrate distributed transaction processing and crash recovery. See  https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CONFIGURE_BYTEMAN.adoc#configure_byteman_for_use_with_the_quickstarts[Configure Byteman for Use with the Quickstarts] for instructions.

// END ifndef::ProductRelease,EAPCDRelease[]
endif::[]

//**********************************************************************************
//
// WildFly Developers: You can ignore the rest of this file.
// It is for the JBoss EAP product and CD Releases.
//
//**********************************************************************************

ifdef::ProductRelease,EAPCDRelease[]
// These instrutions are only for the JBoss EAP product and CD Releases.
= {productNameFull} ({productName}) Quickstarts

[abstract]
The quickstarts demonstrate {javaVersion} and a few additional technologies from the {productNameFull} stack. They provide small, specific, working examples that can be used as a reference for your own project.

[[introduction]]
== Introduction

These quickstarts run on {productNameFull} {productVersion}. Each quickstart folder contains a `README{outfilesuffix}` file that describes the quickstart features and provides instructions about how to build and run it.

We recommend that you use the *{quickstartDownloadName}* ZIP file, which you can download from the {quickstartDownloadUrl}[{productName} Software Download] page on the Red Hat Customer Portal. This version of the quickstarts uses the correct dependencies and ensures that you test and compile against the correct server runtime environment.

Each quickstart folder contains a `README{outfilesuffix}` file that describes the quickstart features and provides instructions about how to build and run it.

Make sure you read this entire document before you attempt to work with the quickstarts.


ifdef::ProductRelease[]
// System Requirements are not needed for the CD Releases, only for the Product Release.
[[system_requirements]]
== System Requirements

The applications these projects produce are designed to be run on {productNameFull} {productVersion} or later.

All you need to build these projects is {buildRequirements}.
// END ifdef::ProductRelease[]
endif::[]

ifdef::ProductRelease[]
// Replaceable values are not used in the CD Releases, only for the Product Release.
[[use_of_product_home_and_jboss_home_variables]]
== Use of {jbossHomeName} and QUICKSTART_HOME Variables

The quickstart `README` files use the _replaceable_ value `__{jbossHomeName}__`  to denote the path to the {productName} installation. When you encounter this value in a `README` file, make sure you replace it with the actual path to your {productName} installation. The installation path is described in detail here: link:{useProductHomeDocUrl}[Use of __{jbossHomeName}__ and __JBOSS_HOME__ Variables]

When you see the replaceable variable __QUICKSTART_HOME__, replace it with the path to the root directory of all of the quickstarts.
// END ifdef::ProductRelease[]
endif::[]

[[suggested_approach_to_the_quickstarts]]
== Suggested Approach to the Quickstarts

We suggest you approach the quickstarts as follows:

* Regardless of your level of expertise, we suggest you start with the `helloworld{outfilesuffix}` quickstart. It is the simplest example and is an easy way to prove the server is configured and running correctly.
* If you are a beginner or new to JBoss, start with the quickstarts labeled `Beginner`, then try those marked as `Intermediate`. When you are comfortable with those, move on to the `Advanced` quickstarts.
* Some quickstarts are based upon other quickstarts but have expanded capabilities and functionality. If a prerequisite quickstart is listed, make sure you deploy and test it before looking at the expanded version.


ifdef::EAPCDRelease[]
// Getting Started with OpenShift is only needed for the CD Releases
// Getting Started with OpenShift
include::shared-doc/cd-openshift-getting-started-overview.adoc[leveloffset=+1]
// END ifdef::EAPCDRelease[]
endif::[]


ifdef::ProductRelease[]
// Running the quickstarts is not used in the CD Releases, only for the Product Release.
[[run_the_quickstarts]]
== Run the Quickstarts Using the Maven Command Line

The root folder of each individual quickstart contains a `README` file with specific details on how to build and run the example. In most cases you do the following:

* link:{StartServerDocUrl}[Start the {productName} server].
* Optionally, you can xref:build_the_quickstart_archive[build the quickstart archive] to test for compile errors.
* xref:build_and_deploy_the_quickstart[Build and deploy the quickstart].
* xref:undeploy_the_quickstart[Undeploy the quickstart] when you are finished testing.

IMPORTANT: See the `README` file in each individual quickstart folder for specific details and information on how to run and access the example.

[[build_the_quickstart_archive]]
==== Build the Quickstart Archive

You can follow these steps to build the application to test for compile errors or to view the contents of the archive. See the specific quickstart `README` file for complete details.

. Open a terminal and navigate to the root directory of the quickstart you want to build.
. Use the following command if you only want to build the archive, but not deploy it.
+
[source,options="nowrap"]
----
$ mvn clean install
----

[[build_and_deploy_the_quickstart]]
==== Build and Deploy the Quickstart

This section describes the basic steps to build and deploy an application. See the specific instructions in each quickstart `README` file for any variations to this process.

. Make sure you start the {productName} server as described in the quickstart `README` file.
. Open a terminal and navigate to the root directory of the quickstart you want to run.
. Use the following command to build and deploy the archive.
+
[source,options="nowrap"]
----
$ mvn clean install wildfly:deploy
----

[[undeploy_the_quickstart]]
==== Undeploy an Quickstart

Use the following command to undeploy the quickstart.

[source,options="nowrap"]
----
$ mvn wildfly:undeploy
----
// END ifdef::ProductRelease[]
endif::[]


ifdef::ProductRelease[]
// Running the quickstarts in Eclipse is not used in the CD Releases, only for the Product Release.
[[run_the_quickstarts_in_jboss_developer_studio_or_eclipse]]
== Run the Quickstarts in {JBDSProductName} or Eclipse

You can also start the server and deploy the quickstarts or run the Arquillian tests from Eclipse using JBoss tools. For general information about how to import a quickstart, add a {productName} server, and build and deploy a quickstart, see link:{useEclipseUrl}[Use {JBDSProductName} or Eclipse to Run the Quickstarts].
// END ifdef::ProductRelease[]
endif::[]


ifdef::ProductRelease[]
// Optional components are not used in the CD Releases, only for the Product Release.
[[optional_components]]
== Configure Optional Components

The following components are needed for only a small subset of the quickstarts. Do not install or configure them unless the quickstart requires it.

* xref:create_quickstart_users[Create Quickstart Users]
* xref:configure_postgresql[Configure the PostgreSQL Database]
* xref:configure_byteman[Configure Byteman]

[[create_quickstart_users]]
=== Create Quickstart Users

Some of the quickstarts, particularly those that run in a secured mode and demonstrate security, require that you create quickstart users with different roles for authorization purposes. See https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CREATE_USERS.adoc#create_users_required_by_the_quickstarts[Create Users Required by the Quickstarts] for detailed instructions to create users required by the quickstarts.

[[configure_postgresql]]
=== Configure the PostgreSQL Database

Some of the quickstarts that demonstrate transactions require that you install and configure the PostgreSQL database. See https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CONFIGURE_POSTGRESQL_JBOSS_EAP.adoc#configure_the_postgresql_database_for_use_with_the_quickstarts[Configure the PostgreSQL Database for Use with the Quickstarts] for instructions.

[[configure_byteman]]
=== Configure Byteman

A few of the quickstarts use _Byteman_ to demonstrate distributed transaction processing and crash recovery. See  https://github.com/jboss-developer/jboss-developer-shared-resources/blob/master/guides/CONFIGURE_BYTEMAN.adoc#configure_byteman_for_use_with_the_quickstarts[Configure Byteman for Use with the Quickstarts] for instructions.
// END ifdef::ProductRelease[]
endif::[]

// END ifdef::ProductRelease,EAPCDRelease[]
endif::[]

// The following is included for all versions: WildFly, JBoss EAP, and EAP CD
[[available_quickstarts]]
== Table of Available Quickstarts

All available quickstarts, which are listed in the following table, can be found here: {githubRepoUrl}.

Each quickstart provides the list of technologies demonstrated by the quickstart and the required experience level needed to build and deploy it. Click on the quickstart link in the table to see more detailed information about how to run it. Some quickstarts require deployment of other quickstarts. This information is noted in the `Prerequisites` section of the quickstart `README.html` file.

NOTE: Some of these quickstarts use the H2 database included with WildFly. It is a lightweight, relational example datasource that is used for examples only. It is not robust or scalable, is not supported, and should NOT be used in a production environment!

//<TOC>
[cols="1,1,2,1,1", options="header"]
|===
| Quickstart Name | Demonstrated Technologies | Description | Experience Level Required | Prerequisites 
| link:app-client/README{outfilesuffix}[app-client]|EJB, EAR, AppClient | The `app-client` quickstart demonstrates how to code and package a client app and use the {productName} client container to start the client `Main` program. | Intermediate | _none_
| link:batch-processing/README{outfilesuffix}[batch-processing]|CDI, Batch 1.0, JSF | The `batch-processing` quickstart shows how to use chunk oriented batch jobs to import a file to a database. | Intermediate | _none_
| link:bean-validation/README{outfilesuffix}[bean-validation]|CDI, JPA, BV | The `bean-validation` quickstart provides Arquillian tests to demonstrate how to use CDI, JPA, and Bean Validation. | Beginner | _none_
| link:bean-validation-custom-constraint/README{outfilesuffix}[bean-validation-custom-constraint]|CDI, JPA, BV | The `bean-validation-custom-constraint` quickstart demonstrates how to use the Bean Validation API to define custom constraints and validators. | Beginner | _none_
| link:bmt/README{outfilesuffix}[bmt]|EJB, BMT | The `bmt` quickstart demonstrates Bean-Managed Transactions (BMT), showing how to manually manage transaction demarcation while accessing JPA entities. | Intermediate | _none_
| link:cmt/README{outfilesuffix}[cmt]|EJB, CMT, JMS | The `cmt` quickstart demonstrates Container-Managed Transactions (CMT), showing how to use transactions managed by the container. | Intermediate | _none_
| link:contacts-jquerymobile/README{outfilesuffix}[contacts-jquerymobile]|jQuery Mobile, jQuery, JavaScript, HTML5, REST | The `contacts-jquerymobile` quickstart demonstrates a {javaVersion} mobile database application using HTML5, jQuery Mobile, JAX-RS, JPA, and REST. | Beginner | _none_
| link:ejb-asynchronous/README{outfilesuffix}[ejb-asynchronous]|Asynchronous EJB | The `ejb-asynchronous` quickstart demonstrates the behavior of asynchronous EJB invocations by a deployed EJB and a remote client and how to handle errors. | Advanced | _none_
| link:ejb-in-ear/README{outfilesuffix}[ejb-in-ear]|EJB, EAR | The `ejb-in-ear` quickstart demonstrates how to deploy an EAR archive that contains a *JSF* WAR and an EJB JAR. | Intermediate | _none_
| link:ejb-in-war/README{outfilesuffix}[ejb-in-war]|EJB, JSF, WAR | The `ejb-in-war` quickstart demonstrates how to package an EJB bean in a WAR archive and deploy it to {productName}. Arquillian tests are also provided. | Intermediate | _none_
| link:ejb-multi-server/README{outfilesuffix}[ejb-multi-server]|EJB, EAR | The `ejb-multi-server` quickstart shows how to communicate between multiple applications deployed to different servers using an EJB to log the invocation. | Advanced | _none_
| link:ejb-remote/README{outfilesuffix}[ejb-remote]|EJB, JNDI | The `ejb-remote` quickstart uses EJB and JNDI to demonstrate how to access an EJB, deployed to {productName}, from a remote Java client application. | Intermediate | _none_
| link:ejb-security/README{outfilesuffix}[ejb-security]|EJB, Security | The `ejb-security` quickstart demonstrates the use of Jakarta EE declarative security to control access to EJBs in {productName}. | Intermediate | _none_
| link:ejb-security-context-propagation/README{outfilesuffix}[ejb-security-context-propagation]|EJB, Security | The `ejb-security-context-propagation` quickstart demonstrates how the security context can be propagated to a remote EJB using a remote outbound connection configuration | Advanced | _none_
| link:ejb-security-jaas/README{outfilesuffix}[ejb-security-jaas]|EJB, Security | The `ejb-security-jaas` quickstart demonstrates how legacy `JAAS` security domains can be used in conjunction with `Elytron` | Intermediate | _none_
| link:ejb-security-programmatic-auth/README{outfilesuffix}[ejb-security-programmatic-auth]|EJB, Security | The `ejb-security-programmatic-auth` quickstart demonstrates how to programmatically setup different identities when invoking a remote secured EJB. | Intermediate | _none_
| link:ejb-throws-exception/README{outfilesuffix}[ejb-throws-exception]|EJB, EAR | The `ejb-throws-exception` quickstart demonstrates how to throw and handle exceptions across JARs in an EAR. | Intermediate | _none_
| link:ejb-timer/README{outfilesuffix}[ejb-timer]|EJB Timer | The `ejb-timer` quickstart demonstrates how to use the EJB timer service `@Schedule` and `@Timeout` annotations with {productName}. | Beginner | _none_
| link:greeter/README{outfilesuffix}[greeter]|CDI, JSF, JPA, EJB, JTA | The `greeter` quickstart demonstrates the use of CDI, JPA, JTA, EJB and JSF in {productName}. | Beginner | _none_
| link:ha-singleton-deployment/README{outfilesuffix}[ha-singleton-deployment]|EJB, Singleton Deployments, Clustering | The `ha-singleton-deployment` quickstart demonstrates the recommended way to deploy any service packaged in an application archive as a cluster-wide singleton. | Advanced | _none_
| link:ha-singleton-service/README{outfilesuffix}[ha-singleton-service]|JBoss MSC, Singleton Service, Clustering | The `ha-singleton-service` quickstart demonstrates how to deploy a cluster-wide singleton JBoss MSC service. | Advanced | _none_
| link:helloworld/README{outfilesuffix}[helloworld]|CDI, Servlet | The `helloworld` quickstart demonstrates the use of CDI and Servlet 3 and is a good starting point to verify {productName} is configured correctly. | Beginner | _none_
| link:helloworld-html5/README{outfilesuffix}[helloworld-html5]|CDI, JAX-RS, HTML5 | The `helloworld-html5` quickstart demonstrates the use of CDI 1.2 and JAX-RS 2.0 using the HTML5 architecture and RESTful services on the backend. | Beginner | _none_
| link:helloworld-jms/README{outfilesuffix}[helloworld-jms]|JMS | The `helloworld-jms` quickstart demonstrates the use of external JMS clients with {productName}. | Intermediate | _none_
| link:helloworld-mbean/README{outfilesuffix}[helloworld-mbean]|CDI, JMX, MBean | The `helloworld-mbean` quickstart demonstrates the use of CDI and MBean in {productName} and includes JConsole instructions and Arquillian tests. | Intermediate | _none_
| link:helloworld-mdb/README{outfilesuffix}[helloworld-mdb]|JMS, EJB, MDB | The `helloworld-mdb` quickstart uses JMS and EJB Message-Driven Bean (MDB) to create and deploy JMS topic and queue resources in {productName}. | Intermediate | _none_
| link:helloworld-mdb-propertysubstitution/README{outfilesuffix}[helloworld-mdb-propertysubstitution]|JMS, EJB, MDB | The `helloworld-mdb-propertysubstitution` quickstart demonstrates the use of JMS and EJB MDB, enabling property substitution with annotations. | Intermediate | _none_
| link:helloworld-mutual-ssl/README{outfilesuffix}[helloworld-mutual-ssl]|Mutual SSL, Undertow | The `helloworld-mutual-ssl` quickstart is a basic example that demonstrates mutual SSL configuration in {productName} | Intermediate | _none_
| link:helloworld-mutual-ssl-secured/README{outfilesuffix}[helloworld-mutual-ssl-secured]|Mutual SSL, Security, Undertow | The `helloworld-mutual-ssl-secured` quickstart demonstrates securing a Web application using client mutual SSL authentication and role-based access control | Intermediate | _none_
| link:helloworld-rs/README{outfilesuffix}[helloworld-rs]|CDI, JAX-RS | The `helloworld-rs` quickstart demonstrates a simple Hello World application, bundled and deployed as a WAR, that uses JAX-RS to say Hello. | Intermediate | _none_
| link:helloworld-singleton/README{outfilesuffix}[helloworld-singleton]|EJB, Singleton | The `helloworld-singleton` quickstart demonstrates an EJB Singleton Bean that is instantiated once and maintains state for the life of the session. | Beginner | _none_
| link:helloworld-ssl/README{outfilesuffix}[helloworld-ssl]|SSL, Undertow | The `helloworld-ssl` quickstart is a basic example that demonstrates server side SSL configuration in {productName}. | Beginner | _none_
| link:helloworld-ws/README{outfilesuffix}[helloworld-ws]|JAX-WS | The `helloworld-ws` quickstart demonstrates a simple Hello World application, bundled and deployed as a WAR, that uses JAX-WS to say Hello. | Beginner | _none_
| link:hibernate/README{outfilesuffix}[hibernate]|Hibernate | The `hibernate` quickstart demonstrates how to use Hibernate ORM 5 API over JPA, using Hibernate-Core and Hibernate Bean Validation, and EJB. | Intermediate | _none_
| link:inter-app/README{outfilesuffix}[inter-app]|EJB, CDI, JSF | The `inter-app` quickstart shows you how to use a shared API JAR and an EJB to provide inter-application communication between two WAR deployments. | Advanced | _none_
| link:jaxrs-client/README{outfilesuffix}[jaxrs-client]|JAX-RS | The `jaxrs-client` quickstart demonstrates JAX-RS Client API, which interacts with a JAX-RS Web service that runs on {productName}. | Beginner | _none_
| link:jaxws-addressing/README{outfilesuffix}[jaxws-addressing]|JAX-WS | The `jaxws-addressing` quickstart is a working example of the web service using WS-Addressing. | Beginner | _none_
| link:jaxws-ejb/README{outfilesuffix}[jaxws-ejb]|JAX-WS | The `jaxws-ejb` quickstart is a working example of the web service endpoint created from an EJB. | Beginner | _none_
| link:jaxws-pojo/README{outfilesuffix}[jaxws-pojo]|JAX-WS | The `jaxws-pojo` quickstart is a working example of the web service endpoint created from a POJO. | Beginner | _none_
| link:jaxws-retail/README{outfilesuffix}[jaxws-retail]|JAX-WS | The `jaxws-retail` quickstart is a working example of a simple web service endpoint. | Beginner | _none_
| link:jsonp/README{outfilesuffix}[jsonp]|CDI, JSF, JSON-P | The `jsonp` quickstart demonstrates how to use the JSON-P API to produce object-based structures and then parse and consume them as stream-based JSON strings. | Beginner | _none_
| link:jta-crash-rec/README{outfilesuffix}[jta-crash-rec]|JTA, Crash Recovery | The `jta-crash-rec` quickstart uses JTA and Byteman to show how to code distributed (XA) transactions in order to preserve ACID properties on server crash. | Advanced | _none_
| link:jts/README{outfilesuffix}[jts]|JTS, EJB, JMS | The `jts` quickstart shows how to use JTS to perform distributed transactions across multiple containers, fulfilling the properties of an ACID transaction. | Intermediate | link:cmt/README.html[cmt]
| link:jts-distributed-crash-rec/README{outfilesuffix}[jts-distributed-crash-rec]|JTS, Crash Recovery | The `jts-distributed-crash-rec` quickstart uses JTS and Byteman to demonstrate distributed crash recovery across multiple application servers. | Advanced | link:jts/README.html[jts]
| link:kitchensink/README{outfilesuffix}[kitchensink]|CDI, JSF, JPA, EJB, JAX-RS, BV | The `kitchensink` quickstart demonstrates a {javaVersion} web-enabled database application using JSF, CDI, EJB, JPA, and Bean Validation. | Intermediate | _none_
| link:kitchensink-angularjs/README{outfilesuffix}[kitchensink-angularjs]|AngularJS, CDI, JPA, EJB, JPA, JAX-RS, BV | The `kitchensink-angularjs` quickstart demonstrates a {javaVersion} application using AngularJS with JAX-RS, CDI, EJB, JPA, and Bean Validation. | Intermediate | _none_
| link:kitchensink-ear/README{outfilesuffix}[kitchensink-ear]|CDI, JSF, JPA, EJB, JAX-RS, BV, EAR | The `kitchensink-ear` quickstart demonstrates web-enabled database application, using JSF, CDI, EJB, JPA, and Bean Validation, packaged as an EAR. | Intermediate | _none_
| link:kitchensink-jsp/README{outfilesuffix}[kitchensink-jsp]|JSP, JSTL, CDI, JPA, EJB, JAX-RS, BV | The `kitchensink-jsp` quickstart demonstrates how to use JSP, JSTL, CDI, EJB, JPA, and Bean Validation in {productName}. | Intermediate | _none_
| link:kitchensink-ml/README{outfilesuffix}[kitchensink-ml]|CDI, JSF, JPA, EJB, JAX-RS, BV, i18n, l10n | The `kitchensink-ml` quickstart demonstrates a localized {javaVersion} compliant application using JSF, CDI, EJB, JPA, and Bean Validation. | Intermediate | _none_
| link:logging/README{outfilesuffix}[logging]|Logging | The `logging` quickstart demonstrates how to configure different logging levels in {productName}. It also includes an asynchronous logging example. | Intermediate | _none_
| link:logging-tools/README{outfilesuffix}[logging-tools]|JBoss Logging Tools | The `logging-tools` quickstart shows how to use JBoss Logging Tools to create internationalized loggers, exceptions, and messages and localize them. | Beginner | _none_
| link:mail/README{outfilesuffix}[mail]|JavaMail, CDI, JSF | The `mail` quickstart demonstrates how to send email using CDI and JSF and the default Mail provider that ships with {productName}. | Beginner | _none_
| link:managed-executor-service/README{outfilesuffix}[managed-executor-service]|EE Concurrency Utilities, JAX-RS, JAX-RS Client API | The `managed-executor-service` quickstart demonstrates how Jakarta EE applications can submit tasks for asynchronous execution. | Beginner | _none_
| link:messaging-clustering/README{outfilesuffix}[messaging-clustering]|JMS, MDB | The `messaging-clustering` quickstart does not contain any code and instead uses the `helloworld-mdb` quickstart to demonstrate clustering using ActiveMQ Messaging. | Intermediate | link:helloworld-mdb/README.html[helloworld-mdb]
| link:messaging-clustering-singleton/README{outfilesuffix}[messaging-clustering-singleton]|JMS, MDB, Clustering | The `messaging-clustering-singleton` quickstart uses a JMS topic and a queue to demonstrate clustering using {productName} messaging with MDB singleton configuration where only one node in the cluster will be active. | Advanced | _none_
| link:numberguess/README{outfilesuffix}[numberguess]|CDI, JSF | The `numberguess` quickstart demonstrates the use of CDI  (Contexts and Dependency Injection) and JSF (JavaServer Faces) in {productName}. | Beginner | _none_
| link:payment-cdi-event/README{outfilesuffix}[payment-cdi-event]|CDI, JSF | The `payment-cdi-event` quickstart demonstrates how to create credit and debit CDI Events in {productName}, using a JSF front-end client. | Beginner | _none_
| link:resteasy-jaxrs-client/README{outfilesuffix}[resteasy-jaxrs-client]|JAX-RS, CDI | The `resteasy-jaxrs-client` quickstart demonstrates an external JAX-RS RestEasy client, which interacts with a JAX-RS Web service that uses CDI and JAX-RS. | Intermediate | link:helloworld-rs/README.html[helloworld-rs]
| link:servlet-async/README{outfilesuffix}[servlet-async]|Asynchronous Servlet, CDI, EJB | The `servlet-async` quickstart demonstrates how to use asynchronous servlets to detach long-running tasks and free up the request processing thread. | Intermediate | _none_
| link:servlet-filterlistener/README{outfilesuffix}[servlet-filterlistener]|Servlet Filter, Servlet Listener | The `servlet-filterlistener` quickstart demonstrates how to use Servlet filters and listeners in an application. | Intermediate | _none_
| link:servlet-security/README{outfilesuffix}[servlet-security]|Servlet, Security | The `servlet-security` quickstart demonstrates the use of Jakarta EE declarative security to control access to Servlets and Security in {productName}. | Intermediate | _none_
| link:shopping-cart/README{outfilesuffix}[shopping-cart]|SFSB EJB | The `shopping-cart` quickstart demonstrates how to deploy and run a simple {javaVersion} shopping cart application that uses a stateful session bean (SFSB). | Intermediate | _none_
| link:spring-greeter/README{outfilesuffix}[spring-greeter]|Spring MVC, JSP, JPA | The `spring-greeter` quickstart is based on the `greeter` quickstart, but differs in that it uses Spring MVC for Mapping `GET` and `POST` requests. | Beginner | _none_
| link:spring-kitchensink-basic/README{outfilesuffix}[spring-kitchensink-basic]|JSP, JPA, JSON, Spring, JUnit | The `spring-kitchensink-basic` quickstart is an example of a {javaVersion} application using JSP, JPA and Spring 4.x. | Intermediate | _none_
| link:spring-kitchensink-springmvctest/README{outfilesuffix}[spring-kitchensink-springmvctest]|JSP, JPA, JSON, Spring, JUnit | The  `spring-kitchensink-springmvctest` quickstart demonstrates how to create an MVC application using JSP, JPA and Spring 4.x. | Intermediate | _none_
| link:spring-resteasy/README{outfilesuffix}[spring-resteasy]|Resteasy, Spring | The `spring-resteasy` quickstart demonstrates how to package and deploy a web application that includes resteasy-spring integration. | Beginner | _none_
| link:tasks-jsf/README{outfilesuffix}[tasks-jsf]|JSF, JPA | The `tasks-jsf` quickstart demonstrates how to use JPA persistence with JSF as the view layer. | Intermediate | _none_
| link:tasks-rs/README{outfilesuffix}[tasks-rs]|JPA, JAX-RS | The `tasks-rs` quickstart demonstrates how to implement a JAX-RS service that uses JPA persistence. | Intermediate | _none_
| link:temperature-converter/README{outfilesuffix}[temperature-converter]|CDI, JSF, SLSB EJB | The `temperature-converter` quickstart does temperature conversion using an EJB Stateless Session Bean (SLSB), CDI, and a JSF front-end client. | Beginner | _none_
| link:thread-racing/README{outfilesuffix}[thread-racing]|Batch, CDI, EE Concurrency, JAX-RS, JMS, JPA, JSON, Web Sockets | A thread racing web application that demonstrates technologies introduced or updated in the latest Jakarta EE specification. | Beginner | _none_
| link:websocket-client/README{outfilesuffix}[websocket-client]|Web Socket, CDI Events, JSON, SSL | Demonstrates use of a Javascript WebSocket client, WebSocket configuration, programmatic binding, and secure WebSocket. | Intermediate | _none_
| link:websocket-endpoint/README{outfilesuffix}[websocket-endpoint]|CDI, WebSocket, JSON-P | Shows how to use WebSockets with JSON to broadcast information to all open WebSocket sessions in {productName}. | Beginner | _none_
| link:websocket-hello/README{outfilesuffix}[websocket-hello]|WebSocket, CDI, JSF | The `websocket-hello` quickstart demonstrates how to create a simple WebSocket application. | Beginner | _none_
| link:wsat-simple/README{outfilesuffix}[wsat-simple]|WS-AT, JAX-WS | The `wsat-simple` quickstart demonstrates a WS-AT (WS-AtomicTransaction) enabled JAX-WS Web service, bundled as a WAR, and deployed to {productName}. | Intermediate | _none_
| link:wsba-coordinator-completion-simple/README{outfilesuffix}[wsba-coordinator-completion-simple]|WS-BA, JAX-WS | The `wsba-coordinator-completion-simple` quickstart deploys a WS-BA (WS Business Activity) enabled JAX-WS Web service WAR (CoordinatorCompletion protocol). | Intermediate | _none_
| link:wsba-participant-completion-simple/README{outfilesuffix}[wsba-participant-completion-simple]|WS-BA, JAX-WS | The `wsba-participant-completion-simple` quickstart deploys a WS-BA (WS Business Activity) enabled JAX-WS Web service WAR (ParticipantCompletion Protocol). | Intermediate | _none_
| link:xml-jaxp/README{outfilesuffix}[xml-jaxp]|JAXP, SAX, DOM, Servlet | The `xml-jaxp` quickstart demonstrates how to use Servlet and JSF to upload an XML file to {productName} and validate and parse it using DOM or SAX. | Intermediate | _none_
|===
//</TOC>

