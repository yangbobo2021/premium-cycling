#!/usr/bin/env python3
"""Outer launcher compatibility: Playbook 16 wants workspace-relative grants."""
import importlib.util, json, sys
from pathlib import Path
SKILL = Path("/Users/boboyang/.codex/skills/app-delivery-acceptance")
sys.path.insert(0, str(SKILL / "scripts"))
spec = importlib.util.spec_from_file_location("acceptance_outer_launcher", SKILL / "scripts/run_workflow.py")
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)
original = launcher.stream_playbook
def stream_compatible(command, project, env, *args):
    overlay_path = Path(command[command.index("--with") + 1])
    overlay = json.loads(overlay_path.read_text())
    for agent in [overlay["captain"], *overlay["players"].values()]:
        permission = agent["permissions"]
        permission["writablePaths"] = [Path(p).relative_to(project).as_posix() for p in permission["writablePaths"]]
    overlay_path.write_text(json.dumps(overlay))
    return original(command, project, env, *args)
launcher.stream_playbook = stream_compatible
sys.exit(launcher.main())
