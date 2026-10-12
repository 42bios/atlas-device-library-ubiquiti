# Atlas Ubiquiti 19-inch device library

**74 native full-width 19-inch Ubiquiti rack models**, with hardware specifications, interfaces and original manufacturer pictures for Atlas homelab inventory. This is a device catalog, independent of the UniFi connector.

## Add to Atlas

Open **Device catalogs → Add repository** and enter:

`https://github.com/42bios/atlas-device-library-ubiquiti`

Select a model when adding equipment, then set its instance name, hostname, placement and IP addresses. Model specifications belong to the catalog; addresses and cable connections belong to your inventory. Updating this catalog does not replace hardware specifications or rack placements on existing device instances.

## Coverage

Verified on **2026-10-12** against 498 manufacturer index entries across cloud gateways, switching, physical security, integrations, accessories and door access, supplemented by official legacy quick-start guides. Includes rack switches, gateways, NAS, video recorders, CloudKey Enterprise, the legacy application server, storage expansion and rack power hardware. See `coverage.json` for scope and exclusions. This does not claim exhaustive coverage of every historical or regional Ubiquiti product.

Desktop equipment requiring a rack adapter, rack cabinets, shelves and mounting kits are excluded. The vertical 0U USP-PDU-HD is outside this full-width 19-inch scope.

## Hardware details

- Rack space and dimensions use manufacturer specifications. Chassis width is not always 482.6 mm; older measurements may include ears. The CloudKey Enterprise dimension order is explicitly mapped to width, depth and height.
- Interface speeds describe maximum hardware capabilities. They are not negotiated speed or monitoring data. Management ports are included; console sockets are excluded.
- USG-Pro-4 has four logical network interfaces. Its WAN RJ45 and SFP sockets share interfaces, so they must not be treated as six independent ports.
- USP-PDU-Pro is marked **US / 125V**. Its 20 outputs are 16 AC outlets and four USB-C outputs; management network ports are listed separately.
- UPS variants are marked **US / 120V**. Surge in/out Ethernet sockets are pass-through protection, not independent switch ports.
- USP-RPS uses proprietary redundant DC outputs; it is not an AC PDU. UACC-ESE-16 is storage expansion, not a standalone network NAS.

## Models

