import asyncio
import importlib
import os
import traceback

from shared_client import start_client, stop_client


async def load_plugins():

    await start_client()

    plugin_dir = "plugins"

    plugins = [
        f[:-3]
        for f in os.listdir(plugin_dir)
        if f.endswith(".py") and f != "__init__.py"
    ]

    for plugin in plugins:

        try:
            module = importlib.import_module(
                f"plugins.{plugin}"
            )

            func = getattr(
                module,
                f"run_{plugin}_plugin",
                None
            )

            if callable(func):
                print(f"Loading {plugin}")
                await func()

        except Exception:
            traceback.print_exc()


async def main():

    await load_plugins()

    print("Bot Started Successfully")

    await asyncio.Event().wait()


if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Stopping Bot...")

    except Exception:
        traceback.print_exc()

    finally:
        try:
            asyncio.run(stop_client())
        except:
            pass
