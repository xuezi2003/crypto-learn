## Index

3DES, see triple-DES

AES (Advanced Encryption Standard)

    competition, 238

    cryptanalysis, 240

    design, 238–240

Assumptions, reliance on, 18–20, 64

Asymmetric encryption, see public-key encryption

Asymptotic security, 45–51

Authenticated encryption, see private-key encryption, 493

    generic constructions, 154

Authenticated encryption scheme

    CCM, 162

    ChaCha20-Poly1305, 162

    GCM, 161

Authentication, message, see message authentication

Avalanche effect, 222–224, 226, 231

Birthday attack, 178–181, 369, 377, 501

    small-space, 179–181, 369, 377

Birthday problem, 94, 119, 130, 178–181, 184, 192, 235, 253, 369, 377, 457, 580–582

Bleichenbacher's attack, 448

Block cipher, see pseudorandom permutation, see strong pseudorandom permutation, 88

    AES, see AES

    as strong pseudorandom permutation, 217–218

    block length and security, 95, 235

    constructing stream cipher from, 87

    cryptanalysis, 224–228, 231–234, 236–237, 240–246

    DES, see DES

    design principles, 217–224, 226–227

    meet-in-the-middle attack on, 236, 237

    modes of operation, 89–98, 107

    security against quantum algorithms, 500

    taxonomy of attacks, 218–219

Blum integer, 564

Caesar's cipher, 6

CBC mode, see modes of operation

CBC-MAC, 120–128

CCM (Counter with CBC-MAC), 162

Certificate, 485–491

    expiration, 490

    revocation, 490

Certificate authority, 486

ChaCha20, 162, 216–217

ChaCha20-Poly1305, 162

Challenge ciphertext, 29, 54

Chebyshev's inequality, 578

Chernoff bound, 580

Chinese remainder theorem, 317, 317–321, 329, 335, 366–368, 374, 440, 455, 548, 560, 562

Chosen-ciphertext attack, see private-key encryption, CCA-security, see public-key encryption, CCA-security, 18, 146–149, 149–151, 413–414, 424, 442, 447–448, 450, 566

    on block cipher, 219

Chosen-plaintext attack, see private-key encryption, CPA-security, see public-key encryption, CPA-security, 18, 72–75, 187, 240, 406

    on block cipher, 218, 246

Cipher-block chaining, see CBC-MAC, see modes of operation, CBC mode

Ciphertext-only attack, see private-key encryption, EAV-security, 17, 27, 52

Collision-resistant hash function

    birthday attack on, 178–181

    construction, 357–359, 363

    Davies–Meyer construction, 246–249

    definition of collision resistance, 169

    design principles, 246–249

    fingerprinting using, 195

    Keccak, 250–253

    MD5, 249

    Merkle trees based on, 196–197

    Merkle–Damgård transform, 170–172

    message authentication using, 172–177

    random oracle as, 191

    security against quantum algorithms, 501

    SHA family, 249–250

    SHA-1, 249–250

    SHA-2, 250

    SHA-3, 250–253

    signature scheme based on, 513–522

    syntax, 168

Commitment scheme, 200–202

Compression function, 168, 170, 175

    Davies–Meyer construction, 246–249

Computational Diffie–Hellman assumption, 340, 393, 432

    KEM based on, 434

Computational indistinguishability, 296–298, 341, 420

Computational security, 43–51

Computing discrete logarithms, algorithms for, 372–380

    baby-step/giant-step, 373, 375–377

    index calculus, 378–380

    number field sieve, 374

    Pohlig–Hellman, 341, 373–375

    Pollard's rho, 373, 377

    quantum algorithm, 503

    Shanks' algorithm, 373

Concrete security, 44–45, 69, 84, 95, 179, 217, 235, 266, 365, 380

Confusion-diffusion paradigm, 219

Coppersmith's theorem, 439

Counter mode, see modes of operation, CTR mode, see CTR mode

CPA-security, see chosen-plaintext attack

