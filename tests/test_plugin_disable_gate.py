import unittest
from pathlib import Path


class DuelPluginDisableGateTest(unittest.TestCase):
    def test_all_duel_message_rules_check_runtime_plugin_disable(self) -> None:
        source = Path("src/pallas_plugin_duel/__init__.py").read_text(encoding="utf-8")
        assert "from packages.help.plugin_manager import is_plugin_disabled" in source
        assert "await is_plugin_disabled(" in source
        assert '"duel", event.group_id, int(event.self_id)' in source
        assert "bot=bot, event=event" in source
        assert "rule=Rule(is_duel_qte_msg)" in source
