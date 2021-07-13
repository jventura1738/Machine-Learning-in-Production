# CargoBay

> **Note**: This project is no longer being maintained.

[`StoreKit`](http://developer.apple.com/library/ios/#documentation/StoreKit/Reference/StoreKit_Collection/) is the Apple framework for [making In-App Purchases](https://developer.apple.com/library/IOS/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html). It's pretty good, but it has a few rough edges.

`CargoBay` smooths out those rough parts by providing:

- One step receipt & transaction verification, done securely [according to Apple's guidelines](https://developer.apple.com/library/IOS/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW12)
- Block-based interface for requesting product information
- Ability to request product information for identifiers asynchronously from a remote web service
- Block-based callbacks for payment queue observation delegate methods
- Automatic check for transaction uniqueness

## Usage

### Product Requests

```objective-c
NSArray *identifiers = @[
  @"com.example.myapp.apple",
  @"com.example.myapp.pear",
  @"com.example.myapp.banana"
];

[[CargoBay sharedManager] productsWithIdentifiers:[NSSet setWithArray:identifiers]
success:^(NSArray *products, NSArray *invalidIdentifiers) {
  NSLog(@"Products: %@", products);
  NSLog(@"Invalid Identifiers: %@", invalidIdentifiers);
} failure:^(NSError *error) {
  NSLog(@"Error: %@", error);
}];
```

### Payment Queue Observation

**AppDelegate.m**

```objective-c
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)options {
  [[CargoBay sharedManager] setPaymentQueueUpdatedTransactionsBlock:^(SKPaymentQueue *queue, NSArray *transactions) {
    NSLog(@"Updated Transactions: %@", transactions);
  }];

  [[SKPaymentQueue defaultQueue] addTransactionObserver:[CargoBay sharedManager]];

  // ...
}
```

### Verifying Receipts

```objective-c
[[CargoBay sharedManager] verifyTransaction:transaction password:nil success:^(NSDictionary *receipt) {
  NSLog(@"Receipt: %@", receipt);
} failure:^(NSError *error) {
    NSLog(@"Error %d (%@)", [error code], [error localizedDescription]);
}];
```

## License

CargoBay is available under the MIT license. See the LICENSE file for more info.