Cryptographic hash function, see random oracle, see collision-resistant hash function

    application to password hashing, 198–199

    collision resistance, 169

    commitment scheme from, 200–202

    Fiat–Shamir transform using, 477

    key derivation using, 199–200

    preimage resistance, 170, 182

    second-preimage resistance, 170, 198

    security notions, 170

CTR mode, see modes of operation, 92–95

Data Encryption Standard, see DES

Data integrity, see message authentication

Data-encapsulation mechanism (DEM), see KEM/DEM paradigm, 417

Davies–Meyer construction, 246–249

Decisional Diffie–Hellman assumption, 341, 342, 394, 431

    KEM based on, 430

    key exchange based on, 394

    public-key encryption based on, 428

Definitions, importance of, 15–16

DES (Data Encryption Standard)

    cryptanalysis, 231–234, 240–246

    design, 228–231

    mangler function, 229

    security, 234–235

    triple-DES, see triple-DES

DHIES, 434

Difference-universal function, 128–132, 137–138

Differential cryptanalysis, 240–245

Diffie–Hellman key exchange, 389–396, 426

    insecurity against man-in-the-middle attacks, 395

Digital Signature Standard (DSS), see DSA, see ECDSA

Discrete-logarithm assumption, 339, 341, 393, 594

    collision resistance from, 359

    signatures from, 475–485

Discrete-logarithm problem, see computing discrete logarithms, algorithms for, 340

    elliptic-curve groups and, 374, 380

    one-way permutation from, 266

    preference for prime-order groups, 341, 343, 357, 373, 602

Division with remainder, 307

Domain extension

    collision-resistant hash function, 170, 196

    message authentication code, 116

    private-key encryption, 75

    public-key encryption, 408

    signature scheme, 467–468

Double encryption, 236

DSA, 483–485

EAV-security, 55, 52–55, 65–69, 419

ECB mode, see modes of operation

ECDSA, 483–485

ECIES, 436

(Twisted) Edwards representation, 350

El Gamal encryption, 426–430, 538

Elliptic curves, 345–354, 380

    affine vs. projective coordinates, 352

    Curve25519, 354

    ECDSA signature scheme, 483

    ECIES encryption scheme, 435

    (Twisted) Edwards representation, 350

    Montgomery representation, 350

    P-256, 354

    point compression, 352

    secp256k1, 354

    Weierstrass representation, 346

Encryption, see private-key encryption, see public-key encryption, see private-key encryption

    definitions of security for, 16–18

Euclidean algorithm, 308, 321, 457, 590–591, 592

    extended, 591

Euler phi function, 316

Existential unforgeability, 467, 510

Existential unforgeability under adaptive chosen-message attack, 110

Exponentiation, group, 313–315

    algorithm for, 593–595

Extractor, strong, 431

Factoring, algorithms for, 366–372

    general number field sieve, 366, 374

    Pollard's p −1, 367–368

    Pollard's rho, 368–369

    quadratic sieve, 369–372

    quantum algorithm, 503

    trial division, 322, 366

Factoring, hardness of, 322, 331

    one-way function from, 265, 356

    one-way permutation from, 561

    relation between RSA and, 334–336, 556, 565

    trapdoor permutation from, 561

Family, one-way function, 265

Family, one-way permutation, 265, 356

Feistel network, 226–229, 289, 448

    cryptanalysis, 227–228, 231–234

    round function in, 226

Fiat–Shamir transform, 477–480

Forward secrecy, 493

Frequency analysis, 9, 10, 12, 33

Full domain hash (FDH), 470–475

Gap-CDH assumption, 434

GCM (Galois/counter mode), 161

GMAC, 132

Goldreich–Levin theorem, 269

Goldwasser–Micali encryption, 553–556

Group, 311

    $\mathbb{Z}_{N^2}^*$, 530

    $\mathbb{Z}_N$, 312, 315, 591, 598

    $\mathbb{Z}_N^*$, 315, 591, 598

    cyclic, 336

    elliptic-curve, 345–354

Grover's algorithm, 500–502

