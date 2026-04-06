import importlib


def test_config_reads_env_vars(monkeypatch):
    monkeypatch.setenv("DISCORD_TOKEN", "token")
    monkeypatch.setenv("CHANNEL_ID", "123")
    monkeypatch.setenv("RUST_SERVER_HOST", "1.2.3.4")
    monkeypatch.setenv("RUST_SERVER_PORT", "28018")
    monkeypatch.setenv("UPDATE_INTERVAL", "60")

    import bot.config as config
    importlib.reload(config)

    assert config.DISCORD_TOKEN == "token"
    assert config.CHANNEL_ID == 123
    assert config.RUST_SERVER_HOST == "1.2.3.4"
    assert config.RUST_SERVER_PORT == 28018
    assert config.UPDATE_INTERVAL == 60


def test_config_defaults(monkeypatch):
    monkeypatch.delenv("DISCORD_TOKEN", raising=False)
    monkeypatch.delenv("CHANNEL_ID", raising=False)
    monkeypatch.delenv("RUST_SERVER_HOST", raising=False)
    monkeypatch.delenv("RUST_SERVER_PORT", raising=False)
    monkeypatch.delenv("UPDATE_INTERVAL", raising=False)

    import bot.config as config
    importlib.reload(config)

    assert config.DISCORD_TOKEN is None
    assert config.CHANNEL_ID == 0
    assert config.RUST_SERVER_HOST == "127.0.0.1"
    assert config.RUST_SERVER_PORT == 28017
    assert config.UPDATE_INTERVAL == 30
