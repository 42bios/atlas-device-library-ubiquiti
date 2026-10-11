# Atlas Ubiquiti 19-inch device library

Curated Ubiquiti hardware definitions and front/rear manufacturer pictures for Atlas homelab inventory. **Only full-width 19-inch rack-mounted devices.** This is a device model library, not a connector plugin or a complete listing of the Ubiquiti store.

## Initial models

| Model | Rack space | Network interfaces |
| --- | --- | --- |
| UDM-Pro-Max | 1U | 8 × 1 GbE RJ45, 1 × 2.5 GbE RJ45, 2 × 10G SFP+ |
| USW-Pro-Max-24-PoE | 1U | 16 × 1 GbE RJ45, 8 × 2.5 GbE RJ45, 2 × 10G SFP+ |
| USW-Aggregation | 1U | 8 × 10G SFP+ |

Dimensions describe the chassis without rack ears; 19-inch refers to the supported rack mounting standard, not a 482.6 mm chassis width. Width, depth and height are explicitly separate because manufacturer listings use different dimension orders. Interface speeds are hardware capabilities, not monitoring measurements. PoE/DC/AC connectors are visible in pictures but are not counted as network ports. Shelf-mounted desktop devices, APs, Cloud Keys and small switches requiring an extra rack adapter are excluded from this initial scope.

## Add to Atlas

Open **Device catalogs → Add repository** and enter:

`https://github.com/42bios/atlas-device-library-ubiquiti`

Atlas reads `catalog.json`, imports the models and loads images from this repository. Choose a model when adding a device, then enter its instance name, hostname, placement and IPs. Existing inventory is not changed by library updates; manually created devices are not automatically replaced.

## Files and provenance

- `catalog.json`: Atlas version 1 catalog.
- `images/<model>/front.png` and `rear.png`: reviewed corresponding views.
- `sources.json`: official source URLs, verification date and image checksums.
- `tests/`: catalog consistency, 19-inch scope, image-file integrity and interface validation.

Specification sources: [Dream Machine Pro Max](https://techspecs.ui.com/unifi/cloud-gateways/udm-pro-max), [Pro Max 24 PoE](https://techspecs.ui.com/unifi/switching/usw-pro-max-24-poe), [Aggregation](https://techspecs.ui.com/unifi/switching/usw-aggregation).

## Contributing

Add one stable model ID and both correctly oriented views. Verify 19-inch mounting, rack height, chassis dimensions and port layout from official technical specifications; record the source and date. Do not use an angled product image as a straight rack elevation. Maintain empty instance IP lists. Do not invent dimensions, port speeds, rear views or cable types. Run `python -m unittest discover -s tests` before submitting changes. Add models incrementally; the initial three entries do not claim full coverage.

## Image and brand attribution

Manufacturer photographs, device designs and trademarks belong to Ubiquiti Inc. This library is independent and is not endorsed by Ubiquiti. Source assets are listed individually in `sources.json`; no open-source license or redistribution permission is claimed for manufacturer imagery. No blanket MIT license is applied to these third-party assets.