Hard-core predicate, 266–277

    definition, 267

    for Rabin, 565

    for RSA, 443

    from one-way function, 274

    Goldreich–Levin, 269

    used for pseudorandom number generation, 277–279, 284

    used for public-key encryption, 444–447, 527–529, 565

Hash function, see collision-resistant hash function, see cryptographic hash function, see random oracle

Hash-and-sign, 467–468

Historical ciphers, 6–14

    Caesar's cipher, 6

    shift cipher, 7, 10, 26

    substitution cipher, 8

    Vigenère cipher, 11, 30

HMAC, 174–177

Homomorphic encryption, 537–538, 543, 568

Hybrid argument, 282, 284, 285, 287, 288, 298, 411

Hybrid encryption, 415–425

Ideal-cipher model, 247, 250

Identification scheme, 476–482

    Schnorr, 480–482

Index of coincidence, 13

Indistinguishability of encryptions, 53–55, 57, 58, 405

    perfect, 29

Indistinguishability, computational, see computational indistinguishability

Information-theoretic encryption, see perfect secrecy

Information-theoretic message authentication, 133–139

Integrity (of data), see message authentication

Isomorphism, group, 317, 319, 339, 373, 530

Jacobi symbol, 546–552

    computation of, 552

Kasiski's method, 12

Keccak, see SHA-3, 250

KEM/DEM paradigm, 415–425, 435

Kerckhoffs' principle, 5

Key derivation, 199–200, 395, 431, 492

Key distribution center (KDC), 386–389

    Kerberos, 388

    Needham–Schroeder protocol, 388

Key lengths, recommended, 380

Key-encapsulation mechanism (KEM), see KEM/DEM paradigm, 415–425

    CCA-security, 424–425

    CDH-based, 431–434

    CPA-security, 419–424

    DDH-based, 430–431

    RSA-based, 445–447, 451–455

Key-exchange protocol, 87, see Diffie–Hellman key exchange, 389–396

    definition of security for, 391

    Diffie–Hellman, 389

    forward secrecy, 493

    TLS, 491–493

Known-plaintext attack, 17, 72, 187

    on block cipher, 218, 232, 246

Lamport signature scheme, 510–513

Learning with Errors (LWE) assumption, 504–509

Legendre symbol, 546

Linear cryptanalysis, 245

Linear-feedback shift register (LFSR), 208–211

Logarithm, discrete, see discrete-logarithm problem

Malleability, see non-malleability, 150, 414, 434, 447

Manger's attack, 450

Markov's inequality, 578

MD5, 249

Meet-in-the-middle attack, 236, 237

Merkle tree, 196–197, 515

Merkle–Damgård transform, 170–172, 195, 246

Message authentication, see message authentication code, 105–106

    combined with encryption, 151–162

    information-theoretic, 133–139

    unsuitability of encryption for, 96

    vs. digital signature, 464

    vs. private-key encryption, 106–108

Message authentication code

    canonical verification, 109, 112, 113

    CBC-MAC, 120–128

    definition of security for, 110, 112, 134

    fixed-length vs. arbitrary-length messages, 116–120, 122

    GMAC, 132

    HMAC, 174–177

    Poly1305, 132

    replay attack, 111–112, 162–164

    strong security for, 112

    syntax, 109

    timing attack on, 113

Message integrity, see message authentication

Miller–Rabin algorithm, 324, 325–331

Modern cryptography, principles of, 14–20

Modes of operation, see private-key encryption

    Block-cipher based, 89–98

    CBC mode, 89–91, 95, 107, 121, 146–148

    CTR mode, 92–95, 95, 107, 235

    ECB mode, 89, 107

    OFB mode, 92, 95, 107

    Stream-cipher based, 87

Montgomery multiplication, 595

Montgomery representation, 350

Negligible probability, 46, 48–49

Non-malleability, 150, 414

Non-repudiation, 397

Nonce-based private-key encryption

    syntax, 97

OAEP, 447–451

OFB mode, see modes of operation

One-time MAC, see message authentication, information-theoretic

One-time pad, 31–33, 65, 67, 107

One-time signature, 510–513

    construction of, 510

    definition of security for, 510

