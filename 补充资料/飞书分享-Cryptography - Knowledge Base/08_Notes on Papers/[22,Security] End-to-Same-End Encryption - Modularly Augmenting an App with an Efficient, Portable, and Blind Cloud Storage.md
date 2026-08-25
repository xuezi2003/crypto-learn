# [22,Security] End-to-Same-End Encryption:Modularly Augmenting an App with an Efficient, Portable, and Blind Cloud Storage


[2022-End-to-Same-End Encryption.pptx](<./assets/2022-End-to-Same-End Encryption.pptx>)
<!-- 飞书原始链接: https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZWRiNzExYmI0MzBlMWE2MmI2ZTdhMjY5NmM0NzYxYWJfY2VjNmIxNDUyNjkxYTEwMjc4YWVhNTBiYjFmNDRkZmVfSUQ6NzQzNzc0NDg4MDY0ODEyNjQ5Ml8xNzg1NDYxOTY1OjE3ODU0NjU1NjVfVjM -->

Abstract

The cloud has become pervasive, and we ask: how can we protect cloud data against the cloud itself? For messaging Apps, facilitating user-to-user private communication via a cloud server, security has been formulated and solved efficiently via End-to-End encryption, building on existing channels between end users via servers (i.e., exploiting TLS, and encryption, without the need to program new primitives).


However, the analogous problem for Apps employing servers for storing and retrieving end-user data privately, solving the analogous “privacy from the server itself” (cloud-blind storage) where (1) based on existing infrastructure and (2) allowing user mobility, is, in fact, still open. Existing proposals, like password protected secret sharing (PPSS), target end-to-sameend encryption of storage, but need new protocols, whereas most popular commercial cloud storage services are not programmable. Namely they lack the simplicity needed for being portable over any cloud storage service. Here, we propose a novel system for storing private data in the cloud with the help of a key server (necessary given the requirements).


 In our system, the user data will be secure from any of: the cloud server, the key server, or any illegitimate users, while the authenticated user can access the data on any devices just via a correct passphrase. The most attractive feature of our system is that it does not require the cloud storage server to support any newly programmable operations, except the existing client login and the data storing. Moreover, our system is simply built on top of the existing App login, and the user only needs one passphrase to login the App and access his secure storage. The security of our protocol, in turn, is proved under our rigorous models, and the efficiency is further demonstrated by real-world network experiments over Amazon S3. We remark that a preliminary variant, based on our principles, was deployed by Snapchat in their My Eyes Only module, serving hundreds of millions of users!