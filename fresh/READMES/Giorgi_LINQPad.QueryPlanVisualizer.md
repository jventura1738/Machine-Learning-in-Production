# LINQPad.QueryPlanVisualizer

[![NuGet Package](https://img.shields.io/nuget/dt/LINQPadQueryPlanVisualizer.svg?label=LINQPadQueryPlanVisualizer&style=flat-square&logo=NuGet)](https://www.nuget.org/packages/LINQPadQueryPlanVisualizer/)
[![GitHub all releases](https://img.shields.io/github/downloads/Giorgi/LINQPad.QueryPlanVisualizer/total?logo=github&style=flat-square)](https://github.com/Giorgi/LINQPad.QueryPlanVisualizer/releases)
[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square&logo=Apache)](License.md)
[![Ko-Fi](https://img.shields.io/static/v1?style=flat-square&message=Support%20the%20Project&color=success&style=plastic&logo=ko-fi&label=$$)](https://ko-fi.com/U6U81LHU8)

## SQL Server and PostgreSQL query execution plan visualizer for LINQPad

<img align="right" width="200" height="200" src="IconSmall.png">

## Features

* View query execution plan inside LINQPad
* View missing indexes for query
* Share plan to [https://www.brentozar.com/pastetheplan/](https://www.brentozar.com/pastetheplan/) or [https://explain.dalibo.com/](https://explain.dalibo.com/)
* Create missing indexes directly from LINQPad
* Open plan in SQL Server Management Studio or another default app
* Save plan to disk

Supported databases: Sql Server and PostgreSQL.

Supported ORMs: `Entity Framework Core 5` and `LINQ to SQL`

## Getting Started

**If you use LINQPad 6, you must use version 2.X of this library. For LINQPad 5, you must use version 1.X**

Version 2.1 and newer uses **Microsoft Edge WebView2** to display the query plan. This requires either **WebView2 Runtime** to be installed or a recent version of Edge Canary. To download WebView2 Runtime visit [Microsoft Edge WebView2 Download Page](https://developer.microsoft.com/en-us/microsoft-edge/webview2/).

### Install from NuGet

If you have a Developer or higher edition of LINQPad, you can use the `LINQPadQueryPlanVisualizer` package from NuGet
to add the visualizer to your queries.

### Install as plugin

To install the visualizer as a LINQPad plugin, download the [latest release](https://github.com/Giorgi/QueryPlanVisualizer/releases/latest) and drop the visualizer dll directly inside LINQPad's plugins folder (by default found at **My Documents\LINQPad Plugins\NetCore3** for LINQPad 6 and **My Documents\LINQPad Plugins\Framework 4.6** for LINQPad 5). The plugin will be automatically available in all your queries.

## Viewing query plan

To view query plan or missing indexes, call static `QueryPlanVisualizer.DumpPlan(query)` method or call `DumpPlan` extension method on an `IQueryable` instance. You will also need to add `ExecutionPlanVisualizer` to the namespaces list (click F4 to open the dialog). If you want to dump query result as well, pass `true` as a second parameter.

Query execution plan for Sql Server:

![Sql Server query plan](screenshots/Query%20Plan.PNG "Query execution plan inside LINQPad")

Query execution plan for PostgreSQL:

![PostgreSQL query plan](screenshots/Postgres%20Query%20Plan.PNG "Query execution plan inside LINQPad")

## Viewing missing indexes

For SQL Server, the query plan can also return information about missing indexes in `QueryPlan/MissingIndexes/MissingIndexGroup` element. If missing indexes are present in the plan the visualizer will show a second tab with the missing index details and a button to create the index.

Missing index:

![missing indexes](screenshots/Missing%20Index.PNG "Missing index")