One-way function, 262–266, 305, 354–356

    candidates, 265

    definition, 263

    family, 265

    necessary for cryptography, 296

    signature scheme based on, 510, 522

    sufficient for private-key cryptography, 293

One-way permutation, 264, 356–357

    based on discrete-logarithm assumption, 266

    based on factoring, 563

    family, 265, 356

    pseudorandom generator from, 268

Padding-oracle attack, 146–149, 413, 447

Paillier encryption, 532–539

Perfect indistinguishability, 29

Perfect secrecy

    comparison to computational security, 43, 53, 64

    definitions of, 27–30

    impossibility for public-key encryption, 406

    limitations of, 33, 43

    one-time pad, 31

    Shannon's theorem, 34

    Vernam's cipher, 31

PGP, 488, 489

$\phi(N)$, see Euler phi function

PKCS #1 v1.5, 442, 447

PKCS #1 v2.0, 448

PKCS #1 v2.1, 470–475

Pohlig–Hellman algorithm, see computing discrete logarithms, algorithms for

Pollard's p−1, see factoring, algorithms for

Pollard's rho, see computing discrete logarithms, algorithms for, see factoring, algorithms for

Poly1305, 132

Polynomial-time computation, 46, 47, 50

Primes

    distribution of, 323

    generation of, 324, 322–325

    strong, 325, 368, 602

    testing of, see Miller–Rabin algorithm

Private-key cryptography

    setting, 2

Private-key encryption

    arbitrary-length messages, see modes of operation, 56, 75

    authenticated encryption, 151–162

    CCA-security, 145–151

    combined with message authentication, 151–162

    CPA-security, 72–75, 80–84

    definition of security for, 55, 59, 70, 74, 98, 149, 151, 153

    EAV-security, 55

    from one-way function, 293

    hiding message length in, 55

    indistinguishability in the presence of an eavesdropper, 419

    limitations of, 385–386

    modes of operation, 84–98

    multiple-message security, 70–72, 74–75, 150

    semantic security, 53, 56–60

    setting, 2, 402

    stateful, 91

    stateless vs. stateful, 52

    syntax, 4, 24, 52

    threat models, 17

    vs. message authentication, 96, 106–108

    vs. public-key encryption, 402

Probabilistic algorithms, 47–48

Probabilistic encryption, 71, 406

Proofs by reduction, 57, 64–65, 69

Proofs, importance of, 20

Pseudorandom function, 76–79, 79, 269, 284–289, 521

    construction from pseudorandom generator, 285

    construction in the random-oracle model, 192

    CPA-secure encryption from, 80

    definition, 77

    message authentication from, 114–116

    proofs of security based on, 81

    pseudorandom generator from, 78

Pseudorandom generator, see stream cipher, 60–64, 277–284, 297

    construction from one-way permutation, 268, 278

    definition, 62

    EAV-secure encryption from, 66

    from one-way permutation, 284

    from pseudorandom function, 78

    increasing expansion factor, 268, 279

    random oracle as, 191

    variable-output-length, 85

Pseudorandom permutation, see block cipher, 79–80, 269

    block cipher as, 217–218

    construction from pseudorandom function, 289

    definition, 80

    vs. strong pseudorandom permutation, 80

Public keys, secure distribution of, 403, 485

Public-key encryption

    arbitrary-length messages and, 408

    CCA-security, 412–415, 434, 451

    CPA-security, 405–447

    deterministic encryption and, 406

    DHIES, 434–436

    El Gamal, 426–430, 538, 543

    from trapdoor permutations, 527

    Goldwasser–Micali, 553–556

    homomorphic, 537, 543

    hybrid encryption, see hybrid encryption

    in the random-oracle model, 448

    LWE-based, 503–509

    multiple message security, 407

    OAEP, 447–451

    padded RSA, 440–442

    Paillier, 532–539

    PKCS #1 v1.5, 442

    PKCS #1 v2.0, 448

    plain RSA, 436–440, 565

    post-quantum, 503–509

    Rabin, 564–566

    setting, 396, 401, 402

    signcryption, 493–495

    syntax, 404

    threshold, 543

    vs. private-key encryption, 402

