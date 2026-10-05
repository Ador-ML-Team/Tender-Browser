import logging
import os
import sys

# Plain messages on stdout, like print(), so the output reads the same.
# LOG_LEVEL=WARNING shows only problems; LOG_LEVEL=DEBUG shows more detail.
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    format="%(message)s",
    stream=sys.stdout,
)

# A problem in config/categories.json (CategoriesError, a ValueError) or in
# sources.json (SourcesError) stops the run with its readable list of
# problems instead of a traceback, before anything is fetched or written.
try:
    from tender_radar import run
    from tender_radar.sources import SourcesError
except ValueError as e:
    sys.exit(f"[!] {e}")

if __name__ == "__main__":
    try:
        run()
    except SourcesError as e:
        sys.exit(f"[!] {e}\nNothing was scraped; data file left unchanged.")
