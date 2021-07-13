# Datav
The open-source platform for data monitoring and observability. 

Datav is forked from **@grafana**, but changed a lot, e.g :
- remove angular dependency, using pure react
- much better alerting features
- multi spoken languages supported
- large screen supported
- different team and acl design,no orgs any more 
- 100% free. Forever and always

## Key Features 
- **Plugins** Performance,Extensible,Beautiful,Configurable
- **Dynamic Dashboards** Create dynamic & reusable dashboards with template variables
- **Interactive Panel** You can set click events for panels, like: go to a page, set variable etc
- **Beautifult Large Screen** Customize your own big data large screen,it's very very cool
- **Alerting** Visually define alert rules for your most important metrics
- **Variables**  Global and Dashboard scope, global vars can help you achieve personalized features such as multiple environments etc
- **Teams and ACL** Besides global dashboards, you can create teams, manage and share dashboards in your team
- **Custom sidemenu**  Link dashboards to sidemenu items, build your own sidemenu and websites.

## How to start(developing mode)
### Start datav main server
```bash
> git clone https://github.com/datav-io/datav
> cd datav
> go build
> ./datav generate ##only needed for first time or new plugins been added
> ./datav &
```

### start datav docs server
```bash
> cd docs
> yarn
> yarn dev
```
Access http://localhost:3000/docs-cn/installation to see the results

### Start datav ui server
```bash
> cd ui
> nvm use    
> yarn install
> yarn start
```

Open http://localhost:3001, then login with admin/admin

## Visitors Count

<img align="left" src = "https://profile-counter.glitch.me/datav/count.svg" alt ="Loading">


## Screenshots
![screenshot1](ui/public/img/screenshot1.jpg)
![screenshot2](ui/public/img/screenshot2.jpg)
![screenshot3](ui/public/img/screenshot3.jpg)

## Design Philosophy
Contrary to Grafana's big and all, DataV's design goal is small and beautiful.We support 90% of common usage scenarios.In these scenarios, DataV can ensure that it is simple enough and easy to use. Plug-in development will also be very simple. 

1. The special needs of users are left to themselves to do, **don't try to cover all scenarios**
> e.g Simplify datasources, only provide some most frequently-used metrics/logs/traces store, others willl be supported via standard http ways

2. Users from grafana MUST NOT pay too much on migration 
> Query api,import json format, panel plugins, variables these should be compatible with grafana

3. Keep our codes and core features clean and simple
> Code maintaing and re-developing shouldn't  be a nightmare.

4. The needs of the bosses must be taken into account
> Our bosses usually have different sights, so datav will take their needs too, e.g big screen dashboard, data report, **data association** etc

