# NettyRpc
An RPC framework based on Netty, ZooKeeper and Spring  
中文详情：[Chinese Details](http://www.cnblogs.com/luxiaoxun/p/5272384.html)
### Features:
* Simple code and framework
* Service registry/discovery support by ZooKeeper
* High availability, load balance and failover
* Support different load balance strategy
* Support asynchronous/synchronous call
* Support different versions of service
* Support different serializer/deserializer
* Dead TCP connection detecting with heartbeat
### Design:
![design](https://github.com/luxiaoxun/NettyRpc/blob/master/picture/NettyRpc-design.png)
### How to use (netty-rpc-test)
1. Define an interface:
    ```  
    public interface HelloService { 
        String hello(String name); 
        String hello(Person person);
    }
    ```  
2. Implement the interface with annotation @NettyRpcService:
    ```  
    @NettyRpcService(HelloService.class, version = "1.0")
    public class HelloServiceImpl implements HelloService {
        public HelloServiceImpl(){}
	
        @Override
        public String hello(String name) {
            return "Hello " + name;
        }

        @Override
        public String hello(Person person) {
            return "Hello " + person.getFirstName() + " " + person.getLastName();
        }
    }
    ```  
3. Run zookeeper

   For example: zookeeper is running on 127.0.0.1:2181

4. Start server:
   1. Start server with spring config: RpcServerBootstrap
   2. Start server without spring config: RpcServerBootstrap2

5. Call the service:
    1. Use the client:
    ```  
   	final RpcClient rpcClient = new RpcClient("127.0.0.1:2181");
   		
   	// Sync call
   	HelloService helloService = rpcClient.createService(HelloService.class, "1.0");
   	String result = helloService.hello("World");
   		
   	// Async call
   	RpcService client = rpcClient.createAsyncService(HelloService.class, "2.0");
   	RPCFuture helloFuture = client.call("hello", "World");
   	String result = (String) helloFuture.get(3000, TimeUnit.MILLISECONDS);
	``` 
    2. Use annotation @RpcAutowired:
    ``` 
    public class Baz implements Foo {
        @RpcAutowired(version = "1.0")
        private HelloService helloService1;
           
        @RpcAutowired(version = "2.0")
        private HelloService helloService2;
           
        @Override
        public String say(String s) {
            return helloService1.hello(s);
        }
    }
    ``` 