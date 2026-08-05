from types import SimpleNamespace

import nonebot

nonebot.init()


def test_parse_duel_at_qqs_ignores_non_numeric_target() -> None:
    from pallas_plugin_duel.duel_bots import parse_duel_at_qqs

    event = SimpleNamespace(
        message=[
            SimpleNamespace(type="at", data={"qq": "啥比牛子"}),
            SimpleNamespace(type="at", data={"qq": "3023094357"}),
        ],
        raw_message="牛牛决斗 [CQ:at,qq=啥比牛子]",
    )

    assert parse_duel_at_qqs(event) == ["3023094357"]


def test_duel_qte_replies_are_not_forced_to_the_host_bot() -> None:
    from pallas_plugin_duel import __plugin_meta__

    ingress = __plugin_meta__.extra["hosted_activity_ingress"]
    assert ingress["speak_at_fleet_bot_only"] is True
    assert __plugin_meta__.extra["ingress_route"]["passive"] is True
