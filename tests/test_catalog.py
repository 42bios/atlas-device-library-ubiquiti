import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CatalogTests(unittest.TestCase):
 def setUp(self):
  self.data=json.loads((ROOT/'catalog.json').read_text())
  self.models={m['id']:m for m in self.data['devices']}
  self.sources={s['id']:s for s in json.loads((ROOT/'sources.json').read_text())}
 def test_scope_and_interfaces(self):
  self.assertEqual(self.data['version'],1)
  self.assertEqual(len(self.models),74)
  self.assertEqual(len(self.models),len(self.data['devices']))
  self.assertEqual(set(self.models),set(self.sources))
  for key,m in self.models.items():
   self.assertEqual(self.sources[key]['rackWidthInches'],19)
   self.assertIn(m['height'],[1,2,3]);self.assertTrue(400<=m['widthMm']<=520)
   self.assertTrue(0<m['depthMm']<=1000)
   self.assertEqual(len({i['name'] for i in m['interfaces']}),len(m['interfaces']))
   self.assertTrue(all(i['ips']==[] for i in m['interfaces']))
   counted=[i for i in m['interfaces'] if i['type']==('Power outlet' if m['kind']=='PDU' else 'Ethernet') or (m['kind']!='PDU' and i['type']=='Fiber')]
   self.assertEqual(m['ports'],len(counted),key)
 def test_regression_specs(self):
  for key,ports in {'enas':3,'unvr':2,'ups-2u-us':3,'cloud-key-enterprise':3,'ecs-aggregation':54,'ef-core':19,'usw-enterprisexg-24':26,'us-16-xg':16,'usg-pro-4':4,'usp-pdu-pro':20}.items():
   self.assertEqual(self.models[key]['ports'],ports,key)
  ck=self.models['cloud-key-enterprise']
  self.assertEqual(ck['interfaces'][-1]['speedMbps'],1000)
  self.assertEqual(self.models['ef-core']['interfaces'][-1]['speedMbps'],1000)
  self.assertEqual((ck['widthMm'],ck['depthMm'],ck['heightMm']),(481.4,787,43.7))
  self.assertEqual(self.models['envr']['height'],3)
  self.assertNotIn('usp-pdu-hd',self.models)
  self.assertEqual(self.models['uxg-enterprise']['kind'],'Router')
 def test_viewports_are_valid(self):
  for m in self.models.values():
   for face in ['front','rear']:
    if face+'Image' not in m:continue
    f=m[face+'ImageFrame']
    self.assertTrue(f['width']>0 and f['height']>0)
    self.assertTrue(f['x']>=0 and f['y']>=0)
    self.assertTrue(f['x']+f['width']<=f['canvasWidth'])
    self.assertTrue(f['y']+f['height']<=f['canvasHeight'])
  self.assertFalse(self.models['us-16-xg']['frontImageFrame']['rackSuitable'])
  self.assertTrue(self.models['eav-fiber']['frontImageFrame']['rackSuitable'])
 def test_image_integrity(self):
  for key,s in self.sources.items():
   self.assertIn('front',s['images'])
   if key!='usg-pro-4':self.assertIn('rear',s['images'])
   for face,a in s['images'].items():
    p=ROOT/a['path'];content=p.read_bytes()
    self.assertEqual(hashlib.sha256(content).hexdigest(),a['sha256'])
    self.assertTrue(content.startswith(b'\x89PNG\r\n\x1a\n'))
    self.assertTrue(a['sourceUrl'].startswith(('https://cdn.ecomm.ui.com/','https://dl.ui.com/')))
    self.assertEqual(self.models[key][face+'Image'],a['path'])