| Manufacturer model | Type | Rack space | Port count* |
| --- | --- | --- | --- |
| [CK-Enterprise](https://techspecs.ui.com/unifi/accessories/cloud-key-enterprise) | Server | 1U | 3 |
| [EAV-Fiber](https://techspecs.ui.com/unifi/switching/eav-fiber) | Switch | 1U | 23 |
| [EAV-XG-24-PoE](https://techspecs.ui.com/unifi/switching/eav-xg-24-poe) | Switch | 1U | 29 |
| [ECS-24-PoE](https://techspecs.ui.com/unifi/switching/ecs-24-poe) | Switch | 1U | 26 |
| [ECS-24S](https://techspecs.ui.com/unifi/switching/ecs-24s) | Switch | 1U | 31 |
| [ECS-24S-PoE](https://techspecs.ui.com/unifi/switching/ecs-24s-poe) | Switch | 1U | 31 |
| [ECS-48-PoE](https://techspecs.ui.com/unifi/switching/ecs-48-poe) | Switch | 1U | 52 |
| [ECS-48S](https://techspecs.ui.com/unifi/switching/ecs-48s) | Switch | 1U | 55 |
| [ECS-48S-PoE](https://techspecs.ui.com/unifi/switching/ecs-48s-poe) | Switch | 1U | 55 |
| [ECS-Aggregation](https://techspecs.ui.com/unifi/switching/ecs-aggregation) | Switch | 1U | 54 |
| [ECS-Core](https://techspecs.ui.com/unifi/switching/ecs-core) | Switch | 1U | 33 |
| [EF-Core](https://techspecs.ui.com/unifi/cloud-gateways/ef-core) | Router | 1U | 19 |
| [EFG](https://techspecs.ui.com/unifi/cloud-gateways/efg) | Router | 1U | 6 |
| [ENAS](https://techspecs.ui.com/unifi/integrations/enas) | NAS | 3U | 3 |
| [ENVR](https://techspecs.ui.com/unifi/physical-security/envr) | NAS | 3U | 3 |
| [ENVR-Core](https://techspecs.ui.com/unifi/physical-security/envr-core) | NAS | 3U | 3 |
| [UACC-ESE-16](https://techspecs.ui.com/unifi/accessories/uacc-ese-16) | Other | 3U | 0 |
| [UCI](https://techspecs.ui.com/unifi/accessories/uci) | Other | 1U | 1 |
| [UDM-Beast](https://techspecs.ui.com/unifi/cloud-gateways/udm-beast) | Router | 1U | 14 |
| [UDM-Pro](https://techspecs.ui.com/unifi/cloud-gateways/udm-pro) | Router | 1U | 11 |
| [UDM-Pro-Max](https://techspecs.ui.com/unifi/cloud-gateways/udm-pro-max) | Router | 1U | 11 |
| [UDM-SE](https://techspecs.ui.com/unifi/cloud-gateways/udm-se) | Router | 1U | 11 |
| [UNAS-Pro](https://techspecs.ui.com/unifi/integrations/unas-pro) | NAS | 2U | 2 |
| [UNAS-Pro-4](https://techspecs.ui.com/unifi/integrations/unas-pro-4) | NAS | 1U | 3 |
| [UNAS-Pro-8](https://techspecs.ui.com/unifi/integrations/unas-pro-8) | NAS | 2U | 3 |
| [UNVR](https://techspecs.ui.com/unifi/physical-security/unvr) | NAS | 1U | 2 |
| [UNVR-G2](https://techspecs.ui.com/unifi/physical-security/unvr-g2) | NAS | 1U | 2 |
| [UNVR-G2-Pro](https://techspecs.ui.com/unifi/physical-security/unvr-g2-pro) | NAS | 2U | 2 |
| [UNVR-Pro](https://techspecs.ui.com/unifi/physical-security/unvr-pro) | NAS | 2U | 2 |
| [UPS-2U-Pro-US](https://techspecs.ui.com/unifi/integrations/ups-2u-pro-us) | UPS | 2U | 3 |
| [UPS-2U-US](https://techspecs.ui.com/unifi/integrations/ups-2u-us) | UPS | 2U | 3 |
| [US-24](https://techspecs.ui.com/unifi/switching/us-24) | Switch | 1U | 26 |
| [US-24-250W](https://techspecs.ui.com/unifi/switching/us-24-250w) | Switch | 1U | 26 |
| [US-24-500W](https://techspecs.ui.com/unifi/switching/us-24-500w) | Switch | 1U | 26 |
| [US-48](https://techspecs.ui.com/unifi/switching/us-48) | Switch | 1U | 52 |
| [US-48-500W](https://techspecs.ui.com/unifi/switching/us-48-500w) | Switch | 1U | 52 |
| [US-48-750W](https://techspecs.ui.com/unifi/switching/us-48-750w) | Switch | 1U | 52 |
| [USP-PDU-Pro](https://techspecs.ui.com/unifi/integrations/usp-pdu-pro) | PDU | 2U | 20 |
| [USP-RPS](https://techspecs.ui.com/unifi/integrations/usp-rps) | Other | 1U | 1 |
| [USW-16-POE](https://techspecs.ui.com/unifi/switching/usw-16-poe) | Switch | 1U | 18 |
| [USW-24](https://techspecs.ui.com/unifi/switching/usw-24) | Switch | 1U | 26 |
| [USW-24-POE](https://techspecs.ui.com/unifi/switching/usw-24-poe) | Switch | 1U | 26 |
| [USW-48](https://techspecs.ui.com/unifi/switching/usw-48) | Switch | 1U | 52 |
| [USW-48-POE](https://techspecs.ui.com/unifi/switching/usw-48-poe) | Switch | 1U | 52 |
| [USW-Aggregation](https://techspecs.ui.com/unifi/switching/usw-aggregation) | Switch | 1U | 8 |
| [USW-Enterprise-24-PoE](https://techspecs.ui.com/unifi/switching/usw-enterprise-24-poe) | Switch | 1U | 26 |
| [USW-Enterprise-48-PoE](https://techspecs.ui.com/unifi/switching/usw-enterprise-48-poe) | Switch | 1U | 52 |
| [USW-EnterpriseXG-24](https://techspecs.ui.com/unifi/switching/usw-enterprisexg-24?s=us) | Switch | 1U | 26 |
| [USW-Mission-Critical](https://techspecs.ui.com/unifi/switching/usw-mission-critical) | Switch | 1U | 9 |
| [USW-Pro-24](https://techspecs.ui.com/unifi/switching/usw-pro-24) | Switch | 1U | 26 |
| [USW-Pro-24-POE](https://techspecs.ui.com/unifi/switching/usw-pro-24-poe) | Switch | 1U | 26 |
| [USW-Pro-48](https://techspecs.ui.com/unifi/switching/usw-pro-48) | Switch | 1U | 52 |
| [USW-Pro-48-POE](https://techspecs.ui.com/unifi/switching/usw-pro-48-poe) | Switch | 1U | 52 |
| [USW-Pro-Aggregation](https://techspecs.ui.com/unifi/switching/usw-pro-aggregation) | Switch | 1U | 32 |
| [USW-Pro-HD-24](https://techspecs.ui.com/unifi/switching/usw-pro-hd-24) | Switch | 1U | 28 |
| [USW-Pro-HD-24-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-hd-24-poe) | Switch | 1U | 28 |
| [USW-Pro-Max-24](https://techspecs.ui.com/unifi/switching/usw-pro-max-24) | Switch | 1U | 26 |
| [USW-Pro-Max-24-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-max-24-poe) | Switch | 1U | 26 |
| [USW-Pro-Max-48](https://techspecs.ui.com/unifi/switching/usw-pro-max-48) | Switch | 1U | 52 |
| [USW-Pro-Max-48-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-max-48-poe) | Switch | 1U | 52 |
| [USW-Pro-XG-10-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-xg-10-poe) | Switch | 1U | 12 |
| [USW-Pro-XG-24](https://techspecs.ui.com/unifi/switching/usw-pro-xg-24) | Switch | 1U | 26 |
| [USW-Pro-XG-24-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-xg-24-poe) | Switch | 1U | 26 |
| [USW-Pro-XG-48](https://techspecs.ui.com/unifi/switching/usw-pro-xg-48) | Switch | 1U | 52 |
| [USW-Pro-XG-48-PoE](https://techspecs.ui.com/unifi/switching/usw-pro-xg-48-poe) | Switch | 1U | 52 |
| [USW-Pro-XG-Aggregation](https://techspecs.ui.com/unifi/switching/usw-pro-xg-aggregation) | Switch | 1U | 32 |
| [USW-WAN](https://techspecs.ui.com/unifi/switching/usw-wan) | Switch | 1U | 4 |
| [USW-WAN-RJ45](https://techspecs.ui.com/unifi/switching/usw-wan-rj45) | Switch | 1U | 4 |
| [UXG-Enterprise](https://techspecs.ui.com/unifi/accessories/uxg-enterprise) | Router | 1U | 6 |
| [UXG-Pro](https://techspecs.ui.com/unifi/cloud-gateways/uxg-pro) | Router | 1U | 4 |
| [US-16-150W](https://dl.ui.com/qsg/US-16-150W/US-16-150W_EN.html) | Switch | 1U | 18 |
| [US-16-XG](https://dl.ui.com/qsg/US-16-XG/US-16-XG_EN.html) | Switch | 1U | 16 |
| [USG-PRO-4](https://dl.ui.com/qsg/USG-PRO-4/USG-PRO-4_EN.html) | Router | 1U | 4 |
| [UAS-XG](https://dl.ui.com/qsg/UAS-XG/UAS-XG_EN.html) | Server | 1U | 2 |

*Network interfaces except the PDU, where the count denotes power outputs. Consult each model's interface list and notes for management, shared-media and pass-through details.

## Pictures and provenance

`images/<model>/front.png` and `rear.png` are original, unmodified manufacturer assets. Gallery orientations were reviewed individually; `image-roles.json` records exceptions to the usual gallery ordering. Original transparent margins and reflections remain in the files. Per-face `ImageFrame` metadata gives Atlas the visible bounds for proportional display. Annotated legacy QSG figures are marked `rackSuitable: false`; Atlas uses its schematic face in rack elevations for these models. Legacy quick-start-guide figures can contain annotations. USG-Pro-4 currently has a front image only; its rear view is deliberately unavailable rather than fabricated.

`sources.json` records official specification URLs, verification dates, image source URLs and SHA-256 checksums. `catalog.json` follows Atlas catalog version 1. No credentials or instance IP addresses are included.

## Contributing and validation

Add stable IDs, verified native 19-inch mounting, dimensions, rack space and explicit interfaces. Record official sources and image checksums. Prefer orthogonal front and rear views; never invent missing dimensions, speeds or images. Keep instance IP lists empty. Run:

```sh
python -m unittest discover -s tests
```

The tests check scope, interface counts, known dimension/port regressions and asset integrity. The catalog is also validated with Atlas's actual import parser before publication.

## Image and brand attribution

Manufacturer photographs, device designs and trademarks belong to Ubiquiti Inc. This library is independent and is not endorsed by Ubiquiti. Source assets are listed individually in `sources.json`; no open-source license or redistribution permission is claimed for manufacturer imagery. No blanket MIT license is applied to these third-party assets.
