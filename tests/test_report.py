from pathlib import Path
import unittest
import importlib.util
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build', ROOT / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
class ReportTests(unittest.TestCase):
    def test_all_twelve_practicals_exist(self):
        self.assertEqual([p.name for p in sorted((ROOT/'practicals').glob('P*.md'))], [f'P{i:02}.md' for i in range(1,13)])
    def test_evidence_links_resolve(self):
        import re
        for doc in (ROOT/'practicals').glob('P*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',doc.read_text()):
                self.assertTrue((doc.parent/target).is_file(), target)
    def test_report_is_safe_html_and_contains_all_sections(self):
        html=build.render()
        self.assertEqual(html.count('<section>'),12)
        self.assertIn('&lt;commit-sha&gt;',html)
        self.assertNotIn('<commit-sha>',html)
if __name__ == '__main__': unittest.main()
