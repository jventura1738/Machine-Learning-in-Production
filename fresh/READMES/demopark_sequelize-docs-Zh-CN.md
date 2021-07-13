# Sequelize Docs 中文版

![](http://docs.sequelizejs.com/manual/asset/logo-small.png)

[![npm version](https://badgen.net/npm/v/sequelize)](https://www.npmjs.com/package/sequelize)
[![Build Status](https://github.com/sequelize/sequelize/workflows/CI/badge.svg)](https://github.com/sequelize/sequelize/actions?query=workflow%3ACI)
[![npm downloads](https://badgen.net/npm/dm/sequelize)](https://www.npmjs.com/package/sequelize)
<!-- [![codecov](https://badgen.net/codecov/c/github/sequelize/sequelize?icon=codecov)](https://codecov.io/gh/sequelize/sequelize) -->
[![Last commit](https://badgen.net/github/last-commit/sequelize/sequelize)](https://github.com/sequelize/sequelize)
[![Merged PRs](https://badgen.net/github/merged-prs/sequelize/sequelize)](https://github.com/sequelize/sequelize)
[![GitHub stars](https://badgen.net/github/stars/sequelize/sequelize)](https://github.com/sequelize/sequelize)
[![Slack Status](http://sequelize-slack.herokuapp.com/badge.svg)](http://sequelize-slack.herokuapp.com/)
[![node](https://badgen.net/npm/node/sequelize)](https://www.npmjs.com/package/sequelize)
[![License](https://badgen.net/github/license/sequelize/sequelize)](https://github.com/sequelize/sequelize/blob/main/LICENSE)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

> 此项目同步自 [sequelize](https://github.com/sequelize) / [sequelize](https://github.com/sequelize/sequelize) 项目中的  docs. 除特殊情况, 将保持每月一次的同步频率.
> 
> 更新日志请参阅: [CHANGELOG](CHANGELOG.md)

Sequelize 是一个基于 promise 的 [Node.js](https://nodejs.org/) [ORM 工具](https://en.wikipedia.org/wiki/Object-relational_mapping), 目前支持 [Postgres](https://en.wikipedia.org/wiki/PostgreSQL), [MySQL](https://en.wikipedia.org/wiki/MySQL), [MariaDB](https://en.wikipedia.org/wiki/MariaDB), [SQLite](https://en.wikipedia.org/wiki/SQLite) 以及 [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server). 它具有强大的事务支持, 关联关系, 预读和延迟加载,读取复制等功能.

Sequelize 遵从 [语义版本控制](http://semver.org). 支持 Node v10 及更高版本以便使用 ES6 功能.

你目前正在查看 Sequelize 的**教程和指南**.你可能还对[API 参考](http://docs.sequelizejs.com/identifiers) (英文)感兴趣.

# 数据库引擎支持

## v6
|  引擎 |  支持的最低版本 |
| :------------: | :------------: |
|  Postgre | [9.5 ](https://www.postgresql.org/docs/9.5/ ) |
|  MySQL |  [5.7](https://dev.mysql.com/doc/refman/5.7/en/) |
|  MariaDB |  [10.1](https://mariadb.com/kb/en/changes-improvements-in-mariadb-101/) |
|  Microsoft SQL |  `12.0.2000` |
|  SQLite |  [3.0](https://www.sqlite.org/version3.html) 

## 版本

### [v6 中文文档](https://github.com/demopark/sequelize-docs-Zh-CN/tree/master)(现行版本)

### [v5 中文文档](https://github.com/demopark/sequelize-docs-Zh-CN/tree/v5)(计划停止)

### [v4 中文文档](https://github.com/demopark/sequelize-docs-Zh-CN/tree/v4)(停止更新)


## 文档(v6)

### 核心概念

- [Getting Started - 入门](core-concepts/getting-started.md)
- [Model Basics - 模型基础](core-concepts/model-basics.md)
- [Model Instances - 模型实例](core-concepts/model-instances.md)
- [Model Querying - Basics - 模型查询(基础)](core-concepts/model-querying-basics.md)
- [Model Querying - Finders - 模型查询(查找器)](core-concepts/model-querying-finders.md)
- [Getters, Setters & Virtuals - 获取器, 设置器 & 虚拟字段](core-concepts/getters-setters-virtuals.md)
- [Validations & Constraints - 验证 & 约束](core-concepts/validations-and-constraints.md)
- [Raw Queries - 原始查询](core-concepts/raw-queries.md)
- [Associations - 关联](core-concepts/assocs.md)
- [Paranoid - 偏执表](core-concepts/paranoid.md)

### 高级关联概念

- [Eager Loading - 预先加载](advanced-association-concepts/eager-loading.md)
- [Creating with Associations - 创建关联](advanced-association-concepts/creating-with-associations.md)
- [Advanced M:N Associations - 高级 M:N 关联](advanced-association-concepts/advanced-many-to-many.md)
- [Association Scopes - 关联作用域](advanced-association-concepts/association-scopes.md)
- [Polymorphic Associations - 多态关联](advanced-association-concepts/polymorphic-associations.md)

### 其它主题

- [Dialect-Specific Things - 方言特定事项](other-topics/dialect-specific-things.md)
- [Transactions - 事务](other-topics/transactions.md)
- [Hooks - 钩子](other-topics/hooks.md)
- [Query Interface - 查询接口](other-topics/query-interface.md)
- [Naming Strategies - 命名策略](other-topics/naming-strategies.md)
- [Scopes - 作用域](other-topics/scopes.md)
- [Sub Queries - 子查询](other-topics/sub-queries.md)
- [Other Data Types - 其他数据类型](other-topics/other-data-types.md)
- [Constraints & Circularities - 约束 & 循环](other-topics/constraints-and-circularities.md)
- [Extending Data Types - 扩展数据类型](other-topics/extending-data-types.md)
- [Indexes - 索引](other-topics/indexes.md)
- [Optimistic Locking - 乐观锁定](other-topics/optimistic-locking.md)
- [Read Replication - 读取复制](other-topics/read-replication.md)
- [Connection Pool - 连接池](other-topics/connection-pool.md)
- [Working with Legacy Tables - 使用遗留表](other-topics/legacy.md)
- [Migrations - 迁移](other-topics/migrations.md)
- [TypeScript](other-topics/typescript.md)
- [Resources - 资源](other-topics/resources.md)
- [Upgrade to v6 - 升级到 V6](other-topics/upgrade-to-v6.md)

## 简单示例

```js
const { Sequelize, Model, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

class User extends Model {}
User.init({
  username: DataTypes.STRING,
  birthday: DataTypes.DATE
}, { sequelize, modelName: 'user' });

(async () => {
  await sequelize.sync();
  const jane = await User.create({
    username: 'janedoe',
    birthday: new Date(1980, 6, 20)
  });
  console.log(jane.toJSON());
})();
```

请通过 [Getting started - 入门](core-concepts/getting-started.md) 来学习更多相关内容. 如果你想要学习 Sequelize API 请通过 [API 参考](http://docs.sequelizejs.com/identifiers) (英文).

# 赞赏支持
![赞赏支持](https://raw.githubusercontent.com/demopark/electron-api-demos-Zh_CN/master/assets/img/td.png)
