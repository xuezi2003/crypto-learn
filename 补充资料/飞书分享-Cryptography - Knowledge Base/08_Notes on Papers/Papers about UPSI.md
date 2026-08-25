# Papers about UPSI

## [DRRT18, PETS] PIR-PSI: Scaling Private Contact Discovery

### Motivation

Private Contact Discovery (Server set size $N$ >> client set size $n$): Protect private information, improved efficiency (Use PIR to reduce PSI's size)

### Features

这篇文章并不是专门为了streaming做的，但是有一些性质让streaming更高效，一个是服务器做PIR之前会构造一个Cuckoo hash表，这个表是static的，要更新的话直接插入元素就行；做完PIR之后会做一个数据集大小为2n的PSI，对于client side的更新没有特别的处理。

### Idea

- 这篇文章貌似没有专门为了updatable做优化，可不可以把下面那篇MZRA21的incremental PIR用到这里，提升update的性能
- 实际上没有看懂这篇文章的构造，构造中对于PIR的描述是非常具体的，基本思想和MZRA21很像，都是allowing the original preprocessing to continue to be used after database changes, while incurring an update cost proportional to the number of changes rather than the size of the database

## [BMX22, PETS] Updatable Private Set Intersection

### Motivation

之前虽然有人做uspi，但是没有人做出一个形式化的定义，所以这篇文章做了新的upsi构造，并且给出了形式化的定义。

### Features

给出了三个类型的upsi形式化定义和构造，分别是one-sided/two-sided addition和weak deletion，addition已经讲过了，核心点就是把更新的数据分成两个部分，并且采用合适的方式去计算这两个部分。在deletion中，提到一种新的PSI，sender streaming psi（sender每个epoch都会输入新的数据然后计算），作者给出了一个引理，基于OT和correlation robust hash的PSI可以实现sender streaming PSI。第d天更新的时候，只会输出d-t到d天之间的交集，实现方式就是重新计算一遍，感觉也可以通过psi with addition实现（可以用于追踪秘接）。

## [DIO22, SCN] Streaming and Unbalanced PSI from Function Secret Sharing

### Motivation

提出了streaming unbalanced PSI weight cardinality (PSI-WCA)，适用于需要频繁对数据集进行小更新的场景

### Features

计算cardinality使用到了DPF，client生成DPF key，server计算DPF，然后把DPF的结果相加得到结果。如果server需要更新数据，对新的点计算DPF就可以了，如果client需要更新数据，新生成DPF key。

## [KLS+17, PoPETs] Private set intersection for unequal set sizes with mobile applications

### Motivation

现有的（17年以前）unbalanced PSI protocols效率不高，并且不平衡PSI用的地方很多，比如恶意软件检测， 泄露密码检测，contact discovery等等。

### Features

把已有PSI抽象成三个阶段，base phase，setup phase和online phase，base phase做一些与独立于数据的precomputation，setup phase对数据做预计算，online phase做查询，把传输的集合数据（加密之后的数据）变成bloom filter（插入加密之后的），然后server更新bloom filter就可以。根据BMX22。这样会泄露额外的交集信息，server对于bloom filter的更新项client是知道的，有些情况下server会直接把更新元素发送给client，会造成隐私泄露：

- 比如server的更新数据是X'，这会修改BF的几个对应位置，client可以仅用自己的更新数据Y'查询BF更新的位置，来获得 $X' \cap Y'$
- 如果server直接把X'传输给client的话，也会有这个问题

### Idea

浏览了这篇文章之后感觉这篇文章的思路比较好，BF很通用，对于RSA，OPRF，DH的PSI都可以用，不知道能不能通过某些方法改进BF更新，解决上面提到的隐私泄露问题。

## [ATD20, Preprint] Feather: Lightweight multi-party updatable delegated private set intersection

### Motivation

One limitation of existing delegated PSI protocols is that they are all designed for static data and do not allow efficient update on outsourced data. Another limitation is that they cannot efficiently support PSI among multiple clients, which is often needed in practice.

### Features

这篇文章更新的基本思路还是利用bloom filter更新，先把数据映射到hash表中，对于每个bin，建立一个BF；然后把元素编码到多项式的根上，加入随机多项式后，双方求出多项式的gcd，然后根据BF判断gcd的根是否在交集中。更新一个元素的时候，就只需要提取出一个bin及其对应的BF，做更新后再计算出新的用于多项式插值的点。

## [MZRA22, SECURITY] Incremental Offline/Online PIR、

### Motivation

在以前的PIR中，database是不可变的，这里提出了一个可以增加数据库大小的PIR

### Features

把协议的整个过程分为了online和offline阶段，offline阶段用于preprocessing生成hints，更新hints是很高效的，online阶段用于处理client的查询，这样的话更新数据只需要更新hints，复杂度和更新的数据量成比例。

May be suitable for PIR based PSI.


[[ACG+24](https://eprint.iacr.org/2024/1183)] Updatable Private Set Intersection from Structured Encryption

[[BMSTZ24](https://eprint.iacr.org/2024/1446)] Updatable Private Set Intersection Revisited: Extended Functionalities, Deletion, and Worst-Case Complexity

[[LTQ24](https://eprint.iacr.org/2024/1712)] Low-Communication Updatable PSI from Asymmetric PSI and PSU