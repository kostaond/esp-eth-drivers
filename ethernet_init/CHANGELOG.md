# Changelog

## [1.3.0](https://github.com/kostaond/esp-eth-drivers/compare/ethernet_init@v1.2.0...ethernet_init@v1.3.0) (2025-12-04)


### Features

* Added api for deinitialization of ethernet. ([877af17](https://github.com/kostaond/esp-eth-drivers/commit/877af17cf870614da5f42a557e1c2671930b4bfa))
* Added support of SPI Ethernet PHY poll mode to ethernet_init component ([51966b5](https://github.com/kostaond/esp-eth-drivers/commit/51966b5b16b1615d05b033a9cc680d70ff19b42e))
* **ch390:** Added support for CH390H. It needs further tests. ([921c311](https://github.com/kostaond/esp-eth-drivers/commit/921c311e332d898e5786254c1fe989c41583085e))
* **common_examples:** Add common examples aplicable for all phys ([aa2f96e](https://github.com/kostaond/esp-eth-drivers/commit/aa2f96eb3cae704f672380bc97dbf0735a38cb03))
* **enc28j60:** moved ENC28J60 driver from ESP-IDF ([5219908](https://github.com/kostaond/esp-eth-drivers/commit/521990810d24c301fb7556ec491e23832b15a78b))
* **eth_drivers:** migrated SPI ETH modules and PHY drivers ([952f637](https://github.com/kostaond/esp-eth-drivers/commit/952f63745074569d5b27e4d44263c9055cb6fb64))
* **eth_init:** added configuration option for EMAC Rx Task size ([4484f21](https://github.com/kostaond/esp-eth-drivers/commit/4484f21303711d1f7d0291d99463cb2fa88bc6f4))
* **eth_init:** added Generic 802.3 PHY as supported device ([ce809a3](https://github.com/kostaond/esp-eth-drivers/commit/ce809a36dbb3cd5b27bc7c7b35b3b6ace7aa6673))
* **ethernet_init:** Added 10BASE-T1S configuration and board specific config ([7c589f8](https://github.com/kostaond/esp-eth-drivers/commit/7c589f8dcf5a9852922927a410c55a0f295c9ad7))
* **ethernet_init:** added dependency to use migrated drivers ([952f637](https://github.com/kostaond/esp-eth-drivers/commit/952f63745074569d5b27e4d44263c9055cb6fb64))
* **ethernet_init:** added ETHERNET_INIT_OVERRIDE_DISABLE, ETHERNET_INIT_DEFAULT_ETH_DISABLED ([10ebd4c](https://github.com/kostaond/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** added OPENETH, extended skdconfig default behavior ([10ebd4c](https://github.com/kostaond/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** added support of Ethernet for P4 ([5813d0d](https://github.com/kostaond/esp-eth-drivers/commit/5813d0d0e2fce49e77f2bcc5e3bf0cde1ab89fbe))
* **ethernet_init:** added support of LAN865x ([7c4c19f](https://github.com/kostaond/esp-eth-drivers/commit/7c4c19fe6a942afd2db56a44c064ad1a9ef4d8a2))
* **ethernet_init:** added test text to test ([32f1fed](https://github.com/kostaond/esp-eth-drivers/commit/32f1fedccb86c833c5228c39c8039188e62c708c))
* **ethernet_init:** extended EMAC kconfig by detailed RMII GPIO configuration ([d314dd0](https://github.com/kostaond/esp-eth-drivers/commit/d314dd059dc5ac12f2e30b44919ff06d2aec3c65))
* **ethernet_init:** made Dependencies conditional ([10ebd4c](https://github.com/kostaond/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** streamlined conditional dependencies evaluation ([6645db3](https://github.com/kostaond/esp-eth-drivers/commit/6645db345e638b50858e5672663f85e6e088c492))
* **ethernet-init:** added option to select different SPI ETH modules at a time ([7c4c19f](https://github.com/kostaond/esp-eth-drivers/commit/7c4c19fe6a942afd2db56a44c064ad1a9ef4d8a2))
* Initialize Ethernet driver based on Espressif IDF Configuration ([51d7900](https://github.com/kostaond/esp-eth-drivers/commit/51d79003afb52f25fbfd08d26fdc590c759a5b32))


### Bug Fixes

* **ch390:** length filter is not enabled ([6315a47](https://github.com/kostaond/esp-eth-drivers/commit/6315a47918c1f8cc566fdffb94dce15eaa151dae))
* **ch390:** start/stop issue ([6315a47](https://github.com/kostaond/esp-eth-drivers/commit/6315a47918c1f8cc566fdffb94dce15eaa151dae))
* **ethernet_init:** fixed build when no Ethernet selected ([da6ad85](https://github.com/kostaond/esp-eth-drivers/commit/da6ad850b6901995aa0c4c2cd685f058cc26928e))
* **ethernet_init:** fixed ethernet_deinit_all and add return ([10ebd4c](https://github.com/kostaond/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** fixed lan865x build issues on older IDFs ([8334c3e](https://github.com/kostaond/esp-eth-drivers/commit/8334c3e9cc87618ddc49d0f6c00ef20f7e945ce9))
* **ethernet_init:** temporalily remove lan867x from ethernet_init ([2ca2628](https://github.com/kostaond/esp-eth-drivers/commit/2ca2628a54ec1d4c8c79d0f6e74a1e61f9fdb1e8))
* fixed formatting in all components ([9f0f356](https://github.com/kostaond/esp-eth-drivers/commit/9f0f356a4b1402c6c19787619288e0f84310464a))
* **ksz8863:** fixed previous corrupted component upload ([972933c](https://github.com/kostaond/esp-eth-drivers/commit/972933c0c907415fef26d3a1e5cda321b62834f7))

## [1.2.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v1.1.0...ethernet_init@v1.2.0) (2025-11-11)


### Features

* **ethernet_init:** streamlined conditional dependencies evaluation ([6645db3](https://github.com/espressif/esp-eth-drivers/commit/6645db345e638b50858e5672663f85e6e088c492))


### Bug Fixes

* **ethernet_init:** fixed build when no Ethernet selected ([da6ad85](https://github.com/espressif/esp-eth-drivers/commit/da6ad850b6901995aa0c4c2cd685f058cc26928e))

## [1.1.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v1.0.0...ethernet_init@v1.1.0) (2025-10-17)


### Features

* **ethernet_init:** added ETHERNET_INIT_OVERRIDE_DISABLE, ETHERNET_INIT_DEFAULT_ETH_DISABLED ([10ebd4c](https://github.com/espressif/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** added OPENETH, extended skdconfig default behavior ([10ebd4c](https://github.com/espressif/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))
* **ethernet_init:** made Dependencies conditional ([10ebd4c](https://github.com/espressif/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))


### Bug Fixes

* **ethernet_init:** fixed ethernet_deinit_all and add return ([10ebd4c](https://github.com/espressif/esp-eth-drivers/commit/10ebd4c08d7a9a448576a1e2cd113101eec3a7b8))

## [1.0.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v0.7.0...ethernet_init@v1.0.0) (2025-09-24)


### Features

* **eth_drivers:** migrated SPI ETH modules and PHY drivers ([952f637](https://github.com/espressif/esp-eth-drivers/commit/952f63745074569d5b27e4d44263c9055cb6fb64))
* **ethernet_init:** added dependency to use migrated drivers ([952f637](https://github.com/espressif/esp-eth-drivers/commit/952f63745074569d5b27e4d44263c9055cb6fb64))

## [0.7.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v0.6.1...ethernet_init@v0.7.0) (2025-09-16)


### Features

* **ethernet_init:** extended EMAC kconfig by detailed RMII GPIO configuration ([d314dd0](https://github.com/espressif/esp-eth-drivers/commit/d314dd059dc5ac12f2e30b44919ff06d2aec3c65))

## [0.6.1](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v0.6.0...ethernet_init@v0.6.1) (2025-08-06)


### Bug Fixes

* **ethernet_init:** fixed lan865x build issues on older IDFs ([8334c3e](https://github.com/espressif/esp-eth-drivers/commit/8334c3e9cc87618ddc49d0f6c00ef20f7e945ce9))

## [0.6.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v0.5.0...ethernet_init@v0.6.0) (2025-07-18)


### Features

* **ethernet_init:** added support of LAN865x ([7c4c19f](https://github.com/espressif/esp-eth-drivers/commit/7c4c19fe6a942afd2db56a44c064ad1a9ef4d8a2))
* **ethernet-init:** added option to select different SPI ETH modules at a time ([7c4c19f](https://github.com/espressif/esp-eth-drivers/commit/7c4c19fe6a942afd2db56a44c064ad1a9ef4d8a2))

## [0.5.0](https://github.com/espressif/esp-eth-drivers/compare/ethernet_init@v0.4.0...ethernet_init@v0.5.0) (2025-05-06)


### Features

* **ethernet_init:** Added 10BASE-T1S configuration and board specific config ([7c589f8](https://github.com/espressif/esp-eth-drivers/commit/7c589f8dcf5a9852922927a410c55a0f295c9ad7))


### Bug Fixes

* fixed formatting in all components ([9f0f356](https://github.com/espressif/esp-eth-drivers/commit/9f0f356a4b1402c6c19787619288e0f84310464a))
