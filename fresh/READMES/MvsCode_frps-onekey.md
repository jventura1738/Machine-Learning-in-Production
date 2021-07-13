
Frps服务端一键配置脚本，Frp最新版本：0.37.0
===========

*Frp 是一个高性能的反向代理应用，可以帮助您轻松地进行内网穿透，对外网提供服务，支持 tcp, http, https 等协议类型，并且 web 服务支持根据域名进行路由转发。*

* 详情：fatedier (https://github.com/fatedier/frp)
* 此脚本原作者：clangcn (https://github.com/clangcn/onekey-install-shell)

## Frps-Onekey-Install-Shell For CentOS/Debian/Ubuntu/Fedora (32bit/64bit)

### Install（安装）

#### Aliyun
```Bash
wget https://code.aliyun.com/MvsCode/frps-onekey/raw/master/install-frps.sh -O ./install-frps.sh
chmod 700 ./install-frps.sh
./install-frps.sh install
```
#### Github
```Bash
wget https://raw.githubusercontent.com/MvsCode/frps-onekey/master/install-frps.sh -O ./install-frps.sh
chmod 700 ./install-frps.sh
./install-frps.sh install
```


### Uninstall（卸载）
```Bash
./install-frps.sh uninstall
```
### Update（更新）
```Bash
./install-frps.sh update
```
### Server management（服务管理器）
```Bash
Usage: /etc/init.d/frps {start|stop|restart|status|config|version}
```
Frps onkey-install-shell Changelog<br>Frp版本更新说明
---------------------------------------

 <!-- vim-markdown-toc GFM -->

* ## [v0.37.0 [2021/06/03]](#v0.37.0[2021/06/03])
    * ### NEW
     > frpc add subcommand verify to validate configures before running.
     
     > frpc support includes option to split multiple proxy configs into different files.
     
     > Support sudp in dashboard.

    * ### FIX
     > Use empty string as default value for dashboard user and password.
     
     > login_fail_exit is not valid when protocol = kcp.
     
* ## [v0.36.2 [2021/03/22]](#v0.36.2[2021/03/22])
    * ### IMPROVE
     > Support reverseproxy to dashboard with additional parts in path.

    * ### FIX
     > Fix logic error when parsing configs.

* ## [v0.36.1 [2021/03/19]](#v0.36.1[2021/03/19])
    * ### FIX
     > Fix bind_udp_port listen on error port.

* ## [v0.36.0 [2021/03/17]](#v0.36.0[2021/03/17])
    * ### NEW
     > New plugin https2https.

     > frpc supports tls_server_name to override the default value from server_addr.

    * ### IMPROVEMENT
     > Increase reconnect frequency if it occurs an network error between frpc and frps

* ## [v0.35.1 [2021/01/25]](#v0.35.1[2021/01/25])
    * ### FIX
     > Reduce binary file size.

* ## Shell Upadte [2021/01/24]
    * ### Amend
     > Aliyun download url replace by Gitee download url

* ## [v0.35.0 [2021/01/20]](#v0.35.0[2021/01/20])
    * ### NEW
     > Server Plugin supports HTTPS.

    * ### FIX
     > Fix IPv6 address parse problem.

     > HTTP type proxy can't handle websocket protocol due to error Connection header value.

* ## [v0.34.3 [2020/11/20]](#v0.34.2[2020/11/20])
    * ### NEW
     > Command line parameters support enable_prometheus.

* ## [v0.34.2 [2020/11/12]](#v0.34.2[2020/11/12])
    * ### FIX
     > Stream data transfer delay(e.g. chunked data) for HTTP type proxy.

* ## [v0.34.1 [2020/10/01]](#v0.34.1[2020/10/01])
    * ### NEW
     > Support NTLM protocol for http proxy to connect frps.

     > Official docker image support on DockerHub and Github registry.

    * ### FIX
     > Fix a dashboard stats data lost problem after client reconnect more than 7 days.

     > Fix TLS certificate verification failed.


* ## [v0.34.0 [2020/09/19]](#v0.34.0[2020/09/19])
    * ### NEW
     > Support TLS certificate and mutual TLS authentication.

     > Support set max UDP package size, default is 1500.

     > New e2e test framework.

    * ### FIX
     > UDP and SUDP proxy don't support compression and encrytion.

     > Call server plugins in fixed order.

* ## [v0.33.0 [2020/04/27]](#v0.33.0[2020/04/27])
    * ### NEW
     > Server plugin add NewUserConn interface.

     > New proxy type sudp to provide a safe way to expose udp service like stcp.

     > Support load balancing for tcpmux.

    * ### FIX
     > Fix invalid of AuthenticateNewWorkConns in frpc.
      
     > Fix a panic problem if accept many connections concurrently.

* ## [v0.32.1 [2020/04/03]](#v0.32.1[2020/04/03])
    * ### NEW
     > New operation Ping and NewWorkConn support in Server Plugin.

     > Add apiVersion and op params in Server Plugin HTTP request.

    * ### Improvement
     > Prevent frequently relogin when connection broken after login success soon.

    * ### Fix
     > Fix a memory leak problem caused by frequently relogin.

* ## Shell Upadte [2020/03/24]
    * ### Add
     > Add new download url-gitee，just support install package

* ## [v0.32.0 [2020/03/11]](#v0.32.0[2020/03/11])
    * ### New
     > Support tls_only = true in frps.ini to enforce frps only accept TLS connection.
     
     > Set detailed_errors_to_client = false in frps.ini to hide detailed error information to client.  
     
     > Support prometheus monitor.
     
     > Optional OIDC authentication.  
     
     > New proxy type tcpmux. Support TCP port multiplexing over HTTP Connect tunnel.
    * ### Fix
     > Bandwidth limit configure not compared correctly when reloading.
     
     > Incorrect connection count stats.

* ## [v0.31.2 [2020/02/05]](#v0.31.2[2020/02/05])
    * ### Fix
     > Fix not release port when client start proxy error.
     
* ## [v0.31.1 [2020/01/06]](#v0.31.1[2020/01/06])
    * ### Fix
     > Fix panic when proxy meta data is set.

* ## [v0.31.0 [2020/01/03]](#v0.31.0[2020/01/03])
    * ### New
     > New server manage plugin to extend frp's ability
    * ### Improvement
     > Improve xtcp's success rate in some special case.

* ## [v0.30.0 [2019/11/29]](#v0.30.0[2019/11/29])
    * ### New
     > Support bandwidth limit for each proxy.
     
     > New plugin https2http, explore https service as http protocol.

* ## [v0.29.1 [2019/11/03]](#v0.29.1[2019/11/03])
    * ### Fix
     > Fix bug when use_encryption is true for xtcp.

* ## [v0.29.0 [2019/08/30]](#v0.29.0[2019/08/30])
    * ### New
     > New disable_log_color configure to disable console log color.
     
     > Plugin https2http support attatch headers by plugin_header_ prefix.
    * ### Change
     > Provide a high-level Go API.
    * ### Fix
     > max_pool_count is invalid.
     
     > Judge error between IPv4 and IPv6 in proxy protocol

* ## [v0.28.2 [2019/08/10]](#v0.28.2[2019/08/10])
    * ### Fix
     > Fix a bug that health check worker may stop unexpected.

* ## [v0.28.1 [2019/08/08]](#v0.28.1[2019/08/08])
    * ### New
     > Update standard http ReverseProxy to handle more upgrade protocol
     
     > Update some vendor packages.

* ## [v0.28.0 [2019/08/03]](#v0.28.0[2019/08/03])
    * ### New
     > type http support load balancing.
    * ### Fix
     > Fix a connection leak problem when login_fail_exit is false.

* ## [v0.27.1 [2019/07/15]](#v0.27.1[2019/07/15])
    * ### Fix
     > Add read timeout for TLS connection check.

* ## [v0.27.0 [2019/04/25]](#v0.27.0[2019/04/25])
    * ### New
     > Proxy Protocol support plugin unix_domain_socket.
     
     > frps support custom 404 page.

* ## [v0.26.0 [2019/04/10]](#v0.26.0[2019/04/10])
    * ### New
     > Support Proxy Protocol.
     
     > New plugin https2http.
    * ### Fix
     > Fix router config conflict when frpc start by command line mode. #1165

* ## [v0.25.3 [2019/03/26]](#v0.25.3[2019/03/26])
    * ### Fix
     > Fix panic error when reconnection with tls_enable is true.

* ## [v0.25.2 [2019/03/25]](#v0.25.2[2019/03/25])
    * ### Change
     > Change Update version of kcp-go.
    * ### Fix
     > Fix connection leak of http health check. #1155

* ## [v0.25.1 [2019/03/15]](#v0.25.1[2019/03/15])
    * ### Fix
     >Fix a match problem with multilevel subdomain. #1132  
      frps --log_file is useless. #1125

* ## [v0.25.0 [2019/03/11]](#v0.25.0[2019/03/11])
    * ### New
     > Support TLS between frpc and frps, Set
 tls enable to enable this feature in frpC.Improve stability of xtcp.
    * ### Fix
     > Fix a bug that xtcp don't release connections in some case.
     
    ##### Note: xtcp is incompatible with old versions.
 
    ##### 注意:此版本的xtcp和之前版本不兼容,需要同步升级服务端和客户端才能正常使用
 
* ## [v0.24.1 [2019/02/12]](#v0.24.1[2019/02/12])
    * ### Fix
     > Fix Error clear frpc configure file when /api/config called without token set
     
* ## [v0.24.0 [2019/02/11]](#v0.24.0[2019/02/11])
    * ### New
     > New Support admin UI for frpc
     
* ## [v0.23.3 [2019/01/30]](#v0.23.3[2019/01/30])
    * ### Fix
     > Fix Reload proxy not saved after reconnecting
  
* ## [v0.23.2 [2019/01/26]](#v0.23.2[2019/01/26])  
    * ### Fix 
     > Fix client not working caused by reconnecting.

* ## [v0.23.1 [2019/01/16]](#v0.23.1[2019/01/16])  
    * ### Fix 
     >Fix status api.
     
     >Fix reload and status command error.

* ## [v0.23.0 [2019/01/15]](#v0.23.0[2019/01/15])
    * ### New
     >Support render configure file template with os environment.
    * ### Change
     >Remove check for authentication timeout.