Public-key infrastructure (PKI), 485–491

Quadratic residue

    modulo a composite, 370, 548–552

    modulo a prime, 346, 545–548

Quadratic residuosity assumption, 552–553

Quantum computing, 499

Rabin encryption, 564–566

Rainbow table, 183, 198

Random function, 189

Random oracle

    as collision-resistant hash function, 191

    as pseudorandom generator, 191

    extractability, 190, 455

    programmability of, 191, 455, 472

    used to construct a KEM, 431

    used to construct pseudorandom function, 192

    used to construct public-key encryption, 448

    used to construct signature scheme, 471, 477

Random-number generation, 23–24

Random-oracle model, see random oracle, 217, 247, 250

    overview, 187–195

Random-permutation model, 217, 247, 250

RC4, 213–216

    cryptanalysis, 215

Replay attack, 111–112, 162–164, 466

Rijndael, see AES

RSA assumption, 331–336, 357

    collision resistance from, 363

    public-key encryption from, 436–457

    relation between factoring and, 334–336, 556, 565

    signatures from, 468–475

S-box, 220, 222–224, 229

Secret-key encryption, see private-key encryption

Secret-sharing scheme, 539–543

    Shamir's, 540

    verifiable, 541

Security parameter, 45–47, 52, 54

Semantic security, 56–60

SHA family, 249–250

SHA-3, 250

    competition, 250

Shanks' algorithm, see computing discrete logarithms, algorithms for

Shannon's theorem, 34–36

Shift cipher, 7, 26

Shor's algorithm, 502–503

Signature scheme

    based on hash function, 509

    based on one-way function, 509

    certificate, see certificate

    chain-based, 513

    definition of security for, 467, 510

    DSA, 483–485

    ECDSA, 483–485

    EdDSA, 483

    Lamport, 510–513

    one-time signature, 510–513

    overview of, 463

    PKCS #1 v2.1, 470–475

    plain RSA, 468

    properties of, 464

    RSA-FDH, 470–475

    Schnorr, 475–483

    signcryption, 493–495

    stateful, 513

    strong security for, 495

    syntax, 466

    tree-based, 516–522

    vs. message authentication, 464

Signcryption, 493–495

Sponge construction, 250

Square root

    modulo a composite, 334, 370, 560–563

    modulo a prime, 328, 556–560

SSL, see (LS)1

Stream cipher, see pseudorandom generator, 85–87, 284

    ChaCha20, 216–217

    from block cipher, 87

    linear-feedback shift register, 208–211

    modes of operation, 87–107

    RC4, 213–216

    Trivium, 212–213

Strong primes, see primes

Strong pseudorandom permutation, see block cipher, 79–80

    construction from pseudorandom function, 292

    definition, 80

    vs. pseudorandom permutation, 80

Strongly secure message authentication code, 112, 129, 157, 436, 495

Strongly secure signature scheme, 495

Strongly universal function, 134–136

Substitution cipher, 8

Substitution-permutation network, 219–226, 239

    cryptanalysis, 224–226

Sufficient key-space principle, 8

Symmetric-key encryption, see private-key encryption

Threshold encryption, 543

Time/space tradeoff, 181–187, 234

Timing attack, 113, 157

TLS, 146, 157, 491–493

Trapdoor permutation, 525–527, 561–564

    based on factoring, 564

    based on RSA assumption, 526

    public-key encryption from, 527

Triple encryption, 237

Triple-DES, 228, 237, 238

Trivium, 212–213

Unforgeable encryption

    definition of, 151

Union bound, 576

Verifiable secret sharing (VSS), 541

Vernam's cipher, see one-time pad

Vigenère cipher, 11, 30

Voting, electronic, 538, 543

Weierstrass representation, 346

$\mathbb{Z}_N$, 312, 315, 591, 598

$\mathbb{Z}_N^*$, 315–321, 331, 591, 598

$\mathbb{Z}_{N^2}^*$, 530–532
