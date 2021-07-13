# Developers Guide to HIPAA Compliance
=================================

Version 1.0

## About

This guide is designed to provide developers with a solid understanding of HIPAA guidelines and their implications for application development. 

HIPAA was originally written in 1996, well in advance of the consumer Internet and a decade ahead of the first iPhone. Therefore, many of the rules and provisions deal with security and privacy issues from a world that didn't have a notion of apps, smartphones, and wearables. And while it's been amended to address privacy and security for the web, the complexity and wide-sweeping nature of the law makes teasing out the exact details to ensure compliance a bit cumbersome. 

Further, unlike PCI, there is no certification entity that can provide developers a rubber stamp of compliance approval. It's up to developers and companies alike to ensure compliance requirements are implemented properly. 

This guide will give you enough information to give you a strong understanding of HIPAA without getting bogged down in the legalese. We've tried to keep it straight forward, written in plain language.

[Read the Introduction](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md)

## Table of Contents
01 — [Introduction](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md)
+ [2013 Final Omnibus Rule Update](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#2013-final-omnibus-rule-update)
+ [Why this guide?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#why-this-guide)
+ [Who is this guide for?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#who-is-this-guide-for)
+ [Build on our work](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#build-on-our-work)
+ [Questions/Feedback](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#questionsfeedback)
+ [Mandatory Disclaimer](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/01%20Introduction.md#mandatory-disclaimer)

02 — [What is HIPAA?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md)
+ [Background](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#background)
+ [2013 Final Omnibus Rule Update](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#2013-final-omnibus-rule-update)
+ [The Four Rules of HIPAA](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#the-four-rules-of-hipaa)
+ [Important Terms to Know](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#important-terms-to-know)
  + [Protected Health Information](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#protected-health-information-phi)
  + [The Difference Between PHI and Consumer Health Information](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#the-difference-between-protected-health-information-and-consumer-health-information)
  + [Covered Entity](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#covered-entity)
  + [Business Associate](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#business-associate)
  + [No Safe Harbor Clause](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/02%20What%20is%20HIPAA%3F.md#no-safe-harbor-clause)

03 — [Do I Need to Be HIPAA Compliant?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/03%20Do%20I%20Need%20to%20Be%20HIPAA%20Compliant%3F.md)
+ [Who Needs to Be HIPAA Compliant?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/03%20Do%20I%20Need%20to%20Be%20HIPAA%20Compliant%3F.md#who-needs-to-be-hipaa-compliant)

04 — [HIPAA Security Rule](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md)
+ [3 Parts to the HIPAA Security Rule](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#3-parts-to-the-hipaa-security-rule)
  + [Administrative Safeguards](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#administrative-safeguards)
  + [Technical Safeguards](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#technical-safeguards)
    + [Access Control Safeguards](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#access-control-requirements)
    + [Transmission Security](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#transmission-security)
    + [Audit and Integrity](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#audit-and-integrity)
  + [Physical Safeguards](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#physical-safeguards)
    + [Facility Access Controls](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#facility-access-controls)
    + [Device and Media Controls](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#device-and-media-controls)
    + [Workstation Security](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#workstation-security)
+ [Required vs. Addressable Specifications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/04%20HIPAA%20Security%20Rule.md#required-vs-addressable-specifications)

05 — [Becoming HIPAA Compliant](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/05%20Becoming%20HIPAA%20Compliant.md)
+ [What Does HIPAA Require](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/05%20Becoming%20HIPAA%20Compliant.md#what-does-hipaa-require)
+ [What it Means for Developers](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/05%20Becoming%20HIPAA%20Compliant.md#what-it-means-for-developers)
+ [If We're Being Honest](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/05%20Becoming%20HIPAA%20Compliant.md#if-were-being-honest)

06 — [Who Certifies HIPAA Compliance](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/06%20Who%20Certifies%20HIPAA%20Compliance%3F.md)
+ [The Short Answer](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/06%20Who%20Certifies%20HIPAA%20Compliance%3F.md#the-short-answer-is-no-one)
+ [But Texas](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/06%20Who%20Certifies%20HIPAA%20Compliance%3F.md#but-texas)

07 — [HIPAA Fines](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/07%20HIPAA%20Fines.md)
+ [Unencrypted Data](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/07%20HIPAA%20Fines.md#unencrypted-data)
+ [Employee Error](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/07%20HIPAA%20Fines.md#employee-error)
+ [Data Stored on Devices](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/07%20HIPAA%20Fines.md#data-stored-on-devices)
+ [Business Associates](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/07%20HIPAA%20Fines.md#business-associates)

08 — [Developer Considerations](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md)
+ [Build vs. Buy](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#build-vs-buy)
+ [Unintended Use Cases](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#unintended-use-cases)
+ [HIPAA Hosting and Compliance](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#hipaa-hosting-and-compliance)
  + [Does Using HIPAA Hosting Make My Application HIPAA Compliant?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#does-using-hipaa-hosting-make-my-application-hipaa-compliant)
  + [What Data Should Be Stored in HIPAA Compliant Hosting Environments?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#what-data-should-be-stored-in-hipaa-compliant-hosting-environments)
  + [What Makes a Hosting Environment HIPAA Compliant?](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#what-makes-a-hosting-environment-hipaa-compliant)
  + [Network and Application Security](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#network-and-application-security)
  + [High-Availability and Redundancy](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#high-availability-and-redundancy)
  + [Required vs. Addressable HIPAA Implementation Specifications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/08%20Developer%20Considerations.md#required-vs-addressable-hipaa-implementation-specifications)

09 — [Mobile Applications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md)
+ [Use Cases](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#use-cases)
+ [PHI in the Application](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#phi-in-the-application)
+ [User Communication](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#user-communication)
  + [Email](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#email)
  + [Database/API Calls](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#databaseapi-calls)
+ [Push Notifications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#push-notifications)
+ [Physical Phone Security](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#physical-phone-security)
  + [Using the Lock Screen](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#using-the-lock-screen)
  + [Enabling Remote Wiping of Lost Phones](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/09%20Mobile%20Applications.md#enabling-remote-wiping-of-lost-phones)

10 — [Wearable Applications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md)
+ [Considerations for Wearables](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#considerations-for-wearables)
  + [Alerts and Notifications](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#alerts-and-notifications)
  + [Default Displays](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#default-displays)
  + [APIs and Data Sharing](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#apis-and-data-sharing)
  + [Medical Devices](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#medical-devices)
  + [Data Encryption](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#data-encryption)
  + [Data Synching](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/10%20Wearable%20Applications.md#data-synching)

11 — [Apple HealthKit and iOS 8](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/11%20Apple%20HealthKit%20and%20iOS%208.md)
+ [TrueVault iOS 8 SDK](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/11%20Apple%20HealthKit%20and%20iOS%208.md#truevault-ios-8-sdk)
+ [iOS 8 Health-Related Announcements](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/11%20Apple%20HealthKit%20and%20iOS%208.md#ios-8-health-related-announcements)
+ [Apple HealthKit Announcements](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/11%20Apple%20HealthKit%20and%20iOS%208.md#apple-healthkit-announcements)

12 — [About TrueVault](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md)
+ [Built for Developers Like You](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#built-for-developers-like-you)
+ [HIPAA Compliant](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#hipaa-compliant)
+ [BAA + Insurance](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#baa--insurance)
+ [Startups](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#startups)
+ [Mobile Apps](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#mobile-apps)
+ [Web Apps](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#web-apps)
+ [Wearable Health Tech Devices](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#wearable-health-tech-devices)
+ [Why People Like TrueVault](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#why-people-like-truevault)
+ [Try TrueVault for Free](https://github.com/truevault/hipaa-compliance-developers-guide/blob/master/12%20About%20TrueVault.md#try-truevault-for-free)

## About TrueVault

TrueVault is a HIPAA compliant API and secure data store that makes meeting the technical safeguard requirements of HIPAA easy for developers. Think of us like Stripe, but instead of payments, we make sure your app is checking all the boxes for HIPAA security and privacy. [Learn more](https://www.truevault.com/)

## Disclaimer

We're not lawyers. Nothing in this guide constitutes legal advice. Talk to one if you have specific questions regarding your application and HIPAA compliance.

