# DB Operations

## Set Membership test

- Experimental environment: Intel Xeon Platinum 8375C@2.90GHz with 192GB RAM
- Experimental setting (data structure parameter):

  - CF: $|T|=1.2n$
  - BF: false positive rate = 0.001

| **Set Size** | **Redis Set** | **Cuckoo filter** | **Bloom filter** |
|-|-|-|-|
| ${10}^6$ | 129.442µs | 10.879µs | 7.406µs |
| ${10}^7$ | 185.519µs |  |  |
| ${10}^8$ | 399.138µs |  |  |