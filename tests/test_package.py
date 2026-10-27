import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PackageTests(unittest.TestCase):
    def test_manifests_agree(self):
        root = json.loads((ROOT / 'plugin.json').read_text())
        compat = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(root['$schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        for key in ('name', 'version', 'description', 'author', 'keywords', 'license'):
            self.assertEqual(root[key], compat[key], key)
        self.assertEqual(root['extensions']['com.openai']['interface'], compat['interface'])
        self.assertRegex(root['version'], r'^\d+\.\d+\.\d+$')

    def test_skill_inventory_and_frontmatter(self):
        expected = {'uiux-master','ux-research','a11y-audit','human-ai-review','ai-ux-evaluation','deceptive-design-audit'}
        dirs = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
        self.assertEqual(dirs, expected)
        for name in sorted(dirs):
            text = (ROOT / 'skills' / name / 'SKILL.md').read_text()
            self.assertTrue(text.startswith('---\n'), name)
            header = text.split('---\n', 2)[1]
            self.assertRegex(header, rf'(?m)^name: {re.escape(name)}$')
            self.assertRegex(header, r'(?m)^description: .+')

    def test_local_markdown_references_exist(self):
        for f in (ROOT / 'skills').rglob('*.md'):
            text = f.read_text()
            for match in re.finditer(r'`(references/[^`]+\.md)`', text):
                self.assertTrue((f.parent / match.group(1)).is_file(), f'{f}: {match.group(1)}')

    def test_routing_contract(self):
        text = (ROOT / 'skills/uiux-master/SKILL.md').read_text()
        for required in ('deceptive-design-audit', 'human-ai-review', 'ai-ux-evaluation', 'ux-research', 'a11y-audit', 'fallback', 'read-only', 'do not install'):
            self.assertIn(required, text, required)

if __name__ == '__main__':
    unittest.main()
