#!/usr/bin/env python3
"""Export confirmed external behavior verbatim; run outside acceptance workflow."""
import hashlib, json, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
ASSETS = ROOT / "tests/delivery-acceptance"
files = sorted(p for p in (ROOT / "specs/packages").glob("*.md") if p.name not in {"git.md", "licensing.md"})
items, sources = [], []
for path in files:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    section = re.search(r"^## 外部行为\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    assert section, path
    external = section.group(1)
    headers = list(re.finditer(r"^### ([a-z][a-z0-9-]*-\d+)\s*$", external, re.M))
    for index, header in enumerate(headers):
        end = headers[index + 1].start() if index + 1 < len(headers) else len(external)
        body = external[header.end():end].strip()
        assert body
        item_id = header.group(1)
        items.append({"id": item_id, "text": body, "package": path.stem,
                      "source": str(path.relative_to(ROOT)), "anchor": item_id,
                      "source_line": text[:section.start(1) + header.start()].count("\n") + 1,
                      "related_requirement_ids": sorted(set(re.findall(r"\]\([^)]*#([a-z][a-z0-9-]*-\d+)\)", body)))})
    sources.append({"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(raw).hexdigest(),
                    "external_behavior_count": len(headers)})
assert len({i["id"] for i in items}) == len(items)
revision = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
digest = hashlib.sha256(json.dumps(sources, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
context_paths = ["specs/map.md", "specs/decisions/001-candidate-business-requirements.md"]
context_sources = [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in context_paths]
snapshot = {"source": "specs/packages/*.md::外部行为 (excluding git.md and licensing.md)",
            "version": f"confirmed-external-behavior-2026-10-08; candidate-v0.1; git:{revision}; source-set-sha256:{digest}",
            "confirmation": {"status": "confirmed_for_black_box_scenario_design", "date": "2026-10-08", "authority": "human user in this Codex task", "statement": "我确认当前业务需求包中的‘外部行为’作为本次场景设计的需求基线。"},
            "scope": {"stage": "black-box", "excluded_packages": ["git.md", "licensing.md"], "excluded_sections": ["意图", "验证"],
                      "constraints": ["经营参数保持待定，不擅自补充具体值", "不沿用 K.P 滑板项目经营政策", "仅生成和审查场景；不实现、不执行应用测试、不生成白盒、不宣称网站验收通过", "未来配置与数据仅在确认后用于执行，合成夹具不是经营决策", "电助力车、定制装配、经销商能力为待定扩展，不作为首版要求"]},
            "baseline_context": {"sources": context_sources, "decision_record": (ROOT/context_paths[1]).read_text(),
                                 "interpretation": "DR-001 的候选身份由用户本次外部行为确认限定覆盖；经营参数仍待定，测试目录已明确。"},
            "source_files": sources, "items": items}
ASSETS.mkdir(parents=True, exist_ok=True)
(ASSETS/"requirements.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"requirements": len(items), "by_package": {s["path"]: s["external_behavior_count"] for s in sources}, "version": snapshot["version"]}, ensure_ascii=False, indent=2))
