import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CatalogTests(unittest.TestCase):
 def test_19inch_scope_and_ports(self):
  data=json.loads((ROOT/'catalog.json').read_text());sources={s['id']:s for s in json.loads((ROOT/'sources.json').read_text())}
  self.assertEqual(data['version'],1);ids=set()
  for model in data['devices']:
   self.assertNotIn(model['id'],ids);ids.add(model['id']);self.assertEqual(sources[model['id']]['rackWidthInches'],19)
   self.assertEqual(model['height'],1);self.assertTrue(400<=model['widthMm']<483)
   self.assertEqual(model['ports'],len(model['interfaces']));self.assertEqual(len({i['name'] for i in model['interfaces']}),model['ports'])
   self.assertTrue(all(i['ips']==[] for i in model['interfaces']))
 def test_image_integrity_and_orientation(self):
  sources=json.loads((ROOT/'sources.json').read_text())
  for source in sources:
   for face in ['front','rear']:
    asset=source['images'][face];path=ROOT/asset['path'];self.assertTrue(path.is_file());self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),asset['sha256'])
    self.assertTrue(path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'));self.assertTrue(asset['sourceUrl'].startswith('https://cdn.ecomm.ui.com/'))
